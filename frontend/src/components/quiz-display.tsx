"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { CheckCircle, XCircle, Trophy, RotateCcw } from "lucide-react";

interface QuizQuestion {
  id: number;
  question: string;
  options: {
    A: string;
    B: string;
    C: string;
    D: string;
  };
  correct_answer: string;
  explanation: string;
}

interface QuizData {
  questions: QuizQuestion[];
}

interface QuizDisplayProps {
  quizData: QuizData;
  onRetakeQuiz?: () => void;
}

interface QuestionState {
  selectedAnswer: string | null;
  isAnswered: boolean;
  isCorrect: boolean;
}

export function QuizDisplay({ quizData, onRetakeQuiz }: QuizDisplayProps) {
  const [questionStates, setQuestionStates] = useState<Record<number, QuestionState>>({});
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [quizCompleted, setQuizCompleted] = useState(false);

  const currentQuestion = quizData.questions[currentQuestionIndex];
  const currentState = questionStates[currentQuestion?.id];

  const handleAnswerSelect = (option: string) => {
    if (currentState?.isAnswered) return;

    const isCorrect = option === currentQuestion.correct_answer;

    setQuestionStates(prev => ({
      ...prev,
      [currentQuestion.id]: {
        selectedAnswer: option,
        isAnswered: true,
        isCorrect
      }
    }));
  };

  const handleNextQuestion = () => {
    if (currentQuestionIndex < quizData.questions.length - 1) {
      setCurrentQuestionIndex(prev => prev + 1);
    } else {
      setQuizCompleted(true);
    }
  };

  const handlePreviousQuestion = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(prev => prev - 1);
    }
  };

  const handleRestartQuiz = () => {
    setQuestionStates({});
    setCurrentQuestionIndex(0);
    setQuizCompleted(false);
  };

  const getScore = () => {
    const answeredQuestions = Object.values(questionStates).filter(state => state.isAnswered);
    const correctAnswers = answeredQuestions.filter(state => state.isCorrect);
    return {
      correct: correctAnswers.length,
      total: answeredQuestions.length,
      percentage: answeredQuestions.length > 0 ? Math.round((correctAnswers.length / answeredQuestions.length) * 100) : 0
    };
  };

  const getOptionColor = (option: string) => {
    if (!currentState?.isAnswered) {
      return "hover:bg-muted";
    }

    if (option === currentQuestion.correct_answer) {
      return "bg-green-100 border-green-500 text-green-800 dark:bg-green-950 dark:border-green-600 dark:text-green-200";
    }

    if (option === currentState.selectedAnswer && !currentState.isCorrect) {
      return "bg-red-100 border-red-500 text-red-800 dark:bg-red-950 dark:border-red-600 dark:text-red-200";
    }

    return "bg-muted/50";
  };

  const score = getScore();

  // Quiz completion screen
  if (quizCompleted) {
    return (
      <div className="space-y-6 bg-gradient-to-r from-blue-50 to-purple-50 dark:from-blue-950/20 dark:to-purple-950/20 p-6 rounded-lg border">
        <div className="text-center space-y-4">
          <Trophy className="h-16 w-16 text-yellow-500 mx-auto" />
          <h3 className="text-2xl font-bold">Quiz Complete!</h3>
          <div className="space-y-2">
            <p className="text-lg">
              You scored <span className="font-bold text-primary">{score.correct}</span> out of{" "}
              <span className="font-bold">{score.total}</span> questions correct
            </p>
            <Badge variant={score.percentage >= 70 ? "default" : "destructive"} className="text-lg px-4 py-2">
              {score.percentage}%
            </Badge>
          </div>

          {score.percentage >= 70 ? (
            <p className="text-green-600 dark:text-green-400 font-medium">
              Great job! You have a solid understanding of the material.
            </p>
          ) : (
            <p className="text-orange-600 dark:text-orange-400 font-medium">
              Consider reviewing the material and trying again.
            </p>
          )}
        </div>

        <div className="flex justify-center gap-4">
          <Button onClick={handleRestartQuiz} variant="outline">
            <RotateCcw className="h-4 w-4 mr-2" />
            Retake Quiz
          </Button>
          {onRetakeQuiz && (
            <Button onClick={onRetakeQuiz}>
              Generate New Quiz
            </Button>
          )}
        </div>

        {/* Review incorrect answers */}
        <Card>
          <CardHeader>
            <CardTitle className="text-sm">Review</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            {quizData.questions.map((question) => {
              const state = questionStates[question.id];
              if (!state || state.isCorrect) return null;

              return (
                <div key={question.id} className="space-y-2 p-4 bg-red-50 dark:bg-red-950/20 rounded-lg">
                  <p className="font-medium">{question.question}</p>
                  <div className="grid grid-cols-1 gap-2 text-sm">
                    <p className="text-red-600 dark:text-red-400">
                      Your answer: {state.selectedAnswer} - {question.options[state.selectedAnswer as keyof typeof question.options]}
                    </p>
                    <p className="text-green-600 dark:text-green-400">
                      Correct answer: {question.correct_answer} - {question.options[question.correct_answer as keyof typeof question.options]}
                    </p>
                    <p className="text-muted-foreground italic">{question.explanation}</p>
                  </div>
                </div>
              );
            })}
          </CardContent>
        </Card>
      </div>
    );
  }

  if (!currentQuestion) {
    return (
      <div className="text-center p-6">
        <p className="text-muted-foreground">No quiz questions available.</p>
      </div>
    );
  }

  return (
    <div className="space-y-6 bg-gradient-to-r from-blue-50 to-purple-50 dark:from-blue-950/20 dark:to-purple-950/20 p-6 rounded-lg border">
      {/* Quiz Header */}
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-xl font-bold text-blue-800 dark:text-blue-200">
            📚 Knowledge Check
          </h3>
          <p className="text-sm text-muted-foreground">
            Question {currentQuestionIndex + 1} of {quizData.questions.length}
          </p>
        </div>
        <div className="text-right text-sm text-muted-foreground">
          Score: {score.correct}/{score.total}
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full bg-muted rounded-full h-2">
        <div
          className="bg-primary h-2 rounded-full transition-all duration-300"
          style={{
            width: `${((currentQuestionIndex + (currentState?.isAnswered ? 1 : 0)) / quizData.questions.length) * 100}%`
          }}
        />
      </div>

      {/* Question Card */}
      <Card>
        <CardHeader>
          <CardTitle className="text-lg">{currentQuestion.question}</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          {/* Answer Options */}
          <div className="grid grid-cols-1 gap-3">
            {Object.entries(currentQuestion.options).map(([option, text]) => (
              <button
                key={option}
                onClick={() => handleAnswerSelect(option)}
                disabled={currentState?.isAnswered}
                className={`p-4 text-left rounded-lg border-2 transition-all duration-200 ${getOptionColor(option)} ${
                  !currentState?.isAnswered ? "cursor-pointer hover:scale-[1.02]" : "cursor-default"
                }`}
              >
                <div className="flex items-center gap-3">
                  <span className="font-bold text-lg">{option}.</span>
                  <span>{text}</span>
                  {currentState?.isAnswered && option === currentQuestion.correct_answer && (
                    <CheckCircle className="h-5 w-5 text-green-600 ml-auto" />
                  )}
                  {currentState?.isAnswered &&
                   option === currentState.selectedAnswer &&
                   !currentState.isCorrect && (
                    <XCircle className="h-5 w-5 text-red-600 ml-auto" />
                  )}
                </div>
              </button>
            ))}
          </div>

          {/* Feedback */}
          {currentState?.isAnswered && (
            <div className="mt-4 p-4 rounded-lg bg-muted">
              <div className="flex items-center gap-2 mb-2">
                {currentState.isCorrect ? (
                  <CheckCircle className="h-5 w-5 text-green-600" />
                ) : (
                  <XCircle className="h-5 w-5 text-red-600" />
                )}
                <span className="font-medium">
                  {currentState.isCorrect ? "Correct!" : "Incorrect"}
                </span>
              </div>
              <p className="text-sm text-muted-foreground">{currentQuestion.explanation}</p>
            </div>
          )}

          {/* Navigation */}
          <div className="flex justify-between pt-4">
            <Button
              onClick={handlePreviousQuestion}
              disabled={currentQuestionIndex === 0}
              variant="outline"
            >
              Previous
            </Button>

            {currentState?.isAnswered && (
              <Button onClick={handleNextQuestion}>
                {currentQuestionIndex === quizData.questions.length - 1 ? "Finish Quiz" : "Next Question"}
              </Button>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

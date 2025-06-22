"use client";

import { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { CheckCircle, XCircle } from "lucide-react";

interface QuizQuestion {
  question: string;
  options: string[];
  correctAnswer: string;
  explanation: string;
}

interface QuizQuestionsProps {
  questions: QuizQuestion[];
}

export function QuizQuestions({ questions }: QuizQuestionsProps) {
  const [selectedAnswers, setSelectedAnswers] = useState<{[key: number]: string}>({});
  const [showExplanations, setShowExplanations] = useState<{[key: number]: boolean}>({});

  if (!questions || questions.length === 0) {
    return null;
  }

  const handleSelectAnswer = (questionIndex: number, answer: string) => {
    setSelectedAnswers(prev => ({
      ...prev,
      [questionIndex]: answer
    }));
    setShowExplanations(prev => ({
      ...prev,
      [questionIndex]: true
    }));
  };

  return (
    <Card className="mt-6 overflow-hidden">
      <CardHeader className="bg-primary/5">
        <CardTitle>Test Your Understanding</CardTitle>
      </CardHeader>
      <CardContent className="p-6">
        {questions.map((question, qIndex) => (
          <div 
            key={qIndex} 
            className={`mb-8 ${qIndex > 0 ? 'pt-6 border-t' : ''}`}
          >
            <h3 className="text-lg font-medium mb-3">{question.question}</h3>
            <div className="space-y-2">
              {question.options.map((option, oIndex) => {
                const optionLetter = option.charAt(0);
                const isSelected = selectedAnswers[qIndex] === optionLetter;
                const isCorrect = optionLetter === question.correctAnswer;
                const showResult = isSelected;
                
                return (
                  <div 
                    key={oIndex}
                    onClick={() => {
                      if (!selectedAnswers[qIndex]) {
                        handleSelectAnswer(qIndex, optionLetter)
                      }
                    }}
                    className={`
                      p-3 rounded-md border cursor-pointer flex items-center
                      ${isSelected ? (isCorrect ? 'border-green-500 bg-green-50' : 'border-red-500 bg-red-50') : 'hover:bg-gray-50'}
                      ${selectedAnswers[qIndex] && !isSelected ? 'opacity-70' : ''}
                    `}
                  >
                    <div className="flex-1">
                      {option}
                    </div>
                    {showResult && (
                      <div className="ml-2">
                        {isCorrect ? 
                          <CheckCircle className="text-green-500 h-5 w-5" /> : 
                          <XCircle className="text-red-500 h-5 w-5" />
                        }
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
            
            {showExplanations[qIndex] && (
              <div className={`mt-3 p-4 rounded-md ${selectedAnswers[qIndex] === question.correctAnswer ? 'bg-green-50' : 'bg-red-50'}`}>
                <p className="font-medium mb-1">
                  {selectedAnswers[qIndex] === question.correctAnswer ? 'Correct!' : 'Not quite!'}
                </p>
                <p className="text-sm">{question.explanation}</p>
              </div>
            )}
          </div>
        ))}
      </CardContent>
    </Card>
  );
}
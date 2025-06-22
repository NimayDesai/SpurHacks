"use client";

import React, { useState, useRef, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Send, Play, Video } from "lucide-react";
import { useAuth } from "@/lib/auth-context";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { QuizDisplay } from "@/components/quiz-display";

interface Message {
  id: string;
  content: string;
  role: "user" | "assistant";
  timestamp: Date;
}

interface PresentationData {
  script: string;
  video_url: string;
  prompt: string;
  video_path?: string;
  scene_class?: string;
}

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

// Component to display inline presentation
function PresentationDisplay({
  presentationData,
}: {
  presentationData: PresentationData;
}) {
  const [aiAgentActive, setAiAgentActive] = useState(false);
  const [aiAgentLoading, setAiAgentLoading] = useState(false);
  const [aiConversationUrl, setAiConversationUrl] = useState<string | null>(
    null,
  );
  const [videoError, setVideoError] = useState(false);
  const videoRef = useRef<HTMLVideoElement>(null);
  // Track if video has started playing on AI speech
  const [hasPlayed, setHasPlayed] = useState(false);
  const [micAllowed, setMicAllowed] = useState(false);
  const [quizData, setQuizData] = useState<QuizData | null>(null);
  const [quizLoading, setQuizLoading] = useState(false);
  const [showQuiz, setShowQuiz] = useState(false);
  // Request microphone permission and enable mic toggle
  const handleEnableMic = async () => {
    try {
      await navigator.mediaDevices.getUserMedia({ audio: true });
      setMicAllowed(true);
    } catch (err) {
      console.error("Microphone permission denied", err);
      alert("Microphone permission is required for the AI tutor to speak.");
    }
  };

  const requestAiAgent = async () => {
    setAiAgentLoading(true);

    try {
      const apiBaseUrl =
        process.env.NEXT_PUBLIC_API_URL || "http://localhost:5002/api";

      const response = await fetch(`${apiBaseUrl}/ai-agent/create`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          custom_script: presentationData.script,
          room_id: "presentation-room",
        }),
      });

      const data = await response.json();

      if (data.success) {
        setAiConversationUrl(data.agent_data.conversation_url);
        setAiAgentActive(true);
        // Play video immediately after joining meeting
        if (videoRef.current) {
          videoRef.current.playbackRate = 2.0;
          videoRef.current.play().catch(() => {});
        }
        console.log("AI agent created successfully:", data.agent_data);
      } else {
        console.error("Failed to create AI agent:", data.error);
        alert("Failed to create AI agent: " + data.error);
      }
    } catch (error) {
      console.error("Error creating AI agent:", error);
      alert("Error creating AI agent. Please try again.");
    } finally {
      setAiAgentLoading(false);
    }
  };

  // Generate quiz from the script
  const generateQuiz = async () => {
    setQuizLoading(true);

    try {
      const apiBaseUrl =
        process.env.NEXT_PUBLIC_API_URL || "http://localhost:5002/api";

      const response = await fetch(`${apiBaseUrl}/gemini/generate-quiz`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          script: presentationData.script,
          num_questions: 5,
        }),
      });

      const data = await response.json();

      if (data.success) {
        setQuizData(data.quiz);
        setShowQuiz(true);
        console.log("Quiz generated successfully:", data.quiz);
      } else {
        console.error("Failed to generate quiz:", data.error);
        alert("Failed to generate quiz: " + data.error);
      }
    } catch (error) {
      console.error("Error generating quiz:", error);
      alert("Error generating quiz. Please try again.");
    } finally {
      setQuizLoading(false);
    }
  };

  const handleRetakeQuiz = () => {
    generateQuiz();
  };

  // useEffect removed: video starts in requestAiAgent when AI agent active

  return (
    <div className="space-y-4 bg-gradient-to-r from-purple-50 to-blue-50 dark:from-purple-950/20 dark:to-blue-950/20 p-6 rounded-lg border">
      {/* Header */}
      <div className="text-center mb-4">
        <h3 className="text-xl font-bold text-purple-800 dark:text-purple-200">
          🎓 Educational Presentation: {presentationData.prompt}
        </h3>
        <p className="text-sm text-gray-600 dark:text-gray-400 mt-2">
          Your personalized learning experience with AI-generated video and
          interactive tutor
        </p>
      </div>

      {/* Script Display */}
      <Card>
        <CardHeader>
          <CardTitle className="text-sm">📝 Educational Script</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="bg-muted p-3 rounded text-sm">
            {presentationData.script}
          </div>
        </CardContent>
      </Card>

      {/* AI Tutor + Video Section */}
      <Card>
        <CardHeader>
          <CardTitle className="text-sm">
            🤖 Interactive AI Tutor & 🎬 Animation
          </CardTitle>
        </CardHeader>
        <CardContent>
          {!aiAgentActive && !aiAgentLoading && (
            <div className="text-center space-y-3">
              <p className="text-sm text-muted-foreground">
                Start a conversation with your AI tutor who already knows this
                script!
              </p>
              <Button
                onClick={requestAiAgent}
                className="bg-purple-600 hover:bg-purple-700 text-white"
                size="sm"
              >
                🚀 Start AI Conversation
              </Button>
            </div>
          )}

          {aiAgentLoading && (
            <div className="text-center space-y-3">
              <div className="inline-block animate-spin h-6 w-6 border-4 border-current border-t-transparent rounded-full"></div>
              <p className="text-sm">Setting up your AI tutor...</p>
            </div>
          )}

          {aiAgentActive && aiConversationUrl && (
            <div className="flex flex-col lg:flex-row gap-4">
              {/* AI iframe */}
              <div className="flex-1 aspect-video bg-black rounded-md overflow-hidden relative">
                <iframe
                  src={aiConversationUrl!}
                  className="w-full h-full border-0"
                  allow="camera; microphone; autoplay; fullscreen"
                  title="AI Conversation"
                />
              </div>

              {/* Video Playback */}
              <div className="flex-1 aspect-video bg-black rounded-md overflow-hidden">
                <video
                  ref={videoRef}
                  src={presentationData.video_url}
                  controls
                  muted={false}
                  className="w-full h-full"
                />
              </div>
            </div>
          )}
        </CardContent>
      </Card>

      {/* Quiz Section */}
      <Card>
        <CardHeader>
          <CardTitle className="text-sm">🧠 Test Your Understanding</CardTitle>
        </CardHeader>
        <CardContent>
          {!showQuiz && !quizLoading && (
            <div className="text-center space-y-3">
              <p className="text-sm text-muted-foreground">
                Test your knowledge with AI-generated questions based on this
                presentation
              </p>
              <Button
                onClick={generateQuiz}
                className="bg-blue-600 hover:bg-blue-700 text-white"
                size="sm"
              >
                📝 Generate Quiz
              </Button>
            </div>
          )}

          {quizLoading && (
            <div className="text-center space-y-3">
              <div className="inline-block animate-spin h-6 w-6 border-4 border-current border-t-transparent rounded-full"></div>
              <p className="text-sm">Generating quiz questions...</p>
            </div>
          )}

          {showQuiz && quizData && (
            <QuizDisplay quizData={quizData} onRetakeQuiz={handleRetakeQuiz} />
          )}
        </CardContent>
      </Card>
    </div>
  );
}

export function ChatInterface() {
  const router = useRouter();
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "welcome",
      content:
        "Hi there! I'm your AI assistant. Ask me about any topic and I'll create an educational presentation with both a video animation and an interactive AI tutor for you!",
      role: "assistant",
      timestamp: new Date(),
    },
  ]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const scrollAreaRef = useRef<HTMLDivElement>(null);
  const { token, user } = useAuth();

  // API URL - use environment variable or default
  const apiBaseUrl =
    process.env.NEXT_PUBLIC_API_URL || "http://localhost:5002/api";

  // Auto-resize textarea
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
      textareaRef.current.style.maxHeight = "200px"; // Limit height
    }
  }, [input]);

  // Scroll to bottom when new message is added
  useEffect(() => {
    if (scrollAreaRef.current) {
      const scrollElement = scrollAreaRef.current;
      scrollElement.scrollTop = scrollElement.scrollHeight;
    }
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      content: input.trim(),
      role: "user",
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
      // Get the latest message as the prompt
      const prompt = userMessage.content;

      console.log("Making API request with prompt:", prompt);
      console.log("API URL:", `${apiBaseUrl}/gemini/generate-presentation`);

      // Make API call to generate-presentation endpoint for full workflow
      const response = await fetch(
        `${apiBaseUrl}/gemini/generate-presentation`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          // Send the previously captured prompt, not the cleared input
          body: JSON.stringify({ prompt }),
        },
      );

      console.log("API response status:", response.status);
      console.log("API response ok:", response.ok);

      if (!response.ok) {
        const errorText = await response.text();
        console.error("API error response:", errorText);
        throw new Error(`API Error: ${response.status} - ${errorText}`);
      }

      const data = await response.json();

      if (data.success) {
        // Show an inline presentation with video and AI agent
        const presentationMessage: Message = {
          id: (Date.now() + 1).toString(),
          content: `PRESENTATION_READY:${JSON.stringify({
            script: data.script,
            video_url: `${apiBaseUrl.replace("/api", "")}${data.video_url}`,
            prompt: prompt,
            video_path: data.video_path,
            scene_class: data.scene_class,
          })}`,
          role: "assistant",
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, presentationMessage]);
      } else {
        throw new Error(data.error || "Failed to generate presentation");
      }
    } catch (error) {
      console.error("Error calling Gemini API:", error);

      // Show error message to user
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        content:
          "Sorry, I encountered an error creating your presentation. Please try again later.",
        role: "assistant",
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <div className="flex flex-col h-full">
      <ScrollArea className="flex-1 p-4" ref={scrollAreaRef}>
        <div className="space-y-4">
          {messages.map((message) => {
            // Check if this is a presentation ready message
            if (message.content.startsWith("PRESENTATION_READY:")) {
              const presentationData = JSON.parse(
                message.content.replace("PRESENTATION_READY:", ""),
              );
              return (
                <div key={message.id} className="flex justify-start">
                  <div className="flex items-start gap-2.5 w-full max-w-5xl">
                    <Avatar>
                      <AvatarFallback>AI</AvatarFallback>
                      <AvatarImage src="/robot.png" alt="AI" />
                    </Avatar>
                    <div className="w-full">
                      <PresentationDisplay
                        presentationData={presentationData}
                      />
                      <span className="text-xs opacity-50 block mt-2">
                        {message.timestamp.toLocaleTimeString()}
                      </span>
                    </div>
                  </div>
                </div>
              );
            }

            return (
              <div
                key={message.id}
                className={`flex ${
                  message.role === "user" ? "justify-end" : "justify-start"
                }`}
              >
                <div
                  className={`flex items-start gap-2.5 max-w-3xl ${
                    message.role === "user" ? "flex-row-reverse" : ""
                  }`}
                >
                  {message.role === "assistant" ? (
                    <Avatar>
                      <AvatarFallback>AI</AvatarFallback>
                      <AvatarImage src="/robot.png" alt="AI" />
                    </Avatar>
                  ) : (
                    <Avatar>
                      <AvatarFallback>
                        {user?.username?.charAt(0) || "U"}
                      </AvatarFallback>
                    </Avatar>
                  )}
                  <div
                    className={`px-4 py-2 rounded-lg ${
                      message.role === "user"
                        ? "bg-primary text-primary-foreground"
                        : "bg-muted"
                    }`}
                  >
                    <p className="whitespace-pre-wrap text-sm">
                      {message.content}
                    </p>
                    <span className="text-xs opacity-50 block mt-1">
                      {message.timestamp.toLocaleTimeString()}
                    </span>
                  </div>
                </div>
              </div>
            );
          })}
          {isLoading && (
            <div className="flex justify-start">
              <div className="flex items-center gap-2.5">
                <Avatar>
                  <AvatarFallback>AI</AvatarFallback>
                  <AvatarImage src="/robot.png" alt="AI" />
                </Avatar>
                <div className="px-4 py-2 rounded-lg bg-muted">
                  <div className="flex gap-1">
                    <div
                      className="w-2 h-2 rounded-full bg-current animate-bounce"
                      style={{ animationDelay: "0ms" }}
                    ></div>
                    <div
                      className="w-2 h-2 rounded-full bg-current animate-bounce"
                      style={{ animationDelay: "150ms" }}
                    ></div>
                    <div
                      className="w-2 h-2 rounded-full bg-current animate-bounce"
                      style={{ animationDelay: "300ms" }}
                    ></div>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </ScrollArea>

      <div className="p-4 border-t">
        <form onSubmit={handleSubmit} className="flex gap-2">
          <Textarea
            ref={textareaRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type a message..."
            className="resize-none min-h-[40px]"
            disabled={isLoading}
          />
          <Button
            type="submit"
            size="icon"
            disabled={isLoading || !input.trim()}
          >
            <Send className="h-4 w-4" />
          </Button>
        </form>
      </div>
    </div>
  );
}

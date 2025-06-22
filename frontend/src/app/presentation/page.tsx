'use client';

import { useState, useEffect, useRef } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/lib/auth-context';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Socket, io } from 'socket.io-client';

interface PresentationPageProps {
  searchParams: {
    script?: string;
    video_url?: string;
    prompt?: string;
  };
}

export default function PresentationPage({ searchParams }: PresentationPageProps) {
  const router = useRouter();
  const { user, token } = useAuth();
  const [aiAgentActive, setAiAgentActive] = useState(false);
  const [aiAgentLoading, setAiAgentLoading] = useState(false);
  const [aiConversationUrl, setAiConversationUrl] = useState<string | null>(null);
  const socketRef = useRef<Socket | null>(null);
  
  const script = searchParams.script || '';
  const videoUrl = searchParams.video_url || '';
  const prompt = searchParams.prompt || '';

  // Initialize socket connection
  useEffect(() => {
    const initializeSocket = async () => {
      try {
        const apiBaseUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5002';
        const socket = io(`${apiBaseUrl}/meet`, {
          transports: ['websocket'],
          timeout: 10000,
        });

        socket.on('connect', () => {
          console.log('Connected to presentation socket');
          // Join a presentation room
          socket.emit('join-room', { roomId: 'presentation-room' });
        });

        socket.on('ai-agent-joined', (data) => {
          console.log('AI agent joined:', data);
          setAiConversationUrl(data.agent_data.conversation_url);
          setAiAgentActive(true);
          setAiAgentLoading(false);
        });

        socket.on('error', (error) => {
          console.error('Socket error:', error);
          setAiAgentLoading(false);
        });

        socketRef.current = socket;
      } catch (error) {
        console.error('Error initializing socket:', error);
      }
    };

    initializeSocket();

    return () => {
      if (socketRef.current) {
        socketRef.current.disconnect();
      }
    };
  }, []);

  const requestAiAgent = () => {
    if (!socketRef.current) {
      console.error('Socket not connected');
      return;
    }

    setAiAgentLoading(true);
    
    // Send the generated script to the AI agent
    socketRef.current.emit('request-ai-agent', {
      roomId: 'presentation-room',
      custom_script: script
    });
  };

  if (!user) {
    return (
      <div className="h-screen flex items-center justify-center bg-background">
        <div className="text-center">
          <p>Please log in to view the presentation.</p>
          <Button onClick={() => router.push('/login')} className="mt-4">
            Log In
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <header className="border-b py-4 px-6 flex items-center justify-between">
        <h1 className="text-2xl font-bold">AI Educational Presentation</h1>
        <div className="flex items-center gap-4">
          <Button variant="outline" onClick={() => router.push('/')}>
            Back to Home
          </Button>
        </div>
      </header>
      
      <main className="flex-1 p-6">
        <div className="max-w-7xl mx-auto">
          {/* Topic and Script Info */}
          <div className="mb-6">
            <Card>
              <CardHeader>
                <CardTitle>Topic: {prompt}</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground mb-4">Generated Educational Script:</p>
                <div className="bg-muted p-4 rounded-md">
                  <p className="whitespace-pre-wrap">{script}</p>
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Main Content Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Video Section */}
            <div className="space-y-4">
              <Card>
                <CardHeader>
                  <CardTitle>Educational Animation</CardTitle>
                </CardHeader>
                <CardContent>
                  {videoUrl ? (
                    <div className="aspect-video bg-black rounded-md overflow-hidden">
                      <video
                        src={videoUrl}
                        controls
                        className="w-full h-full"
                        poster="/api/placeholder/800/450"
                      >
                        Your browser does not support the video tag.
                      </video>
                    </div>
                  ) : (
                    <div className="aspect-video bg-muted rounded-md flex items-center justify-center">
                      <p className="text-muted-foreground">Video not available</p>
                    </div>
                  )}
                </CardContent>
              </Card>
            </div>

            {/* AI Agent Section */}
            <div className="space-y-4">
              <Card>
                <CardHeader>
                  <CardTitle>Interactive AI Tutor</CardTitle>
                </CardHeader>
                <CardContent>
                  {!aiAgentActive && !aiAgentLoading && (
                    <div className="text-center space-y-4">
                      <p className="text-muted-foreground">
                        Start an interactive conversation with your AI tutor about this topic.
                      </p>
                      <Button 
                        onClick={requestAiAgent}
                        className="bg-purple-600 hover:bg-purple-700"
                      >
                        Start AI Conversation
                      </Button>
                    </div>
                  )}

                  {aiAgentLoading && (
                    <div className="text-center space-y-4">
                      <div className="inline-block animate-spin h-8 w-8 border-4 border-current border-t-transparent rounded-full"></div>
                      <p>Starting AI conversation...</p>
                    </div>
                  )}

                  {aiAgentActive && aiConversationUrl && (
                    <div className="space-y-4">
                      <p className="text-sm text-muted-foreground">
                        Your AI tutor is ready! The AI has the educational script and can help you understand the concepts better.
                      </p>
                      <div className="aspect-video bg-black rounded-md overflow-hidden">
                        <iframe
                          src={aiConversationUrl}
                          className="w-full h-full border-0"
                          allow="camera; microphone; autoplay; encrypted-media; fullscreen"
                          title="AI Conversation"
                        />
                      </div>
                    </div>
                  )}
                </CardContent>
              </Card>
            </div>
          </div>

          {/* Instructions */}
          <div className="mt-6">
            <Card>
              <CardHeader>
                <CardTitle>How to Use This Presentation</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <h4 className="font-semibold mb-2">📹 Educational Video</h4>
                    <p className="text-sm text-muted-foreground">
                      Watch the AI-generated animation that visualizes the concepts from your topic. 
                      The video follows the exact script with synchronized visuals and timing.
                    </p>
                  </div>
                  <div>
                    <h4 className="font-semibold mb-2">🤖 AI Tutor</h4>
                    <p className="text-sm text-muted-foreground">
                      Start a conversation with your AI tutor who has already learned the script. 
                      Ask questions, get clarifications, or explore related concepts interactively.
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </main>
    </div>
  );
}

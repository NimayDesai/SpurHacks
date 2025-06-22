'use client';

import React, { useState, useRef, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { io, Socket } from 'socket.io-client';

export default function MeetPage() {
  // Basic states - removed camera/video states since Tavus handles everything
  const [aiAgentActive, setAiAgentActive] = useState(false);
  const [aiAgentLoading, setAiAgentLoading] = useState(false);
  const [aiIsResponding, setAiIsResponding] = useState(false);
  const [aiConversationUrl, setAiConversationUrl] = useState<string | null>(null);
  const [chatMessages, setChatMessages] = useState<Array<{
    text: string;
    sender: 'user' | 'ai' | 'system';
    timestamp: string;
  }>>([]);
  const [aiConfig, setAiConfig] = useState<{
    custom_script: string;
    persona_instructions: string;
    conversation_style: string;
    knowledge_base: string;
  } | null>(null);
  const [aiTemplates, setAiTemplates] = useState<any>(null);
  const [selectedTemplate, setSelectedTemplate] = useState<string>('hackathon_assistant');
  
  // Refs - removed video/media refs since Tavus handles everything
  const socketRef = useRef<Socket | null>(null);

  // Auto-initialize when component mounts
  useEffect(() => {
    initializeApp();
    return () => {
      cleanup();
    };
  }, []);

  const fetchAiConfig = async () => {
    try {
      console.log('Fetching AI configuration from backend...');
      const response = await fetch('http://localhost:5002/api/ai/default-config');
      const data = await response.json();
      
      if (data.success) {
        setAiConfig(data.config);
        console.log('AI configuration loaded:', data.config);
      } else {
        console.error('Failed to fetch AI config:', data.error);
        // Fallback to hardcoded config
        setAiConfig({
          custom_script: "Hello! I'm your AI assistant. How can I help you today?",
          persona_instructions: "You are a helpful AI assistant.",
          conversation_style: "friendly",
          knowledge_base: "General knowledge"
        });
      }
    } catch (error) {
      console.error('Error fetching AI config:', error);
      // Fallback to hardcoded config
      setAiConfig({
        custom_script: "Hello! I'm your AI assistant. How can I help you today?",
        persona_instructions: "You are a helpful AI assistant.",
        conversation_style: "friendly",
        knowledge_base: "General knowledge"
      });
    }
  };

  const fetchAiTemplates = async () => {
    try {
      console.log('Fetching AI templates from backend...');
      const response = await fetch('http://localhost:5002/api/ai/config-templates');
      const data = await response.json();
      
      if (data.success) {
        setAiTemplates(data.templates);
        // Set the default template as the current config
        const defaultTemplate = data.templates[selectedTemplate];
        if (defaultTemplate) {
          setAiConfig({
            custom_script: defaultTemplate.custom_script,
            persona_instructions: defaultTemplate.persona_instructions,
            conversation_style: defaultTemplate.conversation_style,
            knowledge_base: defaultTemplate.knowledge_base
          });
        }
        console.log('AI templates loaded:', data.templates);
      }
    } catch (error) {
      console.error('Error fetching AI templates:', error);
    }
  };

  const selectTemplate = (templateKey: string) => {
    if (aiTemplates && aiTemplates[templateKey]) {
      const template = aiTemplates[templateKey];
      setSelectedTemplate(templateKey);
      setAiConfig({
        custom_script: template.custom_script,
        persona_instructions: template.persona_instructions,
        conversation_style: template.conversation_style,
        knowledge_base: template.knowledge_base
      });
      console.log('Selected template:', templateKey, template);
    }
  };

  const initializeApp = async () => {
    try {
      console.log('Initializing app...');
      await fetchAiTemplates(); // This will also set the default config
      await initializeSocket();
    } catch (error) {
      console.error('Failed to initialize app:', error);
    }
  };

  const initializeSocket = async () => {
    try {
      console.log('Connecting to socket...');
      const socket = io('http://10.200.6.212:5002/meet', {
        transports: ['websocket', 'polling']
      });

      socketRef.current = socket;

      socket.on('connect', () => {
        console.log('Socket connected:', socket.id);
        // Auto-join a main room since we don't have room selection
        socket.emit('join-room', { roomId: 'main-room' });
      });

      socket.on('connected', (data) => {
        console.log('Server confirmed connection:', data);
      });

      socket.on('room-joined', (data) => {
        console.log('Joined room:', data);
      });

      socket.on('ai-agent-joined', (data) => {
        console.log('AI agent joined event received:', data);
        setAiAgentActive(true);
        setAiAgentLoading(false);
        
        // Set AI conversation URL for iframe embedding
        if (data.agent_data && data.agent_data.conversation_url) {
          console.log('Setting AI conversation URL:', data.agent_data.conversation_url);
          setAiConversationUrl(data.agent_data.conversation_url);
        } else {
          console.error('No conversation URL received from AI agent');
        }
        
        setChatMessages(prev => [...prev, {
          text: 'AI Assistant has joined! You can now interact with the AI using the video interface below.',
          sender: 'system',
          timestamp: new Date().toISOString()
        }]);
        
        console.log('AI agent state updated: active =', true, 'loading =', false);
      });

      socket.on('ai-message-sent', (data) => {
        console.log('AI response received:', data);
        console.log('AI heard:', data.user_message);
        console.log('AI responded:', data.ai_response);
        
        setAiIsResponding(false); // AI finished responding
        
        setChatMessages(prev => [
          ...prev,
          {
            text: data.ai_response,
            sender: 'ai',
            timestamp: new Date().toISOString()
          }
        ]);
      });

      socket.on('error', (error) => {
        console.error('Socket error:', error);
        setAiAgentLoading(false);
      });

      socket.on('connect_error', (error) => {
        console.error('Socket connection error:', error);
        setAiAgentLoading(false);
      });

      socket.on('disconnect', (reason) => {
        console.log('Socket disconnected:', reason);
        setAiAgentLoading(false);
        setAiAgentActive(false);
      });

      return socket;
    } catch (error) {
      console.error('Socket initialization failed:', error);
      throw error;
    }
  };

  const requestAiAgent = () => {
    if (!socketRef.current) {
      console.error('Socket not connected');
      alert('Socket not connected. Please refresh the page.');
      return;
    }
    
    if (!socketRef.current.connected) {
      console.error('Socket is not connected');
      alert('Socket is not connected. Please refresh the page.');
      return;
    }
    
    console.log('Requesting AI agent...');
    setAiAgentLoading(true);
    const roomId = 'main-room'; // Fixed room ID since we're removing room functionality
    
    // Send simple AI agent request - all configuration is hardcoded in backend
    socketRef.current.emit('request-ai-agent', { 
      roomId
    });
    
    console.log('AI agent request sent (configuration is hardcoded in backend)');
    
    // Add a timeout to reset loading state if no response
    setTimeout(() => {
      if (aiAgentLoading && !aiAgentActive) {
        console.error('AI agent request timed out');
        setAiAgentLoading(false);
        alert('AI agent request timed out. Please try again.');
      }
    }, 10000);
  };

  const sendMessageToAi = (message: string, isVoice = false) => {
    if (!socketRef.current || !message.trim()) return;
    
    console.log(isVoice ? 'Sending voice message to AI:' : 'Sending text message to AI:', message);
    
    setAiIsResponding(true); // Show AI is thinking/responding
    
    socketRef.current.emit('send-to-ai', { 
      message: message.trim(),
      roomId: 'main-room'
    });
    
    // Add user message to chat
    setChatMessages(prev => [...prev, {
      text: isVoice ? `🎤 ${message}` : message,
      sender: 'user',
      timestamp: new Date().toISOString()
    }]);
  };

  const cleanup = () => {
    if (socketRef.current) {
      socketRef.current.disconnect();
    }
  };

  return (
    <div className="min-h-screen bg-background p-6">
      <div className="max-w-6xl mx-auto space-y-6">
        <div className="text-center">
          <h1 className="text-3xl font-bold mb-2">AI Video Assistant</h1>
          <p className="text-gray-600">Start a conversation with your AI assistant - all camera and microphone functionality is handled through the AI interface</p>
        </div>

        {/* AI Video Interface */}
        {aiAgentActive ? (
          <div className="grid gap-6 grid-cols-1">
            {/* AI Agent Video - Full Width */}
            <Card className="relative">
              <div className="w-full h-96 bg-gradient-to-br from-blue-900 to-purple-900 rounded-lg relative overflow-hidden">
                {aiConversationUrl ? (
                  <iframe
                    src={aiConversationUrl}
                    className="w-full h-full rounded-lg border-0"
                    allow="camera; microphone; autoplay; encrypted-media; fullscreen"
                    allowFullScreen
                    title="AI Assistant Video Call"
                  />
                ) : (
                  /* Fallback content when conversation URL is not available */
                  <div className="absolute inset-0 flex items-center justify-center bg-gradient-to-br from-blue-900 to-purple-900 rounded-lg">
                    <div className="text-center text-white">
                      <div className="text-6xl mb-4 animate-pulse">🤖</div>
                      <div className="text-xl font-semibold">AI Assistant</div>
                      <div className="text-sm opacity-80 mt-2">Loading conversation...</div>
                    </div>
                  </div>
                )}
              </div>
              <div className="absolute bottom-4 left-4 bg-black bg-opacity-70 text-white px-3 py-2 rounded-lg text-sm font-medium">
                🤖 AI Assistant {aiIsResponding ? '(Thinking...)' : '(Online)'}
              </div>
              <div className="absolute top-4 right-4 bg-green-500 text-white px-2 py-1 rounded-full text-xs font-medium">
                {aiIsResponding ? 'Responding...' : 'Live'}
              </div>
            </Card>
          </div>
        ) : (
          <div className="text-center">
            <div className="bg-gray-50 border-2 border-dashed border-gray-300 rounded-lg p-12">
              <div className="text-6xl mb-4">🤖</div>
              <h3 className="text-xl font-semibold mb-2">No AI Assistant Active</h3>
              <p className="text-gray-600 mb-6">Click "Add AI" to start a conversation with your AI assistant</p>
            </div>
          </div>
        )}
        
        {/* Controls */}
        <div className="flex justify-center space-x-4">
          <Button
            onClick={requestAiAgent}
            variant="default"
            size="lg"
            disabled={aiAgentLoading || aiAgentActive}
            className="h-12 px-6 bg-gray-800 hover:bg-gray-900 text-white"
          >
            {aiAgentLoading ? '⏳ Loading...' : aiAgentActive ? '🤖 AI Active' : '🤖 Add AI'}
          </Button>
          
          {/* Force New AI Button */}
          {aiAgentActive && (
            <Button
              onClick={() => {
                setAiAgentActive(false);
                setAiConversationUrl(null);
                setTimeout(requestAiAgent, 1000);
              }}
              variant="outline"
              size="lg"
              className="h-12 px-6 border-orange-500 text-orange-600 hover:bg-orange-50"
            >
              🔄 Force New AI
            </Button>
          )}
        </div>
        
        {/* AI Configuration Display */}
        {aiConfig && (
          <Card className="p-4 bg-blue-50 border-blue-200">
            <h3 className="font-semibold mb-3 text-sm text-blue-800">AI Assistant Configuration</h3>
            
            {!aiAgentActive && (
              <div className="mb-3 p-2 bg-yellow-100 border border-yellow-300 rounded text-xs text-yellow-800">
                <strong>💡 Tip:</strong> Customize the script below, then click "Add AI" to create your agent.
              </div>
            )}
            
            {/* Template Selector */}
            {aiTemplates && (
              <div className="mb-3">
                <label className="block text-xs font-medium text-blue-700 mb-1">
                  Choose AI Template:
                </label>
                <select 
                  value={selectedTemplate}
                  onChange={(e) => selectTemplate(e.target.value)}
                  className="w-full text-xs border border-blue-300 rounded px-2 py-1 bg-white"
                  disabled={aiAgentActive}
                >
                  {Object.entries(aiTemplates).map(([key, template]: [string, any]) => (
                    <option key={key} value={key}>
                      {template.name}
                    </option>
                  ))}
                </select>
              </div>
            )}
            
            {/* Editable AI Configuration */}
            <div className="space-y-3">
              <div>
                <label className="block text-xs font-medium text-blue-700 mb-1">
                  Opening Script (what AI says first):
                </label>
                <textarea
                  value={aiConfig.custom_script}
                  onChange={(e) => setAiConfig({...aiConfig, custom_script: e.target.value})}
                  className="w-full text-xs border border-blue-300 rounded px-2 py-1 bg-white h-16"
                  disabled={aiAgentActive}
                  placeholder="Enter what the AI should say when it first joins..."
                />
              </div>
              
              <div>
                <label className="block text-xs font-medium text-blue-700 mb-1">
                  Persona Instructions:
                </label>
                <textarea
                  value={aiConfig.persona_instructions}
                  onChange={(e) => setAiConfig({...aiConfig, persona_instructions: e.target.value})}
                  className="w-full text-xs border border-blue-300 rounded px-2 py-1 bg-white h-12"
                  disabled={aiAgentActive}
                  placeholder="How should the AI behave during conversation..."
                />
              </div>
              
              <div>
                <label className="block text-xs font-medium text-blue-700 mb-1">
                  Conversation Style:
                </label>
                <select
                  value={aiConfig.conversation_style}
                  onChange={(e) => setAiConfig({...aiConfig, conversation_style: e.target.value})}
                  className="w-full text-xs border border-blue-300 rounded px-2 py-1 bg-white"
                  disabled={aiAgentActive}
                >
                  <option value="friendly">Friendly</option>
                  <option value="professional">Professional</option>
                  <option value="enthusiastic">Enthusiastic</option>
                  <option value="casual">Casual</option>
                  <option value="formal">Formal</option>
                </select>
              </div>
            </div>
          </Card>
        )}
        
        {/* AI Chat Interface */}
        {aiAgentActive && (
          <Card className="p-6">
            <h3 className="font-semibold mb-4 text-lg">AI Assistant Status</h3>
            <div className="space-y-4">
              {/* Instructions */}
              <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
                <div className="text-sm text-blue-800">
                  <strong>How to interact with the AI:</strong>
                  <ul className="mt-2 list-disc ml-4 space-y-1">
                    <li>The Tavus AI interface above includes both your camera and the AI's video</li>
                    <li>Speak directly to the AI - it can see and hear you in real-time</li>
                    <li>All camera and microphone controls are built into the AI interface</li>
                    <li>No separate camera setup needed - everything is integrated!</li>
                  </ul>
                </div>
              </div>
              
              {/* Chat Messages */}
              <div className="h-48 overflow-y-auto border rounded-lg p-4 bg-gray-50 space-y-3">
                {chatMessages.map((msg, index) => (
                  <div key={index} className={`flex ${
                    msg.sender === 'user' ? 'justify-end' : 
                    msg.sender === 'ai' ? 'justify-start' : 'justify-center'
                  }`}>
                    <span className={`inline-block px-4 py-2 rounded-lg text-sm max-w-xs lg:max-w-md ${
                      msg.sender === 'user' ? 'bg-blue-500 text-white' :
                      msg.sender === 'ai' ? 'bg-green-500 text-white' :
                      'bg-gray-400 text-white'
                    }`}>
                      {msg.text}
                    </span>
                  </div>
                ))}
                
                {/* AI Typing Indicator */}
                {aiIsResponding && (
                  <div className="flex justify-start">
                    <span className="inline-block px-4 py-2 rounded-lg text-sm bg-gray-200 text-gray-600">
                      <span className="animate-pulse">AI is processing</span>
                      <span className="inline-flex ml-1">
                        <span className="animate-bounce">.</span>
                        <span className="animate-bounce" style={{ animationDelay: '0.1s' }}>.</span>
                        <span className="animate-bounce" style={{ animationDelay: '0.2s' }}>.</span>
                      </span>
                    </span>
                  </div>
                )}
              </div>
              
              {/* Disabled Message Input - encouraging video interaction */}
              <div className="flex gap-3">
                <input
                  type="text"
                  value="Use the video interface above for real conversation"
                  disabled
                  className="flex-1 px-4 py-3 border border-gray-300 rounded-lg bg-gray-100 text-gray-500"
                />
                <Button 
                  disabled
                  className="px-6 bg-gray-300 text-gray-500"
                >
                  Use Video
                </Button>
              </div>
            </div>
          </Card>
        )}
      </div>
    </div>
  );
}

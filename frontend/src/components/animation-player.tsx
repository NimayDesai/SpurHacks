'use client';

import { useState } from "react";
import { Button } from "@/components/ui/button";

interface AnimationPlayerProps {
  className?: string;
}

export default function AnimationPlayer({ className }: AnimationPlayerProps) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [animationUrl, setAnimationUrl] = useState<string | null>(null);
  const [promptText, setPromptText] = useState<string>('');

  const apiBaseUrl = process.env.NEXT_PUBLIC_API_URL || 'http://10.200.6.212:5001/api';

  const generateAnimation = async () => {
    if (!promptText.trim()) {
      setError("Please enter a prompt to generate an animation");
      return;
    }

    setLoading(true);
    setError(null);
    setAnimationUrl(null);

    try {
      const response = await fetch(`${apiBaseUrl}/animation/render`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          animation_type: 'circle', // Default to simple circle animation
          prompt: promptText
        })
      });
      
      if (response.ok) {
        const data = await response.json();
        
        // Construct full URL for the video
        let fullAnimationUrl;
        if (data.animation_url.startsWith('http')) {
          fullAnimationUrl = data.animation_url;
        } else if (data.animation_url.startsWith('/api/')) {
          const baseUrlParts = apiBaseUrl.split('/api');
          const baseUrl = baseUrlParts[0];
          fullAnimationUrl = `${baseUrl}${data.animation_url}`;
        } else {
          fullAnimationUrl = `${apiBaseUrl}${data.animation_url.startsWith('/') ? '' : '/'}${data.animation_url}`;
        }
        
        setAnimationUrl(fullAnimationUrl);
      } else {
        const data = await response.json();
        setError(data.error || 'Failed to generate animation');
      }
    } catch (err) {
      setError('Error connecting to server');
      console.error('Animation generation error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={`space-y-4 ${className}`}>
      <h2 className="text-2xl font-bold">Animation Generator</h2>
      
      <div className="space-y-4">
        <div className="flex gap-2">
          <input
            type="text"
            value={promptText}
            onChange={(e) => setPromptText(e.target.value)}
            placeholder="Enter a prompt to generate an animation..."
            className="flex-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            onKeyPress={(e) => e.key === 'Enter' && generateAnimation()}
          />
          <Button 
            onClick={generateAnimation}
            disabled={loading || !promptText.trim()}
            className="px-6"
          >
            {loading ? 'Generating...' : 'Generate'}
          </Button>
        </div>
      </div>
      
      {loading && (
        <div className="text-center py-8">
          <div className="inline-block animate-spin h-8 w-8 border-2 border-current border-t-transparent rounded-full"></div>
          <p className="mt-2">Generating animation...</p>
        </div>
      )}
      
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
          {error}
        </div>
      )}
      
      {animationUrl && !loading && (
        <div className="mt-6">
          <video 
            src={animationUrl} 
            controls 
            autoPlay
            muted
            loop
            className="w-full rounded-lg shadow-lg" 
            onError={() => setError('Error loading video. Please try again.')}
          />
        </div>
      )}
    </div>
  );
}

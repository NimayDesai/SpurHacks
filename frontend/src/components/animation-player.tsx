'use client';

import { useState } from "react";
import { useAuth } from "@/lib/auth-context";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";

interface AnimationPlayerProps {
  className?: string;
}

export default function AnimationPlayer({ className }: AnimationPlayerProps) {
  const { token } = useAuth();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [animationUrl, setAnimationUrl] = useState<string | null>(null);

  const animations = [
    { id: 'circle', name: 'Create Circle' },
    { id: 'square_to_circle', name: 'Square to Circle' },
    { id: 'text', name: 'Write Text' },
    { id: 'math', name: 'Math Formula' },
  ];

  const renderAnimation = async (animationType: string) => {
    if (!token) {
      setError("You must be logged in to render animations");
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await fetch('/api/animation/render', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ animation_type: animationType })
      });

      const data = await response.json();
      
      if (response.ok) {
        setAnimationUrl(data.animation_url);
      } else {
        setError(data.error || "Failed to render animation");
      }
    } catch (err) {
      setError("An error occurred while rendering the animation");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={`space-y-4 ${className}`}>
      <h2 className="text-2xl font-bold mb-4">Math Animations</h2>
      
      <div className="grid grid-cols-2 gap-2 mb-4">
        {animations.map((anim) => (
          <Button 
            key={anim.id}
            onClick={() => renderAnimation(anim.id)}
            disabled={loading}
            variant="outline"
            className="h-16"
          >
            {anim.name}
          </Button>
        ))}
      </div>
      
      {loading && (
        <div className="text-center py-4">
          <div className="inline-block animate-spin h-6 w-6 border-2 border-current border-t-transparent rounded-full"></div>
          <p className="mt-2">Rendering animation...</p>
        </div>
      )}
      
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
          {error}
        </div>
      )}
      
      {animationUrl && !loading && (
        <Card className="p-2">
          <video 
            src={animationUrl} 
            controls 
            autoPlay 
            className="w-full rounded" 
          />
        </Card>
      )}
    </div>
  );
}

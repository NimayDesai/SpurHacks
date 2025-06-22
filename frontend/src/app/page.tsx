'use client';

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import AnimationPlayer from "@/components/animation-player";
import { useAuth } from "@/lib/auth-context";

export default function Home() {
  const { user, isLoading, logout } = useAuth();
  const router = useRouter();
  
  useEffect(() => {
    if (!isLoading && !user) {
      router.push('/login');
    }
  }, [user, isLoading, router]);

  const startVideoCall = () => {
    // Direct navigation to meet page without room parameters
    router.push('/meet');
  };

  if (isLoading) {
    return (
      <div className="h-screen flex items-center justify-center bg-background">
        <div className="text-center">
          <div className="inline-block animate-spin h-8 w-8 border-4 border-current border-t-transparent rounded-full"></div>
          <p className="mt-4">Loading...</p>
        </div>
      </div>
    );
  }

  if (!user) {
    return null; // Will redirect in the useEffect
  }

  return (
    <div className="min-h-screen bg-background">
      <header className="border-b py-4 px-6 flex items-center justify-between">
        <h1 className="text-2xl font-bold">SpurHacks</h1>
        <div className="flex items-center gap-4">
          <span>Welcome, {user.username}</span>
          <Button variant="outline" onClick={() => logout()}>Log out</Button>
        </div>
      </header>
      
      <main className="p-6">
        <div className="max-w-4xl mx-auto space-y-8">
          {/* Quick Actions */}
          <div className="text-center space-y-4">
            <h2 className="text-3xl font-bold">Welcome to SpurHacks</h2>
            <p className="text-gray-600">Start a video call or generate animations</p>
            <div className="flex justify-center gap-4">
              <Button 
                onClick={startVideoCall}
                size="lg"
                className="bg-green-600 hover:bg-green-700 text-white px-8 py-3"
              >
                🎥 Start Video Call with AI
              </Button>
              <Button 
                onClick={() => router.push('/meet')}
                variant="outline"
                size="lg"
                className="px-8 py-3"
              >
                📞 Join Existing Call
              </Button>
            </div>
          </div>
          
          {/* Animation Player */}
          <div className="border-t pt-8">
            <AnimationPlayer />
          </div>
        </div>
      </main>
    </div>
  );
}

'use client';

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import AnimationPlayer from "@/components/animation-player";
import { useAuth } from "@/lib/auth-context";
import { ChatInterface } from "@/components/chat-interface";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Card } from "@/components/ui/card";

export default function Home() {
  const { user, isLoading, logout } = useAuth();
  const router = useRouter();
  
  useEffect(() => {
    if (!isLoading && !user) {
      // Redirect unauthenticated users to login
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

  // Block rendering until authenticated
  if (!isLoading && !user) {
    return null;
  }

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <header className="border-b py-4 px-6 flex items-center justify-between">
        <h1 className="text-2xl font-bold">SpurHacks AI</h1>
        <div className="flex items-center gap-4">
          <span>Welcome, {user?.username || 'Guest'}</span>
          <Button variant="outline" onClick={() => logout()}>Log out</Button>
        </div>
      </header>
      
      <main className="flex-1 p-6">
        <div className="max-w-6xl mx-auto space-y-8">
          {/* Quick Actions */}
          <div className="text-center space-y-4">
            <h2 className="text-3xl font-bold">Welcome to Numina</h2>
            <p className="text-gray-600">Start a video call or generate animations</p>
            <div className="flex justify-center gap-4">
              {/* <Button 
                onClick={startVideoCall}
                size="lg"
                className="bg-green-600 hover:bg-green-700 text-white px-8 py-3"
              >
                🎥 Start Video Call with AI
              </Button> */}
              {/* <Button 
                onClick={() => router.push('/meet')}
                variant="outline"
                size="lg"
                className="px-8 py-3"
              >
                📞 Join Existing Call
              </Button> */}
            </div>
          </div>
          
          {/* Tabbed Interface */}
          <Tabs defaultValue="chat" className="w-full">
            <TabsContent value="chat" className="h-[calc(100vh-16rem)]">
              <Card className="h-full border">
                <ChatInterface />
              </Card>
            </TabsContent>
            <TabsContent value="animation">
              <Card className="p-6">
                <h2 className="text-xl font-semibold mb-4">Animation Preview</h2>
                <AnimationPlayer />
              </Card>
            </TabsContent>
          </Tabs>
        </div>
      </main>
    </div>
  );
}

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
        <div className="max-w-4xl mx-auto">
          <AnimationPlayer />
        </div>
      </main>
    </div>
  );
}

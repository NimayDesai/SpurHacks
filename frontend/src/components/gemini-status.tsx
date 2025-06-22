"use client";

import { useEffect, useState } from "react";
import { Badge } from "@/components/ui/badge";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";

export function GeminiStatus() {
  const [status, setStatus] = useState<'loading' | 'available' | 'unavailable'>('loading');
  const apiBaseUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5002/api';

  useEffect(() => {
    const checkStatus = async () => {
      try {
        const response = await fetch(`${apiBaseUrl}/gemini/status`);
        const data = await response.json();
        
        if (response.ok && data.available) {
          setStatus('available');
        } else {
          setStatus('unavailable');
        }
      } catch (error) {
        console.error("Failed to check Gemini status:", error);
        setStatus('unavailable');
      }
    };
    
    checkStatus();
  }, [apiBaseUrl]);
  
  const getStatusColor = () => {
    switch (status) {
      case 'available': return "bg-green-500";
      case 'unavailable': return "bg-red-500";
      default: return "bg-yellow-500";
    }
  };
  
  const getStatusText = () => {
    switch (status) {
      case 'available': return "Gemini API Connected";
      case 'unavailable': return "Gemini API Unavailable";
      default: return "Checking Gemini API...";
    }
  };
  
  return (
    <TooltipProvider>
      <Tooltip>
        <TooltipTrigger asChild>
          <Badge variant="outline" className="cursor-help">
            <div className={`w-2 h-2 rounded-full ${getStatusColor()} mr-2`}></div>
            {getStatusText()}
          </Badge>
        </TooltipTrigger>
        <TooltipContent>
          {status === 'available' 
            ? "Gemini API is responding normally" 
            : "There may be issues with the Gemini API connection"}
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  );
}
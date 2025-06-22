/**
 * API service for Gemini AI
 */

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5001/api';

export interface GeminiResponse {
  success: boolean;
  response: string;
  prompt?: string;
  instructions?: string;
  message_count?: number;
  last_message?: string;
  error?: string;
}

/**
 * Generate content using Gemini API
 */
export const generateContent = async (
  prompt: string,
  instructions?: string,
  token?: string
): Promise<GeminiResponse> => {
  const response = await fetch(`${API_URL}/gemini/generate`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { "Authorization": `Bearer ${token}` } : {})
    },
    body: JSON.stringify({ prompt, instructions }),
  });

  const data = await response.json();
  
  if (!response.ok) {
    throw new Error(data.error || 'Failed to generate content');
  }

  return data;
};

/**
 * Chat with Gemini API
 */
export const chatWithGemini = async (
  messages: string[],
  systemInstruction?: string,
  token?: string
): Promise<GeminiResponse> => {
  const response = await fetch(`${API_URL}/gemini/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { "Authorization": `Bearer ${token}` } : {})
    },
    body: JSON.stringify({ 
      messages, 
      system_instruction: systemInstruction 
    }),
  });

  const data = await response.json();
  
  if (!response.ok) {
    throw new Error(data.error || 'Failed to chat with Gemini');
  }

  return data;
};
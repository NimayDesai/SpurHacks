/**
 * API service for authentication
 */

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:5002/api';

export interface User {
  id: number;
  username: string;
  email: string;
  created_at: string;
  updated_at: string;
}

export interface LoginResponse {
  message: string;
  user: User;
  access_token: string;
}

export interface SignupResponse {
  message: string;
  user: User;
}

export interface AuthError {
  error: string;
}

/**
 * Sign up a new user
 */
export const signUp = async (
  username: string,
  email: string,
  password: string
): Promise<SignupResponse> => {
  const response = await fetch(`${API_URL}/auth/signup`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, email, password }),
  });

  if (!response.ok) {
    const errorData: AuthError = await response.json();
    throw new Error(errorData.error || 'Failed to sign up');
  }

  return response.json();
};

/**
 * Log in a user
 */
export const login = async (
  username: string,
  password: string
): Promise<LoginResponse> => {
  const response = await fetch(`${API_URL}/auth/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, password }),
  });

  if (!response.ok) {
    const errorData: AuthError = await response.json();
    throw new Error(errorData.error || 'Failed to login');
  }

  return response.json();
};

/**
 * Log out a user
 */
export const logout = async (token: string): Promise<{ message: string }> => {
  const response = await fetch(`${API_URL}/auth/logout`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    const errorData: AuthError = await response.json();
    throw new Error(errorData.error || 'Failed to logout');
  }

  return response.json();
};

/**
 * Get the current user
 */
export const getCurrentUser = async (token: string): Promise<{ user: User }> => {
  console.log('Getting current user with token length:', token?.length);
  console.log('API URL:', `${API_URL}/auth/me`);

  try {
    const response = await fetch(`${API_URL}/auth/me`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
    });

    console.log('Current user response status:', response.status);
    
    if (!response.ok) {
      const errorData = await response.json();
      console.error('Auth error details:', errorData);
      
      // Create enhanced error with status code
      const error = new Error(errorData.error || 'Failed to get user') as any;
      error.status = response.status;
      throw error;
    }

    const data = await response.json();
    console.log('Current user retrieved successfully');
    return data;
  } catch (error) {
    console.error('Error in getCurrentUser:', error);
    throw error;
  }
};

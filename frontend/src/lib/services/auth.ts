/**
 * API service for authentication
 */

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://10.200.6.212:5001/api';

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
  const response = await fetch(`${API_URL}/auth/me`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    const errorData: AuthError = await response.json();
    throw new Error(errorData.error || 'Failed to get user');
  }

  return response.json();
};

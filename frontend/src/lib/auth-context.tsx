'use client';

import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { User, getCurrentUser } from '@/lib/services/auth';

interface AuthContextType {
  user: User | null;
  token: string | null;
  login: (token: string, userData: User) => void;
  logout: () => void;
  isLoading: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // Load user data from localStorage on initial load
  useEffect(() => {
    const loadStoredAuth = async () => {
      setIsLoading(true);
      
      try {
        // Check for token in localStorage
        const storedToken = localStorage.getItem('token');
        const storedUserJson = localStorage.getItem('user');
        
        if (storedToken && storedUserJson) {
          // First set the stored user data from localStorage
          try {
            const storedUser = JSON.parse(storedUserJson);
            setUser(storedUser);
            setToken(storedToken);
            
            // Then try to validate the token by making an API call
            getCurrentUser(storedToken)
              .then(response => {
                // Update with fresh user data from server
                setUser(response.user);
              })
              .catch(error => {
                console.error('Token validation failed:', error);
                // If token is invalid, clear everything
                setUser(null);
                setToken(null);
                localStorage.removeItem('token');
                localStorage.removeItem('user');
              });
          } catch (parseError) {
            console.error('Failed to parse stored user data:', parseError);
            localStorage.removeItem('user');
          }
        }
      } catch (error) {
        console.error('Auth initialization error:', error);
      } finally {
        setIsLoading(false);
      }
    };
    
    // Only run on client side
    if (typeof window !== 'undefined') {
      loadStoredAuth();
    } else {
      setIsLoading(false);
    }
  }, []);

  const login = (newToken: string, userData: User) => {
    setToken(newToken);
    setUser(userData);
    
    // Store in localStorage for persistence
    if (typeof window !== 'undefined') {
      localStorage.setItem('token', newToken);
      localStorage.setItem('user', JSON.stringify(userData));
    }
  };

  const logout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  };

  const value = {
    user,
    token,
    login,
    logout,
    isLoading
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}

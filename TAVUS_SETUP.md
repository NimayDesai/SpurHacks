# Tavus AI Setup Guide

## Getting Your Tavus API Key

1. **Sign up for Tavus**: Go to [https://tavus.io](https://tavus.io)
2. **Create an account**: Use your email to register
3. **Verify your email**: Check your inbox and verify
4. **Access the dashboard**: Navigate to the API section
5. **Generate API key**: Create a new API key for your project

## Free Tier Limits

- **10-15 minutes** of AI video generation per month
- Perfect for testing and demos
- No credit card required for free tier

## Environment Setup

1. Copy the `.env.example` to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Add your Tavus API key to `.env`:

   ```bash
   TAVUS_API_KEY=your_actual_tavus_api_key_here
   ```

3. Restart the backend server to load the new environment variables

## Testing Without Tavus API Key

If you don't have a Tavus API key yet, the application will still work:

- All WebRTC functionality works normally
- AI agent button will show an error message
- You can still use video calls and chat features

## Alternative: Mock AI Agent

For development/testing, you can enable a mock AI agent that simulates responses without using Tavus API. This is useful for frontend development and testing the chat interface.

The application is designed to gracefully handle missing API keys and will display appropriate error messages to users.

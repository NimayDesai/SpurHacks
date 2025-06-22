# Tavus Portal Setup Instructions

## Overview

Your application is now configured to work with Tavus AI agents. The backend creates real Tavus conversations and the frontend embeds them using iFrames for interactive video chat.

## Required: Tavus Portal Setup

### 1. Create a Tavus Account

1. Go to [https://www.tavus.io](https://www.tavus.io)
2. Sign up for an account (free tier available)
3. Verify your email address

### 2. Create a Replica (AI Avatar)

1. **Login to Tavus Dashboard**
2. **Navigate to "Replicas"** in the sidebar
3. **Click "Create Replica"**
4. **Upload Training Video**:
   - Record or upload a 2-5 minute video of someone speaking
   - Face should be clearly visible and well-lit
   - Speak naturally and make eye contact with camera
   - Various facial expressions and head movements are good
5. **Enter Replica Details**:
   - Name: "AI Assistant" (or your preferred name)
   - Description: "Interactive AI assistant for video calls"
6. **Wait for Processing**:
   - This can take 1-4 hours depending on queue
   - You'll receive an email when it's ready

### 3. Get Your API Key

1. **Go to "Developer" section** in Tavus dashboard
2. **Click "API Keys"**
3. **Create New API Key**:
   - Name: "SpurHacks App"
   - Permissions: All (for full functionality)
4. **Copy the API Key**: Save it securely

### 4. Configure Your Environment

Your API key is already set in `/backend/.env`. If you need to update it:

```bash
# Update backend/.env
TAVUS_API_KEY=your_actual_api_key_here
```

### 5. Test Your Setup

1. **Start Backend**: `cd backend && python main.py`
2. **Start Frontend**: `cd frontend && npm run dev`
3. **Open**: http://localhost:3000
4. **Login/Signup** with your account
5. **Click "Start Video Call with AI"**
6. **Click "Add AI Agent"** (dark button on the right)
7. **Wait for Tavus iframe to load**

## How It Works

### Backend Flow

1. When user clicks "Add AI Agent", frontend sends request to backend
2. Backend calls Tavus API to create a new conversation
3. Tavus returns a conversation URL (not a video file)
4. Backend sends this URL to frontend via WebSocket

### Frontend Flow

1. Frontend receives the conversation URL
2. Displays Tavus conversation in an `<iframe>`
3. User can interact directly with AI through the iframe
4. All video/audio processing happens within Tavus's interface

### Real Interaction

- The AI can see and hear the user through their webcam/microphone
- The AI responds with video and audio in real-time
- All conversation happens within the Tavus iframe
- No additional chat interface needed - everything is in the video

## Troubleshooting

### "No Replica Available" Error

- **Cause**: No replica has been created yet
- **Solution**: Complete step 2 above (create a replica)
- **Note**: Processing can take 1-4 hours

### "API Key Invalid" Error

- **Cause**: API key is missing or incorrect
- **Solution**: Update `.env` file with correct API key
- **Restart**: Backend server after updating `.env`

### "Conversation Failed to Load" Error

- **Cause**: Network issues or API limits
- **Solution**: Check internet connection and API usage limits
- **Free Tier**: Limited to ~10-15 minutes per month

### AI Not Responding in Video

- **Cause**: Microphone permissions or browser issues
- **Solution**:
  - Allow microphone/camera permissions
  - Try in Chrome/Safari (best supported)
  - Refresh page and try again

## Free Tier Limitations

- **Monthly Limit**: 10-15 minutes of AI conversation
- **Replicas**: 1-2 free replicas
- **Processing Time**: 1-4 hours for replica creation
- **Usage**: Perfect for demos and testing

## Production Considerations

- Upgrade to paid plan for production use
- Consider rate limiting on your backend
- Add error handling for API failures
- Monitor usage to avoid hitting limits

## Current Status

✅ Backend configured for real Tavus integration  
✅ Frontend updated to use iframe embedding  
✅ API key configured  
⏳ **NEXT STEP**: Create a replica in Tavus portal

Once you create a replica in the Tavus portal, the AI agent will be fully functional with real video conversation capabilities.

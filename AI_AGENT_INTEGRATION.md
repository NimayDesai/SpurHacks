# Adding AI Agent to WebRTC Video Calls

## Current Implementation

The WebRTC video call interface is now implemented with:

- **Frontend**: React-based video call interface (`/meet` page) using Socket.IO
- **Backend**: Flask-SocketIO server handling WebRTC signaling
- **Features**: Room creation/joining, video/audio controls, real-time communication

## Adding an AI Agent (HeyGen or Alternatives)

### Option 1: HeyGen API Integration (Recommended)

HeyGen provides avatar-based AI agents that can join video calls. Here's how to integrate:

#### Backend Changes Needed:

1. **Create AI Agent Service** (`backend/services/ai_agent.py`):

```python
import requests
import asyncio
from typing import Optional

class HeyGenAgent:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.heygen.com"

    async def create_avatar_session(self, room_id: str):
        # Create a HeyGen avatar session
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {
            "avatar_id": "your_avatar_id",
            "room_id": room_id,
            "voice_settings": {"voice_id": "en-US-female"}
        }
        response = requests.post(f"{self.base_url}/avatar/create_session",
                               headers=headers, json=data)
        return response.json()

    async def send_message(self, session_id: str, message: str):
        # Send text for the avatar to speak
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"text": message, "session_id": session_id}
        response = requests.post(f"{self.base_url}/avatar/speak",
                               headers=headers, json=data)
        return response.json()
```

2. **Update WebRTC Routes** (`backend/routes/webrtc.py`):

```python
from services.ai_agent import HeyGenAgent

ai_agent = HeyGenAgent(os.getenv('HEYGEN_API_KEY'))

@socketio.on('request-ai-agent', namespace='/meet')
def handle_ai_agent_request(data):
    room_id = data.get('roomId')
    # Create HeyGen session and add to room
    session = ai_agent.create_avatar_session(room_id)
    emit('ai-agent-joined', {'agent_data': session}, room=room_id)
```

#### Frontend Changes:

3. **Add AI Agent Controls** to `meet/page.tsx`:

```typescript
const [aiAgentActive, setAiAgentActive] = useState(false);

const requestAiAgent = () => {
  if (socketRef.current) {
    socketRef.current.emit("request-ai-agent", { roomId });
  }
};

// Add to controls section:
<Button
  onClick={requestAiAgent}
  variant={aiAgentActive ? "default" : "outline"}
  size="lg"
>
  🤖 AI Agent
</Button>;
```

### Option 2: Alternative Free AI Agents

Since HeyGen can be expensive, here are free alternatives:

#### 2A. OpenAI + Text-to-Speech + Avatar

1. **Backend Service** (`backend/services/openai_agent.py`):

```python
import openai
from gtts import gTTS
import tempfile
import base64

class OpenAIAgent:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    async def generate_response(self, user_input: str):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant in a video call."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content

    async def text_to_speech(self, text: str):
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp:
            tts.save(tmp.name)
            with open(tmp.name, 'rb') as audio_file:
                audio_data = base64.b64encode(audio_file.read()).decode()
        return audio_data
```

#### 2B. Ready Player Me + Eleven Labs

1. **3D Avatar**: Use Ready Player Me for free 3D avatars
2. **Voice**: Eleven Labs for high-quality text-to-speech
3. **Integration**: Stream avatar video with synchronized audio

### Option 3: Simple AI Chat Integration

For a minimal implementation:

#### Backend Addition (`backend/routes/ai_chat.py`):

```python
@app.route('/api/ai/chat', methods=['POST'])
def ai_chat():
    user_message = request.json.get('message')

    # Use OpenAI API (free tier available)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    ai_response = response.choices[0].message.content

    return jsonify({
        'response': ai_response,
        'timestamp': datetime.now().isoformat()
    })
```

#### Frontend Chat Component:

```typescript
const [chatMessages, setChatMessages] = useState<
  Array<{
    text: string;
    sender: "user" | "ai";
    timestamp: string;
  }>
>([]);

const sendChatMessage = async (message: string) => {
  const response = await fetch("/api/ai/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  const data = await response.json();
  setChatMessages((prev) => [
    ...prev,
    { text: message, sender: "user", timestamp: new Date().toISOString() },
    { text: data.response, sender: "ai", timestamp: data.timestamp },
  ]);
};
```

## Implementation Steps (Recommended Approach)

### Phase 1: Basic AI Chat (Free)

1. Add OpenAI API integration
2. Create chat interface in video call
3. Allow users to text-chat with AI during calls

### Phase 2: Voice AI (Low Cost)

1. Add speech-to-text for user input
2. Add text-to-speech for AI responses
3. Integrate with video call audio

### Phase 3: Visual Avatar (Premium)

1. Integrate HeyGen or similar service
2. Add avatar video stream to WebRTC
3. Synchronize avatar movements with speech

## Required Environment Variables

Add to your `.env` file:

```
OPENAI_API_KEY=your_openai_key
HEYGEN_API_KEY=your_heygen_key  # if using HeyGen
ELEVENLABS_API_KEY=your_elevenlabs_key  # if using ElevenLabs
```

## Files to Create/Modify

1. **Backend**:

   - `services/ai_agent.py` - AI agent service
   - `routes/ai_chat.py` - AI chat endpoints
   - Update `main.py` to include new routes

2. **Frontend**:

   - `components/ai-chat.tsx` - Chat interface
   - `components/ai-avatar.tsx` - Avatar display
   - Update `meet/page.tsx` - Integrate AI features

3. **Utils**:
   - `utils/speech.ts` - Speech recognition/synthesis
   - `utils/audio.ts` - Audio processing

The simplest start would be Option 3 (AI Chat) as it requires minimal setup and provides immediate value. You can then progressively enhance with voice and visual features.

Would you like me to implement any of these specific approaches?

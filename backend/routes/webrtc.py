"""WebRTC signaling routes for video calls."""

import json
import logging
from flask import request
from flask_socketio import SocketIO, emit, join_room, leave_room, rooms
from collections import defaultdict
import requests
import os

logger = logging.getLogger(__name__)

# Store active rooms and their participants
active_rooms = defaultdict(set)
user_rooms = {}
room_ai_agents = {}  # Track AI agents in rooms

def init_webrtc_routes(socketio: SocketIO):
    """Initialize WebRTC signaling routes."""
    
    @socketio.on('connect', namespace='/meet')
    def handle_connect():
        """Handle client connection."""
        logger.info(f"Client connected: {request.sid}")
        emit('connected', {'status': 'success'})
    
    @socketio.on('disconnect', namespace='/meet')
    def handle_disconnect():
        """Handle client disconnection."""
        logger.info(f"Client disconnected: {request.sid}")
        
        # Remove user from their room
        if request.sid in user_rooms:
            room_id = user_rooms[request.sid]
            leave_room(room_id)
            active_rooms[room_id].discard(request.sid)
            
            # Notify other participants
            emit('user-left', {
                'userId': request.sid
            }, room=room_id)
            
            # Clean up empty rooms
            if not active_rooms[room_id]:
                del active_rooms[room_id]
            
            del user_rooms[request.sid]
    
    @socketio.on('join-room', namespace='/meet')
    def handle_join_room(data):
        """Handle user joining a room."""
        room_id = data.get('roomId')
        if not room_id:
            emit('error', {'message': 'Room ID is required'})
            return
        
        # Join the room
        join_room(room_id)
        active_rooms[room_id].add(request.sid)
        user_rooms[request.sid] = room_id
        
        logger.info(f"User {request.sid} joined room {room_id}")
        
        # Notify existing participants about new user
        emit('user-joined', {
            'userId': request.sid,
            'roomId': room_id
        }, room=room_id, include_self=False)
        
        # Send current participants to new user
        participants = list(active_rooms[room_id] - {request.sid})
        emit('room-joined', {
            'roomId': room_id,
            'participants': participants
        })
        
        # If there's already someone in the room, start the call
        if len(active_rooms[room_id]) > 1:
            # The new user should create an offer
            emit('initiate-call', {
                'shouldCreateOffer': True
            })
    
    @socketio.on('offer', namespace='/meet')
    def handle_offer(data):
        """Handle WebRTC offer."""
        room_id = user_rooms.get(request.sid)
        if not room_id:
            emit('error', {'message': 'Not in a room'})
            return
        
        logger.info(f"Received offer from {request.sid} in room {room_id}")
        
        # Forward offer to other participants in the room
        emit('offer', {
            'offer': data.get('offer'),
            'from': request.sid
        }, room=room_id, include_self=False)
    
    @socketio.on('answer', namespace='/meet')
    def handle_answer(data):
        """Handle WebRTC answer."""
        room_id = user_rooms.get(request.sid)
        if not room_id:
            emit('error', {'message': 'Not in a room'})
            return
        
        logger.info(f"Received answer from {request.sid} in room {room_id}")
        
        # Forward answer to other participants in the room
        emit('answer', {
            'answer': data.get('answer'),
            'from': request.sid
        }, room=room_id, include_self=False)
    
    @socketio.on('ice-candidate', namespace='/meet')
    def handle_ice_candidate(data):
        """Handle ICE candidate."""
        room_id = user_rooms.get(request.sid)
        if not room_id:
            emit('error', {'message': 'Not in a room'})
            return
        
        # Forward ICE candidate to other participants in the room
        emit('ice-candidate', {
            'candidate': data.get('candidate'),
            'from': request.sid
        }, room=room_id, include_self=False)
    
    @socketio.on('leave-room', namespace='/meet')
    def handle_leave_room():
        """Handle user leaving a room."""
        if request.sid in user_rooms:
            room_id = user_rooms[request.sid]
            leave_room(room_id)
            active_rooms[room_id].discard(request.sid)
            
            # Notify other participants
            emit('user-left', {
                'userId': request.sid
            }, room=room_id)
            
            # Clean up empty rooms
            if not active_rooms[room_id]:
                del active_rooms[room_id]
            
            del user_rooms[request.sid]
            
            logger.info(f"User {request.sid} left room {room_id}")
            
            emit('left-room', {'status': 'success'})
    
    @socketio.on('request-ai-agent', namespace='/meet')
    def handle_request_ai_agent(data):
        """Handle request to add AI agent to room."""
        room_id = data.get('roomId', 'main-room')
        
        try:
            logger.info(f"Creating Tavus AI agent for room {room_id}")
            
            # HARDCODED AI CONFIGURATION - EDIT THESE VALUES DIRECTLY:
            persona_instructions = "The first thing you will do is read the script and time your self according to the time stamps but don't say the time stamps out loud. Then you will respond to the user in a helpful and insightful way. If they ask questions that are irrelavent, respond in a kind way that veers them back to the subject. If they ask about a related topic that is very vast in nature (i.e. explaining something that can't be learnt quickly, recommend them to asking the program a new prompt.)"
            custom_script = ""
            conversation_style = "polite, insighful, focused, and helpful"
            knowledge_base = "General knowledge and helpful information"
            
            logger.info(f"Using hardcoded persona_instructions: '{persona_instructions}'")
            logger.info(f"Using hardcoded custom_script: '{custom_script}'")
            logger.info(f"Using hardcoded conversation_style: '{conversation_style}'")
            
            # Import Tavus agent service
            from services.tavus_agent import TavusAgent
            import os
            
            tavus_agent = TavusAgent(os.getenv('TAVUS_API_KEY', ''))
            
            if not tavus_agent.api_key:
                logger.error("No Tavus API key found")
                emit('error', {'message': 'Tavus API key not configured'})
                return
            
            # Use your specific replica ID
            replica_id = os.getenv('TAVUS_REPLICA_ID', 'r1a4e22fa0d9')
            logger.info(f"Using your replica: {replica_id}")
            
            # Test the replica first
            replica_test = tavus_agent.test_replica(replica_id)
            if not replica_test:
                logger.error(f"Replica {replica_id} is not available")
                emit('error', {'message': f'Your replica {replica_id} is not ready. Please check Tavus dashboard.'})
                return
            
            logger.info(f"Replica test successful: {replica_test.get('name', 'Unknown')}")
            
            # Clean up any active conversations first to free up slots
            logger.info("Cleaning up active conversations...")
            ended_count = tavus_agent.cleanup_active_conversations()
            if ended_count > 0:
                logger.info(f"Ended {ended_count} active conversations")
                # Wait a moment for cleanup to complete
                import time
                time.sleep(2)
            
            # Create a conversation with your specific replica
            conversation_response = tavus_agent.create_conversation(
                replica_id=replica_id,
                persona_instructions=persona_instructions,
                custom_script=custom_script,
                conversation_style=conversation_style
            )
            
            if not conversation_response:
                logger.error("Failed to create Tavus conversation")
                emit('error', {'message': 'Failed to create AI conversation. Please try again in a moment.'})
                return
            
            # Get conversation details
            conversation_id = conversation_response.get('conversation_id')
            conversation_url = tavus_agent.get_conversation_url(conversation_id)
            
            if not conversation_url:
                # Fallback URL construction
                conversation_url = f"https://tavus.daily.co/{conversation_id}"
            
            logger.info(f"Conversation created with custom script context: {conversation_id}")
            
            # Create agent data with hardcoded configuration
            agent_data = {
                'agent_id': f'tavus_agent_{room_id}',
                'conversation_id': conversation_id,
                'conversation_url': conversation_url,
                'replica_id': replica_id,
                'agent_name': replica_test.get('name', 'Your AI Assistant'),
                'status': 'active',
                'type': 'tavus_conversation',
                'persona_instructions': persona_instructions,
                'custom_script': custom_script,
                'knowledge_base': knowledge_base,
                'conversation_style': conversation_style
            }
            
            room_ai_agents[room_id] = agent_data
            
            logger.info(f"Tavus AI agent created successfully: {agent_data}")
            
            # Notify all participants that AI agent joined
            emit('ai-agent-joined', {
                'agent_data': agent_data,
                'room_id': room_id
            }, room=room_id)
                
        except Exception as e:
            logger.error(f"Error requesting Tavus AI agent: {e}")
            emit('error', {'message': f'Error creating AI agent: {str(e)}'})
    
    @socketio.on('send-to-ai', namespace='/meet')
    def handle_send_to_ai(data):
        """Handle message sent to AI agent."""
        room_id = data.get('roomId', 'main-room')
        message = data.get('message', '').strip()
        
        if not message:
            emit('error', {'message': 'Message required'})
            return
        
        try:
            logger.info(f"User message to Tavus AI in room {room_id}: {message}")
            
            # Get the active AI agent for this room
            agent_data = room_ai_agents.get(room_id)
            
            if not agent_data:
                emit('error', {'message': 'No AI agent active in this room'})
                return
            
            # Import Tavus agent service
            from services.tavus_agent import TavusAgent
            import os
            
            tavus_agent = TavusAgent(os.getenv('TAVUS_API_KEY', ''))
            
            # For Tavus, we can send messages directly to the conversation
            conversation_id = agent_data.get('conversation_id')
            if conversation_id:
                # Send message to Tavus conversation
                response = tavus_agent.send_message(conversation_id, message)
                
                if response:
                    ai_response = "I received your message! I'll respond through the video interface above with full audio and video."
                else:
                    ai_response = "I'm listening! Continue talking to me through the video interface for the full conversational experience."
            else:
                ai_response = "I'm ready to chat! Use the video interface above for our full conversation with audio and video."
            
            # Add a small delay to make it feel more natural
            import time
            time.sleep(0.5)
            
            # Notify room that message was sent to AI and show AI response
            emit('ai-message-sent', {
                'user_message': message,
                'ai_response': ai_response,
                'sender': request.sid,
                'timestamp': time.time(),
                'note': 'Main conversation happens in the video interface above'
                
            }, room=room_id)
            
            logger.info(f"Tavus AI acknowledged message in room {room_id}")
                
        except Exception as e:
            logger.error(f"Error sending message to Tavus AI: {e}")
            emit('error', {'message': f'Error sending message to AI: {str(e)}'})

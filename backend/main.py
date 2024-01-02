from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
from pydantic import BaseModel
from openai import OpenAI
import os
import uuid
from pymongo import MongoClient
from dotenv import load_dotenv

class ChatMessage(BaseModel):
    message: str
    sender: str  # 'user' or 'bot'

class ChatSession(BaseModel):
    session_id: str
    email: None
    conversation: List[ChatMessage]

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Configure MongoDB Connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client.chatbot_db

# Configure OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID")

# WebSocket Endpoint
@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket, session_id: str = "", email: str = None):
    await websocket.accept()

    if not session_id:
        session_id = str(uuid.uuid4())
    
    conversation = []

    # Create a new thread
    thread = client.beta.threads.create()

    try:
        while True:
            data = await websocket.receive_text()
            user_message = ChatMessage(message=data, sender='user')
            conversation.append(user_message)

            # Add message to the thread
            message = client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=data
            )

            # Run the assistant
            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=ASSISTANT_ID,
                instructions="Please provide a response."
            )

            # Monitor the run status
            while True:
                run_status = client.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id
                )
                if run_status.status == 'completed':
                    print("Run status:", run_status)
                    break

            # Retrieve messages from the assistant
            messages = client.beta.threads.messages.list(thread_id=thread.id)

            # Assuming the last message is from the assistant
            bot_message_text = messages.data[0].content[0].text.value if messages.data else "Sorry, I couldn't process that."
            bot_message = ChatMessage(message=bot_message_text, sender='bot')
            conversation.append(bot_message)
            await websocket.send_text(bot_message.message)

    except WebSocketDisconnect:
        # Save conversation to MongoDB
        chat_session = ChatSession(session_id=session_id, email=email, conversation=conversation)
        db.sessions.insert_one(chat_session.dict())

        print(f"Session {session_id} ended.")

    except Exception as e:
        print(f"Error: {e}")
# Run the server using: uvicorn your_file_name:app --reload

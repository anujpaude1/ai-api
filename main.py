from fastapi import FastAPI, HTTPException, Request, WebSocket
from aiModels.claude import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Load Claude cookie from environment variables
claudeCookie = os.getenv("claudeCookie")
claude = Client(claudeCookie)

# Define route for sending message
@app.post('/claude/send-message')
async def send_message(request: Request):
    # Get the conversation IDs
    conversationIDs = claude.list_all_conversations()
    lastestCID = conversationIDs[-1]["uuid"]

    # Get the prompt from request
    data = await request.json()
    prompt = data.get('prompt')

    # Send message to Claude and get the response
    response = claude.send_message(prompt, lastestCID)

    return response

@app.post("/claude/delete-conversation")
async def delete_conversation(conversation_id):
    success = claude.delete_conversation(conversation_id.conversation_id)
    if success:
        return {"message": "Conversation deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to delete conversation")

@app.post("/claude/new-chat")
async def new_chat():
    new_chat_info = claude.create_new_chat()
    return new_chat_info["uuid"]

# WebSocket endpoint for streaming messages
@app.websocket("/claude/stream-message/{conversation_id}")
async def stream_message(websocket: WebSocket, conversation_id: str):
    await websocket.accept()

    async for message in claude.stream_message("", conversation_id):
        await websocket.send_text(message)

        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

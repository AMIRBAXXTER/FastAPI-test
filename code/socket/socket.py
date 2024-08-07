import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from code.models.message import Message
from code.crud.message import create_message
from code.db.database import mongodb

sio = socketio.AsyncServer(async_mode="asgi")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/ws", socketio.ASGIApp(sio))

online_users = {}


@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")


@sio.event
async def disconnect(sid):
    if sid in online_users:
        del online_users[sid]
    print(f"Client disconnected: {sid}")


@sio.event
async def join(sid, data):
    username = data["username"]
    online_users[sid] = username
    await sio.emit("online_users", list(online_users.values()))


@sio.event
async def send_message(sid, data):
    message = Message(**data)
    await create_message(mongodb.db, message)
    await sio.emit("new_message", data, room=message.group_id or message.receiver_id)

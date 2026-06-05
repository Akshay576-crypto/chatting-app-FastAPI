from fastapi import WebSocket
from typing import List

class ConnectionManager:

    def __init__(self):

        self.active_connection : List[WebSocket] = []

    async def connect(self,websocket:WebSocket):

        await websocket.accept()
        self.active_connection.append(websocket)

    def disconnect(self,websocket:WebSocket):

        self.active_connection.remove(websocket)

    async def send_personal_messages(self,websocket:WebSocket,messages:str):

        await websocket.send_text(messages)
        
    async def broadcast(self,messages:str):

        for connection in self.active_connection:

            await connection.send_text(messages)

manager = ConnectionManager()




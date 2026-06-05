from fastapi import APIRouter
from app.schemas.messages_schema import MessageSchema
from app.databases.message_query import save_message , get_message

router = APIRouter()

@router.post("/send_message")
async def send_message(data:MessageSchema):

    save_message(sender_id=data.sender_id , receiver_id=data.receiver_id,message=data.message)

    return {"Message":"Message Sent Successfully"}


@router.get("/get-messages")
async def fetch_messages(sender_id:int,receiver_id:int):

    messages = get_message(sender_id,receiver_id)

    return {"Messages":messages}


from fastapi import FastAPI ,Request, Form
from app.routes.chat_routes import router as chat_router
from app.routes.users_routes import router as user_router
from fastapi import WebSocket
from app.websocket.chat_socket import manager
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.database import get_db_connection
from fastapi.responses import RedirectResponse
from app.databases.saver_message import insert_message




app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static",StaticFiles(directory="app/templates/static"),name="static")

#app.include_router(user_router)
app.include_router(chat_router)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request,name="index.html")

@app.get("/login")
async def login_page(request:Request):
    return templates.TemplateResponse(request=request,name="login.html")

@app.post("/login")
async def login_user(request:Request , email : str = Form(...),password: str = Form(...)):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s",(email,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    if not user:
        return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "request": request,
            "error": "User Not Found"
        }
    )

    
    if user["password"]!= password:
        return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "request": request,
            "error": "Wrong Password"
        }
    )
    
    return RedirectResponse(url="/chat",status_code=303)


@app.get("/signup")
async def signup(request:Request):
    return templates.TemplateResponse(request=request,name="signup.html")


@app.get("/otp")
async def otp(request:Request):
    return templates.TemplateResponse(request=request,name="otp.html")


@app.get("/forgetpassword")
async def forget_password(request:Request):
    return templates.TemplateResponse(request=request,name="forgetpassword.html")


@app.get("/chat")
async def chat(request:Request):
    return templates.TemplateResponse(request=request,name="chat.html")




@app.get("/profile")
async def profile(request:Request):
    return templates.TemplateResponse(request=request,name="profile.html")


@app.get("/settings")
async def settings(request:Request):
    return templates.TemplateResponse(request=request,name="settings.html")


@app.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):

    await manager.connect(websocket)
    print("Connection Started")

    try:

        while True:

            data = await websocket.receive_text()
            print(f"Received message: {data}")

            sender_id = 1
            receiver_id = 2

            insert_message(sender_id,receiver_id,data)

            
            await manager.broadcast(f"message:{data}")

    except:
        manager.disconnect(websocket)
        print("Connection Closed")
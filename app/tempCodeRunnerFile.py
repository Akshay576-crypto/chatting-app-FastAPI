from fastapi import FastAPI ,Request, Form
from app.routes.chat_routes import router as chat_router
from app.routes.users_routes import router as user_router
from fastapi import WebSocket
from app.websocket.chat_socket import manager
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.database import get_db_connection
from fastapi.responses import RedirectResponse




app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static",StaticFiles(directory="app/templates/static"),name="static")

#app.include_router(user_router)
app.include_router(chat_router)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request,name="index.html")

@app.get("/login")
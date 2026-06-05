from fastapi import APIRouter , HTTPException , Depends , Header
from app.schemas.user_schema import UserSignup
from app.databases.user_query import (create_user,get_user_by_email)
from app.schemas.login_schema import Userlogin
from app.utils.password_utils import verify_password
from app.utils.jwt_utils import create_access_token
from mysql.connector.errors import IntegrityError
from app.dependencies import verify_access_token

router = APIRouter()

@router.post("/signup")
async def signup(user:UserSignup):
    try:
            
        create_user(username=user.username,email=user.email,password=user.password)

        return{"Message":"User Created "}

        
    except IntegrityError:
        raise HTTPException(status_code=404 , detail="User Already Exist")


@router.post("/login")
async def login(user:Userlogin):

    db_user = get_user_by_email(user.email)

    if not db_user:

        raise HTTPException(status_code=404 , detail="User Not Found")
    
    password_valid = verify_password(user.password , db_user["password"])

    if not password_valid:

        raise HTTPException(status_code=404 , detail="Password Invalid")
    
    access_token = create_access_token({"sub":db_user["email"]})

    return {"access token":access_token ,
            "token_type": "bearer"}

@router.get("/current_user")
async def current_user( authorization: str = Header(None)):

    return {"Token_user":authorization}
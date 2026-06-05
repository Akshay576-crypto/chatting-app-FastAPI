from app.schemas.user_schema import UserSignup


user = UserSignup(

    username="Akshay",

    email="akshay@gmail.com",

    password="123456"

)

print(user)
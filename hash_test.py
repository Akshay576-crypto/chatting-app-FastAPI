from app.utils.password_utils import hash_password


password = "123456"

hashed = hash_password(password)

print(hashed)
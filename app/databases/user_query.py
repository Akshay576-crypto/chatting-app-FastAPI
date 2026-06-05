from app.database import get_db_connection
from app.utils.password_utils import hash_password

def create_user(username,email,password):
    connection = get_db_connection()

    cursor = connection.cursor()

    hashed_password = hash_password(password)

    query = """INSERT INTO users(username,email,password) VALUES(%s,%s,%s)"""

    values = (username,email,hashed_password)

    cursor.execute(query,values)

    connection.commit()

    cursor.close()

    connection.close()

def get_user_by_email(email):

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    query = """SELECT * FROM users where email = %s"""

    cursor.execute(query,(email,))

    user = cursor.fetchone()

    cursor.close()

    connection.close()

    return user



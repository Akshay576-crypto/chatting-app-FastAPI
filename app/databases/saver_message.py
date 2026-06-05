from app.database import get_db_connection

def insert_message(sender_id:int , receiver_id:int ,message:str):

    db = get_db_connection()

    cursor = db.cursor()

    query = """INSERT INTO messages (sender_id, receiver_id, message)VALUES (%s, %s, %s)"""

    cursor.execute(query,(sender_id,receiver_id,message))

    db.commit()
    cursor.close()
    db.close()
    
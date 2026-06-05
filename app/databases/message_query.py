from app.database import get_db_connection

def save_message(sender_id,receiver_id,message):

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """INSERT INTO messages (sender_id,receiver_id,message) VALUES(%s,%s,%s)"""

    values = (sender_id,receiver_id,message)

    cursor.execute(query,values)

    connection.commit()
    cursor.close()
    connection.close()

def get_message(sender_id,receiver_id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """SELECT * FROM messages WHERE (sender_id = %s AND receiver_id = %s)
    OR (sender_id = %s AND receiver_id = %s) ORDER BY created_at ASC"""

    values = (sender_id,receiver_id,receiver_id,sender_id)

    cursor.execute(query,values)

    messages = cursor.fetchall()
    cursor.close()
    connection.close()

    return messages

    

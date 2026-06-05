from app.database import get_db_connection

connection = get_db_connection()

print("Data Base connect Sucessfully :",connection)

connection.close()

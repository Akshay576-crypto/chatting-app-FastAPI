import mysql.connector

from app.config import settings


def get_db_connection():

    connection = mysql.connector.connect(

        host=settings.MYSQL_HOST,

        user=settings.MYSQL_USER,

        password=settings.MYSQL_PASSWORD,

        database=settings.MYSQL_DATABASE

    )

    return connection
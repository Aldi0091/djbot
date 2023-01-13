import psycopg2
from .config import host, user, password, db_name

class Postgres:

    @classmethod
    def insert_id(cls, user_id, token):
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    f"UPDATE api_user SET telegram_id={user_id} WHERE token='{token}'"
                )

        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection was closed")
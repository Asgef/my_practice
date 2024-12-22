import psycopg2
from psycopg2.extras import DictCursor
from models import User
from urllib.parse import urlparse
from python_sql.settings import DATABASE_URL

parsed_url = urlparse(DATABASE_URL)

dbname = parsed_url.path.lstrip('/')
user = parsed_url.username
password = parsed_url.password
hostname = parsed_url.hostname


def get_connection():
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=hostname,
        cursor_factory=DictCursor
    )


def commit(conn):
    conn.commit()

def save_user(conn, user):
    with conn.cursor() as cur:
        if user.id is None:
            cur.execute(
                "INSERT INTO users (username, phone) VALUES (%s, %s) RETURNING id;",
                (user.username, user.phone)
            )
            user.id = cur.fetchone()['id']
        else:
            cur.execute(
                "UPDATE users SET username = %s, phone = %s WHERE id = %s;",
                (user.username, user.phone, user.id)
            )
    return user


def find_user(conn, user_id):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
        result = cur.fetchone()
        if result:
            return User(**result)
    return None


def delete_user(connect, user_id):
    sql = f'''
    DELETE FROM users WHERE id = %(user_id)s;
    '''
    with connect.cursor() as curs:
        curs.execute(sql, {'user_id': user_id})
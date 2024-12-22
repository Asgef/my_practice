import psycopg2
from psycopg2.extras import execute_batch, execute_values, NamedTupleCursor
import dotenv
import os

dotenv.load_dotenv()
DB_PASS = os.getenv("DB_PASS")

# try:
#     conn = psycopg2.connect(
#         "dbname='example_hexlet' user='asgef' host='localhost' password={}".format(DB_PASS)
#     )
# except Exception as e:
#     print(f'Can`t establish connection to database. Error: {e}')
#

# try:
#     # пытаемся подключиться к базе данных
#     conn = psycopg2.connect('postgresql://user:password@host:port/database_name')
# except:
#     # в случае сбоя подключения будет выведено сообщение  в STDOUT
#     print('Can`t establish connection to database')


# sql = "CREATE TABLE users (id BIGSERIAL PRIMARY KEY, username VARCHAR(255), phone VARCHAR(255))"
# # Запрос выполняется через создание объекта курсора
# cursor = conn.cursor()
# cursor.execute(sql)
# cursor.close()
#
#
# sql2 = "INSERT INTO users (username, phone) VALUES ('tommy', '123456789');"
#
# cursor = conn.cursor()
# cursor.execute(sql2)
# cursor.close()
#
#
# sql3 = "SELECT * FROM users;"
# cursor = conn.cursor()
# # Указатель на набор данных в памяти СУБД
# cursor.execute(sql3)
# for row in cursor:
#     print(row)
#
# cursor.close()
# conn.commit()
# conn.close()

def get_all_users(connect):
    sql = '''
    SELECT * FROM users;
    '''
    with connect.cursor() as curs:
        curs.execute(sql)
        result = curs.fetchall()
    return result


# Контекстный менеджер и плейсхолдеры в sql запросе

# def delete_user(connect, name):
#     sql = f'''
#     DELETE FROM users WHERE username = %s;
#     '''
#     with connect.cursor() as curs:
#         curs.execute(sql, (name,))
#
#
# with psycopg2.connect("dbname='example_hexlet' user='asgef' host='localhost' password={}".format(DB_PASS)) as conn:
#     name = 'asgef'
#     phone = '1432523534'
#     sql = f"INSERT INTO users (username, phone) VALUES(%s, %s);"
#
#     with conn.cursor() as curs:
#         curs.execute(sql, (name, phone,))
#
#     delete_user(conn, 'asgef')
#     print(print_all_users(conn))

# Именованные плейсхолдеры


def delete_user(connect, name):
    sql = f'''
    DELETE FROM users WHERE username = %(name)s;
    '''
    with connect.cursor() as curs:
        curs.execute(sql, {'name': name})


# with psycopg2.connect("dbname='example_hexlet' user='asgef' host='localhost' password={}".format(DB_PASS)) as conn:
#     name = 'asgef'
#     phone = '1432523534'
#     sql = f"INSERT INTO users (username, phone) VALUES(%(name)s, %(phone)s);"

    # with conn.cursor() as curs:
    #     curs.execute(sql, {'name': name, 'phone': phone})

    # delete_user(conn, 'asgef')
    # print(f'Метод execute >>>>>>>>>: {print_all_users(conn)}')
    #
    # users = [
    #     {'name': 'igor', 'phone': '1112223333'},
    #     {'name': 'anna', 'phone': '4445556666'},
    #     {'name': 'max', 'phone': '7778889990'},
    #     {'name': 'ivan', 'phone': '9876543210'},
    #     {'name': 'petr', 'phone': '5551234567'}
    # ]
    #
    # with conn.cursor() as curs:
    #     execute_batch(curs, sql, users)
    #
    # print(f'Метод execute_batch >>>>>>>>>: {print_all_users(conn)}')

    # sql_2 = f"INSERT INTO users (username, phone) VALUES (%s, %s) RETURNING id;"
    #
    # with conn.cursor() as curs:
    #     curs.execute(sql_2, ('mark', 559084737652))
    #     id = curs.fetchone()[0]
    # print(id)


    # Серверный курсор

    # with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
    #     sql = "SELECT MAX(id) FROM users;"
    #     curs.execute(sql)
    #     print(curs.fetchall())
    #
    # with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
    #     sql = "SELECT * FROM users;"
    #     curs.execute(sql)
    #     rec = curs.fetchmany(size=5)
    #     print(rec[4]['username'])


    # Транзакции

# conn = psycopg2.connect("dbname='example_hexlet' user='asgef' host='localhost' password={}".format(DB_PASS))
# sql = f'''
#     DELETE FROM users WHERE username = %(name)s;
#     '''
# curs = conn.cursor()
# try:
#     curs.execute(sql, {'name': 'timmy'})
#     raise Exception("Ошибка во время транзакции")
# except Exception as e:
#     print(e)
# finally:
#     conn.close()
#
# with psycopg2.connect("dbname='example_hexlet' user='asgef' host='localhost' password={}".format(DB_PASS)) as conn:
#     print(get_all_users(conn))


# DAO


# Пример использования:

from models import User
import db

conn = db.get_connection()


user = User(username="John Doe", phone="1234567890")
print(user.id) # None

new_user = db.save_user(conn, user)
# делаем коммит после каждого изменения
db.commit(conn)
print(new_user.id) # тут уже выводится какой-то id

found_user = db.find_user(conn, 42)
db.commit(conn)
print(found_user) # здесь выводится найденный user

print(get_all_users(conn))
db.commit(conn)

db.delete_user(conn, new_user.id)
db.commit(conn)

print(get_all_users(conn))
# закрываем соединение
conn.close()
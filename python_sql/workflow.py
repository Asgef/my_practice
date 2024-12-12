import psycopg2
import dotenv
import os

dotenv.load_dotenv()
DB_PASS = os.getenv("DB_PASS")

try:
    conn = psycopg2.connect(
        "dbname='example_hexlet' user='asgef' host='localhost' password={}".format(DB_PASS)
    )
except Exception as e:
    print(f'Can`t establish connection to database. Error: {e}')


# try:
#     # пытаемся подключиться к базе данных
#     conn = psycopg2.connect('postgresql://user:password@host:port/database_name')
# except:
#     # в случае сбоя подключения будет выведено сообщение  в STDOUT
#     print('Can`t establish connection to database')


sql = "CREATE TABLE users (id BIGSERIAL PRIMARY KEY, username VARCHAR(255), phone VARCHAR(255))"
# Запрос выполняется через создание объекта курсора
cursor = conn.cursor()
cursor.execute(sql)
cursor.close()


sql2 = "INSERT INTO users (username, phone) VALUES ('tommy', '123456789');"

cursor = conn.cursor()
cursor.execute(sql2)
cursor.close()


sql3 = "SELECT * FROM users;"
cursor = conn.cursor()
# Указатель на набор данных в памяти СУБД
cursor.execute(sql3)
for row in cursor:
    print(row)

cursor.close()
conn.commit()
conn.close()

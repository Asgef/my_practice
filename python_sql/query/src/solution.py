import psycopg2
from psycopg2.extras import execute_values
import dotenv
import os


dotenv.load_dotenv()

DB_PASS = os.getenv('DB_PASS')

conn = psycopg2.connect(f'postgresql://asgef:{DB_PASS}@localhost:5432/asgef_db')

def batch_insert(connect, product):
    sql = f"""
        INSERT INTO products
            (name, price, quantity)
        VALUES %s;
    """
    products = [
        (item['name'], item['price'], item['quantity']) for item in product
    ]

    with connect.cursor() as curs:
        execute_values(curs, sql, products )
    conn.commit()



def get_all_products(connect):
    sql = """
    SELECT * FROM products
    ORDER BY price DESC;
    """
    with connect.cursor() as curs:
        curs.execute(sql)
        result = curs.fetchall()

    conn.commit()
    return result

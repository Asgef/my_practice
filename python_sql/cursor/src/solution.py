import psycopg2
import dotenv
import os
from psycopg2.extras import DictCursor


dotenv.load_dotenv()
DB_PASS = os.getenv("DB_PASS")


conn = psycopg2.connect(f'postgresql://asgef:{DB_PASS}@localhost:5432/asgef_db')


def get_order_sum(connector, month):
    sql = """
        SELECT c.customer_name, SUM(o.total_amount)
        FROM orders o
        INNER JOIN customers c ON o.customer_id = c.customer_id
        WHERE EXTRACT(MONTH FROM o.order_date) = %s
        GROUP BY c.customer_name
        ORDER BY c.customer_name;
    """
    lines = []
    with connector.cursor(cursor_factory=DictCursor) as curs:
        curs.execute(sql, (month,))
        customers = curs.fetchall()
        for customer in customers:
            lines.append(
                f'Покупатель {customer["customer_name"]} совершил покупок на сумму {customer["sum"]}'
            )
        conn.commit()
    return '\n'.join(lines)


# Решение учителя:


# # BEGIN
# def get_order_sum(conn, month):
#     template = "Покупатель {customer} совершил покупок на сумму {total}".format
#     with conn.cursor(cursor_factory=DictCursor) as cur:
#         query = """
#             SELECT
#                 c.customer_name,
#                 SUM(o.total_amount) AS total
#             FROM
#                 customers c
#             LEFT JOIN
#                 orders o ON c.customer_id = o.customer_id
#             WHERE
#                 EXTRACT(MONTH FROM o.order_date) = %s
#             GROUP BY
#                 c.customer_name;"""
#         month_formated = '{:02d}'.format(month)
#         cur.execute(query, (month_formated,))
#         result = []
#         for row in cur:
#             customer_name = row['customer_name']
#             total = row['total']
#             result.append(template(customer=customer_name, total=total))
#     conn.commit()
#
#     return '\n'.join(result)
# # END

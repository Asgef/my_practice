import psycopg2
from psycopg2.extras import DictCursor
import os
import dotenv


dotenv.load_dotenv()
DB_PASS = os.getenv("DB_PASS")


conn = psycopg2.connect(f'postgresql://asgef:{DB_PASS}@localhost:5432/asgef_db')


def create_post(connect, post):
    sql = """
        INSERT INTO posts
            (title, content, author_id)
        VALUES
            (%(title)s, %(content)s, %(author_id)s)
        RETURNING id;
    """
    with connect.cursor() as curs:
        curs.execute(sql, post)
        post_id = curs.fetchone()[0]
    connect.commit()
    return post_id


def add_comment(connect, comment):
    sql = """
        INSERT INTO comments
            (post_id, author_id, content)
        VALUES
            (%(post_id)s, %(author_id)s, %(content)s)
        RETURNING id;
    """
    with connect.cursor() as curs:
        curs.execute(sql, comment)
        comment_id = curs.fetchone()[0]
    connect.commit()
    return comment_id


def get_latest_posts(connect, n):
    sql = """
        SELECT
            p.id, p.title, p.content, p.author_id, p.created_at,
            json_agg(
                json_build_object(
                    'id', c.id, 'author_id', c.author_id, 'content',
                    c.content, 'created_at', c.created_at
                )
            ) AS comments
        FROM posts p
        LEFT JOIN comments c ON c.post_id = p.id
        GROUP BY p.id, p.title, p.content, p.author_id, p.created_at
        ORDER BY p.created_at DESC
        LIMIT %s;
    """

    with connect.cursor(cursor_factory=DictCursor) as curs:
        curs.execute(sql, (n,))
        result = curs.fetchall()
    connect.commit()
    return result


# Решение учителя

# # BEGIN
# def create_post(conn, post):
#     with conn.cursor() as cur:
#         cur.execute("""
#             INSERT INTO posts (title, content, author_id)
#             VALUES (%(title)s, %(content)s, %(author_id)s)
#             RETURNING id
#         """, post)
#         post_id = cur.fetchone()[0]
#     conn.commit()
#     return post_id
#
#
# def add_comment(conn, comment):
#     with conn.cursor() as cur:
#         cur.execute("""
#             INSERT INTO comments (post_id, author_id, content)
#             VALUES (%(post_id)s, %(author_id)s, %(content)s)
#             RETURNING id
#         """, comment)
#         comment_id = cur.fetchone()[0]
#     conn.commit()
#     return comment_id
#
#
# def get_latest_posts(conn, n):
#     with conn.cursor(cursor_factory=DictCursor) as cur:
#         cur.execute("""
#             SELECT
#                 p.*,
#                 c.id as comment_id,
#                 c.author_id as comment_author_id,
#                 c.content as comment_content,
#                 c.created_at as comment_created_at
#             FROM posts p
#             LEFT JOIN comments c ON p.id = c.post_id
#             WHERE p.id IN (
#                 SELECT id FROM posts
#                 ORDER BY created_at DESC
#                 LIMIT %s
#             )
#         """, (n,))
#
#         rows = cur.fetchall()
#
#         posts_dict = {}
#         for row in rows:
#             post_id = row['id']
#             if not posts_dict.get(post_id):
#                 posts_dict[post_id] = {
#                     'id': row['id'],
#                     'title': row['title'],
#                     'content': row['content'],
#                     'author_id': row['author_id'],
#                     'created_at': row['created_at'],
#                     'comments': []
#                 }
#
#             if row.get('comment_id'):
#                 posts_dict[post_id]['comments'].append({
#                     'id': row['comment_id'],
#                     'author_id': row['comment_author_id'],
#                     'content': row['comment_content'],
#                     'created_at': row['comment_created_at']
#                 })
#
#         return list(posts_dict.values())
# # END
from python_sql.dao.src.models import Course, Lesson
import psycopg2
from psycopg2.extras import NamedTupleCursor
import os
import dotenv

dotenv.load_dotenv()
DB_PASS = os.getenv("DB_PASS")


conn = psycopg2.connect(f'postgresql://asgef:{DB_PASS}@localhost:5432/asgef_db')


def commit(conn):
    conn.commit()


def save_course(conn, course):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        if course.id is None:
            cur.execute(
                "INSERT INTO courses (name, description) VALUES (%s, %s) RETURNING id;",
                (course.name, course.description)
            )
            course.id = cur.fetchone().id
        else:
            cur.execute(
                "UPDATE courses SET name = %s, description = %s WHERE id = %s;",
                (course.name, course.description, course.id)
            )
    return course.id


def find_course(conn, course_id):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT id, name, description FROM courses WHERE id = %s;", (course_id,))
        result = cur.fetchone()
        if result:
            return Course(
                id=result.id,
                name=result.name,
                description=result.description
                )
    return None


def get_all_courses(conn):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT id, name, description FROM courses;")
        return [
            Course(id=row.id, name=row.name, description=row.description)
            for row in cur.fetchall()
        ]


# BEGIN (write your solution here)
def save_lesson(conn, lesson):
    sql_crete_lesson = """
        INSERT INTO lessons
            (name, text, course_id)
        VALUES
            (%s, %s, %s)
        RETURNING id;
    """
    sql_update_lesson = """
        UPDATE lessons
        SET name = %s, text = %s, course_id = %s;
    """
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        if not lesson.id:
           curs.execute(
               sql_crete_lesson, (
                   lesson.name, lesson.text, lesson.course_id
               )
           )
           lesson.id = curs.fetchone().id
        else:
            curs.execute(
                sql_update_lesson, (
                    lesson.name, lesson.text, lesson.course_id
                )
            )
    return lesson.id




def find_lesson(conn, lesson_id):
    sql = """
        SELECT id, name, text, course_id
        FROM lessons
        WHERE id = %s;
    """
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute(sql, (lesson_id,))
        result = curs.fetchone()
        if result:
            return Lesson(
                id=result.id,
                name=result.name,
                text=result.text,
                course_id=result.course_id
            )
    return None
        


def get_course_lessons(conn, course_id):
    sql = """
        SELECT id, name, text, course_id
        FROM lessons
        WHERE course_id = %s;
    """
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute(sql, (course_id,))
        return [
            Lesson(
                id=row.id, name=row.name,
                text=row.text, course_id=row.course_id
            )
            for row in curs.fetchall()
        ]

# END



# Решение учителя


# # BEGIN
# def save_lesson(conn, lesson):
#     with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
#         if lesson.id is None:
#             cur.execute(
#                 "INSERT INTO lessons (name, text, course_id) VALUES (%s, %s, %s) RETURNING id;",
#                 (lesson.name, lesson.text, lesson.course_id)
#             )
#             lesson.id = cur.fetchone().id
#         else:
#             cur.execute(
#                 "UPDATE lessons SET name = %s, text = %s, course_id = %s WHERE id = %s;",
#                 (lesson.name, lesson.text, lesson.course_id, lesson.id)
#             )
#     return lesson.id
#
#
# def find_lesson(conn, lesson_id):
#     with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
#         cur.execute("SELECT id, name, text, course_id FROM lessons WHERE id = %s;", (lesson_id,))
#         result = cur.fetchone()
#         if result:
#             return Lesson(
#                 id=result.id,
#                 name=result.name,
#                 text=result.text,
#                 course_id=result.course_id
#                 )
#     return None
#
#
# def get_course_lessons(conn, course_id):
#     with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
#         cur.execute("SELECT * FROM lessons WHERE course_id = %s ORDER BY id;", (course_id,))
#         return [
#             Lesson(id=row.id, name=row.name, text=row.text, course_id=row.course_id)
#             for row in cur.fetchall()
#         ]
# # END
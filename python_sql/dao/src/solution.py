from models import Course, Lesson
import psycopg2
from psycopg2.extras import NamedTupleCursor

conn = psycopg2.connect('postgresql://asgef:secret@localhost:5432/asgef_db')


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

# END

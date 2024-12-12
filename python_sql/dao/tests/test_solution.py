from models import Course, Lesson
from solution import save_course, find_course, save_lesson, find_lesson, get_course_lessons


def test_solution(db_transaction):
    course1 = Course('test_course', 'test_description')
    course2 = Course('test_course', 'test_description')
    course1_id = save_course(db_transaction, course1)
    course2_id = save_course(db_transaction, course2)

    found_course = find_course(db_transaction, course1_id)

    assert found_course.name == course1.name

    lesson1 = Lesson('test_lesson_1', 'test_text_1', course1_id)
    lesson2 = Lesson('test_lesson_2', 'test_text_2', course1_id)
    lesson3 = Lesson('test_lesson_3', 'test_text_3', course2_id)

    save_lesson(db_transaction, lesson1)
    save_lesson(db_transaction, lesson3)
    lesson2_id = save_lesson(db_transaction, lesson2)

    found_lesson_2 = find_lesson(db_transaction, lesson2_id)
    assert found_lesson_2.name == lesson2.name

    course1_lessons = get_course_lessons(db_transaction, course1_id)
    assert course1_lessons == [lesson1, lesson2]

    course2_lessons = get_course_lessons(db_transaction, course2_id)
    assert course2_lessons == [lesson3]

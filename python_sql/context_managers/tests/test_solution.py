from python_sql.context_managers.src.solution import get_all_cars


def test_solution(db_transaction):
    assert get_all_cars(db_transaction) == [
        (2, 'cherry', '9'),
        (1, 'lada', 'zaporozhets')
    ]

from my_practice.director_and_his_workday import can_attend


def test_can_attend():
    assert can_attend([(5, 10), (1, 3), (3, 5)]) is False
    assert can_attend([(1, 3), (4, 6), (7, 9)]) is True
    assert can_attend([(1, 2), (2, 3), (3, 4)]) is True
    assert can_attend([(1, 5), (2, 3), (4, 6)]) is False
    assert can_attend([(1, 10), (2, 3), (4, 6)]) is False

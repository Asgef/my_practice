from my_practice.rearrange_array_by_sign_of_element import rearrange_array


def test_rearrange_array_by_sign():
    assert rearrange_array([-4, 3, 1, -2, 1, -3]) == [3, -4, 1, -2, 1, -3]
    assert rearrange_array([1, 2, 3, -3, -1, -2]) == [1, -3, 2, -1, 3, -2]
    assert rearrange_array([1, -1, 2, -2, 3, -3]) == [1, -1, 2, -2, 3, -3]
    assert rearrange_array([1, -1, 2, -2, 3, -3, -7, 8]) == [
        1, -1, 2, -2, 3, -3, 8, -7
    ]

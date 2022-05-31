import pytest
from two_number_sum.solution import two_number_sum

@pytest.mark.parametrize("array, target_sum, expected",
[([3, 5, -4, 8, 11, 1, -1, 6], 10, [-1, 11])])
def test_two_number_sum_with_happy_case(array, target_sum,expected):
    result = two_number_sum(array, target_sum)
    assert (result == expected[::-1] or result == expected)
import pytest
from sorted_squared_array.solution import sorted_squared_array

@pytest.mark.parametrize("array, expected",
[
    ([1, 2, 3, 5, 6, 8, 9], [1, 4, 9, 25, 36, 64, 81]),
    ([-3, -2, -1], [1, 4, 9])
]
)
def test_sorted_squared_array_with_happy_case(array, expected):
    result = sorted_squared_array(array)
    assert result == expected
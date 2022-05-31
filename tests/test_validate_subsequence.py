import pytest
from validate_subsequence.solution import isValidSubsequence

@pytest.mark.parametrize("array, sequence, expected",
[
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10], True),
    ([5, 1, 22, 25, 6, -1, 8, 10],[5, 1, 22, 6, -1, 8, 10], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 10], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [5, -1, 8, 10], True),
    ([5, 1, 22, 25, 6, -1, 8, 10],[5, 1, 22, 25, 6, -1, 8, 10, 12],False),
    ([5, 1, 22, 25, 6, -1, 8, 10],[5, 1, 22, 22, 25, 6, -1, 8, 10],False),
    ([1, 1, 6, 1],[1, 1, 1, 6], False),
    ([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 5], False),
    ([5, 1, 22, 25, 6, -1, 8, 10],[ 1, 6, -1, -1], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1, 10], False)
])
def test_validate_subsequence_sum_with_happy_case(array, sequence,expected):
    result = isValidSubsequence(array, sequence)
    assert (result == expected)

    
     
  

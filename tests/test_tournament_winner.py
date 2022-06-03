import pytest
from tournament_winner.solution import tournamentWinner

@pytest.mark.parametrize("competitions, results, expected",
[([['HTML','C#'], ["C#", "Python"], ['Python', 'HTML']], [0, 0, 1], "Python")])
def test_tournament_winner_with_happy_case(competitions, results, expected):
    result = tournamentWinner(competitions, results)
    assert result == expected
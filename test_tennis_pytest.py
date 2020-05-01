import unittest

import pytest


class tennis:

    def score_tennis(player1_points, player2_points):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        player1_score = score_names[player1_points]
        return f"{player1_score}-All"

@pytest.mark.parametrize("player1_points, player2_points, expected_score",
                         [(0, 0, "Love-All"),
                          (1, 1, "Fifteen-All"),
                          (2, 2, "Thirty-All")])
def test_score_tennis(player1_points, player2_points, expected_score):
    assert tennis.score_tennis(player1_points, player2_points) == expected_score

def test_0_0_love_all():
    assert tennis.score_tennis(0, 0) == "Love-All"

def test_1_1_fifteen_all():
    assert tennis.score_tennis(1, 1) == "Fifteen-All"

def test_2_2_thirty_all():
    assert tennis.score_tennis(2, 2) == "Thirty-All"
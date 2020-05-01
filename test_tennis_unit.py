import unittest

class tennis:

    def score_tennis(player1_points, player2_points):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        player1_score = score_names[player1_points]
        return f"{player1_score}-All"


class TennisTest(unittest.TestCase):
    def test_score_tennis(self):
        test_cases = [
            (0, 0, "Love-All"),
            (1, 1, "Fifteen-All"),
            (2, 2, "Thirty-All")
        ]
        for player1_points, player2_points, expected_score in test_cases:
            with self.subTest(f"{player1_points}, {player2_points} -> {expected_score}"):
                self.assertEqual(expected_score, tennis.score_tennis(player1_points, player2_points))

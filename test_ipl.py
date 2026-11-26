import unittest

from solution1 import calculate as total_runs
from solution2 import calculate as batsman
from solution4 import calculate as matches_team_season
from solution5 import calculate as matches_year
from solution6 import calculate as matches_team
from solution7 import calculate as extra_runs
from solution8 import calculate as economical_bowlers


class TestIPL(unittest.TestCase):
    def setUp(self):
        self.matches = [
            {
                "id": 1,
                "season": 2015,
                "team1": "Chennai Super Kings",
                "team2": "Mumbai Indians",
                "winner": "Chennai Super Kings",
            },
            {
                "id": 2,
                "season": 2015,
                "team1": "Royal Challengers Bangalore",
                "team2": "Kolkata Knight Riders",
                "winner": "Kolkata Knight Riders",
            },
            {
                "id": 3,
                "season": 2016,
                "team1": "Sunrisers Hyderabad",
                "team2": "Royal Challengers Bangalore",
                "winner": "Sunrisers Hyderabad",
            },
            {
                "id": 4,
                "season": 2016,
                "team1": "Mumbai Indians",
                "team2": "Gujarat Lions",
                "winner": "Mumbai Indians",
            },
            {
                "id": 5,
                "season": 2017,
                "team1": "Kolkata Knight Riders",
                "team2": "Sunrisers Hyderabad",
                "winner": "Sunrisers Hyderabad",
            },
        ]
        self.deliveries = [
            {
                "match_id": 1,
                "batting_team": "Mumbai Indians",
                "batsman": "JJ Bumrah",
                "bowler": "TS Mills",
                "total_runs": 1,
                "extra_runs": 0,
                "wide_runs": 0,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 1,
                "batting_team": "Mumbai Indians",
                "batsman": "SL Malinga",
                "bowler": "A Choudhary",
                "total_runs": 4,
                "extra_runs": 0,
                "wide_runs": 0,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 1,
                "batting_team": "Mumbai Indians",
                "batsman": "JJ Bumrah",
                "bowler": "TS Mills",
                "total_runs": 2,
                "extra_runs": 1,
                "wide_runs": 0,
                "noball_runs": 1,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 2,
                "batting_team": "Kolkata Knight Riders",
                "batsman": "SP Narine",
                "bowler": "YS Chahal",
                "total_runs": 0,
                "extra_runs": 0,
                "wide_runs": 0,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 2,
                "batting_team": "Kolkata Knight Riders",
                "batsman": "AD Russell",
                "bowler": "S Aravind",
                "total_runs": 6,
                "extra_runs": 0,
                "wide_runs": 0,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 2,
                "batting_team": "Kolkata Knight Riders",
                "batsman": "SP Narine",
                "bowler": "SR Watson",
                "total_runs": 1,
                "extra_runs": 0,
                "wide_runs": 0,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 3,
                "batting_team": "Royal Challengers Bangalore",
                "batsman": "YS Chahal",
                "bowler": "TS Mills",
                "total_runs": 1,
                "extra_runs": 1,
                "wide_runs": 1,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 3,
                "batting_team": "Royal Challengers Bangalore",
                "batsman": "SR Watson",
                "bowler": "A Choudhary",
                "total_runs": 4,
                "extra_runs": 0,
                "wide_runs": 0,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 3,
                "batting_team": "Royal Challengers Bangalore",
                "batsman": "YS Chahal",
                "bowler": "A Choudhary",
                "total_runs": 2,
                "extra_runs": 2,
                "wide_runs": 0,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 2,
                "penalty_runs": 0,
            },
            {
                "match_id": 4,
                "batting_team": "Gujarat Lions",
                "batsman": "P Kumar",
                "bowler": "S Aravind",
                "total_runs": 1,
                "extra_runs": 0,
                "wide_runs": 0,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 4,
                "batting_team": "Gujarat Lions",
                "batsman": "DJ Bravo",
                "bowler": "TS Mills",
                "total_runs": 2,
                "extra_runs": 1,
                "wide_runs": 0,
                "noball_runs": 1,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 4,
                "batting_team": "Gujarat Lions",
                "batsman": "P Kumar",
                "bowler": "TS Mills",
                "total_runs": 3,
                "extra_runs": 0,
                "wide_runs": 0,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 5,
                "batting_team": "Sunrisers Hyderabad",
                "batsman": "B Kumar",
                "bowler": "A Choudhary",
                "total_runs": 0,
                "extra_runs": 0,
                "wide_runs": 0,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 5,
                "batting_team": "Sunrisers Hyderabad",
                "batsman": "Rashid Khan",
                "bowler": "S Aravind",
                "total_runs": 2,
                "extra_runs": 0,
                "wide_runs": 0,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
            {
                "match_id": 5,
                "batting_team": "Sunrisers Hyderabad",
                "batsman": "B Kumar",
                "bowler": "YS Chahal",
                "total_runs": 1,
                "extra_runs": 0,
                "wide_runs": 0,
                "noball_runs": 0,
                "bye_runs": 0,
                "legbye_runs": 0,
                "penalty_runs": 0,
            },
        ]

    def test_total_runs_scored(self):
        self.assertEqual(
            total_runs(lambda: self.deliveries),
            (
                [
                    "Mumbai Indians",
                    "Kolkata Knight Riders",
                    "Royal Challengers Bangalore",
                    "Gujarat Lions",
                    "Sunrisers Hyderabad",
                ],
                [7, 7, 7, 6, 3],
            ),
        )

    def test_batsman_RCB(self):
        self.assertEqual(
            batsman(lambda: self.deliveries), (["SR Watson", "YS Chahal"], [4, 3])
        )

    def test_matches_team_season(self):
        self.assertEqual(
            matches_team_season(lambda: self.matches),
            {
                2015: {
                    "Chennai Super Kings": 1,
                    "Kolkata Knight Riders": 1,
                    "Mumbai Indians": 1,
                    "Royal Challengers Bangalore": 1,
                },
                2016: {
                    "Gujarat Lions": 1,
                    "Mumbai Indians": 1,
                    "Royal Challengers Bangalore": 1,
                    "Sunrisers Hyderabad": 1,
                },
                2017: {"Kolkata Knight Riders": 1, "Sunrisers Hyderabad": 1},
            },
        )

    def test_matches_year(self):
        self.assertEqual(
            matches_year(lambda: self.matches), ([2015, 2016, 2017], [2, 2, 1])
        )

    def test_matches_team(self):
        self.assertEqual(
            matches_team(lambda: self.matches),
            {
                2015: {"Chennai Super Kings": 1, "Kolkata Knight Riders": 1},
                2016: {"Mumbai Indians": 1, "Sunrisers Hyderabad": 1},
                2017: {"Sunrisers Hyderabad": 1},
            },
        )

    def test_extra_runs(self):
        self.assertEqual(
            extra_runs(lambda: self.deliveries, lambda: self.matches),
            (
                [
                    "Royal Challengers Bangalore",
                    "Gujarat Lions",
                ],
                [3, 1],
            ),
        )

    def test_economical_bowlers(self):
        self.assertEqual(
            economical_bowlers(lambda: self.deliveries, lambda: self.matches),
            (
                ["YS Chahal", "SR Watson", "TS Mills", "A Choudhary", "S Aravind"],
                [0.0, 6.0, 9.0, 24.0, 36.0],
            ),
        )


if __name__ == "__main__":
    unittest.main()

class TennisPlayer:
    def __init__(self, name: str, age: int, points: float):
        self.name = name
        self.age = age
        self.points = points
        self.wins = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 2:
            raise ValueError("Name should be more than 2 symbols!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError("Players must be at least 18 years of age!")
        self.__age = value

    def add_new_win(self, tournament_name: str):
        if tournament_name not in self.wins:
            self.wins.append(tournament_name)
        else:
            return f"{tournament_name} has been already added to the list of wins!"

    def __lt__(self, other):
        if self.points < other.points:
            return f'{other.name} is a top seeded player and he/she is better than {self.name}'
        return f'{self.name} is a better player than {other.name}'

    def __str__(self):
        return f"Tennis Player: {self.name}\n" \
               f"Age: {self.age}\n" \
               f"Points: {self.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.wins)}"


import unittest


class TestTennisPlayer(unittest.TestCase):

    def setUp(self):
        self.player = TennisPlayer("Grigor Dimitrov", 29, 6000)

    def test_init(self):
        self.assertEqual(self.player.name, "Grigor Dimitrov")
        self.assertEqual(self.player.age, 29)
        self.assertEqual(self.player.points, 6000)
        self.assertEqual(self.player.wins, [])

    def test_name_setter_with_invalid_value_should_raise_error(self):
        with self.assertRaises(ValueError) as context:
            self.player.name = "A"
        self.assertEqual("Name should be more than 2 symbols!", str(context.exception))

    def test_age_setter_with_invalid_value_should_raise_error(self):
        with self.assertRaises(ValueError) as context:
            self.player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(context.exception))

    def test_add_new_win_when_tournament_name_is_not_in_wins(self):
        result = self.player.add_new_win("Roland Garros")
        self.assertEqual(self.player.wins, ["Roland Garros"])
        self.assertEqual(result, None)

    def test_add_new_win_when_tournament_name_is_in_wins(self):
        self.player.wins = ["Roland Garros"]
        result = self.player.add_new_win("Roland Garros")
        self.assertEqual(self.player.wins, ["Roland Garros"])
        self.assertEqual(result, "Roland Garros has been already added to the list of wins!")

    def test_str(self):
        self.player.wins = ["Roland Garros", "US Open"]
        result = str(self.player)
        self.assertEqual(result, "Tennis Player: Grigor Dimitrov\nAge: 29\nPoints: 6000.0\nTournaments won: Roland Garros, US Open")

    def test_lt_when_other_player_has_more_points(self):
        other_player = TennisPlayer("Rafael Nadal", 34, 7000)
        result = self.player < other_player
        self.assertEqual(result, "Rafael Nadal is a top seeded player and he/she is better than Grigor Dimitrov")

    def test_lt_when_other_player_has_less_points(self):
        other_player = TennisPlayer("Rafael Nadal", 34, 5000)
        result = self.player < other_player
        self.assertEqual(result, "Grigor Dimitrov is a better player than Rafael Nadal")

    def test_lt_when_other_player_has_equal_points(self):
        other_player = TennisPlayer("Rafael Nadal", 34, 6000)
        result = self.player < other_player
        self.assertEqual(result, "Grigor Dimitrov is a better player than Rafael Nadal")


if __name__ == "__main__":
    unittest.main()
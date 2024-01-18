from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    def __init__(self, protection: int, price: float):
        self.protection = protection
        self.price = price

    @abstractmethod
    def increase_price(self):
        pass


class KneePad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=120, price=15.0)

    def increase_price(self):
        self.price *= 1.2


class ElbowPad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=90, price=25.0)

    def increase_price(self):
        self.price *= 1.1


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float, wins: int):
        self._name = name
        self._country = country
        self._advantage = advantage
        self._budget = budget
        self._wins = wins
        self._equipment = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        if not new_value.strip() or not new_value:
            raise Exception("A name should not be empty.")
        self._name = new_value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, new_value):
        if not new_value or len(new_value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long and not empty.")
        self._country = new_value

    @property
    def advantage(self):
        return self._advantage

    @advantage.setter
    def advantage(self, new_value):
        if new_value < 0:
            raise ValueError("Advantage must be greater than zero!")
        self._advantage = new_value

    @abstractmethod
    def win(self):
       pass

    def get_statistics(self):
        total_equipment_price = sum(item.price for item in self._equipment)
        avg_protection = 0 if not self._equipment else sum(item.protection for item in self._equipment) // len(
            self._equipment)

        return (f"Name: {self._name}\n"
                f"Country: {self._country}\n"
                f"Advantage: {self._advantage} points\n"
                f"Budget: {self._budget:.2f}EUR\n"
                f"Wins: {self._wins}\n"
                f"Total Equipment Price: {total_equipment_price:.2f}\n"
                f"Average Protection: {avg_protection}")


class OutdoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int, budget: float, wins: int):
        super().__init__(name, country, advantage, budget, wins)

    def win(self):
        self._wins += 1
        self._advantage += 115


class IndoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int, budget: float, wins: int):
        super().__init__(name, country, advantage, budget, wins)

    def win(self):
        self._wins += 1
        self._advantage += 145


class Tournament:
    def __init__(self, name: str, capacity: int):
        if not name.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    def add_equipment(self, equipment_type: str):
        if equipment_type == "KneePad":
            equipment = KneePad()
        elif equipment_type == "ElbowPad":
            equipment = ElbowPad()
        else:
            raise Exception("Invalid equipment type!")

        self.equipment.append(equipment)

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type == "OutdoorTeam":
            team = OutdoorTeam(team_name, country, advantage, 1000, 0)
        elif team_type == "IndoorTeam":
            team = IndoorTeam(team_name, country, advantage, 1000, 0)
        else:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment_to_sell = None

        for equipment in self.equipment:
            if isinstance(equipment, KneePad) and equipment_type == "KneePad":
                equipment_to_sell = equipment
                break
            elif isinstance(equipment, ElbowPad) and equipment_type == "ElbowPad":
                equipment_to_sell = equipment
                break

        if equipment_to_sell is None:
            raise Exception("Invalid equipment type!")

        team = next((team for team in self.teams if team.name == team_name), None)
        if team is None:
            raise Exception("No such team!")

        if team._budget < equipment_to_sell.price:
            raise Exception("Budget is not enough!")

        team._equipment.append(equipment_to_sell)
        team._budget -= equipment_to_sell.price
        self.equipment.remove(equipment_to_sell)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((team for team in self.teams if team.name == team_name), None)
        if team is None:
            raise Exception("No such team!")

        if team._wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)

        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        changed_equipment_count = 0

        for equipment in self.equipment:
            if (isinstance(equipment, KneePad) and equipment_type == "KneePad") or (
                    isinstance(equipment, ElbowPad) and equipment_type == "ElbowPad"):
                equipment.increase_price()
                changed_equipment_count += 1

        return f"Successfully changed {changed_equipment_count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((team for team in self.teams if team.name == team_name1), None)
        team2 = next((team for team in self.teams if team.name == team_name2), None)

        if team1 is None or team2 is None:
            raise Exception("No such team!")

        if isinstance(team1, OutdoorTeam) != isinstance(team2, OutdoorTeam):
            raise Exception("Game cannot start! Team types mismatch!")

        team1_points = team1.advantage + sum(equipment.protection for equipment in team1._equipment)
        team2_points = team2.advantage + sum(equipment.protection for equipment in team2._equipment)

        if team1_points > team2_points:
            team1.win()
            return f"The winner is {team_name1}."
        elif team2_points > team1_points:
            team2.win()
            return f"The winner is {team_name2}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda team: team._wins, reverse=True)

        team_statistics = "\n".join(team.get_statistics() for team in sorted_teams)

        return f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n{team_statistics}"


t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))

print(t.get_statistics())

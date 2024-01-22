from abc import ABC, abstractmethod


class BasePeak(ABC):
    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = self.calculate_difficulty_level()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Peak name cannot be less than 2 symbols!")
        self.__name = value

    @property
    def elevation(self):
        return self.__elevation

    @elevation.setter
    def elevation(self, value):
        if value < 1500:
            raise ValueError("Peak elevation cannot be below 1500m.")
        self.__elevation = value

    @abstractmethod
    def get_recommended_gear(self):
        pass

    @abstractmethod
    def calculate_difficulty_level(self):
        pass


class ArcticPeak(BasePeak):
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self):
        if self.elevation > 3000:
            return "Extreme"
        elif 2000 <= self.elevation <= 3000:
            return "Advanced"


class SummitPeak(BasePeak):
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self):
        if self.elevation > 2500:
            return "Extreme"
        elif 1500 <= self.elevation <= 2500:
            return "Advanced"


class BaseClimber(ABC):
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self, peak: BasePeak):
        pass

    def rest(self):
        self.strength += 15

    def __str__(self):
        return f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered peaks: {', '.join(self.conquered_peaks)} ///"


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak: BasePeak):
        if not self.can_climb():
            raise ValueError("Cannot climb!")
        self.strength -= 20 * 2 if peak.difficulty_level == "Extreme" else 20 * 1.5
        self.conquered_peaks.append(peak.name)


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        if not self.can_climb():
            raise ValueError("Cannot climb!")
        self.strength -= 30 * 1.3 if peak.difficulty_level == "Advanced" else 30 * 2.5
        self.conquered_peaks.append(peak.name)


class SummitQuestManagerApp:
    VALID_CLIMBER_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAK_TYPES = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def find_climber_by_name(self, climber_name: str):
        return next((c for c in self.climbers if c.name == climber_name), None)

    def find_peak_by_name(self, peak_name: str):
        return next((p for p in self.peaks if p.name == peak_name), None)

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."
        if self.find_climber_by_name(climber_name):
            return f"{climber_name} has been already registered."
        climber_class = self.VALID_CLIMBER_TYPES[climber_type]
        climber = climber_class(climber_name)
        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."
        if self.find_peak_by_name(peak_name):
            return f"{peak_name} is already part of the wish list."
        peak = ArcticPeak(peak_name, peak_elevation) if peak_type == "ArcticPeak" else SummitPeak(peak_name, peak_elevation)
        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: list[str]):
        climber = self.find_climber_by_name(climber_name)
        if not climber:
            return f"Climber {climber_name} is not registered yet."
        peak = self.find_peak_by_name(peak_name)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."
        recommended_gear = peak.get_recommended_gear()
        if sorted(recommended_gear) == sorted(gear):
            return f"{climber_name} is prepared to climb {peak_name}."
        climber.is_prepared = False
        missing_gear = [g for g in recommended_gear if g not in gear]
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self.find_climber_by_name(climber_name)
        if not climber:
            return f"Climber {climber_name} is not registered yet."
        peak = self.find_peak_by_name(peak_name)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."
        if not climber.can_climb() or not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        climbers = sorted([c for c in self.climbers if c.conquered_peaks], key=lambda c: (-len(c.conquered_peaks), c.name))
        climbers_info = "\n".join([str(c) for c in climbers])
        return f"Total climbed peaks: {len(self.peaks)}\n**Climber's statistics:**\n{climbers_info}"


climbing_app = SummitQuestManagerApp()

# Register climbers

print(climbing_app.register_climber("ArcticClimber", "Alice"))

print(climbing_app.register_climber("SummitClimber", "Bob"))

print(climbing_app.register_climber("ExtremeClimber", "Dave"))

print(climbing_app.register_climber("ArcticClimber", "Charlie"))

print(climbing_app.register_climber("ArcticClimber", "Alice"))

print(climbing_app.register_climber("SummitClimber", "Eve"))

print(climbing_app.register_climber("SummitClimber", "Frank"))

# Add peaks to the wish list

print(climbing_app.peak_wish_list("ArcticPeak", "MountEverest", 4000))

print(climbing_app.peak_wish_list("SummitPeak", "K2", 3000))

print(climbing_app.peak_wish_list("ArcticPeak", "Denali", 2500))

print(climbing_app.peak_wish_list("UnchartedPeak", "MysteryMountain", 2000))

# Prepare climbers for climbing

print(climbing_app.check_gear("Alice", "MountEverest", ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]))
print(climbing_app.check_gear("Bob", "K2", ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]))
print(climbing_app.check_gear("Charlie", "Denali", ["Ice axe", "Crampons"]))

# Perform climbing

print(climbing_app.perform_climbing("Alice", "MountEverest"))
print(climbing_app.perform_climbing("Bob", "K2"))
print(climbing_app.perform_climbing("Kelly", "Denali"))
print(climbing_app.perform_climbing("Alice", "K2"))
print(climbing_app.perform_climbing("Alice", "MysteryMountain"))
print(climbing_app.perform_climbing("Eve", "MountEverest"))
print(climbing_app.perform_climbing("Charlie", "MountEverest"))
print(climbing_app.perform_climbing("Frank", "K2"))
print(climbing_app.perform_climbing("Frank", "Denali"))
print(climbing_app.perform_climbing("Frank", "MountEverest"))

# Get statistics

print(climbing_app.get_statistics())
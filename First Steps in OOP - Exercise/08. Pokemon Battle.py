class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon_name):
        if pokemon_name in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon_name)
        return f"Caught {pokemon_name.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for p_name in self.pokemon:
            if p_name.name == pokemon_name:
                self.pokemon.remove(p_name)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n- " + "\n- ".join([p.pokemon_details() for p in self.pokemon])

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

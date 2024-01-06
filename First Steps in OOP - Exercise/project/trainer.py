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



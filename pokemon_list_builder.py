import json

class Pokemon:
    def __init__(self, name, p_type, stats):
        self.name = name
        self.type = p_type
        self.base_hp = stats.get('hp')
        self.base_atk = stats.get('attack')
        self.base_def = stats.get('defense')

    def __repr__(self):
        return f"{self.name}: a {self.type} type pokémon." 

    def test(self):
        print("Hey, this works!")

# Creates a dictionary of 'Pokemon name: Pokemon object' for all pokemon in the json file. 
with open('pokemon.json') as pokemon_json:
    pokemon_list_temp = json.load(pokemon_json)
    pokemon_list = []
    for pokemon in pokemon_list_temp:
        pokemon_obj = {pokemon.get('name').lower(): Pokemon(**pokemon)}
        pokemon_list.append(pokemon_obj)

bulb = pokemon_list[0].get("bulbasaur")
print(type(pokemon_list[0].get("bulbasaur")))
bulb.test()

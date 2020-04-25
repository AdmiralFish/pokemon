import json

class Pokemon:
    def __init__(self, name, p_type, stats):
        self.name = name
        self.type = PokeType(p_type)
        self.base_hp = stats.get('hp')
        self.base_atk = stats.get('attack')
        self.base_def = stats.get('defense')

    def __repr__(self):
        return f"{self.name}: a {self.type} type pokémon." 

class PokeType:
    def __init__(self, type_name):
        self.type_name = type_name.lower()
        with open("poke_types.json") as poke_types_json:
            poke_types = json.load(poke_types_json)
            for element in poke_types:
                if element['type'] == self.type_name:
                    type_dic = element
                    self.strong = type_dic['effects']['strong']
                    self.weak = type_dic['effects']['weak']
        
    def __repr__(self):
        return self.type_name

# Creates a dictionary of 'Pokemon name: Pokemon object' for all pokemon in the json file. 
with open('pokemon.json') as pokemon_json:
    pokemon_list_temp = json.load(pokemon_json)
    pokemon_list = []
    for pokemon in pokemon_list_temp:
        pokemon_obj = {pokemon.get('name').lower(): Pokemon(**pokemon)}
        pokemon_list.append(pokemon_obj)

# Function to retreive a Pokemon from list of all.
def get_pokemon(poke_name):
    for pokemon in pokemon_list:
        for key, value in pokemon.items():
            if key == poke_name:
                return value



charmander = get_pokemon("charmander")

test= get_pokemon("squirtle")
print(test.type.strong)
print(test.type.weak)
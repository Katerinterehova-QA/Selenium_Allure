import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
                    json={"name": "generate",
                          "photo": "generate"
                         },
                    headers={"trainer_token": "54469ebaf66530d724b2b286782e2644",
                    "Content-Type" : "application/json"})
print(response.json)


response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
                    json={"pokemon_id": "19339",
                          "name": "Нюша",
                          "photo": "https://dolnikov.ru/pokemons/albums/008.png"},
                    headers={"trainer_token": "54469ebaf66530d724b2b286782e2644",
                    "Content-Type" : "application/json"})
print(response.json)


response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                    json={"pokemon_id": "19339"},
                    headers={"trainer_token": "54469ebaf66530d724b2b286782e2644",
                    "Content-Type" : "application/json"})
print(response.json)
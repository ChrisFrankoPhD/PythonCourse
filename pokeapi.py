import requests
import json

# req = requests.get('https://pokeapi.co/api/v2/pokemon/1')
# pokemon = req.json()
# print(pokemon)

# req = requests.get('https://swapi.dev/api/people/1')
# character = req.json()
# print(character)
# print(type(character))
# print (character['films'])
# for film in character['films']:
#     req = requests.get(film)
#     film = req.json()
#     print(f'{character["name"]} appears in: {film["title"]}')

json_str = '''{
	"name": "Luke Skywalker",
	"height": "172",
	"mass": "77",
	"hair_color": "blond",
	"skin_color": "fair",
	"eye_color": "blue",
	"birth_year": "19BBY",
	"gender": "male",
	"homeworld": "https://swapi.dev/api/planets/1/",
	"films": [
		"https://swapi.dev/api/films/1/",
		"https://swapi.dev/api/films/2/",
		"https://swapi.dev/api/films/3/",
		"https://swapi.dev/api/films/6/"
	],
	"species": [],
	"vehicles": [
		"https://swapi.dev/api/vehicles/14/",
		"https://swapi.dev/api/vehicles/30/"
	],
	"starships": [
		"https://swapi.dev/api/starships/12/",
		"https://swapi.dev/api/starships/22/"
	],
	"created": "2014-12-09T13:50:51.644000Z",
	"edited": "2014-12-20T21:17:56.891000Z",
	"url": "https://swapi.dev/api/people/1/"
}'''

data = json.loads(json_str)
print(type(data))
data['name'] = 'chris franko'
data["bae"] = 'sara huh'
data_str = json.dumps(data)
print(type(data_str))
print(data_str)
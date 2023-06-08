# Python 201: Intermediate Python

## The In Operator

- we actually used this in the previous courses project for rock paper scissors, where we did `move in valid_moves` which simply returns True is the thing stored in the `move` variable is in the `valid_moves` list 
- this is much nicer than looping over the list and checking if each item == our move
- in general built-in python functions are much faster than doing these things manually, since the built in python functions are wrote in 'C', which is a much faster language than python, since python itself is wrote in 'C' behind the scenes, (so its kind of a scripting language, albeit a low level one)
- so in general we can do:
```
valid_moves = ['rock', 'paper', 'scissors', 'r', 'p', 's']
move = 'rock'
if move in valid_moves:
    print(f'{move} is a valid move')
else:
    print(f'{move} is not a valid move')
```
- so it is just anothe rnice conditional, but for checkin if soemthing is in an iterable
- so we can do this with a dictionary as well, or a tuple, or string
- he also wants us to test if it works in a set 
```
move1 = 'rock'
move2 = 'water'
moves_set = set(valid_moves)
print(moves_set)
print(move1 in moves_set)
print(move2 in moves_set)
```
> True
> False

- so yes this works with a set as well
- one interesting application maybe i thought of for dictionaries:
```
type_effects = {
    'fire': {'weakness': {'water', 'rock', 'ground'},
             'strength': {'grass', 'bug', 'steel', 'ice'}
             },
    'water': {'weakness': {'grass', 'electric'},
             'strength': {'ground', 'rock', 'fire'}
             },
    'grass': {'weakness': {'flying', 'poison', 'bug', 'fire', 'ice'},
             'strength': {'ground', 'rock', 'water'}
             }
}

def damage_calc(pokemon_type, attack_type):
    if attack_type in type_effects[pokemon_type]['weakness']:
        return 'double damage!'
    elif attack_type in type_effects[pokemon_type]['strength']:
        return 'half damage!'
    else:
        return 'normal damage'

attack_type1 = 'ground'
user_pokemon1 = 'fire'
attack_type2 = 'rock'
user_pokemon2 = 'water'
attack_type3 = 'fairy'
user_pokemon3 = 'grass'

print(damage_calc(user_pokemon1, attack_type1))
print(damage_calc(user_pokemon2, attack_type2))
print(damage_calc(user_pokemon3, attack_type3))
```
>double damage!
>half damage!
>normal damage
- so little database with a dictionary for deciding how much danage an incming attack does on a pokemin given the pokemon type and attack type

## Not Operator

- we have used the `not` operator a lot by now, which simply flips the boolean
- for example, in my rock paper scissors game, i did:
```
while not is_move_valid(user_move):
    user_move = input('invalid move: please choose rock, paper, or scissors: ').lower().strip();
```
- so we want this loop to happen when the `user_move` is not a valid move, so we have to add the not operator before the boolean check, since the function returns True when user_move is valid, now this entire expression `not is_move_valid(user_move)` evaluates to True when the the user_move is not valid, and is_move_valid(user_move) is True
- in JS this is the same as the `!` operator, in JS we do `!is_move_valid(user_move)`

## Reading Files

- in python we open files with a context manager, we are not getting into the details of what that is apprently, but is a good way to ready files since it is very memory performant, and this way we can do things with those files in a script too
- in general, it seems context managers deal with the handling fo the resources it takes to open and read/write a file, for us
- when we use the `with` command, resources are allocated for the file, and then we can do stuff with that file, and then once the code block exits, we ensure that the files is removed from the resources (like memory or even variable names) we allocated to it
- we can also do these things manually, but we may often have a function, that works on an open file, with many possible branches and return paths, or many ways to return an exception, it is very cumbersome to ensure each of these paths has a statement tht closes the file, or to make sure the file in closed even if the function runs into errors, and this can lead to RAM leaks for example if multiple files are opened and not all get closed as expected
- so as mentioned, we use the with command to open  a file in the syntax like: `with open('filename', 'r') as file-reference:`, 
    - where `with` is our context manager keyword, 
    - `open()` is the method to open the file, 
    - `'filename'` is the name of the file we want to open, 
    - `file-reference` is the short-hand we will use to refer to the file in the code, 
    - and `'r'` is the mode we are opening the file in, 
        - 'r' is the default value, meaning read only, we cannot change the file, just read it
        - 'a' is append, for appending the file, pointer is set to teh end of the file, meaning we can insert text to the end of the file, when we pass a string to the `.write()` function in this mode, the string is appended to the end of the file
        - 'w' is write, opens for writing only, this creates a new file with the `.write()` command, or overwrites an existing one with the same name
        - 'x' is create, this mode is for creating new files
        - there are more but these are the base 4
- so an example here is:
```
with open('PythonCourse/RPS.py', 'r') as file:
    print(file.read())
```
- and we see we get the entire printout of the RPS.py file I made for the last course in the terminal 
- note that even though the relative link to this file *from the python file this code is in* is 'RPS.py', we have to use the relative link from the folder the command line we are using is running in, which is 'PythonCourse/RPS.py'
- so as we expect from our description above, we do not have access to said file out of the `with` code block, we get a 'closed file' error if we try to do file.read() outside of the codeblock
- this is a good thing though since it is what makes this safe to use since it closes the file automatically
- but we can still store things in varibales to use them outside of the block! this is similar to the way using content from the fetch method for APIs in JS outside of the fetch blocks
```
with open('PythonCourse/RPS.py', 'r') as file:
    content = file.read()
print (type(content))
print (content.upper()) 
```
> `<class 'str'>`
> IMPORT RANDOM
> ...
- so i did this to show it is jsut regular data, we can save it the file content to the variable `content` in the `with` block, and one thing we notice is that we can use the `content` reference globally even though we defined it within `with`, interesting
- we can then do `type(content)` to show that it is just a str, a very long one, but just a str, and we can act on it liek a regular string, for example with `.upper()`, which just gets us a bunch of uppercase code, but jsut an example
- so the text from the file is saved in `content`, but the file itself is closed outside the with block, 

## Creating and Writing Files

- we can also write and create files in python, instead of just reading them 
- for this I will create a file named write_file.txt, and we use the write, `w`, mode for the `with` function:
```
with open('pythoncourse/write_file.txt', 'w') as file:
    file.write('this was made in a python file using "with"')
```
- and when we run the program we see that a new file appears in our little vscode file explorer immediately, and the text `'this was made in a python file using "with"'` is in the file
- we see if we run the code a second time, the file is overwritten with the same line, so we do not add to the start of the file or anything, we create a whole new file
- we can add text to the end of a file in append mode, `'a'`, and we still use the `.write()` method
```
with open('pythoncourse/write_file.txt', 'a') as file:
    file.write('\nthis line was appended in the with command in "a" mode')
```
- and now our text file looks like:
```
this was made in a Python file using "with"this line wasy
this line was appended in the with command in "a" mode
```
- if we did not have the `\n` at the start of the sentence there, the added text would start immediately where the old file left off, with no added space or anything, since it just picks the end of the file
- we see we can also add tabs with strings in the same way, using the `\t` keyword
- so now we can take user input, and write files directly from that information, which is very good for us to build files on our server or something

## Reading Multiple Lines

- we want to be able to read multiples lines of data at once, and this is very useful when scraping data from the internet apparently
- so for this we need a file with multile lines, preferably something we could search through, so we can make a scenario here where we want to find specific email addresses
- so we have the 'emails.txt' file that is a different email on every line:
```
chris@gmail.com
sara@gmail.com
matt@yahoo.com
ferbie@gmail.com
email2@yahoo.com
fakename@gmail.com
coolguy69@yahoo.com
```
- and we can then open this file in write mode with the `with` command, and since we just want to read and maybe scrape the data, we can open it up in read-only mode
- and instead of using just `.read()`, we can use `.readlines()` which will give us each line of text as a seperate itme in a list:
```
with open('pythoncourse/emails.txt', 'r') as file:
    print(file.readlines())
``` 
> ['chris@gmail.com\n', 'sara@gmail.com\n', 'matt@yahoo.com\n', 'ferbie@gmail.com\n', 'email2@yahoo.com\n', 
'fakename@gmail.com\n', 'coolguy69@yahoo.com']
- so we see we get a list wiwht each line of text, including the new line indicator `\n`, even though we dont explicitly see those in the file itself
- so we know how to work well with lists, so this makes things much nicer for us, for working for us
- so we can iterate through the list of emails and search for what we want, in this case lets say we want to find only the gmails or the yahoo emails:
```
gmails = [email.strip() for email in email_lst if 'gmail' in email]
print(gmails)
yahoos = [email.strip() for email in email_lst if 'yahoo' in email]
print(yahoos)
```
>['chris@gmail.com', 'sara@gmail.com', 'ferbie@gmail.com', 'fakename@gmail.com']
>['matt@yahoo.com', 'email2@yahoo.com', 'coolguy69@yahoo.com']
- so here we are using list comprehension to make lists with just the gmails or just the yahoos, list comprehension is nice clean and short way to make a new list when looping, we can see we are telling python to create a new list named `gmails`, and to fill it with `email.strip()`, for each `email` in the `email_lst`, but only if the sequence `'gmail'` is in the `email` string
- then we do the same for the yahoo addresses, and this works nicely, 
    - but really we shouldprobably look for `'@gmail`, or else if someone had an email like 'gmailfan@yahoo.com', we would get it in our gmail list even though it is a yahoo email
- now list comprehension is nice, but here we actually have to loop through the whole thing twice to make each new list, really we should just loop through it once, and we can build a better version, and include outliers, like so:
```
gmails2 = []
yahoos2 = []
other2 = []
for email in email_lst:
    if '@gmail' in email:
        gmails2.append(email.rstrip())
    elif '@yahoo' in email:
        yahoos2.append(email.rstrip())
    else:
        other2.append(email.rstrip())
print(gmails2)
print(yahoos2)
print(other2)
```
>['chris@gmail.com', 'sara@gmail.com', 'ferbie@gmail.com', 'fakename@gmail.com']
>['matt@yahoo.com', 'email2@yahoo.com', 'coolguy69@yahoo.com']
>['bleh@hotmail.com', 'pikachu@sympatico.ca']

- so this is a bit nicer since we only loop once and we also get an intuitive way to store the left over emails
- also notice we user `rstrip()` instead of `.strip()` on this one, in our case, either does does the same thing, but maybe it is better to do this since we dont want to accidenally strip anything from the left
- so now that we have this in a typical data structure we can do whatever we want with them

## Writing a File and Executing it

- so we can use user input to interactively build a file and read it
- we can do this by setting variables like `filename` and `content` with various user inputs, then create the file with `with`, setting the name to `filename` and using `write(content)`
- so to do this i made a little command line address book generator:
```
filename = input('What is the file name? ')
contact = input('Please enter contacts in the format "Name, email", followed by a return. When finished enter "d" for "done": ')    
address_book = {}
while contact != 'd' and contact != 'done':
    person = contact.split(",")
    address_book[person[0].strip()] = person[1].strip()
    contact = input('Enter another contact as "name, email" (or type "d" to finish): ')
print(address_book)

with open(filename, "w") as contacts:
    content_str = ''
    for key, value in address_book.items():
        content_str += f'{key}: {value}\n'
    contacts.write(content_str.rstrip())
```
> {'chris franko': 'chris1440@gmail.com', 'sara huh': 
'sara.huh1925@gmail.com', 'mom': 'kfranko62@gmail.com', 'ferb': 'ferbierox@yahoo.com'} 
- ^^ printout of `address_book` dictionary

- so here we ask the command line user for a file name, in this filename, we need to make sure to specify the path too, since this will be relative to the directory the terminal is operating in, in my example i use 'pythoncourse/contact_emails.txt
- we then ask the user to specify a contact and their email, seperated by a comma, so for example, i would enter 'chris, chris1440@gmail.com' then hit return
- the empty address book dictionary is created, and we set up a loop that checks for the exit conditions, when the user-input, saved as `contact`
- we can seperate this string based the comma delimiter, into a list with each comma-seperated part, so the name and the email, using the `contact.split(",")` function
    - so for the example above, `person` then becomes a list in the form of `['chris', 'chris1440@gmail.com']`
- okay so now we can build a dictionary one entry at a time with the line `address_book[person[0].strip()] = person[1].strip()`, stripping each string in the list to account for users adding extra spaces, so in this case the dictionary entry would be `{'chris': 'chris1440@gmail.com'}`, and this continues as we keep prompting the user for additional entires, and the loop will automatically terminate if 'd' or 'done' is input
- so now we have a dictionary with all of our user inputs, which should be names and emails for those names, so we create the file with `with open(filename, "w") as contacts:`
- here instead of adding the entries diectly to the file, which we could do if we opened in append mode, we will instead build the content string of the file, piece by piece and write the entire string
- so we do this by first creating the enmpty string `content_str = ''`, and then looping through the key: value pairs of the dictionary with `for key, value in address_book.items():`, and for each pair, we add a line to the string with `content_str += f'{key}: {value}\n'`, which will create new lines for us with the addition of `\n` at the end of each segment
- so now all we have to do is write this to the file after the loop is done and the string is created with `contacts.write(content_str.rstrip())`, and we make sure to use `rstrip()` on the content string to get rid of the trailing `\n` that will be at the end of the string, otherwise we have en empty line at the end of the file, which may not be preferrable
    - as an aside, i did this in append mode at first since it is intuitive to just add each line to the file one by one:
    ```
    with open(filename, "a") as contacts:
        for key, value in address_book.items():
            contacts.write(f'{key}: {value}\n')
    ```
    - it is less lines as well, but there was no intuitive way to get rid of the trailing `\n` in this way, and we end up with an extra line in the file, this may be inconsequential, but probably good to know both ways
- we can now also add the functionality to read the file after it is created!! which i forgot about 
```
open_file = input(f'would you like to review {filename}? (Y / N) ')
if open_file.lower() in ['y', 'yes']:
    with open(filename, 'r') as file:
        print(file.read())
```
- so here we ask if they want to review the made file, and we check if the input was in the list of 'y' or 'yes',
- then we open the file in readme mode, and simply print `file.read()`

## Functions Inside if Functions

- in python, everything is an object, files, function, int, everything
- and he doesnt mention it immediately, but apparently this is relevant
- as I have done previously, we can define and use functions within another function
```
def outer1(name):
    print(f'{name} is in outer function')
    def inner1():
        print(f"{name} is in inner function")
    inner1()
outer1('chris')
```
- so here we have the outer1() function that we pass `name` to, then we define the inner function with no argument, and we then call the inner function and it is able to use the `name` variable since we are still within the outer functions scope
- however, if we do give an argument to `inner1()`, called `name`, it will use that `name` by default since it is more directly scoped to the inner function, only when it sees there isn't one does it look to the outer scope
- so we have done this before, but this is called a **decorator function**, a function we define and call within another


## Making an Simple API Request

- we are going to be using a package called 'requests', we can also import if we need to using pip if we need to, and we dont have the requests package so i guess we need to, jumping to next lesson on how to install packages then coming back
    - okay so just figured it out in google instead
    - when i did `import requests`, i got the error `ModuleNotFoundError: No module named 'requests'`, which is ecactly as it sounds, i didn ot have that module
    - so when trying to do `pip install requests`, it would begin installation as expected, but then i would get the error 
    ```
    WARNING: Failed to write executable - trying to use .deleteme logic
    ERROR: Could not install packages due to an OSError: [WinError 2] The system cannot find the file specified: 'C:\\Python311\\Scripts\\normalizer.exe' -> 'C:\\Python311\\Scripts\\normalizer.exe.deleteme'
    ```
    - which when i googled it, basically measn i do not have permission to install from vscode here, i could likely install it by opening cmd as adminastrator, but instead we can also install it just for this user using a modified command: `--user`
    - so did a couple of things, first i also switched to using pip with the command `python -m pip...` instead of just `pip...` since this ensures pip is running with the python interpretor we have here, so it is gettign installed to the proper python
    - also i updated pip the newest version with `python -m pip install --user --upgrade pip`, using the `--user` command that gives us permission to instal it for this user
    - we can then check our pip version with `pip -V` to ensure it was updaated correctly
    - so then finally did `python -m pip install --user requests ` to install the requests package as needed
- so now we can move on with using requests
- and for this lesson we are actually just going to make a simple http request, instead of a full api request
- we are going to usr the example of getting the status code from any website:
```
import requests

req = requests.get("https://kalob.io")
print(req)
print(type(req))
```
> <Response [200]>
> <class 'requests.models.Response'>
- so here we use the `requests.get()` method to get an http response from the website, in this case just the website of the person who runs the course
- if we print it we can see we just get this respons object back, and we can also see the type is 'requests.models.Response', which i will just take to mean its a request response type
- so looking at the docs, this is a lot liek the fetch method on JS, 
- i tried doing `req.text` or `req.json`, which i saw on the docs for the requests package, but it seems liek we are getting errors for this, perhaps because we are not getting access to these things or they are not actually returning anyhting like that, instead just returning the public information liek the status codes
- we can access teh status code specifcally though with `print(req.status_code)` and we see we get `200`, which emans everything is all good
- next we are going to actually make requets to endpoints that will give is json data, which is soemthing we've done alot in JS already

## Making JSON API Requests

- so for this we just want to get some information, not going to post or anyhting liek that yet
- for this we will continue to use the starwars or pokemon api that we have been using so far
- so we can do this just like we did above, with the `req.requests.get()` function, except this time we know we are expecting JSON data from the api
```
import requests

req = requests.get('https://pokeapi.co/api/v2/pokemon/1')
pokemon = req.json()
print(pokemon)
```
- this works as we expect, however it gives a ridiculous amount of information, liek too much to even beshown in the entire terminal, and it is not in a nice collapsible form liek it is when we test the JS fetch api calls in chrome
- so for these examples it is probably better to use the starwars api since it seems like it is less info
```
req = requests.get('https://swapi.dev/api/people/1')
character = req.json()
print(character)
```
> {'name': 'Luke Skywalker', 'height': '172', 'mass': '77', 'hair_color': 'blond', 'skin_color': 'fair', 'eye_color': 'blue', 'birth_year': '19BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/1/', 'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/6/'], 'species': [], 'vehicles': ['https://swapi.dev/api/vehicles/14/', 'https://swapi.dev/api/vehicles/30/'], 'starships': ['https://swapi.dev/api/starships/12/', 'https://swapi.dev/api/starships/22/'], 'created': '2014-12-09T13:50:51.644000Z', 'edited': '2014-12-20T21:17:56.891000Z', 'url': 'https://swapi.dev/api/people/1/'}
- so we get a much more managable amount of info here
- and importantly, we notice that this json data is formatted like a python dictionary! so we can just treat it liek a dictionary and accss it the same way, and we see fi we do `print(type(character))`, we indeed get `<class 'dict'>`
- so now we can do some more stuff with this data in the form of a dictionary, we see if we access `character['films']`, we get `['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/6/']`, which is a list of all the films the character appears in, but they are in the form of a further api url!, so we can try calling these and seeing what that data looks like:
```
req = requests.get('https://swapi.dev/api/people/1')
character = req.json()
print(character)
print(type(character))
print (character['films'])

req = requests.get(character['films'][0])
film = req.json()
print(film)
``` 
- so we added a second API call int he second section to the first item of the film list, since the list is a bunch of film orl strings, and we do the same thing with that data and we get a larger dictionary with more data for that first film but we notice: `{'title': 'A New Hope', 'episode_id': 4, 'opening_crawl': "It is ...`, the first item is the film title, so we can just use that, and try printing the title for all films:
```
import requests

req = requests.get('https://swapi.dev/api/people/1')
character = req.json()
print (character['films'])
for film in character['films']:
    req = requests.get(film)
    film = req.json()
    print(f'{character["name"]} appears in: {film["title"]}')
```
> ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/6/']
> Luke Skywalker appears in: A New Hope
> Luke Skywalker appears in: The Empire Strikes Back
> Luke Skywalker appears in: Return of the Jedi
> Luke Skywalker appears in: Revenge of the Sith
- so we see we are able to loop through the film list, and make a new seperate api request for each film, and print that information by accessing teh json response as a dictionary

## Reading JSON and Editing JSON

- often we also get our json data back as a long string, liek with proper dictionay like fomratting, but just as a string like: `"{'name': 'Luke Skywalker', 'height': '172', 'mass': '77', 'hair_color': 'blond', 'skin_color': 'fair', 'eye_color': 'blue', 'birth_year': '19BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/1/', 'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/6/'], 'species': [], 'vehicles': ['https://swapi.dev/api/vehicles/14/', 'https://swapi.dev/api/vehicles/30/'], 'starships': ['https://swapi.dev/api/starships/12/', 'https://swapi.dev/api/starships/22/'], 'created': '2014-12-09T13:50:51.644000Z', 'edited': '2014-12-20T21:17:56.891000Z', 'url': 'https://swapi.dev/api/people/1/'}"`
- to turn this into an actually dictionary object that we can reference properly and stuff we use a library called json, and specifically the `json.loads()` function
    - also a note from this function, i put the above string into a variable, `json_str`, and called `json.loads(json_str)`, and got the error `json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)`
    - so it seems liek the json standard is to have double quotes `"` for string property names and stuff, which my terminal when printing this out is using single quotes, so the `json.loads()` function is realizing this and giving an error
    - indeed when we look at the actual printout of the starwars api data on the website, it is all double quotes, so instead we will copy and paste that from the site and surround it with `'''` quotes to make it a string (since it is multi-line)
- and it works liek so:
```
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
```
- and we get the printout as `<class 'dict'>`, so it successfully turned it into a proper dictionary
- we can then modify it like any dictionary: 
```
data = json.loads(json_str)
print(type(data))

data['name'] = 'chris franko'
data["bae"] = 'sara huh'

data_str = json.dumps(data)
print(type(data_str))
print(data_str)
```
> <class 'dict'>
> {"name": "chris franko",... ..., "bae": "sara huh"}
> <class 'str'>
- so we can see here we got the json data in sring format, made it into a dictionary with `json.loads()`, then we edited the dictionary by cahnging the name to 'chris franko' and added the key `'bae'` with value `'sara huh'`, and then we turn it back into a string with `json.dumps()`
- loads() stands for load string, since we are taking the string and loading it into a dictionary, and dumps() stands fro dump string since we are taking the dictionary and dumping it into a string instead
- so now that we have a string we could send it back to the endpoint or aomthing since it takes and sends string data
- now alot of apis will just give actual json objects as dictionaries, but some sill give strings and we need to know how to handle them

## Function *args

- in a lot of python, particularly in a lot of django, we see a lot of python functions that take arguments like `def func(self, request, *args, **kwargs):`
- specifically wiht the `*args` argument, it lets us pass in an undefined number of arguments to a function, and within the function, these then are accessible as a tuple 
```
def sum1(*args):
    print (args)
    print (type(args))
    result = 0
    for num in args:
        result += num
    return result

print(sum1(1, 2, 3, 4, 5))
```
> (1, 2, 3, 4, 5)
> <class 'tuple'>
> 15
- so within the function, all things passed in as args are extra variables that get tossed into a tuple, we see that this neccessitates our function arguments being formatted as (required-arguments, *args), since args can be infinite length, we the first n arguments will be taken as the first n required variables
- we also see python will accept optional variables here as (required-arguments, optional, *args), but then it just always takes the second argument, or first arg if no optional is given, as the option variable, so they are useless in this sense
- and we dont actually need to use 'args', we just need the '*' delimiter, and in JS it is '...' for example

## Function **kwargs

- so kwargs stands for key-word arguments, and we pass these in after kwargs, and these are accessible within the function as a dictionary, but this means we need to pass in keys and values into the function argument line
- we do this in the function call using the equal sign `=`, in `key=value` notation seperated by commas
- for example, if we wanted to pass kwargs to the sum1 function above from the args lecture, we can do `sum1(1000, 1, 2, 3, 4, 5, name='chris', age=29, best='ferbie')`
- notice here as well that we are not passing keywords as strings to the function, we are doing `name='chris'` and not `'name'='chris'`, even though when we access them within the function we do call them with strings like a regular dictionary:
```
def sum1(num, *args, **kwargs):
    print(f"sum # {num}, by {kwargs.get('name')}")
    print (args)
    print (type(args))
    print (type(kwargs))
    print (f"{kwargs.get('name')} is {kwargs.get('age')} and the goodest boy is {kwargs.get('best')}")
    result = 0
    for num in args:
        result += num
    return result

print(sum1(1000, 1, 2, 3, 4, 5, name='chris', age=29, best='ferbie'))
```
> sum # 1000, by chris
> (1, 2, 3, 4, 5)
> <class 'tuple'>
> <class 'dict'>
> chris is 29 and the goodest boy is ferbie
> 15
- here we are also accessing the dictionary values with the get() method as `dict.get(key)`, this is the same as doing `dict['key']`, except get() is slightly nicer since if the key does not exist it will return `None` instead of raising an error, we can also speicfy a default valeu with `dict.get(key, default_value)` to return if the key does not exist (instead of `None`)
- and this works great as we would expect

## How To Install Pip

- pip allows us to install third party packes for python
- we have pip

## Mutable vs Immutable Variables

- 

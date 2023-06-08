valid_moves = ['rock', 'paper', 'scissors', 'r', 'p', 's']
move1 = 'rock'
if move1 in valid_moves:
    print(f'{move1} is a valid move')
else:
    print(f'{move1} is not a valid move')

move2 = 'water'
moves_set = set(valid_moves)
print(moves_set)
print(move1 in moves_set)
print(move2 in moves_set)

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

with open('PythonCourse/RPS.py', 'r') as file:
    content = file.read()
print (type(content))
# print(content.upper())

# with open('pythoncourse/write_file.txt', 'w') as file:
#     file.write('this was made in a python file using "with"')
with open('pythoncourse/write_file.txt', 'a') as file:
    file.write('\nthis line was appended in the with command in "a" mode')

with open('pythoncourse/emails.txt', 'r') as file:
    email_lst = file.readlines()
gmails = [email.strip() for email in email_lst if 'gmail' in email]
print(gmails)
yahoos = [email.strip() for email in email_lst if 'yahoo' in email]
print(yahoos)

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

# filename = input('What is the file name? ')
# contact = input('Please enter contacts in the format "Name, email", followed by a return. When finished enter "d" for "done": ')    
# address_book = {}
# while contact != 'd' and contact != 'done':
#     person = contact.split(",")
#     address_book[person[0].strip()] = person[1].strip()
#     contact = input('Enter another contact as "name, email" (or type "d" to finish): ')
# print(address_book)

# with open(filename, "w") as contacts:
#     content_str = ''
#     for key, value in address_book.items():
#         content_str += f'{key}: {value}\n'
#     contacts.write(content_str.rstrip())
# # with open(filename, "a") as contacts:
# #     for key, value in address_book.items():
# #         contacts.write(f'{key}: {value}\n')

# open_file = input(f'would you like to review {filename}? (Y / N) ')
# if open_file.lower() in ['y', 'yes']:
#     with open(filename, 'r') as file:
#         print(file.read())

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









        
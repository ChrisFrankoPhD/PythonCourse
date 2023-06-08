message = 'las ratas own this city'
print('Hello World')
print(message)

x = 5
if x > 10:
    print('x is small')
    x += 10
else:
    print('x is big') 

def emptyfunc():
    pass
y = 0

items1 = 4
price1 = 19.97
total1 = items1 * price1
print(total1)
items2 = 4
price2 = '19.97'
total2 = items2 * price2
print(total2)

lst = [1, 'chris', ['ferbie', 'theo'], 500.65]
num1 = lst.pop()
print(lst)
print(num1)

person1 = {
    'name': 'chris',
    'age': 29,
    'fav drink': 'latte'
}
print(person1['name'])
print(person1)
person1['email'] = 'chris@gmail.com'
print(person1)
del person1['age']
print(person1)

lst2 = ['banana', 'apple', 'orange', 'berry']
lst2.sort()
print(lst2)

lst3 = ('banana', 'apple', 'orange', 'berry')
print(lst3.index('banana'))
print(lst3[2])

set1 = {'item1', 'item2', 'item3'}
print(set1)
set1.add('item5')
set1.remove('item2')
print(set1)

is_tall = False

if not is_tall:
    name = 'shrimpy'
else: 
    name = 'chris'

print(name)

# input_age = input('how old are you? ')
# print(type(input_age))

# input_age = int(input_age)
# print(type(input_age))

# print(f"in dog years, you are {str(input_age * 7)} years old")

grocery_list = ['apples', 'oranges', 'bananas', 'apples']
grocery_list.append('apples')
grocery_list.append('flour')
grocery_list.append('bananas')
grocery_list.append('milk')
print(grocery_list)
print(type(grocery_list))
grocery_list = set(grocery_list)
print(grocery_list)
print(type(grocery_list))
grocery_list = tuple(grocery_list)
print(grocery_list)
print(type(grocery_list))

print("format method")
for item in grocery_list:
    print("buy some {} please".format(item))

print("f-string method")
for item in grocery_list:
    print(f"buy some {item} please")

print("old % method")
for item in grocery_list:
    print("buy some %s please" % item)



can_code = True

if can_code:
    # do something
    print('you can code')
else:
    # do soemthing else
    print('you cannot code yet')

username1 = 'chris franko'

if username1 == 'Chris franko':
    print('access granted')
else:
    print('access denied')

username2 = 'christopher'
# username2 = input('username? ')

if username2.lower() == 'chris franko':
    print('access granted')
else:
    print('access denied')

username3 = 'chris franko'
if username3.lower() != 'chris franko':
    print('access denied')
else:
    print('access granted')

important_data = None

if important_data:
    print('data logged')
else:
    print('no important data found')

string1 = 'False'
if string1:
    print('string is True')
else:
    print('string is False')

string1 = '0'
if string1:
    print('string is True')
else:
    print('string is False')

lst4 = []
if lst4:
    print('list is True')
else:
    print('list is False')

set2 = {}
if set2:
    print('set is True')
else:
    print('set is False')

dic1 = {'': 0}
if dic1:
    print('dic is True')
else:
    print('dic is False')

age1 = 19
name1 = 'chris'
if age1 >= 19 and name1:
    print(f'{name1} can drink because they are 19 or over')
else:
    print('sorry they cannot drink because they are too young or do not exist')

age2 = 19
name2 = ''
if age2 >= 19 or name2:
    print('have a drink')
else:
    print('no drink for you')

age3 = 19
name3 = ''
if age3 >= 19 and not name3:
    print('we only serve nameless adults, come in')
else:
    print('sorry no namies or young people around here')

fav_foods = ['latte', 'melon', 'bifana', 'pastel de nata']
for food in fav_foods:
    print(f'i like {food}')

fav_foods_set = {'latte', 'melon', 'bifana', 'pastel de nata'}
for food in fav_foods_set:
    print(f'i like {food}')

person2 = {
    'name': 'chris',
    'age': 29,
    'fav drink': 'latte',
    'fav food': 'sushi'
}
for key in person2:
    print(key)
for key in person2:
    print(f'{key}: {person2[key]}')
for key, value in person2.items():
    print(f'{key}: {value}')

num1 = 0
while num1 <= 10:
    print(num1)
    num1 += 1

num2 = 0
while num2 <= 10:
    if num2 % 2 == 1:
        num2 += 1
        continue
    print(num2)
    num2 += 1

fav_foods2 = ['latte', 'melon', 'bifana', 'pastel de nata', 'sushi', 'cookie']
print('im going on a diet')
for idx in range(len(fav_foods2)):
    if fav_foods2[idx][0] == 'p':
        print (f'{fav_foods2[idx]}? oh no i cant give up "p" foods, bye')
        break
    print(f'no more {fav_foods2[idx]}')

def greet(name, birth_year):
    age = 2023 - birth_year
    print(f'hi {name}, you are {age} this year')

greet('sara', 1996)

def sum(*args):
    result = 0
    for num in args:
        result += num
    return result

print(sum(1, 2, 3, 4, 5))
print(sum(1, 2, 3))

def suma(**kwargs):
    result_sum = 0
    result_str = 'total = 0\n - \n'
    for key, num in kwargs.items():
        result_sum += num
        result_str += f'add {key} = {num}\ntotal = {result_sum} \n - \n'
    result_str += 'done'
    return result_str

print(suma(a=1, b=2, c=3, d=4, e=5))
print(suma(a=1, b=2, c=3))

def greet2(name, birth_year=0):
    age = 2023 - birth_year
    print(f'hi {name}, you are {age} this year')

greet2('sara')

def greet3(name, birth_year=0):
    age = 2023 - birth_year
    print(f'hi {name}, you are {age} this year')

greet3('sara', 1996)

def greet4(name, country, birth_year=0):
    age = 2023 - birth_year
    print(f'hi {name}, you are {age} this year')
    def brit_check():
        print('eff off mate')
    if country == 'britain':
        brit_check()

greet4('sara', 'britain', 1996)

name4 = 'sara'
def greet5():
    name4 = 'chris'
    print(name4)

greet5()
print (name4)

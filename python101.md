# Python101: Beginner Friendly Python

- probably good to note here, I have taken some extensive python courses on Coursera previously, the ones offered by RICE, (Introduction to interactive Programming 1 and 2, Principles of Computing 1 and 2, Algorithmic Thinkng)

## Learning Python 2 vs 3

- python 2 is not maintained and can be a security risk for companies now, so we will use python 3 in this course, 

## Installing Python

- i already have python installed, we can do `python -V` in the command line to check to see what verison we are using, i am using 3.11

## How to Execute Python Code 

- apparently there is really 1 main way to run python code, through the terminal
- to execute a python file we just type `python filename.py` to execute the file
- so ive created a python file int he pythoncourse directory, and it is just a simple hello world named 'python101-Testfile.py':
```
print('Hello World')
```
- and we can run this in the command line in vscode by opening up the terminal with 'ctrl + \`'(just ctrl plus backtick), then typing in `python python101-TestFile.py`, and we see the terminal prints out `Hello World`
- it is good to note that if we want to run the file with a different python verison that we have installed we can do `python3.10 python101-TestFile.py`
- we can see this works in both the vscode terminal and in the git bash terminal, and also in windows poershell, command prompt, and in ubuntu terminal, but for the WSL ubuntu it made me specify `python3 python101-TestFile.py` in order for it work properly, or else we got an error

## Basic Arithmetic

- okay so not sure how much of these lessons I am going to take good notes or try on, since this is all throroughly covered and practiced by me in previous courses/projects
- so we can execute python either in our files, and then running them, or we can also execute python in the terminal by using the `python` command, which opens up a little python shell for us, and to go back to the regular terminal we can do `quit()`
- so doing it in the terminal liek this is good for messing with little thing like arithmetic
- addition uses the `+` operator
- subtraction uses the `-` operator 
- multiplication uses `*`
- divison `/`
- exponential `**`
- modulus `%` (remainder, `10 % 3` gives 1 for example)
- floor division `//` (`10 // 3` gives 3 for example)
- math operations are not as important in wed dev as we may thin, except for thing like algorithms if we got into search engine stuff or big data science stuff

## Introduction to Variables in Python

- a variable is a piece of memory allocated to a named association
- we know how to use variables of course, unlike JS we do not need to define `let` or `const`, we can just say `x = 3`
- we also dont need semi-colon to denote end of line stuff, python instead works with end of lines, python cares about enpty space
- so when we do like `course = 'python 101'` then `print(course)`, we allocated some memory to the allocation of `course` with 'python101', and then when we print it, the computer goes and fetches that from memory using that association
- of course we want to use variables when we need to access the same thing multiple times

## Formatting Code in Python 

- in python we dont use curlybraces or antyhing to show what is encapsulated in a function, instead we just indentation, adn line breaks to show when things end
- you can actuall yindent any way we want as long as it is consistent, can be single space, or double, or tab, which is what most people use
- so if we have two variables we want to declare we just but the on different lines and python figures it out
```
name1 = 'chris'
name2 = 'sara'
```
- no need for the semi colons or anyhting
- also for things like function, or if statements, we follow the statement or function definition with a colon `:` and this tells python the next line should be indented, and the indent defines the coding block
```
if x > 10:
    print('x is small')
    x += 10
print('x is big') 
```
- so python knows that the indented code is inside the conditional block, whereas the next unindented line, even though there is no bracket seperation, is outside that block and not affected by the print statement
- also, something unique to python, is that python will not let us have empty coding blocks, liek empty conditionals or functions, we have to write `pass` in it or we get an error 
- the indentation thing is nice for vscode since we can collapse each indented block of code, which is good for readability if we only want the broad strokes of the function

## Code Comments

- we comment in python by starting the line with `#`, we can also make them at the end of the line which is nice, like after some variable definition
- typically we dont comment basic code, but if were doing something more complex we add comments to explain things
- used ltos to add '#TODO' lists, which are nice to things we know we want to write down to do later
- vscode has a todo tree extention that lets us write todo and then it makes a list of all of them for the project and we can go look though them and go tot he files to fix them 

## Data Types 

- lot so fdata types in python, and we can create our own as well
- strings, text enclosed in quotes, 'this is a string'
- integers, whole numbers, 100
- floats, decimal numbers, 100.0
- lists, like arrays in other languages, [1, 'abc', 5.6, etc]
- tuples, an immutable (can't alter) list, (1, 'abc', 5.6, etc)
- sets, like a list that doesnt maintain its order, unordered, unindexed, and with unchangable elements {5.6, 'abc', 1, etc}
    - in python 2, sets were defined like `set1 = set{c,a,b}`, and were representing with the set prefix, like `print(set1)` -> `set{c,a,b}`
- dictionary, looks liek a JS object, key: value pairs, {key: value, name: 'chris'}
- Booleans, True and Flase, need to use capitals in python
- None type, need to use a capital N, None

## Numeric Data Types: Integers and Floats

- python numbers are a bit different from JS, JS would interpret numerical strigns as Num types, but python does not do that 
- for example
```
items = 4
price = 19.97
total = items * price
print(total)
```
>79.88
- which is as expected, but if we did:
```
items = 4
price = '19.97'
total = items * price
print(total)
```
>19.9719.9719.9719.97
- instead the string was interpretted as a string, and not a numberm, we multiplied the string 4 times, giving us a bigger string made of the price string 4 times in a row
- also integers and floats are of course different datatypes, but they play nice together since they are both datatypes

## Strings

- we can use buth `'` and `"` for our strings, as long as they open and close with the same thing, and we can even do multi line strings with `"""`, which allows us to put returns in a single string itself
- strings, and other data types have a bunch of built in methods we can use to modify and work with them 
- for example if we go in to the `python` program in our termin, and define a string as `sentence = 'string'` lets say, then in the terminal type `sentence.` and hit 'tab', we will get a printout of a ton of different methods we can use with sentence
    - okay actually this isnt working with me, but we can find all the methods we can use online
    - also VSCode works with typing `sentence.` in a python file and it gives us all the methods we can put in there
- `sentence.upper()` makes the whoel thing uppercase, `sentence.lower()` makes it lowercase
- we can also do `type(sentence)` to give us the type of the data, and can do that with anything 
- like with JS, these all take parenthesis since they are something to be executed

## Lists

- lists are defined with square brackets
- we can put anything we want as elements in lists, lists within lists and stuff 
- printint a list just prints the whole list in brackets and everything
- we can do a for loop to print each item 1by1, a for loop loops over the list item by item, and completes some logic ont he item
```
lst = [1, 'chris', ['ferbie', 'theo'], 500.65]
for item in lst:
    print('item: ', item)
```
- this will print all items int he list in different print statements
- we can add items to lists with `lst.append(item)`, where item is the thing to append to the end of the list
- we can also remove something specific with `lst.remove('chris')`, this simply removes the name from the list
- we can also use the pop function, that removes the last item of the lis and returns it, so we could do `x = lst.pop()` and 
```
lst = [1, 'chris', ['ferbie', 'theo'], 500.65]
num = lst.pop()
print(lst)
print(num)
```
> [1, 'chris', ['ferbie', 'theo']]
> 500.65
- so we see pop removed the last item of the list, and reutrned it, so it got set to the variable num1
- we can also give an index to pop as an argument, so `lst.pop(1)` would have removed 'chris' instead of the last item

## Dictionary

- these are a special datatype, they are really a data structure
- we define them with key:value pairs in curly braces, and each key"value pair has to be seperated by a comma, like in JS
- for example:
```
person1 = {
    'name': 'chris',
    'age': 29,
    'fav drink': 'latte'
}
print(person1[name])
```
> chris
- so we access values int he dictionary by the key names with the dict[key] syntax
- we can also set new key:values with the same syntax, where to add an email we would do `person1['email'] = 'chris@gmail.com'`
- the same is true if we want to update a dictioanry value, if our email changed with could do `person1['email'] = 'chris@yahoo.com'`, and it would not create a new item, it would just update the value for the 'email' key
- we can also delete dictionary items with the del keyword, so we could do `del person1['age']`, and the age item would det deleted completely
- dictionaries are very important, this is how we store lots of related vairables, it is basically like a JS object, and we can even put dictionaries within dictionaries 
- in general, we usually will have a string as the dictionary key, and then the values can be anything
    - specifcally, keys must be immutable, so we cant use a list as a dictionary key, we could use an integer, float, or tuple though, but this maynot have many use cases
    - there are 0 restrictions on dictionary values

## Tuples

- tupels are like lists in that they are iterable, but they are different since they are immutable
- so we can use a for loop to work through all the elements of a tuple, and we can do things with those elements and stuff, but we cannot go into the tuple and alter the elements
- for example, the method `.sort()` will alphabetically sort the items of a iterable, so if we do:
```
lst2 = ['banana', 'apple', 'orange', 'berry']
lst2.sort()
print(lst2)
```
> ['apple', 'banana', 'berry', 'orange']
- but if we try to do the same in the tuple:
```
lst3 = ('banana', 'apple', 'orange', 'berry')
lst3.sort()
print(lst3)
```
> AttributeError: 'tuple' object has no attribute 'sort'
- so there is no sort attribtue for the tuple, since it is immutable, and cannot be changed, even the order
- for exampel we could also do:
```
lst3 = ('banana', 'apple', 'orange', 'berry')
lst3[2] = 'watermelon'
print(lst3[2])
```
>TypeError: 'tuple' object does not support item assignment
- so here its not an issue of the mthod not existing, we simply just cant assign things to a tuple, since once it exists it is forever unchanged
- we see that if we do `lst3.` in vscode, the only methods that show up are `lst3.count(item)` and `lst3.index(item)`, which give us the number of times an item appears int he tuple and will give us the index of a given item in a tuple
- as mentioned we can still loop thorugh them though, which is nice, since we are not altering it
- the nice part about tuples is that they take up much less memory since there are so many less thigns we can do with them, they are static, whereas a list has so amny associated methods and can always be cahnging, they are more cumbersome
- interesting behaviour with tuples is that if if have mutable objects inside of a tuple, we can alter them, for example:
```
tup1 = ([1,2], [3,4])
tup1[0][0] = 0
print (tup1)
```
> ([0, 2], [3, 4])
- so since lists are mutable, we can access the list within the tuple and alter that, but we cannot do it in this manner:
```
tup1 = ([1,2], [3,4])
tup1[0] = [0,2]
print (tup1)
```
>TypeError: 'tuple' object does not support item assignment
- here we are actually addressing the tuple item and trying to assign it, so we cannot do that

## Set Data Types 

- so a set looks like a dictionary with the curly braces, but does not take key:value pairs, instead we define it just as a list of items
- the st is a bit mroe performant since it does not need to rememeber ordering or anything
- so we can define a set like:
```
set1 = {'item1', 'item2', 'item3'}
print(set1)
```
> {'item2', 'item3', 'item1'}
- so the set does not have an order, when we printed it just gets us the items in the most efficient way it can, not caring about putting them in order
- we also see a set has to be **unique**, so if we try to define a set with 2 of the same items, it gets rid of the extra item, always keeps it unique
```
set1 = {'item1', 'item2', 'item3', 'itme2'}
print(set1)
```
> {'item3', 'item2', 'item1'}
- it just compeltely got rid of the extra value 
- to add items to a set we use the `set1.add(item)` method, and to remove we can use the `set1.remove(item)` method
- sets can be useful when we want a list of items where we want to keep addign things to it, but do not want to end up with duplicates, we can also cast a list into a set to get rid of any duplicates if we want to as well which is nice

## Booleans

- Booleans can either be a True or False value, either 1 or 0 (1 for True, 0 for False)
- important to note the capitals, will not work otherwise
- booleans are super improtant when we are working with conditionals of course
```
is_tall = False

if not is_tall:
    name = 'shrimpy'
else: 
    name = 'chris'

print(name)
```
- so since is_tall is equal to False, `if not is_tall` evaluates to True, and the condition is passed and name = 'shrimpy', if is_tall is True, then name = 'chris', 
- also if we do `is_tall = 'abc'` we get name = 'chris', since any non-empty data type is evaluated to True
    - for example, `''` `{}` `[]` `0` all evaluate to False, but all strings and other filled data types, even `'False'`, evaluate to True
- Booleans are basic, but they are involved in basically everything we do

## None Type

- the None type measn there is nothing in it yet, or we have specifically set it to be nothing
- to set a variabel to None type, we need to use the uppercase, similar to boolean
```
wallet = None
```
- so this is an empty variable, and we usually use this is we want to initialize a varibale now, and put somhting in it later
    - note this came up in lecture, 'is vs ==' '== vs is', `==` conditonal checks if two variables evaluate to the same thing, `is` checks if two variables point to the same object in memory, so are they literally the same thing

## Indexing and Slicing Iterables 

- iterables are anythign we can loop through, like arrays, tuples, sets, dectionaries, strings
- of course, iterables like arrays have indexes, where the elements each have an associated index number
- for arrays we can do `lst[0]` to reference the first item
- we can also get multiple items from a list by slicing it, where we can grab items 1 t0 3 like `lst[1:3]`
- we can also do `lst[2::]` which wll get us all the elements from index 2 to the end of the list
- we can also grab items starting from the last value with `lst[-1]`, which grabs the last item, for example `lst[-3]` gets the third last item
- we can also do this with strings, all the same things apply, where every character is its own element

## Accepting User Inputs

- so python for us at the moment is really a command line language, and we can ask for user inputs from the command ine which is actually pretty cool 
- we do this with the `input()` function, so when it gets called, the argument of input() gets printed ont he command line, and the program does not continue executing until an input is given from the user
- so we could do a simple input like:
```
input_age = input('how old are you? ')
print(f"in dog years, you are {input_age * 7} years old")
```
>in dog years, you are 29292929292929 years old
- where we are using an f-string here for the print statement, which is like backtick string literals in JS, putting "f" in front of the string allows us to put logic in curly braces in the string
- so this is a good example of understanding data types again, **user inputs are always returned as strings**, so even if I just put a number here in the command line, the variable `input_age` will be `input_age = '29'`, and then the print statement reads 'in dog years, you are 29292929292929 years old'
- so we have to cast the data type into a number, so we could do:
```
input_age = input('how old are you? ')
print(f"in dog years, you are {int(input_age) * 7} years old")
```
>in dog years, you are 203 years old
- so now this works as expected
- even so this is maybe not the best example since python is actually auto-casting the integer into part of a string for the print statement, since `int(input_age) * 7` returns an int, howver it still works in this case, 
- to be more clean we could do:
```
input_age = input('how old are you? ')
print(f"in dog years, you are {str(int(input_age) * 7)} years old")
```
>in dog years, you are 203 years old
- where now we are casting the input_age to a int, then recasting the final value into a string
- so this is a good dual example of casting and of user inputs

## Type Casting

- casting is changing one data type into another, which we did above
- so the example he gives is the one we did above, where we see that the type of the user input is going to be a string no matter what, then we want to cast that into an int
- one notable thing here is that we can look at the type of any variable in python with the `type()` method
- so if we have:
```
input_age = input('how old are you? ')
print(type(input_age))

input_age = int(input_age)
print(type(input_age))

print(f"in dog years, you are {str(input_age * 7)} years old")
```
- and the outputs are `<class 'str'>`, `<class 'int'>`, and `in dog years, you are 203 years old`
- so now we can visualize our types 
- we can also see that this relies on good user input, if I input 'chris' intp the command line instead of an age, then 'chris' cannot be cast into a int, so we get an error:
>ValueError: invalid literal for int() with base 10: 'chris'
- we can also see a good exampel of this with lists and sets, we can cast a list into a set to get rid of all duplicates, imagien a grocery list that we can add things to dynamically, but then we want to be able to get rid of all duplicates before we go to the store incase we added things twice, then once at the store we want to make the list immutable so we dont get extra things, so we want a tuple:
```
grocery_list = ['apples', 'oranges', 'bananas', 'apples']

# add stuff to list
grocery_list.append('apples')
grocery_list.append('flour')
grocery_list.append('bananas')
grocery_list.append('milk')

# print list
print(grocery_list)
print(type(grocery_list))

# get rid of duplicates
grocery_list = set(grocery_list)
print(grocery_list)
print(type(grocery_list))

# make immutable
grocery_list = tuple(grocery_list)
print(grocery_list)
print(type(grocery_list))
```
- and we see the output:
```
['apples', 'oranges', 'bananas', 'apples', 'apples', 
'flour', 'bananas', 'milk']
<class 'list'>
{'apples', 'flour', 'bananas', 'milk', 'oranges'}    
<class 'set'>
('apples', 'flour', 'bananas', 'milk', 'oranges')    
<class 'tuple'>
```
- so understanding casting and what it can do for us is important

## Print Formatting

- lots of ways to format our print statements in python, we will use the most modern ones
- most of the time we do not want to print just a static string, we want to be able to print some of our variales within a static string
- we can do this with the format function, or with f-strings, imo f-strings are superior and easy to use
```
for item in grocery_list:
    print("buy some {} please".format(item))

for item in grocery_list:
    print(f"buy some {item} please")
```
- so we see in the format fucntion, we add some placeholder for a variable in the string, then add the method after with an argument that should be palced in the placeholder
- the f-string method requires us to add `f` before the string quotations, and then we can add variables and logic inside curly braces in-line, and this makes it much more readable since we see them as we go 
- the old old way of doing it is to have a `%s` in the string, and then after the string we denote `% item`, somewhat similar to the format method option
```
for item in grocery_list:
    print("buy some %s please" % item)
```
- this is not used much anymore, but we will likely see it in older code so good to know

## Comparison Operators

- computer needs to be able to make decisions on existing data
- most basic example is if something is True, do something, if soemthing is False, do something else
```
can_code = True

if can_code == True:
    # do something
    print('you can code')
else:
    # do soemthing else
    print('you cannot code yet')
```
- very simple example obviously, and importantly we can also make this simplier:
```
can_code = True

if can_code:
    # do something
    print('you can code')
else:
    # do soemthing else
    print('you cannot code yet')
```
- saying `if can_code` is the same thing as saying `if can_code == True`
- now of course we can have more logic than just checking if soemthing equals True, we just need the overall statement to evaluate to True for a conditional to run its code block, so any condition that evaluates to a Boolean can be used here
```
username1 = 'chris franko'

if username1 == 'chris franko':
    print('access granted')
else:
    print('access denied')
```
- now this is just an example of checking for a fake authentication where only I have access to soem portal, the print staements of course do not give or deny access, they are just there to give context to a possible functionality
- also notice that if `username1 = 'Chris franko'`, we get access denied, because thsi is not exactly the same as `'chris franko'`, 
- this is a good example of how we need to take into account user error in our code
- so if we wanted the username to not be case sensiive, we could change our conditional to be somthing like `if username1.lower() == 'chris franko':`, so that no matter what capitalization is used, as long as the name itself matches we are good
- we can go a step further with this by making it an actual user input:
```
username2 = input('username?')

if username2.lower() == 'chris franko':
    print('access granted')
else:
    print('access denied')
```
- so now we have the same thing, but with user input in the command line
- he also goes over here that we could add `elif` statements to make for comparison operators, and more paths to possibly go down 
```
username2 = input('username?')

if username2.lower() == 'chris franko':
    print('access granted')
elif username2.lower() == 'sara huh':
    print('bae also gets access')
else:
    print('access denied')
```
- so the `elif` statement is the same as an `else if` in JS, it bsays if the condition is not true, test for this next condition to see if we should run this code instead, and we could chain as many `elif` statements as we want, although we also want to be careful and make sure it is still readable 
- if none of the if or elif staemetns pass, we then finally go to the else statement
- we can also use the is not `!=` operator to invert the conditional:
```
username2 = input('username?')

if username2.lower() != 'chris franko':
    print('access denied')
else:
    print('access granted')
```
- so this basically inverts the conditional, and for some instances is more intuitive or can simplify things
- we also have different types of comparison operators, like `>=`, `<=`, `<`, or `>`, which awe are familiar with from basic math, and from JS as well 

## Comparison Shortcuts

- comparison operators are really just looking for a True statement, and if it is, then execute the code block
- so now we are going over the idea of using `if something:` instead of using a direct comparison operator 
- for example:
```
important_data = None

if important_data:
    print('data logged')
else:
    print('no important data found')
```
- we see that this prints `no important data found`, since the `None` type always evaluates to False
- likewise, an empty string always evaluates to false, whereas any string with content will evaluate to True, even 'False' or '0', and we see this is the expected behaviour for all data types:
```
string1 = 'False'

if string1:
    print('string is True')
else:
    print('string is False')
```
>string is True
```
string1 = '0'
if string1:
    print('string is True')
else:
    print('string is False')
```
>string is True
```
lst4 = []
if lst4:
    print('list is True')
else:
    print('list is False')
```
>list is False
```
lst5 = [0]
if lst5:
    print('list is True')
else:
    print('list is False')
```
>list is True
```
set2 = {}
if set2:
    print('set is True')
else:
    print('set is False')
```
>set is False
```
set2 = {''}
if set2:
    print('set is True')
else:
    print('set is False')
```
>set is True
```
dic1 = {'': 0}
if dic1:
    print('dic is True')
else:
    print('dic is False')
```
>dic is True

## Multiple Comparison Operators

- so we can combine operators with the Boolean logical operators `and`, `or`, and `not`
- so instead of doing a nested if statement to check for two conditionals, we could combine them with 'and'
```
age1 = 19
name1 = 'chris'
if age1 >= 19 and name1:
    print(f'{name1} can drink because they are 19 or over')
else:
    print('sorry they cannot drink because they are too young or do not exist')
```
> chris can drink because they are 19 or over
- so it works because both the presented conditionals evaluate to True, we can try changing one of them to not evaluate to True and we see:
```
age1 = 19
name1 = ''
if age1 >= 19 and name1:
    print(f'{name1} can drink because they are 19 or over')
else:
    print('sorry they cannot drink because they are too young or do not exist')
```
> sorry they cannot drink because they are too young or do not exist
- so even though the first coditional passed, the second did not, so the total did not pass
- with an `or` statement, we see that only one of the statements needs to be True, if we do the same as above but change `and`  to `or`:
```
age2 = 19
name2 = ''
if age2 >= 19 or name1:
    print('have a drink')
else:
    print('no drink for you')
```
> have a drink
- so even though only the first one passed, since it is `or`, the whole thing is still True
- for the last one, we can use `not` to flip a Boolean from True to False, or vice-versa, so we have the second example from above, where only 1 of the conditionals in the `and` statement was True, so it did not pass, now we can do:
```
age3 = 19
name3 = ''
if age3 >= 19 and not name3:
    print('we only serve nameless adults, come in')
else:
    print('sorry no namies or young people around here')
```
> we only serve nameless adults, come in
- so even though `name3` is `False`, `not name3` is True! so it works

## For Loops

- lets us iterate through any iterable, set, tuple, list, string, and do something for each item in the iterable
```
fav_foods = ['latte', 'melon', 'bifana', 'pastel de nata']
for food in fav_foods:
    print(f'i like {food}')
```
>i like latte
>i like melon
>i like bifana
>i like pastel de nata
- and this works for sets as well, except as we expect, the order changes since it just iterates through the most efficient path:
```
fav_foods_set = {'latte', 'melon', 'bifana', 'pastel de nata'}
for food in fav_foods_set:
    print(f'i like {food}')
```
>i like latte
>i like melon
>i like pastel de nata
>i like bifana
- and we can do this for all iterables, strings and tuples are pretty self explainatory, but it gets a bit more interesting for dictionaries
- we see if we loop through a dictionary we get just the keys:
```
person2 = {
    'name': 'chris',
    'age': 29,
    'fav drink': 'latte',
    'fav food': 'sushi'
}
for key in person2:
    print(key)
```
>name
>age
>fav drink
>fav food
- but we can easily gain access to the values using the keys if we wish:
```
person2 = {
    'name': 'chris',
    'age': 29,
    'fav drink': 'latte',
    'fav food': 'sushi'
}
for key in person2:
    print(f'{key}: {person2[key]}')
```
>name: chris
>age: 29
>fav drink: latte
>fav food: sushi
- or we can also 'deconstruct' the dictionary using the `for key, value in dict.items()` syntax:
```
person2 = {
    'name': 'chris',
    'age': 29,
    'fav drink': 'latte',
    'fav food': 'sushi'
}
for key, value in person2.items():
    print(f'{key}: {value}')
```
>name: chris
>age: 29
>fav drink: latte
>fav food: sushi
- so we get the same thing here, but it is a bit more concise looking
- .items() returns a dict_items class type object that behaves nicely with this syntax int he for loop, which is why this works

## While Loops

- a for loop iterates through an iterable until it is finished, while a while loop will continue looping indefinetly until some condition evalutates to `False`
- we have to be careful since it is very easy to get ourselves caught in an infinite loop with this, for example:
```
num1 = 0
while num1 <= 10:
    print(num)
```
- so this will just print the number 0 forever, and never stop until we crash our computer or browser
- we need to add some sort of logic to iterate num so that eventually the  condition becomes False
```
num1 = 0
while num1 <= 10:
    print(num)
    num += 1
```
- and this prints num from 0 to 10, then stops itself
 
## Break and Continue

- so the `continue` keyword is used in a loop to automatically move on to the next iteration in the loop
- it does not end the loop entirely, ust skips to the next iteration
```
num2 = 0
while num2 <= 10:
    if num2 % 2 == 1:
        num2 += 1
        continue
    print(num2)
    num2 += 1
```
>0
>2
>4
>6
>8
>10
- so here, we check the modulus of num2 and 2, so checking the remainder of num2/2, and if it equals 1, so if num2 is an odd number, we iterate num2, then we just `continue`, without printing it, so this makes us only print the even numbers
- we could also do this with a for loop of course, and this is nice if we only want to act on a part of the data
- we can also use the `break` keyword to stop the execution of the loop alltogehter, instead of just skiping the current iteration:
```
fav_foods2 = ['latte', 'melon', 'bifana', 'pastel de nata', 'sushi', 'cookie']
print('im going on a diet')
for idx in range(len(fav_foods2)):
    if fav_foods2[idx][0] == 'p':
        print (f'{fav_foods2[idx]}? oh no i cant give up "p" foods, bye')
        break
    print(f'no more {fav_foods2[idx]}')
```
>im going on a diet
>no more latte
>no more melon
>no more bifana
>pastel de nata? oh no i cant give up "p" foods, bye 

- okay so here is a very stupid example I made, where we are using a for loop, but we are actually looping though the idx values instead of the list items themselves
- `len(fav_foods2)` gives us the length of the list, which is 6 here, the number of items, then `range(len(fav_foods2))` is the same as `range(6)`, which constructs a list from 0 to (n-1) for us, so in our case it `range(6)` gives `[0,1,2,3,4,5]`, and so we are looping through the items of this list, which are equal to teh idx values of the fav_foods2 list we actually want to interact with
- so now in the logic itself, we act on each item of fav_foods2 with `fav_foods2[idx]`, and we are just checking if the food starts with a 'p', since `fav_foods2[idx]` references a list item, which is a string, so `fav_foods2[idx][0]` is referencing the first letter of that string
- so if the string starts with 'p', we use the `break` command, and we see the printout is executed and the loop completely stops!

## Functions

- functions allow us to write code once and us it many times
- in python, we use the syntax `def func():` to define a function
```
def greet():
    print('hi')

greet()
```
- this funcion simply prints 'hi', and the function is called whenever we state `greet()` in the code
- we can also pass parameters into the function by definign arguments for the function:
```
def greet(name, birth_year):
    age = 2023 - birth_year
    print(f'hi {name}, you are {age} this year')

greet('sara', 1996)
```
- so now we can pass a name into the function, in this case 'sara', and the function will print `hi sara`
- we also note that we need to be careful with our data types, here we need to make sure `name` is a string, while `birth_year` is a number
- **aside**
---
- one thing to note here that I havent used yet in my other courses, is that if we do not know the number of arguments we may have in a function, we can use the `*args` keywork int he function definition, 
    - really it is just `*` that does the work, `args` is just a name, but using `*args` is the standard 
- so we may have:
```
def sum(*args):
    result = 0
    for num in args:
        result += num
    return result

print(sum(1, 2, 3, 4, 5))
print(sum(1, 2, 3))
```
>15
>6
- so here the function `sum(*args)` works for any number of arguments, as seen in the below function calls
- we could of course just have a function that takes a list or set of numbers and iterate through and sum them `sum(num_list)`, and it would work just fine, but that means we have to construct the list ahead of time, sometimes using `*args` is preferable
- there is also a double asterisk `**`, verion of this usually called `**kwargs`, that is for doing the same but instead with an unknown number of key/value pairs in a dictionary like structure
```
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
```
- so with `kwargs` inside the funciton, we can use the dictionary methods like `.items()`, or `.values()`
- this is a big aside, but i thought it interesting
---
- back in the lecture
- we can also add default values to our functions, that let some arugments be optional, we do this by specifying a defualt value in the function argument definition
```
def greet2(name, birth_year=0):
    age = 2023 - birth_year
    print(f'hi {name}, you are {age} this year')

greet2('sara')

def greet3(name, birth_year=0):
    age = 2023 - birth_year
    print(f'hi {name}, you are {age} this year')

greet3('sara', 1996)
```
>hi sara, you are 2023 this year
>hi sara, you are 27 this year
- so in this case, in `greet2`, we see the printout just uses the default 0 value, so the age becomes 2023, but in the `grret3` we can still give it a value if we want, and we get the old age = 27 printout
- and we can put all the logic we want inside functions, including calls to other funcitons, or even other function definitions
```
def greet4(name, country, birth_year=0):
    age = 2023 - birth_year
    print(f'hi {name}, you are {age} this year')
    def brit_check():
        print('eff off mate')
    if country == 'britain':
        brit_check()

greet4('sara', 'britain', 1996)
```
>hi sara, you are 27 this year
>eff off mate

- this is a useless and silly example, but we can define and use the `brit_check()` function within the `greet4()` function
- and if we try to call `brit_check()` outside of the `greet4()` function, we get `NameError: name 'brit_check' is not defined`, since it is scoped to being inside the `greet4()` function
- and of course we can do lots of things more useful to this with functions

## Scope

- if we define a variable within a function, we cannot access that variable from outside the fucntion
- and this is good, we do not want a ton of global variables floating around 
- a good example of this is the `brit_check()` function defined within the `greet4()` function above, and when I tried to call it outside the funciton, I get the error `NameError: name 'brit_check' is not defined`
- now, liek with JS, we can access variables from outer scopes within inner scopes, however, variables defined within the fuction take precedent 
```
name4 = 'sara'
def greet5():
    name4 = 'chris'
    print(name4)

greet5()
print(name4)
```
>chris
>sara
- so here we have a global parameter `name4`, but we also define `name4` within the function, so the function `name4` takes precedent when we call it within the function, and 'chris' pritns when `greet5()` is called
- then outside of the funciton, when we `print(name4)`, 'sara' is printed instead since we are outside the function now
- in general it is generally best practice to put our parameters inside arguments for funcitons and explicitly pass them in 

## Local Server

- to run a local server, we can go into the command line and do `python -m http.server`, and we see we get teh printout `Serving HTTP on :: port 8000 (http://[::]:8000/) ...`
- so we can go to our browser and navigate in the address bar to "localhost:8000", which apparently read as 'local host port 8000', and we see that we have a little browser version of our current directory in there, in my case it is everything in the 2023 Ultimate Web Development folder since that is the directory we have open in VSCOde
- and if we click on files and stuff we can see the source code within those files, and as we navigate the url changes to 'http://localhost:8000/PythonCourse/p101test.py' for example
- we can simply do 'ctrl + c' in the command line to cancel the server hosting, and then we see when we try to navigate further in the online browser it is unable to load 
- he then goes and makes a simple index.html file that just has an h1 with 'welcome to python101', to show that the index file now loads instead of the directory when the server is loaded
- i actually he does a v ery bad job of explaining what is going on here and its relevance, he mentions being able to use this for simple fun websites like our pokemon character generator, but what does he mean by that? The API calls are to other databases that we certianly are not going to rebuild, and this is just a simple local server so it doesnt seem liek this could actualy host a website for us?
- okay then he also mentions we can make it accessible with 'ngrok.com', but i am still unsure what we are really doing here

## Importing Packages and Using Them

- python packages are very helpful, it seems like packages are really the core of python
- for example, we can import the package 'random', to be able to pick random numbers, or make random choices from a list
- we do this by adding `import` statements at the start of our code, we can also do this right int he python shell as well
- we can then use the `random.choice()` function which given a list will choose a random item from that list
```
import random
moves = ['rock', 'paper', 'scissors']
random.choice(moves)
```
>paper
- and each time we call it we will get a different answer
- now he mentions we are not really learning all about imports and packages yet, but need this for the project

## Our Project: Rock Paper Scissors

- we will be playing rock paper scissors against a computer 
- we will need random, while loop to play until we win, input to give our input, print formatting to say who wins, comparison operators to evaluate resuls, and break/continue
- 
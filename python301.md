# Python 301: Advanced Python

## Creating A Python Class

- I've made classes before in the python courses from coursera, but this is a good refresher since recent courses have been on algorithms and stuff instead
- we create a class with the `class ClassName` syntax, where we always want our classes to start with an uppercase
- this defines the class, but then we want to also create an instance of the object from that class
- we can also give classes properties, which describe the state of the object, they are liek the items in a dictionary, but we have more customizability for how the class works here, 
```
class Person:
    money = 0
    greeting = 'hello'

chris = Person()
print(chris.money)
print(chris.greeting)
```
> 0
> hello
- so here we created a class named `Person`, then created an instance of the Person object, and printed the default properties that
- now this is not terribly useful since all instances of Person are going to be identical here, we want to be able to use an initializer function to make each person different in some, and we also want to be able to give Person some methods to work with, othewise it really is just a fancy dictionary at the moment

## Class Properties

- the class properties can be literall anything, to make it a bt more complicated we will make it a dictionary
```
class Person:
    money = 0
    greeting = 'hello'
    favourites = {
        'dog': 'ferbie',
        'food': 'sushi',
    }

chris = Person()
print(chris.favourites['dog'])
```
- since `chris.favourites` is a dictionary, that expression just grabs the dictionary abject, and then we can act on it and do whatever we want with it liek any other dictionary
- one thing to note i that python does not have private proeprties, all properties in python are public, which means we can access and change them from outside of the class
    - for example, in the code above we could do `chris.favourites['food'] = [1,2]`, and the attribute would simply be changed, since it is public
    - if it was private, then it could only be changed within the class itself, but python does not offer this functionality 
    - instead what we do is denote the property as private by adding a '_' at the start of the name, so it would be `_favourites`
    - this does not actually change anything, but is convention to let people using the code know that that property is not meant to be accessed publically
- to chnage 'private' attributes, we wold use getter/setter methods as defined function from within the class, so we may have:
```
class Person:
    money = 0
    greeting = 'hello'
    
    def set_money(self, num):
        self.money = num

chris = Person()
print(chris.money)
chris.set_money(1)
print(chris.money)
```
> 0
> 1

- and this is nuce since we could add some validation to the method to make sure `num` is indeed a number, and not a string, so that the attribute isnt set improperly and messes up our program
- this is just a long aside though

## Class Methods

- so a method is just a funtion inside of a class that is only accessible by objects of that class
- class methods always have the `self` argment, which references the object that is calling that method, so the object gets passed to the mthod when it is called so the method knows which object from that class it is working on
- however, we do not give it as an argument when we call the method, it is automatic since the method acts on the object as `object.method()
```
class Person:
    money = 0
    greeting = 'hello'
    _favourites = {
        'dog': 'ferbie',
        'food': 'sushi',
    }

    def set_money(self, num):
        self.money = num
    
    def get_favourites(self):
        return self._favourites

print(chris.money)
chris.set_money(1)
print(chris.money)
print(chris.get_favourites())
```
> 0
> 1
> {'dog': 'ferbie', 'food': [1, 2]}

- so note from the set_money() method from above, and the new get_favourites() method, we do not say `get_favourites(self)`, it is implicit, and same with the set_money() method, we only give it the num
- so since we have access to `self` within the method, we have access to each of the properties of that object, so we are encapsulating related data in a new data structure

### Method Property Decorator

#### Decorators General

- it looks like we will go over this in more detail later, but a decorator is a function that takes another function as its argument, and thus adds additional capability to that function, without modifying it
- we could simply define our own decorators by just making a function that takes a function as an argumnet, but python has a unique syntax for them, and a number of built-in decorators that work well for class methods, 
- an example is:
```
def func_name(func):
    print('in func_name(), but outside decorator()')
    def decorator():
        print('inside decorator() inside func_name()')
        print(func.__name__)
        func()
    print('in func_name() after defining decorator')
    return decorator

@func_name
def money():
    print('inside money()')
    return('money() return')

print(money())
```
> in func_name(), but outside decorator()
> inside decorator(), inside func_name()
> in func_name() after defining decorator
> money
> inside money()
> None

- so here we defined our decorator function `func_name(func)`, that takes another function as its argument as `func`
- the `@func_name` syntax above `money()` lets python know that when we call `money()`, we actually want to call the `@func_name` decorator function, with `money()` as an input instead
- really writing out:
```
@func_name
def money():
```
- is acutally equivalent to saying:
```
money = func_name(money)()
```
- so that when we call `money()` we are actually calling `func_name(money)()`
- as a result, when we do `print(money())`, we are actually saying: `print(func_name(money)())`, so its liek we have let python know we want all calls to money() to be rerouted through func_name(), and then execute that final function
- therefore if we follow the logic here, we call `func_name(money)` first, and thus the first print statement to be called is `print('in func_name(), but outside decorator()')`, then within func_name(), `decorator()` is defined, but this is not where it is called, we are just defining it, and we see this because the print statement after the decorator definition is called next where we do `print('in func_name() after defining decorator')`
- so now we return the construced decorator function which now looks like:
```
def decorator():
    print('inside decorator() inside func_name()')
    print(money.__name__)
    money()
```
- and so after this, `print(func_name(money)())` has resolved to `print(decorator())`, and decorator is now executed after it is returned, 
- **BELOW IS MY ORIGINAL MISUNDERSTANDING OF THE LOGIC, BEFORE I REALIZED `money()` RESOLVES TO  `func_name(money)()` INSTEAD OF JUST  `func_name(money)` (WITHOUT THE EXTRA CALL AT THE END), KEEPING IT IN TO SHOW THE LEARNING PROCESS:**
    - and this is where my understanding falters a bit, i do not see where decorator is called in this process, since it is just returned
    - for example, if we did:
    ```
    def func(f):
        print('func')
        def func_func():
            print('func_func')
        f()
        return func_func

    def test():
        print('test')

    test = func(test)
    ```
    > func
    > test
    - then the inner function never gets called and func_func is never printed
    - clearly there is something behind the scnese with the actual decorator syntax that does something more 
    ---
    - **COMING BACK TO THIS NOW, THE REASON WE DIDNT GET THE "func_func" PRINTOUT IS BECUASE WE NEVER ACTUALLY CALLED THE FINAL TEST FUNCTION**, we have to actually run `test()` after doing `test = func(test)`:
    ```
    def func(f):
        print('func')
        def func_func():
            print('func_func')
        f()
        return func_func

    def test():
        print('test')

    test = func(test)
    test()
    ```
    > func
    > test
    > func_func
    - we could also just do `test = func(test)()` as well, but that does look a bit awkward
    ---
**BACK TO THE REALM OF ENLIGHTENMENT**
- anyway we see decorator is executed and `print('inside decorator() inside func_name()')` executes, as well as `print(func.__name__)` which prints 'money', since we passed money() as func, 
- we also see money() is finally called in the `func()` line, and as a result, `print('inside money()')` finally executes
- lastly we see a printout of `None`, and we do not see a print out of 'money() return' from the `return('money() return')` in money, even though we may expect it since the orginal call we are doing is `print(money())`
- this is inline of the way of thinking that calls to money() are rerouted to calls of func_name(money)(), we see that the only time money() is actually called is within decorator() as `func()`, and thus the return string 'money() return' is never actually printed, it just gets returned to nowhere, the actual print statement we get is `None` since again, `print(money())` resolves somewhat to `print(func_name(money)())` and `func_name(money)()` returns a call to decorator as `return decorator`, and decorator itself has no return value, there `print(func_name(money)())` resolves to `print(decorator())` which resolves to `print(None)`
- we can test this simply by making decorator return a string:
```
def func_name(func):
    print('in func_name(), but outside decorator()')
    def decorator():
        print('inside decorator() inside func_name()')
        print(func.__name__)
        func()
        return 'decorator return statement'
    print('in func_name() after defining decorator')
    return decorator

@func_name
def money():
    print('inside money()')
    return('money() return')

print(money())
```
> in func_name(), but outside decorator()
> in func_name() after defining decorator
> inside decorator() inside func_name()
> money
> inside money()
> decorator return statement
- and we see the output 'None' has changed to 'decorator return statement'
---

#### Class Property Decorator 

- that was a very long aside that was for my own understanding of what is going on
- but the pont was, we have some built in decorators for classes that are nice to use, one of them being the `@property` decorator, that makes a get or set function accessible and usable like a regular property
```
class Person:
    money = 0
    greeting = 'hello'
    _favourites = {
        'dog': 'ferbie',
        'food': 'sushi',
    }

    def set_money(self, num):
        self.money = num
    
    def get_favourites(self):
        return self._favourites

    @property
    def get_money(self):
        return self.money

print(chris.get_money)
print(chris.get_money())
```
> 0 
> TypeError: 'int' object is not callable

- so we see normally for a get method, since it is a method, we need to call it like a normal method with the `chris.get_money()` syntax, but since we are using the property decorator, the decorator function extracts the output and lets us access it like a regular property, so `print(chris.get_money)` outputs '0'
- we also see trying to call this like a regular method now result in error, where `print(chris.get_money())` outputs 'TypeError: 'int' object is not callable', since this equates to us doing ``print(0())`, and clearly '0' is not a function
- where this becomes very useful is if we had some sort of attribute, like `money`, and it was accessed publically in our code, so we were doing `print(chris.money)`, but then we wanted to change it to have a private behaviour where we access it by get methods only, we dont have to change every instance of access `money` within our code
- normally we would have to find every instance of `print(chris.money)` and change it to `print(chris.get_money())`, but now instead we can simply use `@property` to do:
```
class Person:
    _money = 0

    @property
    def money(self):

print(chris.money)
```
> 0
- so we added a `_` to the name of the money property, and just gave the getter method the name of `money(self)`, so that with the `@property` decorator, all of the `print(chris.money)` statement in our code still work!

#### Property Setter Decorator

- this is especially useful with the setter decorators to, which are in the form `@money.setter`, or `@<property_name>.setter` in general, and allow for the setting methods to be called as if we were directly accessing the property as well:
```
class Person:
    _money = 0

    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, num):
        self._money = num

print(chris.money)
chris.money = 100
print(chris.money)
```
> 0 
> 1
- so now we can just call the setter method with `chris.money = 100`, and again, we dont have to change all our code if we were already calling the public variable directly, and it is also much more readable and intuitive
- and since the getter and setter functiona re called, we could add all the logic or type checks we wanted 

## Class CleanUp

- so now that we have gone over a bit how classes work, we are going to make a proper example class
- and so he actually just made like a template to use for the nest lesson, didnt really go over anything:
```
class Animal:
    fur = 'white'

    def speak(self):
        print ("bork")

    def eat(self):
        pass

    def chase(self):
        pass

ferbie = Animal()
ferbie.speak()
```
- he mentions going over extending classes and inheritence and stuff but this seems kinda whack without even first going over `__init__` to show how to make actual unique objects and stuff

## Class Inheritance

- we can extend classes to let subclasses access the same methods as the parent class, and we define a new class as an extension of another as `class NewClass(OldClass)`
- for example, we could do:
```
class Tiger(Animal):
    pass

tony = Tiger()

tony.speak()
print(tony.fur)
tony.fur = 'orange'
print(tony.fur)
```
> bork
> white
> orange

- so we defined the new class Tiger as an extension of Animal, and even though all we did was `pass` in the class definition, the `tony` object still has access to the Animal properties and methods liek `speak()` and `fur`
- so we can also give new methods or properties that are unique to the extension, and we can also overwrite the methods of the original class if we want a different behaviour for `speak()` for example
```
class Tiger(Animal):
    fur = 'orange + black'
    def speak(self):
        print("THEY'RE GREAT")

tony = Tiger()
tony.speak()
print(tony.fur)
```
> THEY'RE GREAT
> orange + black

- so now speak does somethign new that is unique to the tiger class, so this is nice if we have a bunch of classes that have some similiar behaviour, but also need to have some unique methods as well 
- creating a parent class as a sort of blueprint for other classes is called an 'interface', and they can be very useful 
- we also see we can create extensions of extensions, and they will get all the methods from the root class as well as the direct parent:
```
class Animal:
    fur = 'white'
    def speak(self):
        print ("bork")
    def eat(self):
        print('chomp chomp')
    def chase(self):
        pass

class Tiger(Animal):
    fur = 'orange + black'
    def speak(self):
        print("THEY'RE GREAT")

class Cat(Tiger):
    fur = 'black'

sylvester = Cat()
print(sylvester.fur)
sylvester.speak()
sylvester.eat()
```
> black
> THEY'RE GREAT
> chomp chomp
- so here is a good exmaple, as we have the Tger extenson of Animal, and I made the Cat extension of Tiger, and we see that Animal has a `eat()` method, and `Cat()` is able to call that successfully even though it is an extension of Tiger, and not directly an extension of Animal
- django web framework apparently makes heavy use of classes, so that will be good practice

## Class Interfaces

- class interface is basically a blueprint for a class, so in this case, the Animal class we made could be an interface 
- **Howver, we typically see in interfaces that the methods they implement simply `pass`**, or sometimes have something like `raise NotImplementedError`, where the `raise` keyword is like 'throw' keyword in JS, it simply raises an error to the user
- so our Animal interface might be something like:
```
class Animal:
    fur = 'white'

    def speak(self):
        pass

    def eat(self):
        pass

    def chase(self):
        raise NotImplementedError
```
- so our methods do not do anything yet, but we have a blueprint for a specific data structure, and if we wish to implement that data structure we can create an extended class of it, see what methods and stuff are available, and then implement those methods by overwriting the inherited ones so they make sense for our extended class
- so we could create the Tiger extension again:
```
class Tiger(Animal):
    pass

tony = Tiger()
tony.chase()
```
> NotImplementedError

- and we just get the error we raised, and this lets us know we need to implement it, so we could just overwrite the method in the Tiger class
- and so again, interfaces are meant as blueprints to tell us that we need to implement specific methods to use the class

## The Super() Method

- the super() method in python gets the direct parent class that ours is extended from, and we can then call methods from the parent class, even if we have overwritten them in the extended class
- for example:
```
class Animal:
    fur = 'white'
    def speak(self):
        pass
    def eat(self):
        raise NotImplementedError
    
    def chase(self, animal='gazelle'):
        print (f"I am chasing a {animal}")

class Tiger(Animal):
    def chase(self, animal='gazelle'):
        super().chase(animal)
        print (f"i like {animal}")

tony = Tiger()
tony.chase()
```
> I am chasing a gazelle
> i like gazelle

- so here, we define the chase() method for the parent Animal class, and then we also define it with the child Tiger class, except we use the line `super().chase()` to call the parent method, which prints `I am chasing a gazelle`, and then rest of te Tiger chase() method resolves and we print `i like gazelle`
- we see this is useful when we want the parent method to do some general thing for all its children, but then we want some additional unique code for different children, but dont want to rewrite all the code for each one
- we see that the arguments of the child method get passed to the parent method when calling super as well:
```
class Animal:
    def chase(self, animal='gazelle'):
        print (f"I am chasing a {animal}")

class Tiger(Animal):
    def chase(self, animal='gazelle'):
        super().chase(animal)
        print (f"i like {animal}")

tony = Tiger()
tony.chase('pigeon')
```
> I am chasing a pigeon
> i like pigeon
- so here the pigeon argument gets passed to the child method, but also makes its way all the way up to the parent as well
- we can pass arguments to the child, but them not pass them to the parent:
```
class Animal:
    def chase(self, animal='gazelle'):
        print (f"I am chasing a {animal}")

class Tiger(Animal):
    def chase(self, animal='gazelle'):
        super().chase()
        print (f"i like {animal}")

tony = Tiger()
tony.chase('pigeon')
```
> I am chasing a gazelle
> i like pigeon

- so the child method uses the new pigeon keyword, but the parent method uses the default gazelle
- also note, if we have an extension of an extension, we can not do `super().super().chase()` to only call the root method, we get an error `AttributeError: 'super' object has no attribute 'super'`, *however* if we do have a double extension, and each has the same chase() class, and call `super().chase()` from the ypoungest child, it will chain up to the root since when the 2nd child calls `super().chase()` then the 1st child will also call `super().chase()` which calls the root, and the leywrod gets passed through each step 

## Dunder (Double Underscore) Methods

- dunder stands for double underscore, since they are labelled by the method name surrounded by two underscores on each side, like `__init__()`
- these methods are run automatically when we do something with the class, for example, `__init__()` is run when we define a new object in that class, since it is used for 'initializing' the object
- `__init__()` is where we do things like define the values for the properties of that object:
```
class Animal():
    fur = ''

    def __init__(self, fur_color='white'):
        self.fur = fur_color

class Elephant(Tiger):
    def chase(self, animal='gazelle'):
        super().chase(animal)
        print (f"{animal}'s are cute")

earl = Elephant('grey')
print(earl.fur)
```
> grey
- so the `init` function is called automatically when the object is made, and we also see that `init` defines the necessary arguments for our class objects, here we did not have to pass the fur color in since we gave init a default value, but if we did not we see we get:
```
class Animal():
    fur = ''

    def __init__(self, fur_color):
        self.fur = fur_color

earl = Elephant()
print(earl.fur)
```
> TypeError: Animal.__init__() missing 1 required positional argument: 'fur_color'

- we get an error telling us we are missing the requirement for init on the animal class
- **also notice** that we are creating a subclass Elephant object, but we still only need to have the init on the parent Animal class, and the subclass is able to automatically use this when the object is created
- in the lecture he uses the example of using an init in the subclass, and making it ust execute `super().__init_(fur_color):`, to do the same thing, but then adding a print statement
- so it is good to see that all the principles we learned with super() and extension also apply to the dunder methods:
```
class Animal():
    fur = ''

    def __init__(self, fur_color):
        self.fur = fur_color

class Elephant(Tiger):
    def __init__(self, fur_color):
        super().__init__(fur_color)
        print ('init from the sub class elephant')

    def chase(self, animal='gazelle'):
        super().chase(animal)
        print (f"{animal}'s are cute")

earl = Elephant()
print(earl.fur)
```
> init from the sub class elephant
> grey
- so we see teh init of the subclass is called preferentially since it exists, but it just calls the super() method on the paretn init, to initialize the properties, and then we do the print statement in the sub-init
- in general, it seems we would always want to call `super()` when initializing a subclass, since if our class is to be an extension of a parent, we want it to have those attribtues, however, we could always overwrite init in our subclass without calling the parent if we did not want it to inherit all the attributes

### Multiple Inheritance 

- in python we also have something called *multiple inheritance*, where we can make a class inherit from multiple parent classes, for example `class ClassC(ClassA, ClassB):`, and this makes for some potential, what seems to be, conflicts in how python chooses what values to inherit if the classes have overlapping attribute sets
- however in python, these are all controlled by the **Method Resolution Order (MRO)**, which is liek a built in system deciding how multiple inheritence should resolve for a object inheriting from multiple classes
- we have a rather long example below"
```
class Class00:
    root = '00'
    num = 00
    message = 'inherited from Class00'
    def __init__(self, num):
        print('class 00 init')
        self.num = num
        self.root = 000

class ClassA(Class00):
    classA = True
    classB = False
    vowel = None
    a = 0
    num = None


    def __init__(self, num):
        print('class A init')
        self.a = 1
        self.vowel = True
        self.num = num

class ClassB(Class00):
    classA = False
    classB = True
    vowel = None
    b = 0
    num = None
    message = 'inherited from ClassB'


    def __init__(self, num):
        print('class B init')
        self.b = 1
        self.vowel = False
        self.num = num * 2

class ClassC(ClassA, ClassB):
    inher = 'A/B'

    def __init__(self, num):
        print('class C init')
        super().__init__(num)

class ClassD(ClassB, ClassA):
    inher = 'B/A'

    def __init__(self, num):
        print('class D init')
        super().__init__(num)


c_obj = ClassC(10)
d_obj = ClassD(10)
print("c-obj || d-obj")
print(f"{c_obj.inher} || {d_obj.inher}")
print(f"{c_obj.classA} || {d_obj.classA}")
print(f"{c_obj.classB} || {d_obj.classB}")
print(f"{c_obj.vowel} || {d_obj.vowel}")
print(f"{c_obj.message} || {d_obj.message}")
print(f"{c_obj.a} || {d_obj.a}")
print(f"{c_obj.b} || {d_obj.b}")
print(f"{c_obj.num} || {d_obj.num}")
print(f"root: {c_obj.root} || {d_obj.root}")
```
> class C init
> class A init
> class D init
> class B init
> Property: c-obj || d-obj
> inher: A/B || B/A
> classA: True || False
> classB: False || True
> vowel: True || False
> message: inherited from ClassB || inherited from ClassB
> a: 1 || 0
> b: 0 || 1
> num: 10 || 20
> root: 00 || 00

- so we have a root class `Class00`, then two subclasses `ClassA` and `ClassB`, then two further subclasses that inherit from both A and B called `ClassC` and `ClassD`
```
      00
     _||_  
    |    |
    A    B
    |\  /|
    | \/ | 
    | /\ | 
    |/  \|
    C    D
```
- the main difference between C and D here are that C's inheritance is defined as `C(A, B)`, while D's inheriance is `D(B, A)`
- we notice that there are conflicts between the attriubtes and init methods of A and B, for example, A has the property `classA = True`, while B has the property `classA = False`, and vice versa for the variable `classB`, and we see that python takes priority for the class that is defined first in the inheritance list, so for obj_c, classA = True, and fot obj_d, classA = False
- we can see this is true of the innit methods as well, teh first 4 lines of the output are various print statements from each init method
- we notice that although every class has the root class 00, we never see the Class00 init being executed, since neither A nor B init() functions call `super().__init__()`, therefore when C and D call `super().__init__()`, they only call the most recent parent, now of course we could make them also call 00 init() by adding `super().__init__()` to the A and B class, but this was just an example of where the propogation stops
- we also see that even though 00 init() is never executed, we have still inherited the properties of the 00 class, since both C and D have the property `root = 00`
- now looking at the init()'s that were called by each object, we notice that first obj_c of class C(A,B) is defined, and here we call the C level init first and then the A init, but the B init is never called even though we also inherit from B
- we see teh reverse with obj_d of class D(B,A), where D init is called, and the B init, with no A init ever getting called
- this is because of the Method Resolution Order (MRO), where the overlapping init method are prioritized by the class that is defined first in the inheritance definition, so for C, A is prioritized, and for D, B is prioritized
- we see that if we get rid of this conflict by commenting out A's init method, then the class C object will print out `class C init, class B init` even though A was defined first, since now there is no conflict and we just inherit all the methods we can, and since B has an init while A does not, we get B's verison of init
- this is a good example of the MRO at work, and shows why in python we do not have the idea of a true 'superclass', we may expect since 'A' is prioritized over 'B' in object C, that when A had no init method, C will go up the chain and use 00 init method since A inherits from 00, but this is not true since we see that B is the 'closest ancestor' taht has an init mthod, so that is now prioritized over going up the chain from A to 00
- this is also shown by the 'message' property, where the 00 has `message = 'inherited from Class00'`, and B has `message = 'inherited from ClassB'`, while A has no message property. Both obj_c and obj_d print out a 'message' of 'inherited from ClassB', since for D, the first inhertiance 'B' has that message, and for C (where A has no message) the second inheritance class 'B' is prioritized over going up the chain to 00
- but we do indeed go all the way up the chain to 00 when no other option exists! we can see this with the last printout statement of the root variable, where 00 class has the property `root = 00`, and neither A nor B have that property, so the printout of root is '00' for both obj_c and obj_d, since we no closer ancestor has that property defined, so we now go up the chain
**Lastly**, we see that this multiple inheritance does create conflicts, for example, imagine we define a new class 'E(C,D)', no distinct priority chain can be made since we have conflicting hierarchy since A > B in C, but B > A in D, and when we try to define that class, *without even making an object in it* we get the error `TypeError: Cannot create a consistent method resolution order (MRO) for bases ClassA, ClassB`

### Descriptors

- not gone over in lecture, but read up on them a bit here and they are interesting, not enough time ot make detailed notes right now:
- https://docs.python.org/3/howto/descriptor.html
- basically a property that calls a class with a dunder __get__() method, so get is called automatically every time we reference that property, and it can generate a value for us, this is nice for a dynamically changing variable liek a 'database size' that we dont want to manually update then reference, since it is updated on reference 

### Bound and Unbound Methods

- same thing:
- https://stackoverflow.com/questions/114214/class-method-differences-in-python-bound-unbound-and-static
- the idea that we can have methods that are bound to an instance of a class, and methods that are not bound, unbound, to an instance, the undound methods would not need to tale 'self' for example, and we could call them directly with `Class.method()` instead `obj.method()`

## Errors and Exceptions

- back to actual video content
- in python we can control our error flow with `try:` and `except:` statements, which allows us to try to execute a peice of code, and instead of just quitting the program if there is an error, we can control what happens with taht error and take an alternative path as well
    - so in that way it is like an if/else statement
- we can use the following simple example of trying to divde by 0:
```
try:
    print('trying 1/0')
    total = 1/0
    print('will not print')
except Exception as err:
    print('there was an error:')
    print(err)
else:
    print('nothing went wrong :)')

print('out of try/except block')
```
> trying 1/0
> there was an error:
> division by zero
> out of try/except block
- so here we are telling python to try the piece of code, and we see the 'trying 1/0' statement is printed, then we run into an error durign that calculation, so the 'will not print' line does not print, then we handle that error with `except Exception as err:`, where 'Exception' is the keyword for the error that happened, so we are bringing the exception into the block of code under the reference 'err'
- in the except block we print our staemetns and we see when we print the error, only a small description of the error prints: 'division by zero', instead of a big long error statement
- since there was an error, else: does not execute, and we then continue with our program and 'out of try/except block' prints
- if there is no error we see:
```
try:
    print('trying 1/1 :')
    total = 1/1
    print('will print')
except Exception as err:
    print('there was an error:')
    print(err)
else:
    print('nothing went wrong :)')

print('out of try/except block')
```
> trying 1/1 :
> will print
> nothing went wrong :)
> out of try/except block
- and everything works
- we can also try a more realistic example where we are asking for user input and checking to make sure it is of the right type:
```
num1 = input('Please enter a number to double: ').lower().strip()
try:
    num1 = float(num1)
    num1 *= 2
except Exception as err:
    print(f'Exception found: {err}')
    print(f'{num1} is not a valid number')
else:
    print(num1)
print('program done')
```
- and if we enter 'ten' as our number, we see we get `Exception found: could not convert string to float: 'ten'` and `ten is not a valid number`
- so we have been doign this for a lot of our user inputs for the pokedex project for example, and it is good to use these types of try blocks so that we can control the error flow when the users inevitably make mistakes
- we can have a bit more realistic one:
```
while True:
    num2 = input('Please enter a number to double: ').lower().strip()
    try:
        num2 = float(num2)
        num2 *= 2
    except Exception as err:
        print(f'Exception found: {err}')
        print(f'{num2} is not a valid number')
        continue
    else:
        print(num2)
        break
print('program done')
```
- so now we have an actual input system that cathces the error, and lets us continue to to ask for more inputs

## Catching Exceptions

- we can catch our exceptions using the method I was using above where we catch our exceptions with `except Exception as err:`, and we can then print our error statement like i did, but we can do some additional things to make the workflow more intuitive, and to catch and do different things given a specific error type:
```
while True:
    num2 = input('Please enter a number to double: ').lower().strip()
    try:
        num2 = float(num2)
        num2 *= 2
    except ValueError:
        print(f'{num2} is not a valid number')
    except Exception as err:
        print(f'an exception of type {type(err)} was raised')
        continue
    else:
        print(num2)
        break
print('program done')
```
- and here, now if we enter 'ten', the error that gets raised will be a 'ValueError', so it will be caught by `except ValueError:` and that except block will run
- if it is an error of a different type, the unspecified exception block will run and we will get a rpintout of the type of err it is at least with the `{type(err)}` part of the string, and once we see that we can possibly add another more specific except block to have a unique message for that
- we can have an example liek this where we try to divide the input by a second input:
```
while True:
    num2 = input('Please enter a dividend number: ').lower().strip()
    num3 = input('Please enter a divisor number: ').lower().strip()
    try:
        num2 = float(num2)
        num3 = float(num3)
        result = num2 / num3
    except ValueError:
        print(f'Either the dividend or divisor were not a valid number')
    except Exception as err:
        print(f'an exception of type {type(err)} was raised')
        continue
    else:
        print(result)
        break
print('program done') 
```
- and we see if we enter 2 valid numbers, everything works correctly and we get the result printed out, and if we enter a string, we get the ValueError exception and get the corresponding printout
- however, if we enter 0 as the divisor number, we get the general exception block, and we see the printout `an exception of type <class 'ZeroDivisionError'> was raised`
- so now we can add another except statement for an exception of 'ZeroDivisionError':
```
while True:
    num2 = input('Please enter a dividend number: ').lower().strip()
    num3 = input('Please enter a divisor number: ').lower().strip()
    try:
        num2 = float(num2)
        num3 = float(num3)
        result = num2 / num3
    except ValueError:
        print(f'Either the dividend or divisor were not a valid number')
    except ZeroDivisionError:
        print(f'Your divisor can not be 0')
    except Exception as err:
        print(f'an exception of type {type(err)} was raised')
        continue
    else:
        print(result)
        break
print('program done')  
```
- so now if we enter a string, we get the nice ValueError message that tells the user the specific issue, but now if we enter 0 as our divisor, we get the specific ZeroDivisionError that tells the user that the divisor cannot be 0, which is really nice since we are giving the user more information on what the problem is and how to use the program correctly, and more importantly for us, we can get more info on what is going wrong if our program is not working correctly
- this is extremely important for programs that are supposed to constantly run, like something on a server, we want it to keep taking more requests if something goes wrong with one of them, and not having to go to our computer and restart the program

## Python Decorators

- so we have used these before with the `@property` in the class methods that makes the method act liek a property that we can call with `obj.method` instead of `obj.method()`
- i wrote some very long notes on decorators from my searching on trying to figure out exactly how they worked in that section
- in general what happens is the decorator function is run with the defined function underneath it as an input 
- here are my notes on that:

---
#### Decorators General

- it looks like we will go over this in more detail later, but a decorator is a function that takes another function as its argument, and thus adds additional capability to that function, without modifying it
- we could simply define our own decorators by just making a function that takes a function as an argumnet, but python has a unique syntax for them, and a number of built-in decorators that work well for class methods, 
- an example is:
```
def func_name(func):
    print('in func_name(), but outside decorator()')
    def decorator():
        print('inside decorator() inside func_name()')
        print(func.__name__)
        func()
    print('in func_name() after defining decorator')
    return decorator

@func_name
def money():
    print('inside money()')
    return('money() return')

print(money())
```
> in func_name(), but outside decorator()
> inside decorator(), inside func_name()
> in func_name() after defining decorator
> money
> inside money()
> None

- so here we defined our decorator function `func_name(func)`, that takes another function as its argument as `func`
- the `@func_name` syntax above `money()` lets python know that when we call `money()`, we actually want to call the `@func_name` decorator function, with `money()` as an input instead
- really writing out:
```
@func_name
def money():
```
- is acutally equivalent to saying:
```
money = func_name(money)()
```
- so that when we call `money()` we are actually calling `func_name(money)()`
- as a result, when we do `print(money())`, we are actually saying: `print(func_name(money)())`, so its liek we have let python know we want all calls to money() to be rerouted through func_name(), and then execute that final function
- therefore if we follow the logic here, we call `func_name(money)` first, and thus the first print statement to be called is `print('in func_name(), but outside decorator()')`, then within func_name(), `decorator()` is defined, but this is not where it is called, we are just defining it, and we see this because the print statement after the decorator definition is called next where we do `print('in func_name() after defining decorator')`
- so now we return the construced decorator function which now looks like:
```
def decorator():
    print('inside decorator() inside func_name()')
    print(money.__name__)
    money()
```
- and so after this, `print(func_name(money)())` has resolved to `print(decorator())`, and decorator is now executed after it is returned, 
- **BELOW IS MY ORIGINAL MISUNDERSTANDING OF THE LOGIC, BEFORE I REALIZED `money()` RESOLVES TO  `func_name(money)()` INSTEAD OF JUST  `func_name(money)` (WITHOUT THE EXTRA CALL AT THE END), KEEPING IT IN TO SHOW THE LEARNING PROCESS:**
    - and this is where my understanding falters a bit, i do not see where decorator is called in this process, since it is just returned
    - for example, if we did:
    ```
    def func(f):
        print('func')
        def func_func():
            print('func_func')
        f()
        return func_func

    def test():
        print('test')

    test = func(test)
    ```
    > func
    > test
    - then the inner function never gets called and func_func is never printed
    - clearly there is something behind the scnese with the actual decorator syntax that does something more 
    ---
    - **COMING BACK TO THIS NOW, THE REASON WE DIDNT GET THE "func_func" PRINTOUT IS BECUASE WE NEVER ACTUALLY CALLED THE FINAL TEST FUNCTION**, we have to actually run `test()` after doing `test = func(test)`:
    ```
    def func(f):
        print('func')
        def func_func():
            print('func_func')
        f()
        return func_func

    def test():
        print('test')

    test = func(test)
    test()
    ```
    > func
    > test
    > func_func
    - we could also just do `test = func(test)()` as well, but that does look a bit awkward
    ---
**BACK TO THE REALM OF ENLIGHTENMENT**
- anyway we see decorator is executed and `print('inside decorator() inside func_name()')` executes, as well as `print(func.__name__)` which prints 'money', since we passed money() as func, 
- we also see money() is finally called in the `func()` line, and as a result, `print('inside money()')` finally executes
- lastly we see a printout of `None`, and we do not see a print out of 'money() return' from the `return('money() return')` in money, even though we may expect it since the orginal call we are doing is `print(money())`
- this is inline of the way of thinking that calls to money() are rerouted to calls of func_name(money)(), we see that the only time money() is actually called is within decorator() as `func()`, and thus the return string 'money() return' is never actually printed, it just gets returned to nowhere, the actual print statement we get is `None` since again, `print(money())` resolves somewhat to `print(func_name(money)())` and `func_name(money)()` returns a call to decorator as `return decorator`, and decorator itself has no return value, there `print(func_name(money)())` resolves to `print(decorator())` which resolves to `print(None)`
- we can test this simply by making decorator return a string:
```
def func_name(func):
    print('in func_name(), but outside decorator()')
    def decorator():
        print('inside decorator() inside func_name()')
        print(func.__name__)
        func()
        return 'decorator return statement'
    print('in func_name() after defining decorator')
    return decorator

@func_name
def money():
    print('inside money()')
    return('money() return')

print(money())
```
> in func_name(), but outside decorator()
> in func_name() after defining decorator
> inside decorator() inside func_name()
> money
> inside money()
> decorator return statement
- and we see the output 'None' has changed to 'decorator return statement'
---
- now we are back in real modern time land
- so i will go through the lectures explaiation of these as well
- we see the decorator will take another function as its argument
- as stated above in the revelations, we can model a decorator without using the special syntax as:
```
def func(f):
    print('func')
    def func_func():
        print('func_func')
    f()
    return func_func

def test():
    print('test')
    return('return statement inside test')

print(func(test)())
```
> func
> test
> func_func
> None

- so we see we have a function that we made `test()`, but instead of calling that function normally, we are going to call it by passing it into func, so that it is now `func(test)`, and func is going to *decorate* that function by adding some additional things, building a new function in the process: `func_func()`, and then `func(test)` returns that function (`func_func()`) as the new function, which is then executed since `func(test)()` resolves to `func_func()`
- **importantly** since we resolve `print(func(test)())` to `print(func_func())`, the final printout is `None` since `func_func()` does nto return anything, and we see the return statement from `test()`: `return('return statement inside test')` never gets printed, even though that is the function we are trying to execute by passing it to `func()`
- we can do this in the special python syntax, where we define a function that we want to always be run with a decorator by preceeding it with `@decorator_name` which looks quite a bit nicer, as:
```
def func1(f):
    print('func1')
    def func_func1():
        print('func_func1')
    f()
    return func_func1

@func1
def test1():
    print('test1')
    return('return statement inside test1')

print(test1())
```
> func
> test
> func_func
> None

- so here we get the exact same behaviour, with a bit of a cleaner printout, but also this is a bit less intuitive since we would expect the return statement of `test1()` to get printed out by the `print(test1())`, but since this is actually being evaluated as `print(func(test)())`, as shown above, it does not
- also with this syntax it seems we have no choice but to execute this with the decorator, but in the other way we would execute it with or without them
- usually though we are just using builtin decorators from apkcages and not creating our own though
- they are a nice way of adding functionality to a function without changing the original thing

## Python Generators

- we have learned generators in the other python courses, and they are not terribly complicated, but I think the use case is a bit hard to understand for me, alot of examples I always feel liek I am not really grasping why the 'generator' version of a solution is better, but in general (generatoral???) it has to do with memory managment
- if we are working in very large data sets, it can be very taxing on memory to store a large number of values in a giant list for example, and so we want this list to be short lived, and we do not want to actually have to build the whole thing and store it if we can
- for example, the function:
```
def first_n(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(first_n(1000000))
print(sum_of_first_n)
```
- constructs a list of the numbers 0 to n, and stores it in memory, returning the list to be summed by the sum function
- now we can also write this in the generator format:
```
def gen_first_n(n):
    num = 0
    while num < n: 
        yield num
        num += 1

sum_of_first_n_gen = sum(gen_first_n(1000000))
print(sum_of_first_n_gen)
```
- we can see that in this generator function, we never actually build and commit a list to memory, the only thing we have in memory is the current number `num`, and in the while loop, instead of *returning* a the number, or the finished list like in the function verison, we simply *yield* `num`, 
- `yield` is a special keyword, like `return`, but for a genertor, which means we yield the number to the object calling the generator, in this case the `sum()` function, but then continue with our number generation instead of just stopping completely (like what we see when a function reaches return)
- this way only 1 number is needed to be kept in memory at a time, and `sum()` is able to consume the number to sum as they are generated
- I was having a bit of a issue with figuring out how this works sunce it seems liek sum needs a whole list to add up, and are we actually jus building the list to add within sum instead?, but if we think about it, sum can only add two numbers at a time, it would iterate through a list, adding its arguments one after another, in this case the values of the iterable are just dynamically generated by the generator for sumto consume 1 at a time, instead of the entire list being made, saved, and then given to sum
- we also see some maybe unexpected behaviour from what we are used to with regular functions when we rint a generator cell like:
```
print(gen_first_n(10))
print(list(gen_first_n(10)))
```
> <generator object gen_first_n at 0x7f7c65ae4350>
> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
- for this we see printing the call to the generator does return the numbers the generator yields, instead we just get the generator object
- if we want to have each number, we can cast the generator to a list, and this is still more efficient since even though we are saving the whole thing to a list, we are not worried about the other numbers when we are constructing that list within the generator, it constructs it one number at a time
- we also see that if we want to use the generator again, we have to make another call to that generator and ti will generate everything again, since that is whoel point it is temporary, so we use more computation at times, for saved memory 

## Using pipenv for a Virtual Environment

- we previously learned of using `venv` to create virtual environments in python, but there are multiple ways to create virtual environments, and a very useful one is with `pipenv`
- pipenv gives us an easy way to make virtual enviroments with different packages and version, and even with different python versions,
- if we just enter `pipen` into the command line it gives us a bunch of things we can do with it
- for the most part it seems liek the other venv we were using, but maybe more nice syntax and easier commands
- we can easly make a new pipenv virtual environment with `pip install`, and to activate the environment we can just do `pipenv shell`
- to exit the pipenv we can simply do 'ctrl+d', which is nice, and just `pipenv shell` again to get back in 
- not sure if this is intended, but for me pipenv shell just activates the already existing `.venv` envrionment it seems
- to remove out environment we can just do `pipenv -rm` and it deletes it easily
- we can also do `pipenv install --python 3.7` and it will make a new pipenv environment for us using python 3.7 instead of my ucrrent python 3.10
- okay so did the above, and when when i do `python -V` it still shows python 3.10, and this is because it also shows we are in `.venv` as well, I imagien they do not play nice together when they are int he same folder because they are trying to do similar things  

## Our Project

- for our final project we want to create a bancking app using classes
- it should be:
    - class based
    - methods for withdrawl and deposit
    - after every methods/withdrawl, we want to write the transaction to a python file
    - we want to have a program that over and over again asks a user if they want to withdrawl or deposit, and writing to a log python file after every one
    - we are going to be using while True
    - using input
    - using classes
    - using methods
    - using properties
    - using the open() syntax for files

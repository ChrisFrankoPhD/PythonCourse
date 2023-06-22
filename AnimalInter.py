class Animal:
    fur = ''

    def __init__(self, fur_color):
        self.fur = fur_color

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

# tony = Tiger()
# tony.chase('pigeon')

class Elephant(Tiger):
    def __init__(self, fur_color):
        super().__init__(fur_color)
        print ('init from the sub class elephant')

    def chase(self, animal='gazelle'):
        super().chase(animal)
        print (f"{animal}'s are cute")

earl = Elephant('grey')
earl.chase('mouse')
print(earl.fur)

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

# class ClassE(ClassC, ClassD):
#     pass

c_obj = ClassC(10)
d_obj = ClassD(10)
print("Property: c-obj || d-obj")
print(f"inher: {c_obj.inher} || {d_obj.inher}")
print(f"classA: {c_obj.classA} || {d_obj.classA}")
print(f"classB: {c_obj.classB} || {d_obj.classB}")
print(f"vowel: {c_obj.vowel} || {d_obj.vowel}")
print(f"message: {c_obj.message} || {d_obj.message}")
print(f"a: {c_obj.a} || {d_obj.a}")
print(f"b: {c_obj.b} || {d_obj.b}")
print(f"num: {c_obj.num} || {d_obj.num}")
print(f"root: {c_obj.root} || {d_obj.root}")
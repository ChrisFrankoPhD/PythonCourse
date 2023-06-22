class Animal:
    fur = 'white'

    def speak(self):
        print ("bork")

    def eat(self):
        print('chomp chomp')

    def chase(self, animal='gazelle'):
        print (f"I am chasing a {animal}")

ferbie = Animal()
ferbie.speak()

class Tiger(Animal):

    fur = 'orange + black'

    def speak(self):
        print("THEY'RE GREAT")
    
    def chase(self, animal='gazelle'):
        super().chase(animal)
        print (f"i like {animal}")
    

tony = Tiger()
tony.speak()
print(tony.fur)

tony.chase()

class Cat(Tiger):
    fur = 'black'

sylvester = Cat()
print(sylvester.fur)
sylvester.speak()
sylvester.eat()



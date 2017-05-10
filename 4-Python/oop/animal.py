'''Assignment: Animal - Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.

Animal Class - Create a class called Animal with the following attributes: name, and health. 
Give the Animal the following three methods: walk, run, and displayHealth. 
Give a new Animal 100 health when it gets created. 
When the walk() method is invoked, have the health decrease by 1. 
When the run() method is invoked, have the health decrease by 5. 
When the displayHealth() method is invoked, display on screen the name of the Animal and the health.
Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.

Dog Class - Create a class called Dog that inherits everything that the Animal does, 
except the Dog class should have a default health of 150 and a new method called pet(), which increases the health by 5. 
Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().

Dragon Class - Finally, create a class called Dragon that also inherits everything from Animal. 
The Dragon class should have the default health be 170 and a new method called fly(), which decreased the health by 10. 
Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth(). 
When the Dragon's displayHealth() function is called, it should say 'this is a dragon!' before it displays the default information. 
You can achieve this by calling the parent's displayHealth() function.

Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and it's displayHealth() is not saying 'this is a dragon!'. 
Also confirm that your Dog class can not fly().
'''
class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "Name: {} and Health: {}".format(self.name, self.health)
animal1 = Animal("MAURICIO").walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
    def pet(self):
        self.health += 5
        return self
dog1 = Dog("POMERANIAN").walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print "This is a dragon!"
        super(Dragon, self).displayHealth()
dragon1 = Dragon("MALEFICENT").walk().walk().walk().run().run().fly().fly().displayHealth()

animal2 = Animal("OTHER").walk().run().displayHealth()
#animal2.pet()
#animal2.fly()
#dog1.fly()
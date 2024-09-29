class Dog:
    #class attribute
    attr1 = "mammal"

    #instance attributr
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

#Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

#Accessing class attribute
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is a {}".format(Tommy.__class__.attr1))

#Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

Rodger.speak()
Tommy.speak()

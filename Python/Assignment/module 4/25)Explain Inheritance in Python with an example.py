"""
# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

=>  one class derived property of another class its called inheritance

"""

# inhertance Example : class child have property of parant

class parant:
    def bike(self):
        print("I have Bike")

class child(parant):
    def cycle(self):
        print("I have My Own Cycle")

"""
constructor : A constructor is a unique function that gets called automatically when an object is created of a class


__init__() : This is Similar Like Constructor

which is invoke automatically when we create object of class

using of __init__() we don't need to call it explicity

"""
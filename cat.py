import numpy as np
"""
Step1: Install pip3 -> sudo apt-get install python3-pip

Step2: Install numpy module -> pip3 install numpy
"""

from animal import Animal
class Cat(Animal):
    
    def bark(self):
        print("I can meow! Meow meow!!")

print(np.sqrt(4))
# Create object of the Dog class
cat1 = Cat()

# Calling members of the base class
cat1.eat()
cat1.sleep()

# Calling member of the derived class
cat2 = Cat()
cat2.eat()
cat2.sleep()

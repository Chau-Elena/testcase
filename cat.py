from animal import Animal
class Cat(Animal):
    
    def bark(self):
        print("I can meow! Meow meow!!")

# Create object of the Dog class
cat1 = Cat()

# Calling members of the base class
cat1.eat()
cat1.sleep()

# Calling member of the derived class
cat1.meow();

cat2 = Cat()
cat2.eat()
cat2.sleep()
cat2.meow()
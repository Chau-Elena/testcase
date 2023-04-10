#make a class called fox
class Fox:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def say(self):
        print("hi my name is " + self.name + " I am " + self.age + " years old and I am " + self.color)
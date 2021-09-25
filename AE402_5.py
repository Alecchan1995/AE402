class Person():
    def __init__(self,name,age,wight,height):
        self.name = name
        self.age = age
        self.wight=wight
        self.height=height
    def BMI(self):
        result = self.wight/self.height**2
        return result
name = input("what is your name")
age = int(input('how old are you'))
wight = int(input("Wigth?"))
height = int(input('Height'))
a = Person(name,age,wight,height)
print("Your name is",a.name)
print("Your age is =",a.age)
print("Your BMI is =",a.BMI())

    
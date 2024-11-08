class mammal:
    def walk(self):
        print("walk")

class Dog(mammal):
    def bark(self):
        print("bark")

class Cat(mammal):
    def mewoo(self):
        print("Mewoooo")

dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.mewoo()
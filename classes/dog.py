class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = 'chiuaua'  # by default

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} is now rolling over")

# Instantiating class
my_dog = Dog('Willy', 8)
print(f"My dog is called: {my_dog.name}.")
my_dog.sit()
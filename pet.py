class Pet:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age  
        self.hunger = 0  
        self.energy = 10  
        self.happiness = 5 
        self.tricks = [] 

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} enjoyed a delicious meal! Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a rejuvenating nap! Energy: {self.energy}")

    def play(self):
        if self.energy >= 2: 
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} had a blast playing! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play! Energy: {self.energy}")

    def get_status(self):
        print(f"Status of {self.name}:")
        print(f"  Age: {self.age} years")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned the trick '{trick}'! Happiness: {self.happiness}")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} has mastered the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def celebrate_birthday(self):
        self.age += 1
        self.happiness = min(10, self.happiness + 2) 
        print(f"It's {self.name}'s birthday! Happy {self.age}th birthday! Happiness: {self.happiness}")

# Example usage
my_pet = Pet("REX", age=2)
my_pet.get_status()
my_pet.eat()
my_pet.sleep()
my_pet.play()
my_pet.train("High Five")
my_pet.show_tricks()
my_pet.celebrate_birthday()
my_pet.get_status()
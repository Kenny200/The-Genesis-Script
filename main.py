class Human:
    def __init__(self, name, ribs = 24):
        self.name = name

    def speak(self):
        print(f"Hello, my name is {self.name}.")

class Adam(Human):
    def __init__(self):
        super().__init__("Adam", 24)  # Calls the parent class constructor

    def origin(self):
        print("I am the first human.")

    def remove_rib(self):
        if self.ribs > 0:
            self.ribs -= 1
            print(f"{self.name} now has {self.ribs} ribs left.")
            return "rib"   # symbolizes the rib that will be used to create Eve
        else:
            print(f"{self.name} has no ribs left to remove.")

class Eve(Human):
    def __init__(self):
        super().__init__("Eve", 0)
        print(f"Eve was created from {self.created_from}'s rib.")

    def origin(self):
        print(f"From {self.created_from}'s rib I was made.")

person = Adam()
print(person)  # Outputs: 24
person.speak()      # Outputs: Hello, my name is Adam

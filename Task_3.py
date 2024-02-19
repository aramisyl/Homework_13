from abc import ABC

class Animal(ABC):
    def __init__(self, name):
        self.name = name

class FlyingAnimal(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wigspan = wingspan
    def fly(self):
        print(f"{self.name} is flying with wingspan {self.wingspan}")


class Bird(FlyingAnimal):
    def __init__(self, name, wingspan):
        super().__init__(name, wingspan)

    def fly(self):
        print(f"Bird {self.name} is flying with wingspan {self.wingspan}")


class Bat(FlyingAnimal):
    def __init__(self, name, wingspan):
        super().__init__(name, wingspan)

    def fly(self):
        print(f"Bat {self.name} is flying with wingspan {self.wingspan}")

class Penguin(Animal):
    def __init__(self, name):
        super().__init__(self, name)
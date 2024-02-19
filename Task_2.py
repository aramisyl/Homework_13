from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, base_salary):
        super().__init__('manager')
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus = 0
        bonus = self.base_salary * 0.2
        return self.base_salary + bonus


class Developer(Employee):
    def __init__(self, base_salary):
        super().__init__('developer')
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus = 0
        bonus = self.base_salary * 0.1
        return self.base_salary + bonus


class Tester(Employee):
    def __init__(self, base_salary):
        super().__init__('tester')
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus = 0
        bonus = self.base_salary * 0.3
        return self.base_salary + bonus

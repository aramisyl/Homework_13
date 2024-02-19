from abc import ABC, abstractmethod


class Order:
    def __init__(self, items, total, storage):
        self.items = items
        self.total = total
        self.storage = storage

    def process(self):
        self.storage.connect()
        self.storage.save_data()


class Storage(ABC):
    @abstractmethod
    def save_data(self):
        pass


class Database(Storage):
    def connect(self):
        return "Connect to database."

    def save_data(self):
        return "Save to database."


class File(Storage):
    def save_data(self):
        return "Save to file."

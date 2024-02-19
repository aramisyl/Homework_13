from abc import ABC, abstractmethod


class Phone(ABC):
    def __init__(self, model, number):
        self.model = model
        self.number = number


class CallPhone(Phone):
    def __init__(self, model, number, other_number):
        super().__init__(model, number)
        self.other_number = other_number

    def call(self, other_number):
        print(f"Calling {other_number} from {self.number}")


class MessagePhone(Phone):
    def __init__(self, model, number, other_number, text):
        super().__init__(model, number)
        self.other_number = other_number
        self.text = text

    def send_message(self, other_number, text):
        print(f"Sending '{text}' to {other_number} from {self.number}")


class PhotoPhone(Phone):
    def __init__(self, model, number):
        super().__init__(model, number)

    def take_photo(self):
        print(f"Taking a photo with {self.model}")


class GamePhone(Phone):
    def __init__(self, model, number, game):
        super().__init__(model, number)
        self.game = game

    def play_game(self, game):
        print(f"Playing {game} on {self.model}")


class BasicPhone(CallPhone, MessagePhone):
    def call(self, other_number):
        print(f"Calling {other_number} from {self.number} old phone")

    def send_message(self, other_number, text):
        print(f"Sending '{text}' to {other_number} from {self.number} old phone")


class CameraPhone(CallPhone, MessagePhone, PhotoPhone):
    def call(self, other_number):
        print(f"Calling {other_number} from {self.number} camera phone")

    def send_message(self, other_number, text):
        print(f"Sending '{text}' to {other_number} from {self.number} camera phone")

    def take_photo(self):
        print(f"Taking a photo with {self.model} camera phone")


class SmartPhone(CallPhone, MessagePhone, PhotoPhone, GamePhone):
    def call(self, other_number):
        print(f"Calling {other_number} from {self.number} smart phone")

    def send_message(self, other_number, text):
        print(f"Sending '{text}' to {other_number} from {self.number} smart phone")

    def take_photo(self):
        print(f"Taking a photo with {self.model} smart phone")

    def play_game(self, game):
        print(f"Playing {game} on {self.model} smart phone")

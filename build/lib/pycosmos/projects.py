import requests

class Projects:
    def __init__(self, name):
        self._name = name

    def say(self):
        print(f'Hi! I am {self._name}')
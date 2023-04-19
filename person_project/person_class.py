"""
    Name: person_class.py
    Author: Samantha Roberts
"""


class Person:

    def __init__(self, name, age, major):
        self._name = name
        self._age = age
        self._major = major

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_major(self):
        return self._major
    
    def set_major(self, major):
        self._major = major
    
    def greet(self):

        print(f"Hello! My name is {self._name} and I am {self._age} years old\
              \nMy major is {self._major}.")

    

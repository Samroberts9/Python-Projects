"""
    Name: person_import
    Author: Samantha Roberts
"""

import person_class

def main():

    Tony = person_class.Person("Tony", "28", "Computer Science")

    Tony.greet()

    Tony.set_major("Human relations")

    Tony.greet()

if __name__ == "__main__":
    main()

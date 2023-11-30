#!/usr/bin/env python3

class Dog:
    pass
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name, breed):
        self._name = None
        self._breed = None
        self._set_name(name)
        self._set_breed(breed)

    def _get_name(self):
        return self._name

    def _set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    def _get_breed(self):
        return self._breed

    def _set_breed(self, value):
        if value in self.APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")

    name = property(_get_name, _set_name)
    breed = property(_get_breed, _set_breed)

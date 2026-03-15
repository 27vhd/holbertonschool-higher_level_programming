#!/usr/bin/python3
"""Module for serializing and deserializing custom objects using pickle."""
import pickle


class CustomObject:
    """A custom class that supports pickle serialization and deserialization."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject with name, age and is_student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance and save it to a file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of CustomObject from a file."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None

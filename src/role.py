from abc import ABC, abstractmethod

class Role(ABC):

    def __init__(self, name, family):

        self.name = name
        self.family = family

    def __repr__(self):
        return f"{self.name} {self.family}"
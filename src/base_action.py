from abc import ABC, abstractmethod


class Action(ABC):

    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    @classmethod
    @abstractmethod
    def products(cls, *args, **kwargs):
        pass

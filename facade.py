from __future__ import annotations
from threading import Lock

class SingletonMetaclass(type):
    """
    Thread-safe singletone metaclass
    """
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        set up metaclass for singleton pattern
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Facade(metaclass=SingletonMetaclass):

    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()

    
    def go(self):
        self.subsystem1.go()
        self.subsystem2.go()

class Subsystem1:
    def go(self):
        print("Subsystem1 works!")

class Subsystem2:
    def go(self):
        print("Subsystem2 starts!")

FACADE = Facade()

FACADE2 = Facade()

assert id(FACADE) == id(FACADE2)

FACADE.go()
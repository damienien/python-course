from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move():
        raise NotImplementedError

class Eagle(Animal):
    def move(self) -> None:
        print('Eagle is flying')
        
class Dolphin(Animal):
    def move(self)-> None:
        print('Dolphin is swimming')
        
class Dog(Animal):
    def move(self)-> None:
        print('Dog is running')

animal = Animal()
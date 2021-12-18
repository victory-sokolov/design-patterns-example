# Abstract factory
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class DogFactory:

    def get_pet(self) -> Animal:
        return Dog()

    def get_food(self):
        return "Dog food!"


class CatFactory:

    def get_pet(self):
        return Cat()

    def get_food(self):
        return "Cat food!"


class PetStore:

    def __init__(self, pet_factory):
        # abstract factory
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the object by the DogFactory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is {pet}")
        print(f"Our pet says hello by {pet.speak()}")
        print(f"Its food is {pet_food}")


# Create concrete factory
dog_factory = DogFactory()
cat_factory = CatFactory()
# Create a Petstore our Abstract factory
shop = PetStore(cat_factory)
print(shop.show_pet())

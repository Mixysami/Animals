from abc import ABC, abstractmethod
from datetime import datetime

class Animal(ABC):
    def __init__(self, id_animal, class_animal, animal_name, birthday, anymal_type, animal_commands):
        self.id_animal = id_animal
        self.class_animal = class_animal
        self.animal_name = animal_name
        self.birthday = birthday
        self.anymal_type = anymal_type
        self.animal_commands = animal_commands

    @abstractmethod
    def get_animal_name(self):
        pass

    @abstractmethod
    def get_birthday(self):
        pass

    @abstractmethod
    def get_class_animal(self):
        pass

    @abstractmethod
    def get_id_animal(self):
        pass

    @abstractmethod
    def set_animal_name(self, name):
        pass

    @abstractmethod
    def set_birthday(self, birthday):
        pass

    @abstractmethod
    def set_class_animal(self, class_animal):
        pass

    @abstractmethod
    def set_id_animal(self, id_animal):
        pass

class ConcreteAnimal(Animal):
    def get_animal_name(self):
        return self.animal_name

    def get_birthday(self):
        return self.birthday

    def get_class_animal(self):
        return self.class_animal

    def get_id_animal(self):
        return self.id_animal

    def set_animal_name(self, name):
        self.animal_name = name

    def set_birthday(self, birthday):
        self.birthday = birthday

    def set_class_animal(self, class_animal):
        self.class_animal = class_animal

    def set_id_animal(self, id_animal):
        self.id_animal = id_animal

from abc import ABC, abstractmethod
from datetime import date

class AbstractAnimal(ABC):
    def __init__(self, id_animal=0, class_animal="none", animal_name="none", birthday=None):
        self.id_animal = id_animal
        self.class_animal = class_animal
        self.animal_name = animal_name
        self.birthday = birthday if birthday else date.today()

    @abstractmethod
    def get_id_animal(self):
        pass

    @abstractmethod
    def get_class_animal(self):
        pass

    @abstractmethod
    def get_animal_name(self):
        pass

    @abstractmethod
    def get_birthday(self):
        pass

    @abstractmethod
    def set_id_animal(self, id_animal):
        pass

    @abstractmethod
    def set_class_animal(self, class_animal):
        pass

    @abstractmethod
    def set_animal_name(self, animal_name):
        pass

    @abstractmethod
    def set_birthday(self, birthday):
        pass

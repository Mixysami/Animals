from abc import ABC, abstractmethod

class MenuManagable(ABC):
    @abstractmethod
    def create_animal(self, animal):
        pass

    @abstractmethod
    def get_class_animal(self):
        pass

    @abstractmethod
    def get_next_id_animal(self):
        pass

    @abstractmethod
    def get_animal_type(self, animal, class_animal_file):
        pass

    @abstractmethod
    def get_animal_by_id(self, find_id):
        pass

    @abstractmethod
    def add_command_to_animal(self, animal, any_command):
        pass

    @abstractmethod
    def change_animal(self, animal):
        pass

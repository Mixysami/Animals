from interfaces.menu_managable import MenuManagable
from models.class_animal import ClassAnimal

class MMSample(MenuManagable):
    def __init__(self, db_actions):
        self.db_actions = db_actions

    def create_animal(self, animal):
        self.db_actions.create_animal(animal)

    def get_class_animal(self):
        return [cls.name for cls in ClassAnimal]

    def get_next_id_animal(self):
        return self.db_actions.get_next_id_animal()

    def get_animal_type(self, animal, class_animal_file):
        return self.db_actions.get_animal_type(animal, class_animal_file)

    def get_animal_by_id(self, find_id):
        return self.db_actions.get_animal_by_id(find_id)

    def add_command_to_animal(self, animal, any_command):
        return self.db_actions.add_command_to_animal(animal, any_command)

    def change_animal(self, animal):
        self.db_actions.change_animal(animal)

    def view_shelter(self):
        animals = []
        with open(self.db_actions.db_file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) >= 6:
                    animals.append({
                        'id': parts[0],
                        'type': parts[1],
                        'class': parts[2],
                        'name': parts[3],
                        'birthday': parts[4],
                        'commands': parts[5]
                    })
        return animals

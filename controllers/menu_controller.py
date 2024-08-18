class MenuController:
    def __init__(self, menu_managable):
        self.menu_managable = menu_managable

    def create_animal(self, animal):
        self.menu_managable.create_animal(animal)

    def get_next_id_animal(self):
        return self.menu_managable.get_next_id_animal()

    def get_class_animal(self):
        return self.menu_managable.get_class_animal()

    def get_animal_type(self, animal, class_animal_file):
        return self.menu_managable.get_animal_type(animal, class_animal_file)

    def get_animal_by_id(self, find_id):
        return self.menu_managable.get_animal_by_id(find_id)

    def add_command_to_animal(self, animal, any_command):
        return self.menu_managable.add_command_to_animal(animal, any_command)

    def change_animal(self, animal):
        self.menu_managable.change_animal(animal)

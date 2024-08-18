from interfaces.db_actions import DBActions
from models.animal import ConcreteAnimal
from models.animal import Animal
from datetime import datetime
import os


class DBASample(DBActions):
    def __init__(self, db_file_name):
        self.db_file_name = db_file_name

    def create_animal(self, animal):
        with open(self.db_file_name, 'a') as file:
            file.write(self.animal_to_string(animal))

    def animal_to_string(self, animal):
        animal_string = (
            f"{animal.id_animal};"
            f"{animal.anymal_type};"
            f"{animal.class_animal};"
            f"{animal.animal_name};"
            f"{animal.birthday};"
            f"{animal.animal_commands};\n"
        )
        return animal_string

    def get_next_id_animal(self):
        if not os.path.exists(self.db_file_name):
            return 1
        with open(self.db_file_name, 'r') as file:
            lines = file.readlines()
            if not lines:
                return 1
            last_line = lines[-1]
            last_id = int(last_line.split(';')[0])
            return last_id + 1

    # dba_sample.py

    def get_animal_type(self, animal, class_animal_file):
        try:
            with open(class_animal_file, 'r') as file:
                for line in file:
                    # Предположим, что формат строки: "Тип;Класс1;Класс2;..."
                    parts = line.strip().split(';')
                    animal_type = parts[0]  # Тип животного
                    classes = parts[1:]  # Список классов
                    if animal.class_animal.lower() in [cls.lower() for cls in classes]:
                        return animal_type
        except FileNotFoundError:
            print(f"Error: File '{class_animal_file}' not found.")
            return "Unknown"

    def get_animal_by_id(self, find_id):
        with open(self.db_file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(';')
                if int(parts[0]) == find_id:
                    return self.string_to_animal(parts)
        return None

    def string_to_animal(self, parts):
        id_animal = int(parts[0])
        anymal_type = parts[1]
        class_animal = parts[2]
        animal_name = parts[3]
        birthday = datetime.strptime(parts[4], '%Y-%m-%d').date()
        animal_commands = parts[5]
        return ConcreteAnimal(id_animal, class_animal, animal_name, birthday, anymal_type, animal_commands)

    def add_command_to_animal(self, animal, any_command):
        commands = animal.animal_commands
        if commands.strip() == "":
            commands = any_command
        else:
            commands += f",{any_command}"
        animal.animal_commands = commands
        return animal

    def change_animal(self, animal):
        lines = []
        with open(self.db_file_name, 'r') as file:
            lines = file.readlines()

        with open(self.db_file_name, 'w') as file:
            for line in lines:
                parts = line.strip().split(';')
                if int(parts[0]) == animal.id_animal:
                    file.write(self.animal_to_string(animal))
                else:
                    file.write(line)

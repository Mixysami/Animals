from interfaces.mm_sample import MMSample
from interfaces.dba_sample import DBASample
from models.animal import ConcreteAnimal
from datetime import datetime
from models.counter import Counter  # Импортируем Counter

def main():
    db_file_name = "animal_db.json"
    db_actions = DBASample(db_file_name=db_file_name)
    menu = MMSample(db_actions=db_actions)
    print("Debug: Меню создано")

    counter = Counter()  # Создаем экземпляр Counter

    while True:
        print("\n--- Animal Shelter Management ---")
        print("CREATE. Create new animal")
        print("VIEW_SHELTER. View shelter")
        print("FIND_ANIMAL_BY_ID. Find animal by ID")
        print("ADD_COMMAND. Add command")
        print("UPDATE_ANIMAL. Update animal")
        print("SHOW_COUNTER. Show counter")
        print("QUIT. Quit")
        choice = input("\nEnter your choice: ").strip().upper()

        print(f"Debug: Выбранный вариант - {choice}")

        if choice == "CREATE":
            class_animal = input("Enter class of animal: ")
            animal_name = input("Enter name of the animal: ")
            birthday = input("Enter birthday (YYYY-MM-DD): ")
            try:
                birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD format.")
                continue

            new_animal = ConcreteAnimal(
                id_animal=menu.get_next_id_animal(),
                class_animal=class_animal,
                animal_name=animal_name,
                birthday=birthday,
                anymal_type="",
                animal_commands=""
            )

            new_animal.anymal_type = menu.get_animal_type(new_animal, "class_animal_file.txt")

            with counter:  # Используем счетчик в блоке with
                menu.create_animal(new_animal)
                counter.add()  # Увеличиваем счетчик при успешном создании животного

            print("Animal created successfully!")

        elif choice == "VIEW_SHELTER":
            shelter = menu.view_shelter()
            if shelter:
                print("\nShelter Information:")
                for animal in shelter:
                    print(f"ID: {animal['id']}, Name: {animal['name']}, Type: {animal['type']}, Commands: {animal['commands']}")
            else:
                print("No animals found in the shelter.")

        elif choice == "FIND_ANIMAL_BY_ID":
            id_animal = int(input("Enter ID of the animal: "))
            animal = menu.get_animal_by_id(id_animal)
            if animal:
                print(f"ID: {animal.get_id_animal()}, Name: {animal.get_animal_name()}, Type: {animal.anymal_type}, Commands: {animal.animal_commands}")
            else:
                print("Animal not found.")

        elif choice == "ADD_COMMAND":
            id_animal = int(input("Enter ID of the animal: "))
            command = input("Enter new command: ")
            animal = menu.get_animal_by_id(id_animal)
            if animal:
                updated_animal = menu.add_command_to_animal(animal, command)
                menu.change_animal(updated_animal)
                print("Command added successfully!")
            else:
                print("Animal not found.")

        elif choice == "UPDATE_ANIMAL":
            id_animal = int(input("Enter ID of the animal: "))
            updated_name = input("Enter new name (leave blank to skip): ")
            updated_birthday = input("Enter new birthday (YYYY-MM-DD, leave blank to skip): ")

            if updated_birthday:
                try:
                    updated_birthday = datetime.strptime(updated_birthday, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format. Please enter in YYYY-MM-DD format.")
                    continue

            animal = menu.get_animal_by_id(id_animal)
            if animal:
                if updated_name:
                    animal.set_animal_name(updated_name)
                if updated_birthday:
                    animal.set_birthday(updated_birthday)
                menu.change_animal(animal)
                print("Animal updated successfully!")
            else:
                print("Animal not found.")

        elif choice == "SHOW_COUNTER":
            try:
                print(f"Counter value: {counter.get_count()}")
            except RuntimeError as e:
                print(e)

        elif choice == "QUIT":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    print("Debug: Запуск программы")
    main()
    print("Debug: Программа завершена")

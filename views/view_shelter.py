class ViewShelter:
    @staticmethod
    def display_shelter_info(shelter):
        print("\nShelter Information:")
        for animal in shelter:
            print(f"ID: {animal.id_animal}, Name: {animal.animal_name}, Type: {animal.animal_type}, Commands: {animal.animal_commands}")

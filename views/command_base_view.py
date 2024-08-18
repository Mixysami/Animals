from enum import Enum

class CommandBaseView(Enum):
    CREATE = "Create new animal"
    VIEW_SHELTER = "View shelter"
    FIND_ANIMAL_BY_ID = "Find animal by ID"
    ADD_COMMAND = "Add command"
    UPDATE_ANIMAL = "Update animal"
    QUIT = "Quit"

from django.contrib import admin
from .models import Equipement, Animal

# Register your models here.
admin.site.register(Equipement)
admin.site.register(Animal)

"""
def restore():
    with open(DB_PATH, 'wb') as working_db:
        with open(OG_PATH, 'rb') as original_db:
            working_db.write(original_db.read())

@orm.db_session
def get_animals() -> list[str]:
    return [animal.name for animal in Animal.select()]

@orm.db_session
def get_race(animal_id: str):
    animal = Animal.get(name=animal_id)
    if animal is None:
        print(f"{animal_id} not found in the petshop.")
        return None

    return animal.race

@orm.db_session
def get_order(animal_id: str):
    animal = Animal.get(name=animal_id)
    if animal is None:
        print(f"{animal_id} not found in the petshop.")
        return None

    return animal.order

@orm.db_session
def get_state(animal_id: str):
    animal = Animal.get(name=animal_id)
    if animal is None:
        print(f"{animal_id} not found in the petshop.")
        return None

    return animal.state

@orm.db_session
def get_emoji(animal_id: str):
    animal = Animal.get(name=animal_id)
    if animal is None:
        print(f"{animal_id} not found in the petshop.")
        return None

    return animal.emoji

@orm.db_session
def get_spot(animal_id: str):
    animal = Animal.get(name=animal_id)
    if animal is None:
        print(f"{animal_id} not found in the petshop.")
        return None

    return animal.spot.name


@orm.db_session
def get_availability(equipement_id: str):
    equipement = Equipement.get(name=equipement_id)
    if equipement is None:
        print(f"{equipement_id} does not exist.")
        return None

    return 'empty' if equipement.is_empty else 'occupied'


@orm.db_session
def filter_by_spot(equipement_id: str):
    equipement = Equipement.get(name=equipement_id)
    if equipement is None:
        print(f"{equipement_id} does not exist.")
        return None

    animals = Animal.select(lambda animal: animal.spot == equipement)
    if animals is None:
        return None

    return [animal.name for animal in animals]


@orm.db_session
def set_state(animal_id: str, state: str) -> None:
    if state not in ['hungry', 'tired', 'full', 'asleep']:
        print(f"{state} is not a valid state.")
        return

    animal = Animal.get(name=animal_id)
    if animal is None:
        print(f"{animal_id} not found in the petshop.")
        return

    animal.state = state


@orm.db_session
def set_spot(animal_id: str, equipement_id: str) -> None:
    animal = Animal.get(name=animal_id)
    spot = Equipement.get(name=equipement_id)

    if spot is None:
        print(f"{equipement_id} doesn't exist.")
        return
    if spot.is_occupied:
        print(f"{equipement_id} is not empty for the time being.")
        return
    if animal is None:
        print(f"{animal_id} not found in the petshop.")
        return

    animal.spot.empty()
    animal.spot = spot
    spot.occupy()
"""
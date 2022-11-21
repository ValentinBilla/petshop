from typing import Callable, ClassVar
from dataclasses import dataclass
from functools import wraps

from pony import orm

DB_PATH = "./db/petshop.sqlite"
OG_PATH = "./db/petshop.backup"


def restore() -> None:
    with open(DB_PATH, 'w', encoding='utf-8') as file:
        with open(OG_PATH, 'r', encoding='utf-8') as source:
            file.write(source.read())


db = orm.Database()


class Equipement(db.Entity):
    name = orm.PrimaryKey(str)
    is_empty = orm.Required(bool)
    occupant = orm.Set('Animal', reverse='spot')

    @property
    def is_occupied(self) -> None:
        return not self.is_empty

    @is_occupied.setter
    def is_occupied(self, value: bool) -> None:
        self.is_empty = not value

    def occupy(self):
        self.is_occupied = True

    def empty(self):
        self.is_empty = True


class Animal(db.Entity):
    name = orm.PrimaryKey(str)
    race = orm.Required(str)
    order = orm.Required(str)
    state = orm.Required(str)
    spot = orm.Required('Equipement', cascade_delete=False, reverse='occupant')

    @property
    def emoji(self) -> str:
        emojis = {'hungry':'🤤', 'tired':'🥱', 'full':'😋', 'asleep':'😴'}
        return emojis[self.state]


db.bind(provider='sqlite', filename=DB_PATH)
db.generate_mapping(create_tables=True)


@orm.db_session
def populate_db():
    litter = Equipement(name='litter', is_empty=True)
    manger = Equipement(name='manger', is_empty=False)
    wheel = Equipement(name='wheel', is_empty=True)
    den = Equipement(name='den', is_empty=False)

    tic = Animal(
        name='Tic', race='chipmunk', order='rodent', state='hungry',  spot=litter)
    tac = Animal(name='Tac', race='chipmunk',
                 order='rodent', state='hungry', spot=litter)
    patrick = Animal(name='Patrick', race='hamster',
                     order='rodent', state='hungry', spot=litter)
    totoro = Animal(name='Totoro', race='ili pika',
                    order='rodent', state='full', spot=manger)
    pocahantas = Animal(name='Pocahontas', race='opossum',
                        order='marsupial', state='asleep', spot=den)


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


if __name__ == '__main__':
    orm.set_sql_debug(True)

from typing import ClassVar, Callable
from dataclasses import dataclass
import sys

import model


@dataclass
class Need:
    action: str
    before: str
    after: str
    spot: str

    @property
    def pp_action(self):
        return self.action.replace('_', ' ')


FEED = Need('feed', 'hungry', 'full', 'manger')
ENTERTAIN = Need('entertain', 'full', 'tired', 'wheel')
PUT_TO_BED = Need('put_to_bed', 'tired', 'asleep', 'den')
WAKE_UP = Need('wake_up', 'asleep', 'hungry', 'litter')

NEEDS = [FEED, ENTERTAIN, PUT_TO_BED, WAKE_UP]
POSSIBLE_ACTIONS = [need.action for need in NEEDS]

def get_satisfier(need: Need) -> Callable[[str], tuple[bool, str]]:
    def _f(animal_id: str) -> None:
        state = model.get_state(animal_id)
        if state is None:
            message = f"{animal_id} isn't a known animal."
            return False, message
        if state != need.before:
            message = f"Impossible to {need.pp_action}, {animal_id} is not {need.before}."
            return False, message
        if model.get_availability(need.spot) != 'empty':
            occupants = model.filter_by_spot(need.spot)
            be = 'is' if len(occupants)==1 else 'are'
            occupants = ', '.join(occupants)
            message = f"{animal_id} cannot move to the {need.spot}: {occupants} {be} in it."
            return False, message

        model.set_spot(animal_id, need.spot)
        model.set_state(animal_id, need.after)

        message = f"Well done, {animal_id} went to the {need.spot} and is now {state}."
        return True, message

    return _f

def generate_satisfiers():
    module = sys.modules[__name__]
    for need in NEEDS:
        setattr(module, need.action, get_satisfier(need))

generate_satisfiers()
from typing import Optional

from django.db import models

# Create your models here.

class Equipement(models.Model):
    # Modified the model to be able to put multiple animals in one equipement.
    name: str = models.CharField(max_length=100, primary_key=True)
    capacity: int = models.IntegerField(default=1)
    state_before: str = models.CharField(max_length=20, default="")
    state_after: str = models.CharField(max_length=20, default="")
    picture: str = models.CharField(max_length=200, default=None, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name

    @property
    def occupants(self) -> list[Optional['Animal']]:
        occupants = list(Animal.objects.filter(spot=self))
        
        occupants.extend([None] * max(0, self.capacity-len(occupants)))

        return occupants

    @property
    def is_full(self) -> None:
        return None not in self.occupants


class Animal(models.Model):
    name: str = models.CharField(max_length=100, primary_key=True)
    race: str = models.CharField(max_length=20)
    order: str = models.CharField(max_length=20)
    state: str = models.CharField(max_length=20)
    spot: Equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    picture: str = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def move_to(self, spot: Equipement) -> tuple[bool, str]:
        if self.spot == spot:
            message = f"{self} is already in {spot}, good for him !"
            return True, message
        if self.state != spot.state_before:
            message = f"Impossible to move to the {spot}, {self} is not {spot.state_before}."
            return False, message
        if spot.is_full:
            occupants = [animal for animal in spot.occupants if animal is not None]
            be = 'is' if len(occupants)==1 else 'are'
            occupants = ', '.join(map(str, occupants))
            message = f"{self} cannot move to the {spot}: {occupants} {be} in it."
            return False, message

        self.spot = spot
        self.state = spot.state_after

        message = f"{self} successfully moved to the {spot} and is now {self.state}."
        return True, message

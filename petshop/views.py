from django.shortcuts import render
from .models import Equipement, Animal
from .forms import MoveForm

def petshop(request):
    equipements = Equipement.objects.order_by('name')
    animals = Animal.objects.order_by('name')
    return render(request, 'petshop.html', {'equipements': equipements, 'animals': animals})

def animal_detail(request, name, message=None):
    animal = Animal.objects.get(**{'name': name})
    form = MoveForm(request.POST, instance=animal)
    
    context = None

    if form.is_valid():
        spot = form.cleaned_data['spot']
        success, message = animal.move_to(spot)
        context = {'success': success, 'message': message}
        
        if success:
            animal.save()

    return render(request, 'animal_detail.html', {'animal': animal, 'form': form, 'context': context})


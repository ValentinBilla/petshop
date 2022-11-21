import functools

from appJar import gui

import model
import controller

model.restore()

app = gui("Petshop")
app.setSticky("news")
app.setExpand("both")
app.setFont(14)

app.addLabel("header", "Welcome in the petshop!", colspan=4)
app.setLabelBg("header", "salmon")
app.setLabelFg("header", "white")

app.addLabel("info_header", " Informations", colspan=4)
app.setLabelAlign("info_header", "left")
app.setLabelFg("info_header", "white")
app.setLabelBg("info_header", "grey")
for i, animal_id in enumerate(model.get_animals()):
    race = model.get_race(animal_id)
    order = model.get_order(animal_id)

    row = app.getRow()
    app.addLabel(animal_id, f"{animal_id}", row, colspan=2)
    app.addLabel(f"{animal_id}_state", "", row, 2, colspan=1)
    app.addLabel(f"{animal_id}_infos", f"[{order} / {race}] ", row, 3, colspan=1)

    app.setLabelAlign(animal_id, "left")
    app.setLabelAlign(f"{animal_id}_state", "left")
    app.setLabelAlign(f"{animal_id}_infos", "left")

    if i % 2 == 0:
        app.setLabelBg(animal_id, "lavender")
        app.setLabelBg(f"{animal_id}_infos", "lavender")
        app.setLabelBg(f"{animal_id}_state", "lavender")


app.addLabel("action_header", " Actions", colspan=4)
app.setLabelAlign("action_header", "left")
app.setLabelFg("action_header", "white")
app.setLabelBg("action_header", "grey")

begin = app.getRow()
for row, animal_id in enumerate(model.get_animals(), begin):
    app.addLabel(f"{animal_id}_emoji", model.get_emoji(animal_id), row)
    app.addRadioButton("animal_id", animal_id, row, 1, colspan=2)


def update():
    for animal_id in model.get_animals():
        state = model.get_state(animal_id)
        spot = model.get_spot(animal_id)
        app.setLabel(f"{animal_id}_state", f"{state} in the {spot}")
        app.setLabel(f"{animal_id}_emoji", model.get_emoji(animal_id))


def press(action, act):
    id_animal = app.getRadioButton("animal_id")
    success, message = getattr(controller, action)(id_animal)
    update()

    app.infoBox('Success', message) if success else app.warningBox(
        'Failure', message)


for row, action in enumerate(controller.POSSIBLE_ACTIONS, begin):
    app.addButton(action.replace('_', ' '), functools.partial(
        press, action), row, 3, colspan=1)

update()

app.go()

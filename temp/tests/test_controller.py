import model
from controller import controller


def test_feed():
    controller.feed('Tic')
    assert model.get_availability('manger') == 'occupied'
    assert model.get_state('Tic') == 'full'
    assert model.get_spot('Tic') == 'manger'
    controller.feed('Tac')
    assert model.get_state('Tac') == 'hungry'
    assert model.get_spot('Tac') == 'litter'
    controller.feed('Pocahontas')
    assert model.get_state('Pocahontas') == 'asleep'
    assert model.get_spot('Pocahontas') == 'den'
    controller.feed('Bob')
    assert model.get_state('Bob') is None
    assert model.get_spot('Bob') is None
    assert model.get_availability('manger') == 'occupied'

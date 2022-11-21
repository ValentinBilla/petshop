import model


def test_get_state():
    assert model.get_state('Tac') == 'hungry'


def test_get_state_null():
    assert model.get_state('Bob') is None


def test_get_spot():
    assert model.get_spot('Tac') == 'litter'


def test_get_spot_null():
    assert model.get_spot('Bob') is None


def test_get_availability():
    assert model.get_availability('litter') == 'empty'
    assert model.get_availability('den') == 'occupied'


def test_get_availability_null():
    assert model.get_availability('nintendo') is None


def test_filter_by_spot():
    assert model.filter_by_spot('den') == ['Pocahontas']
    assert 'Tac' in model.filter_by_spot('litter')
    assert 'Tac' not in model.filter_by_spot('manger')


def test_filter_by_spot_null():
    assert model.filter_by_spot('casino') is None


def test_set_state():
    model.set_state('Totoro', 'tired')
    assert model.get_state('Totoro') == 'tired'
    model.set_state('Totoro', 'excited as a louse')
    assert model.get_state('Totoro') == 'tired'
    model.set_state('Bob', 'tired')
    assert model.get_state('Bob') == None


def test_set_spot():
    model.set_spot('Totoro', 'wheel')
    assert model.get_spot('Totoro') == 'wheel'
    assert model.get_availability('litter') == 'empty'
    assert model.get_availability('wheel') == 'occupied'


def test_set_spot_occupied():
    model.set_spot('Totoro', 'den')
    assert model.get_spot('Totoro') == 'wheel'


def test_set_spot_null_1():
    model.set_spot('Totoro', 'casino')
    assert model.get_spot('Totoro') == 'wheel'


def test_set_spot_null_2():
    model.set_spot('Bob', 'litter')
    assert model.get_spot('Bob') is None

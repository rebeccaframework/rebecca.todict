import pytest
from pyramid import testing


@pytest.fixture
def config(request):
    from rebecca.todict import includeme
    config = testing.setUp()
    def fin():
        testing.tearDown()
    request.addfinalizer(fin)
    config.include(includeme)
    return config


def test_it(config):
    from rebecca.todict import todict
    from dummy import Dummy, to_dict_dummy

    config.set_todict(Dummy, to_dict_dummy)

    dummy = Dummy()
    request = testing.DummyRequest()
    result = todict(request, dummy)
    
    assert result == dict(value="test")

def test_named_todict(config):
    from rebecca.todict import todict
    from dummy import Dummy, to_dict_dummy_another

    config.set_todict(Dummy, to_dict_dummy_another, name="another")

    dummy = Dummy()
    request = testing.DummyRequest()
    result = todict(request, dummy, name="another")
    
    assert result == dict(value="another")


def test_todict_config(config):
    from rebecca.todict import todict
    import dummy
    config.scan(dummy)
    
    request = testing.DummyRequest()
    result = todict(request, dummy.Dummy(), name="testing")
    
    assert result == dict(value="testing")

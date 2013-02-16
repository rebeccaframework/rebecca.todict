import pytest
from pyramid import testing

class Dummy(object):
    pass

def to_dict_dummy(request, obj):
    return dict(value="test")

def to_dict_dummy_another(request, obj):
    return dict(value="another")

@pytest.fixture
def config():
    from rebecca.todict import includeme
    config = testing.setUp()

    config.include(includeme)
    config.set_todict(Dummy, to_dict_dummy)
    config.set_todict(Dummy, to_dict_dummy_another, name="another")
    return config


def test_it(config):
    from pyramid.interfaces import IRequest, IDict
    from rebecca.todict import todict


    dummy = Dummy()
    request = testing.DummyRequest()
    result = todict(request, dummy)
    
    assert result == dict(value="test")

def test_named_todict(config):
    from pyramid.interfaces import IRequest, IDict
    from rebecca.todict import todict


    dummy = Dummy()
    request = testing.DummyRequest()
    result = todict(request, dummy, name="another")
    
    assert result == dict(value="another")

from pyramid import testing

class Dummy(object):
    pass

def to_dict_dummy(request, obj):
    return dict(value="test")

def test_it():
    from pyramid.interfaces import IRequest, IDict
    from . import set_todict, todict, includeme

    config = testing.setUp()

    config.include(includeme)
    config.set_todict(Dummy, to_dict_dummy)

    dummy = Dummy()
    request = testing.DummyRequest()
    result = todict(request, dummy)
    
    assert result == dict(value="test")



import pytest
from pyramid import testing

class Dummy(object):
    pass

def to_dict_dummy(request, obj):
    return dict(value="test")

def dummy_view(request):
    return dict(dummy=Dummy(), extra=100)

@pytest.fixture
def config(request):
    from rebecca.todict import includeme
    config = testing.setUp()
    def fin():
        testing.tearDown()
    request.addfinalizer(fin)
    config.add_renderer('.json', 'rebecca.todict.renderers.json_renderer_factory')
    config.include(includeme)
    return config


def test_it(config):
    config.set_todict(Dummy, to_dict_dummy, name="testing.json")
    config.add_view(dummy_view, name="dummy_view", renderer='testing.json')
    from pyramid.view import render_view
    context = testing.DummyResource()
    request = testing.DummyRequest()
    result = render_view(context, request, name="dummy_view")
    assert request.response.content_type == 'application/json'
    import json
    assert json.loads(result.decode('utf-8')) == json.loads('{"dummy": {"value": "test"}, "extra": 100}')

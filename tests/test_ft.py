from pyramid.config import Configurator
from webtest import TestApp
from rebecca.todict import todict

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("testing", 20)

def person_to_dict1(request, person):
    return dict(name=person.name)


def person_to_dict2(request, person):
    return dict(name=person.name, age=person.age)


def view1(request):
    return todict(request, request.context)


def view2(request):
    return todict(request, request.context, name="test2")


def factory(request):
    return person

def test_app():
    config = Configurator()
    config.include('rebecca.todict')
    config.set_todict(Person, person_to_dict1)
    config.set_todict(object, person_to_dict1)
    config.set_todict(Person, person_to_dict2, name="test2")
    config.set_root_factory(factory)
    config.add_view(view1, name="view1", renderer="json")
    config.add_view(view2, name="view2", renderer="json")

    app = config.make_wsgi_app()

    app = TestApp(app)

    res = app.get('/view1')
    assert res.json == {"name": "testing"}

    res = app.get('/view2')
    assert res.json == {"name": "testing", "age": 20}

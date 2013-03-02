import json
from pyramid.interfaces import IRendererFactory
from zope.interface import implementer
from . import todict

class Encoder(json.JSONEncoder):
    def __init__(self, request, name):
        super(Encoder, self).__init__()
        self.request = request
        self.name = name


    def default(self, obj):
        try:
            return todict(self.request, obj, self.name)
        except:
            super(Encoder, self).default(obj)

@implementer(IRendererFactory)
def json_renderer_factory(info):
    def json_renderer(value, system):
        request = system['request']
        name = system['renderer_name']
        encoder = Encoder(request, name)
        return encoder.encode(value)
    return json_renderer

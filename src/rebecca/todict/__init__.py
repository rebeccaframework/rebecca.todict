from pyramid.interfaces import IDict, IRequest

def set_todict(config, type, callable, name=""):
    type = config.maybe_dotted(type)
    callable = config.maybe_dotted(callable)
    reg = config.registry

    def register():
        reg.registerAdapter(callable,
                            [IRequest, type],
                            IDict,
                            name=name)

    intr = config.introspectable(category_name='todict',
                                 discriminator='todict of {0}'.format(type.__name__),
                                 title='todict of {0}'.format(type.__name__),
                                 type_name=None)

    config.action("todict", register,
                  introspectables=(intr,))


def todict(request, value, name=""):
    adapted = request.registry.getMultiAdapter([request, value], 
                                               IDict,
                                               name=name)
    return adapted


def includeme(config):
    config.add_directive('set_todict',
                         set_todict)


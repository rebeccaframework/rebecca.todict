from rebecca.todict import todict_config

class Dummy(object):
    pass

def to_dict_dummy(request, obj):
    return dict(value="test")

def to_dict_dummy_another(request, obj):
    return dict(value="another")

@todict_config(Dummy, name="testing")
def testing_to_dict(request, obj):
    return dict(value="testing")

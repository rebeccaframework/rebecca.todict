.. contents::

rebecca.todict
================

``rebecca.todict`` is API and directive converting object to ``dict``.

INSTALL
===============

Install using pip or easy_install.::

  $ pip install rebecca.todict
  $ easy_install rebecca.todict

USAGE
===============

rebecca.todict privides ``includeme`` hook that will set up ``set_todict`` directive.::

  config.include('rebecca.todict')

using with paste deploy::

  pyramid.includes = rebecca.todict



register todict adapter
=================================

by directive
----------------------------------

To register todict adapter, you can use ``set_todict`` directive.::

  config.set_todict(Person, person_to_dict)

That register todict adapter converging Person object to dict.

You can register named adapter too::

  config.set_todict(Person, person_to_dict_short, name="short")


by todict_decorator
-----------------------------------

``todict_decorator`` register ``todict`` Adapter casually.::

  @todict_config(Person)
  def person_to_dict(request, person):
      return dict(....)


using todict API
==============================

Registered adapters are used by todict API::

  from rebecca.todict import todict

  d = todict(request, person)

::

  d = todict(request, person, name="short")


JSON Renderer using todict API
==========================================

``rebecca.todict.renderers.json_renderer_factory`` is factory of renderer using todict API.

to use this renderer, register renderer factory::

    config.add_renderer('.json', 'rebecca.todict.renderers.json_renderer_factory')


specify ".json" renderer on ``view_config`` or ``add_view``::

   @view_config(renderer="short.json")
   def person_list(request):
       return dict(people=[Person(), Person()])

the renderer use ``todict`` Adapters named "short".

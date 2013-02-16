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

To register todict adapter, you can use ``set_todict`` directive.::

  config.set_todict(Person, person_to_dict)

That register todict adapter converging Person object to dict.

You can register named adapter too::

  config.set_todict(Person, person_to_dict_short, name="short")


using todict API
==============================

Registered adapters are used by todict API::

  from rebecca.todict import todict

  d = todict(request, person)

::

  d = todict(request, person, name="short")

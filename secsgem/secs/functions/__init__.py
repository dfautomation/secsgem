#####################################################################
# functions.py
#
# (c) Copyright 2013-2015, Benjamin Parzella. All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#####################################################################
"""Wrappers for SECS stream and functions."""
import pkgutil
import inspect

from .base import SecsStreamFunction

# load all available stream/function classes into a dictionary
functions = {}
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    _module = loader.find_module(module_name).load_module(module_name)
    for _name, _member in inspect.getmembers(_module):
        if inspect.isclass(_member) and _member != SecsStreamFunction and \
                issubclass(_member, SecsStreamFunction):
            functions[_name] = _member

# update this module to include all loaded function classes
globals().update(functions)

# build the old style streams functions dictionary
secs_streams_functions = {}

for name, function in functions.items():
    # pylint: disable=protected-access
    if function._stream not in secs_streams_functions:
        secs_streams_functions[function._stream] = {}

    secs_streams_functions[function._stream][function._function] = function

__all__ = [
    "SecsStreamFunction", "secs_streams_functions"
]

# add the loaded class names into the __all__ list
__all__.extend(functions.keys())

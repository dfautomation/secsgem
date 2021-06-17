#####################################################################
# s01f24.py
#
# (c) Copyright 2021, Benjamin Parzella. All rights reserved.
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
"""Class for stream 01 function 24."""

from secsgem.secs.functions.base import SecsStreamFunction
from secsgem.secs.data_items import CEID, CENAME, VID


class SecsS01F24(SecsStreamFunction):
    """
    collection event namelist - reply.

    **Data Items**

    - :class:`CEID <secsgem.secs.data_items.CEID>`
    - :class:`CENAME <secsgem.secs.data_items.CENAME>`
    - :class:`VID <secsgem.secs.data_items.VID>`

    **Structure**::

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS01F24
        [
            {
                CEID: U1/U2/U4/U8/I1/I2/I4/I8/A
                CENAME: A
                [
                    VID: U1/U2/U4/U8/I1/I2/I4/I8/A
                    ...
                ]
            }
            ...
        ]

    **Example**::

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS01F24([[1, "CE1", [3]],
        ...     [1337, "CE2", [5, 1234]]])
        S1F24
          <L [2]
            <L [3]
              <U1 1 >
              <A "CE1">
              <L [1]
                <U1 3>
              >
            >
            <L [3]
              <U2 1337 >
              <A "CE2">
              <L [1]
                <U1 5>
                <U2 1234>
              >
            >
          > .

    :param value: parameters for this function (see example)
    :type value: list
    """

    _stream = 1
    _function = 24

    _data_format = [
        [
            CEID,
            CENAME,
            [VID],
        ]
    ]

    _to_host = True
    _to_equipment = False

    _has_reply = False
    _is_reply_required = False

    _is_multi_block = True

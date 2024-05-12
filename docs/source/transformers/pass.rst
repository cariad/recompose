.. py:module:: recompose
    :noindex:

..  _pass:

pass
====

The **pass** transformer does not directly transform a value, but passes a specific child of the data to a new :ref:`cursor <cursors>`.

This is also the default transformer if a name is not specified in the :ref:`schema <transformer-schema>`.

Configuration
-------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Key
     - Type
     - Required
     - Value
   * - :code:`path`
     - string
     - Yes
     - Key of the child object to pass
   * - :code:`cursor`
     - :ref:`Cursor schema <cursor-schema>`
     - Yes
     - Cursor to pass the child object to

Example
-------

The code below passes the root data object to the **pass** transformer, which then passes only the "firefighters" list to the :ref:`list-to-object <list-to-object>` transformer.

This leaves all the other key values untouched, while replacing the "firefighters" list with just a single value.

.. testcode::

    from json import dumps
    from recompose import CursorSchema, transform

    data = {
        "chefs": [
            {
                "name": "Alice"
            },
            {
                "name": "Bob"
            }
        ],
        "firefighters": [
            {
                "name": "Daniel"
            },
            {
                "name": "Esther"
            }
        ],
        "zookeepers": [
            {
                "name": "Gregory"
            },
            {
                "name": "Harold"
            }
        ]
    }

    schema: CursorSchema = {
        "version": 1,
        "perform": {
            "transform": "pass",
            "path": "firefighters",
            "cursor": {
                "perform": "list-to-object",
            }
        }
    }

    transformed = transform(schema, data)

    print(dumps(transformed, indent=4))

Result
~~~~~~

.. testoutput::
   :options: +NORMALIZE_WHITESPACE

    {
        "chefs": [
            {
                "name": "Alice"
            },
            {
                "name": "Bob"
            }
        ],
        "firefighters": {
            "name": "Daniel"
        },
        "zookeepers": [
            {
                "name": "Gregory"
            },
            {
                "name": "Harold"
            }
        ]
    }

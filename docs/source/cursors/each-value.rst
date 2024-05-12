.. py:module:: recompose
    :noindex:

..  _each-value:

each-value
==========

The **each-value** cursor performs transformations on each of the context object's children.

When the context is a list, each value will be transformed. When the context is a dictionary, the key will be ignored and only the value will be transformed.

Example
-------

The code below uses the **each-value** cursor with the :ref:`list-to-object <list-to-object>` transformer to reduce a dictionary of lists down to a dictionary of values.

.. testcode::

    from json import dumps
    from recompose import CursorSchema, transform

    data = {
        "first": ["one", "two", "three"],
        "second": ["four", "five", "six"],
        "third": ["seven", "eight", "nine"],
    }

    schema: CursorSchema = {
        "version": 1,
        "on": "each-value",
        "perform": "list-to-object",
    }

    transformed = transform(schema, data)
    print(dumps(transformed, indent=4))

Result
~~~~~~

.. testoutput::
   :options: +NORMALIZE_WHITESPACE

    {
        "first": "one",
        "second": "four",
        "third": "seven"
    }

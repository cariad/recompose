.. py:module:: recompose
    :noindex:

..  _list-to-object:

list-to-object
==============

The **list-to-object** transformer reduces a list down to just its first value.

Configuration
-------------

**list-to-object** has no configuration.

Example
-------

The code below uses the inferred :ref:`this-value <this-value>` cursor with the **list-to-object** transformer to reduce a list down to a single value.

.. testcode::

    from recompose import transform, CursorSchema

    data = ["one", "two", "three"]

    schema: CursorSchema = {
        "version": 1,
        "perform": "list-to-object",
    }

    transformed = transform(schema, data)
    print(transformed)

Result
~~~~~~

.. testoutput::
   :options: +NORMALIZE_WHITESPACE

    one

.. py:module:: recompose.cursor_classes
    :noindex:

..  _this-value:

this-value
==========

The **this-value** cursor performs transformations only on the context object and does not iterate over its children.

Example
-------

The code below uses the **this-value** cursor with the :ref:`list-to-object <list-to-object>` transformer to reduce a list down to a single value.

.. testcode::

    from recompose import transform, CursorSchema

    data = ["one", "two", "three "]

    schema: CursorSchema = {
        "version": 1,
        "on": "this-value",
        "perform": "list-to-object",
    }

    transformed = transform(schema, data)
    print(transformed)

Result
~~~~~~

.. testoutput::
   :options: +NORMALIZE_WHITESPACE

    one

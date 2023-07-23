..  _transformers:

Transformers
============

Transformers describe how to modify data.

.. _transformer-schema:

Schema
------

When a transformer does not need any configuration, it can be specified only by its name.

For example:

.. code-block:: json

    {
        "version": 1,
        "on": "this-value",
        "perform": "list-to-object"
    }

Otherwise, this schema applies:

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Key
     - Type
     - Required
     - Value
   * - :code:`transform`
     - string
     - No; defaults to :ref:`pass <pass>`
     - Transformer name
   * - :code:`*`
     - any
     - No
     - Transformer-specific configuration

For example:

.. code-block:: json

    {
        "version": 1,
        "on": "each-value",
        "perform": {
            "transform": "pass",
            "path": "foo",
            "cursor": {
                "on": "each-value",
                "perform": "list-to-object"
            }
        }
    }

.. toctree::
    :titlesonly:

    list-to-object
    pass

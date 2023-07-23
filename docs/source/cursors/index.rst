..  _cursors:

Cursors
=======

Cursors describe how :ref:`transformers <transformers>` move through data.

..  _cursor-schema:

Schema
------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Key
     - Type
     - Required
     - Value
   * - :code:`version`
     - integer
     - Only on the root
     - Schema version
   * - :code:`on`
     - string
     - No; defaults to :ref:`this-value <this-value>`
     - Cursor name
   * - :code:`perform`
     - string, list or object
     - Yes
     - :ref:`Transformers <transformers>` to run

For example:

.. code-block:: json

    {
        "version": 1,
        "on": "each-value",
        "perform": "list-to-object"
    }

.. toctree::
    :titlesonly:

    each-value
    this-value

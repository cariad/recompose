.. py:module:: recompose
    :noindex:

Recompose
=========

**Recompose** is a Python package for recomposing data by following instructional schemas.

For example, the code below describes a dataset with groups of people with specific careers, and a schema that reduces the list of firefighters down to a single object.

.. testcode::

    from json import dumps
    from recompose import transform, CursorSchema

    data = {
        "2023-06-04": {
            "groups": {
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
        },
        "2023-06-05": {
            "groups": {
                "chefs": [
                    {
                        "name": "Jet"
                    },
                    {
                        "name": "Karen"
                    }
                ],
                "firefighters": [
                    {
                        "name": "Mater"
                    },
                    {
                        "name": "Nigel"
                    }
                ],
                "zookeepers": [
                    {
                        "name": "Peter"
                    },
                    {
                        "name": "Quentin"
                    }
                ]
            }
        }
    }

    schema: CursorSchema = {
        "version": 1,
        "on": "each-value",
        "perform": {
            "path": "groups",
            "cursor": {
                "perform": {
                    "path": "firefighters",
                    "cursor": {
                        "perform": "list-to-object",
                    }
                }
            }
        }
    }

    transformed = transform(schema, data)

    print(dumps(transformed, indent=4))

By default, the :ref:`transform` function will raise `PathNotFound` if a path in the schema doesn't exist. To allow missing data, create and pass an :ref:`options` instance.

Result
~~~~~~

.. testoutput::
   :options: +NORMALIZE_WHITESPACE

    {
        "2023-06-04": {
            "groups": {
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
        },
        "2023-06-05": {
            "groups": {
                "chefs": [
                    {
                        "name": "Jet"
                    },
                    {
                        "name": "Karen"
                    }
                ],
                "firefighters": {
                    "name": "Mater"
                },
                "zookeepers": [
                    {
                        "name": "Peter"
                    },
                    {
                        "name": "Quentin"
                    }
                ]
            }
        }
    }

Installation
------------

`Recompose is available on PyPI <https://pypi.org/project/recompose/>`_ for installation via your favourite tool.

.. code:: console

  pip install recompose

Source & Licence
----------------

Recompose is released under the MIT Licence at https://github.com/cariad/recompose by Cariad Eccleston.

.. toctree::
    :hidden:
    :titlesonly:

    self
    transform
    options
    cursors/index
    transformers/index

Author
------

Hello! 👋 I'm **Cariad Eccleston**, and I'm a freelance Amazon Web Services architect, DevOps evangelist, and infrastructure and backend engineer by the beach in the United Kingdom.

You can find me at `cariad.earth <https://cariad.earth>`_, `github.com/cariad <https://github.com/cariad>`_ and `linkedin.com/in/cariad <https://linkedin.com/in/cariad>`_.

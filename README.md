# Recompose

**Recompose** is a Python package for recomposing data by following instructional schemas.

Full documentation is online at [cariad.github.io/recompose](https://cariad.github.io/recompose/).

## Example

For example, the code below describes a dataset with groups of people with specific careers, and a schema that reduces the list of firefighters down to a single object.

```python
from recompose import CursorSchema, transform

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

print(transformed)
```

```json
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
```

## Author

Hello! 👋 I'm **Cariad Eccleston**, and I'm a freelance Amazon Web Services architect, DevOps evangelist, and infrastructure and backend engineer by the beach in the United Kingdom.

You can find me at [cariad.earth](https://cariad.earth), [github.com/cariad](https://github.com/cariad) and [linkedin.com/in/cariad](https://linkedin.com/in/cariad).

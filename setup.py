from pathlib import Path

from setuptools import setup

from recompose import __version__

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.9",
    "Typing :: Typed",
]

if "alpha" in __version__:
    classifiers.append("Development Status :: 3 - Alpha")
elif "beta" in __version__:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="Templated data recomposition",
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="recompose",
    packages=[
        "recompose",
        "recompose.cursor_classes",
        "recompose.exceptions",
        "recompose.schema_readers",
        "recompose.transformer_classes",
    ],
    package_data={
        "recompose": ["py.typed"],
        "recompose.cursor_classes": ["py.typed"],
        "recompose.exceptions": ["py.typed"],
        "recompose.schema_readers": ["py.typed"],
        "recompose.transformer_classes": ["py.typed"],
    },
    python_requires=">=3.9",
    url="https://github.com/cariad/recompose",
    version=__version__,
)

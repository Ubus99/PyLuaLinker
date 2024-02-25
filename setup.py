from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="PyLuaLinker",
    version="0.0.1",
    packages=find_packages(["PyLuaLinker", "PyLuaLinker.*"])
)

import logging
import os
import sys

from PyLuaLinker import linker
from PyLuaLinker import utils
from PyLuaLinker.builddata import BuildData
from PyLuaLinker.dependency_tree.tree import Tree


def build(args):
    logging.info("Starting LUA linker...")

    execution_path = sys.argv[0]
    buildscript_path = args.path.resolve()

    os.chdir(str(buildscript_path.parent))

    buildscript = utils.json_from_path(buildscript_path)

    data = BuildData(
        buildscript,
        buildscript_path.parent
    )

    dt = Tree(data)
    linker.link_project(data, dt)

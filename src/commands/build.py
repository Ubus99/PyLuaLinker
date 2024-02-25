import os
from build_data import build_data
import utils
import linker
from dependency_tree.tree import tree
import sys
import logging

def build(args):

    logging.info("Starting LUA linker...")

    execution_path = sys.argv[0]
    buildscript_path = args.path.resolve()

    os.chdir(str(buildscript_path.parent))

    buildscript = utils.json_from_path(buildscript_path)

    data = build_data(
        buildscript,
        buildscript_path.parent
    )

    dt = tree(data)
    linker.link_project(data, dt)
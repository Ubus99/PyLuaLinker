import os
import sys
import logging
from .. import utils
from .. import linker
from ..build_data import build_data
from ..dependency_tree.tree import tree


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

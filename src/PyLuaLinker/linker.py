from pathlib import Path

import logging
from . import utils
from .build_data import build_data
from .dependency_tree import tree as dt


def link_project(data: build_data, tree: dt.tree):
    logging.info("linking files @ " + str(data.build_dir))

    while True:
        leaves = tree.get_leaves()
        if len(leaves) == 0:
            break
        for l in leaves:
            link_file(data.build_dir, l)
            tree.cull(l)

    clean_up(data)


def link_file(dir_out: Path, dependency: dt.node):
    # get paths
    filename = dependency.name
    cache_path = dir_out / ".cache"
    out_path = cache_path / (filename + ".temp")

    cache_path.mkdir(exist_ok=True, parents=True)

    # open files
    logging.info("> started linking " + filename)
    file_in = dependency.path.open()
    file_out = out_path.open("w+")

    # link file
    for l in file_in:
        if utils.is_import(l):  # link file here
            logging.info(">> inserting @ " + l.strip())
            file_out.write(utils.insert_requirement(l, cache_path))

        else:
            file_out.write(l)

    file_in.close()
    file_out.close()
    logging.info("< finished linking " + filename)


def clean_up(data: build_data):
    inp_path = data.cache_dir / (data.entry_point + ".temp")
    out_path = data.build_dir / (data.app_name + ".lua")

    out_file = out_path.open("+w")
    out_file.write(inp_path.open().read())
    out_file.close()

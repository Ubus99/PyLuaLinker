import dependency_tree.tree as dt
from pathlib import Path
import dependency_tree.utils as utils


def link(dir_out: Path, tree: dt.tree):
    print("linking files @" + str(dir_out))

    while True:
        leaves = tree.get_leaves()
        if len(leaves) == 0:
            break
        for l in leaves:
            link_file(dir_out, l)
            tree.cull(l)

    clean_up(dir_out, tree.entry)


def link_file(dir_out: Path, dependency: dt.node):
    # get paths
    filename = dependency.name
    cache_path = dir_out / "cache"
    out_path = cache_path / (filename + ".temp")

    cache_path.mkdir(exist_ok=True)

    # open files
    print("> linking " + filename)
    file_in = dependency.path.open()
    file_out = out_path.open("w+")

    # link file
    for l in file_in:
        if utils.is_import(l):
            name = utils.extract_import(l)
            path = cache_path / (name + ".temp")
            file_out.write(insert_file(path) + "\n")
        else:
            file_out.write(l)

    print("finished linking " + filename)


def clean_up(dir_out: Path, filename: str):
    temppath = dir_out / "cache"
    in_path = temppath / (filename + ".temp")
    out_path = dir_out / (filename + ".lua")

    out_file = out_path.open("+w")
    out_file.write(in_path.open().read())
    out_file.close()


def insert_file(path: Path) -> str:
    try:
        return path.open().read()
    except FileNotFoundError:
        print("dependency file not found!")
        return "--<include file not found>\n"

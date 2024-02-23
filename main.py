import sys
import json
from pathlib import Path
import os
from pprint import pprint
import dependency_tree.tree as dt
import linker


def load_JSON_from_path(path: Path) -> dict:
    print("loading " + str(path))

    try:
        file = open(path, "r")
        dict = json.load(file)
        pprint("> " + str(dict) + "\n")
        return dict

    except FileNotFoundError:
        print("> File not found\n")
        exit()


def get_sources_in_path(path: Path) -> dict[str]:
    abs_path = path.resolve()
    print(str(abs_path) + ":")

    files = list(abs_path.glob("*.lua"))

    out = {}
    for f in files:
        out[f.stem] = f
        print("> " + str(f.name))
    print()

    return out


def collect_sources(dirs: list[str]):
    src_files = {}
    for dir in dirs:
        src_files |= get_sources_in_path(Path(dir))
    # todo remove dupes / collision detection
    pprint(src_files)
    print()

    return src_files


def main():
    print("\nStarting LUA linker...\n")

    execution_path = sys.argv[0]
    buildscript_path = Path(sys.argv[1]).resolve()
    # buildscript_path = Path("../46d856a8-ccf9-4530-a6c6-3dfdfcea7d67/usr/local/DataClient/buildscript.json")

    os.chdir(str(buildscript_path.parent))

    buildscript = load_JSON_from_path(buildscript_path)

    app_name = buildscript["app_name"]
    src_dirs = buildscript["src_dir"]
    trg_dir = buildscript_path.parent / "build"

    src_files = collect_sources(src_dirs)
    deps = dt.tree("main", src_files)
    deps.grow()
    linker.link(trg_dir, deps)


if __name__ == "__main__":
    main()

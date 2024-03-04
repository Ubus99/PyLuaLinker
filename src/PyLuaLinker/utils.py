import json
import logging
import re
from pathlib import Path
from pprint import pformat


def is_import(line: str) -> bool:
    """determine if a line is a valid import statement

    Args:
        line (str): one line of code

    Returns:
        bool:is a static import statement
    """

    txt = line.strip()
    restr = '.*require\(\".+\"\) --> static'  # only supports duble quotes
    match = re.search(restr, txt)
    return match != None


def scan_file(path: Path) -> dict[int, str]:
    """scans a source file for any valid import statements

    Args:
        path (Path): path to source file

    Returns:
        dict[int, str]: returns dict shaped [line: dependency name]
    """

    logging.info("scanning " + path.name + ":")

    file = path.open()
    deps = {}

    for idx, l in enumerate(file):
        logging.debug(str(idx) + " > " + l.strip())
        if is_import(l):
            _, deps[idx] = extract_import(l)

    logging.info("scanning " + path.name + " completed")
    return deps


def extract_import(line: str) -> tuple[list[str], str]:
    """extracts require statement

    Args:
        line (str): line to scan

    Returns:
        list[str]: list of tokens
        str: name of import
    """

    txt = line.strip()
    tokens = txt.split(" ")

    r = re.compile("require\(\".+\"\)")
    require = list(filter(r.match, tokens))[0]
    name = require.split('"')[1]

    idx = tokens.index(require)
    tokens[idx] = name

    return tokens, name


def insert_requirement(l: str, cache_path: Path) -> str:
    tokens, name = extract_import(l)
    path = cache_path / (name + ".temp")

    try:
        out = path.open().read() + "\n\n"
    except FileNotFoundError:
        logging.error("<<< cached dependency '" + name + ".temp' not found!")
        out = "--<include file not found>\n"

    out += " ".join(tokens) + "\n"
    return out


def json_from_path(path: Path) -> dict:
    logging.info("loading " + str(path))

    try:
        file = open(path, "r")
        dict = json.load(file)
        file.close()

        logging.info(pformat("> " + str(dict)))  # todo broken formating

        return dict

    except FileNotFoundError:
        logging.critical("> File not found\n")
        exit()


def get_sources_in_path(path: Path) -> dict[str, Path]:
    """collects LUA source-files from given path

    Args:
        path (Path): source search path

    Returns:
        dict[str, Path]: dict mapping file name to path
    """

    abs_path = path.resolve()
    logging.info("> " + str(abs_path) + ":")

    file_paths = list(abs_path.glob("**/*.lua"))

    out = {}
    for f in file_paths:
        out[f.stem] = f
        logging.info(">> " + str(f.name))

    return out


def collect_sources(dirs: list[str]) -> dict[str, Path]:
    """collects all LUA source-files from given directries, works recursively

    Args:
        dirs (list[str]): list of path strings to search for source-files

    Returns:
        dict[str, Path]: dictionary mapping source-file names to paths
    """

    logging.info("starting to collect sources")
    src_files = {}
    for dir in dirs:
        # todo remove dupes / collision detection
        src_files |= get_sources_in_path(Path(dir))

    logging.info("finished collecting sources")
    return src_files

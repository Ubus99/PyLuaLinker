from pathlib import Path
import re

def extract_import(line: str) -> str:
    """extracts file path from import statement

    Args:
        line (str): line to scan

    Returns:
        str: file path of dependency
    """
    txt = line.strip()
    return txt.split('"')[1]


def is_import(line: str) -> bool:
    """determine if a line is a valid import statement

    Args:
        line (str): one line of code

    Returns:
        bool:is a static import statement
    """

    txt = line.strip()
    restr = '.*require\(\".+\"\) --> static' # only supports duble quotes
    match = re.search(restr, txt)
    return match != None

def scan_file(path: Path) -> dict[int, str]:
    """scans a source file for any valid import statements

    Args:
        path (Path): path to source file

    Returns:
        dict[int, str]: returns dict shaped [line: dependency name]
    """

    print("scanning " + path.name + ":")

    file = path.open()
    deps = {}

    for idx, l in enumerate(file):
        print(str(idx) + " > " + l.strip())
        if is_import(l):
            deps[idx] = extract_import(l)
    print()

    return deps
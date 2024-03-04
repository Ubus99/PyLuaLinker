import argparse
import logging
from pathlib import Path

from . import build
from . import new


def init_parser():
    parser = argparse.ArgumentParser(
        description="a commandline-tool for linking LUA files into one output file"
    )
    parser.add_argument(
        "-v", "--verbosity",
        action="count",
        default=0,
        help="increase output verbosity"
    )
    subparsers = parser.add_subparsers(title="functions", required=True)

    parser_build = subparsers.add_parser(
        "build", help="build your PyLuaLinker project"
    )
    parser_build.add_argument(
        "path",
        type=Path,
        default="./",
        help="the path to your buildscript.json file"
    )
    parser_build.set_defaults(func=build.build)

    parser_new = subparsers.add_parser(
        "new", help="initialize a new PyLuaLinker project"
    )
    parser_new.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=Path("./"),
        help="initialize a new PyLuaLinker project at path, defaults to current direpipctory"
    )
    parser_new.set_defaults(func=new.new_project)

    return parser


def main():
    parser = init_parser()
    args = parser.parse_args()

    logging.basicConfig(
        format="%(asctime)s %(name)s:%(levelname)s:\t# %(message)s",
        datefmt="%I:%M:%S",
        level=30 - 10 * args.verbosity
    )

    return args.func(args)

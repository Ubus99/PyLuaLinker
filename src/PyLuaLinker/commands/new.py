import argparse
import logging
import shutil
from pathlib import Path


def new_project(args: argparse.Namespace):
    src_path = (Path(__file__) / "../../../data/buildscript.json").resolve()
    dst_dir = args.path.resolve()
    dst_src_dir = dst_dir / "src"

    logging.info("initializing PyLuaLinker project to " + str(dst_dir))
    dst_src_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(src_path, dst_dir)

    logging.info("Finished")

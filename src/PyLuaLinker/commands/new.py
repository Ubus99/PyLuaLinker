import logging
from pathlib import Path
import shutil


def init(args):
    src_path = Path("./data/buildscript.json").resolve()
    dst_dir = args.path.resolve()
    dst_src_dir = dst_dir / "src"
    dst_path = dst_dir / "buildscript.json"

    logging.info("initializing PyLuaLinker project to " + str(dst_path))
    dst_src_dir.mkdir(parents=True)
    shutil.copyfile(src_path, dst_path)

    logging.info("Finished")

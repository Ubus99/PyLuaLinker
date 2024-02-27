from pathlib import Path
from . import utils


class build_data:
    def __init__(self,
                 buildscript: dict,
                 build_dir: Path
                 ) -> None:

        self.src = utils.collect_sources(buildscript["src_dir"],)

        if not buildscript["entry_point"] in self.src:
            print("entry  point not found!")
            exit()

        self.app_name = buildscript["app_name"]
        self.entry_point = buildscript["entry_point"]

        self.build_dir = build_dir / "build"
        self.cache_dir = self.build_dir / ".cache"

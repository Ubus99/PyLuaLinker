import argparse
import shutil
import unittest
from pathlib import Path

from src.PyLuaLinker.commands import new


class TestProjectInitialization(unittest.TestCase):

    def setUp(self):
        self.target_path = Path("./" + __name__ + "/")

    def test_new(self):
        new.new_project(argparse.Namespace(path=self.target_path))

        bs_path = Path(self.target_path / "buildscript.json").resolve()
        bs_template_path = Path("../src/data/buildscript.json").resolve()

        with (bs_path.open() as bs,
              bs_template_path.open() as bs_template):
            bs_string = bs.read()
            bs_template_string = bs_template.read()

            self.assertEqual(bs_template_string, bs_string)

    def tearDown(self):
        shutil.rmtree(self.target_path)


if __name__ == '__main__':
    unittest.main()

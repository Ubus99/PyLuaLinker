import argparse
import unittest
from pathlib import Path

from src.PyLuaLinker.commands import build


class TestLinking(unittest.TestCase):

    def setUp(self):
        self.target_path = Path("./project/buildscript.json")

    def runTest(self):
        build.build(argparse.Namespace(path=self.target_path))

    def tearDown(self):
        pass

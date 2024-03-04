import unittest
from pathlib import Path


# from context import src


class TestProjectInitialization(unittest.TestCase):

    def test_new(self):
        target_path = Path("./")

        # print(dir(src))  # ("build", target_path)


if __name__ == '__main__':
    unittest.main()

import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import create_parser

class CLITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = create_parser()

class TestArgs(CLITestCase):
    """Test for parsing args"""

    def setUp(self):
        self.args = ["some_project", "extra_arg"]

    def test_accepts_only_one_arg(self):
        args = self.parser.parse_args(self.args[:1])
        self.assertEqual(args.name, "some_project")

    def test_does_not_accept_more_than_one_arg(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(self.args)

if __name__ == "__main__":
    unittest.main()

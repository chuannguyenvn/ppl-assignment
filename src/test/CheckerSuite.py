import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test(self):
        input = """
        foo: integer = 1;
        bar: string;
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 101))

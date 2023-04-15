import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test(self):
        input = """
        foo: array [2,2] of string;
        foo[1, "av"];
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 101))

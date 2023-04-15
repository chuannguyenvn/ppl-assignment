import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test(self):
        """Test short variable declaration"""
        input = """delta: integer = 3;delta:integer = 3;"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 101))

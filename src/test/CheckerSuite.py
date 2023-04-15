import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test(self):
        input = """
        foo: function void (){
        a: integer;
        n = 1;
        };
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 101))

import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test(self):
        input = """
        foo: function void (){
  
        };
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 101))

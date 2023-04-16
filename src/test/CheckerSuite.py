import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test(self):
        input = """
        a: integer = 1;
        b: integer = 2;
        foo: function string (a: integer)
        {
        
        }
        main: function void (){
        a = a + b;
        }
        
        
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 101))

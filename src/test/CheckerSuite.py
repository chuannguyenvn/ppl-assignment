import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test(self):
        input = """
        
        foo: function string (a: integer)
        {
        
        }
        main: function void (){
        a: string;
        
        b: string = foo("adsf");
        };
        
        
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 101))

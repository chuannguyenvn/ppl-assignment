import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test(self):
        input = """
        a: string = "v";
        b: auto = "asdf";
        foo: function string (a: string)
        {
        
        }
        main: function void (){
        b: auto = 1;
        a = foo(b);
        }
        
        
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 101))

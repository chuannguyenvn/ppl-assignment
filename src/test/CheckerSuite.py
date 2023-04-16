import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test(self):
        input = """
        main: function void (){
        a: string;
        while(true)
        {
        {
        {
        {
        break;
        }
        }
        }
        }
    
        };
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 101))

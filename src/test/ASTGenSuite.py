import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_expression_with_assignment(self):
        """Simple program: int main() {} """
        input = """float a;
        float b;
        float c,d;"""
        expect = "4"
        self.assertTrue(TestAST.test(input,expect,300))
   

import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def _L1__Test_1_(self):
        self.assertTrue(TestLexer.test("abc", "abc", "_L1__Test_1_"))


    def _L2__Test_2_(self):
        self.assertTrue(TestLexer.test("def", "def", "_L2__Test_2_"))


    def _L3___(self):
        self.assertTrue(TestLexer.test("ghi", "ghi", "_L3___"))


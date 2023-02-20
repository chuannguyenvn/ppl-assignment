
import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_L1__Test_1_(self):
        self.assertTrue(TestLexer.test("abc", "abc", "_L1__Test_1_"))


    def test_L2__Test_2_(self):
        self.assertTrue(TestLexer.test("def", "def", "_L2__Test_2_"))


    def test_L3__Test_3_(self):
        self.assertTrue(TestLexer.test("ghi", "ghi", "_L3__Test_3_"))


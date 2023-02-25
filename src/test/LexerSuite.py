import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def testLexer(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 101))
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 101))
        self.assertTrue(TestLexer.test("1_2_3", "123,<EOF>", 101))
        self.assertTrue(TestLexer.test("_1_2_3", "_1_2_3,<EOF>", 101))
        self.assertTrue(TestLexer.test("1_2_3_", "123,_,<EOF>", 101))
        self.assertTrue(TestLexer.test("1__2__3", "1,__2__3,<EOF>", 101))
        self.assertTrue(TestLexer.test("1.23", "1.23,<EOF>", 101))
        self.assertTrue(TestLexer.test("0.123", "0.123,<EOF>", 101))
        self.assertTrue(TestLexer.test("123_456.789", "123456.789,<EOF>", 101))
        self.assertTrue(TestLexer.test("1.23e45", "1.23e45,<EOF>", 101))
        self.assertTrue(TestLexer.test("1.23e+45", "1.23e+45,<EOF>", 101))
        self.assertTrue(TestLexer.test("123E-45", "123E-45,<EOF>", 101))
        self.assertTrue(TestLexer.test("0.12", "0.12,<EOF>", 101))
        self.assertTrue(TestLexer.test(".01", ".01,<EOF>", 101))
        self.assertTrue(TestLexer.test("0.123_456", "0.123,_456,<EOF>", 101))
        self.assertTrue(TestLexer.test("123E456_789", "123E456,_789,<EOF>", 101))
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
        self.assertTrue(TestLexer.test("abc0", "abc0,<EOF>", 101))
        self.assertTrue(TestLexer.test("_abc", "_abc,<EOF>", 101))
        self.assertTrue(TestLexer.test("0_abc", "0,_abc,<EOF>", 101))
        self.assertTrue(TestLexer.test("__abc", "__abc,<EOF>", 101))
        self.assertTrue(TestLexer.test("a b c", "a,b,c,<EOF>", 101))
        self.assertTrue(TestLexer.test("_a_a_", "_a_a_,<EOF>", 101))

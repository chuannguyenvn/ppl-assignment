
import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_L1__Test_1__fuck_(self):
        self.assertTrue(TestLexer.test("asdf", "asdf", "_L1__Test_1__fuck_"))


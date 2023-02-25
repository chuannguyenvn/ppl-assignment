
import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def testLexer(self):
        self.assertTrue(TestLexer.test("^a","Error Token ^", 101))

        
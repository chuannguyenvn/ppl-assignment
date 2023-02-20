
import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_L1__variable_(self):
        self.assertTrue(TestLexer.test(r'''abc''', r'''abc,<EOF>''', "_L1__variable_"))


    def test_L2__string_literal_(self):
        self.assertTrue(TestLexer.test(r'''"asdfasdf"''', r'''asdfasdf,<EOF>''', "_L2__string_literal_"))


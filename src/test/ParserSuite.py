
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def _P1__Test_1__Test_adsfasdf_(self):
        input = """main function : {asdfasdf}"""
        expect = """sadfasdfasd"""
        self.assertTrue(TestParser.test(input, expect, "_P1__Test_1__Test_adsfasdf_"))

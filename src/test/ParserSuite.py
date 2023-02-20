
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def test_P1__Test_1__Test_adsfasdf_(self):
        input = """main: function void () {}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, "_P1__Test_1__Test_adsfasdf_"))

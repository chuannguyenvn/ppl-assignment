
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def test_P1__Test_1__main___(self):
        input = r'''main: function void () {}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P1__Test_1__main___"))

    def test_P2__Test_2__variable_declaration_(self):
        input = r'''main: function void () {
a : float = "5\"";
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P2__Test_2__variable_declaration_"))

    def test_P3__sadf_(self):
        input = r'''x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P3__sadf_"))

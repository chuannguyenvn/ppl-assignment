import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def test_P1___(self):
        input = r'''main: function integer()
{

}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P1___"))

    def test_P2___(self):
        input = r'''main: function integer()
{
    a = 1;
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P2___"))

    def test_P3___(self):
        input = r'''main: function integer()
{
    a = a;
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P3___"))

    def test_P4___(self):
        input = r'''main: function integer()
{
    a = foo();
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P4___"))

    def test_P5___(self):
        input = r'''main: function integer()
{
    a = foo(1);
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P5___"))

    def test_P6___(self):
        input = r'''main: function integer()
{
    a = foo((1));
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P6___"))

    def test_P7___(self):
        input = r'''main: function integer()
{
    a = foo(foo());
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P7___"))

    def test_P8___(self):
        input = r'''main: function integer()
{
    a = {1, 2, 3};
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P8___"))

    def test_P9___(self):
        input = r'''main: function integer()
{
    a = {(1), 2 + 3, foo(4)};
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P9___"))

    def test_P10___(self):
        input = r'''main: function integer()
{
    a = 123_456_789;
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P10___"))

    def test_P11___(self):
        input = r'''main: function integer()
{
    if (1 > 2) a = 1;
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P11___"))

    def test_P12___(self):
        input = r'''main: function integer()
{
    if (1 > 2) foo();
    else bar();
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P12___"))

    def test_P13___(self):
        input = r'''main: function integer()
{
    if (1 > 2) if (2 > 3) if (3 > 4) if (4 > 5) foo();
    else bar();
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P13___"))

    def test_P14___(self):
        input = r'''main: function integer()
{
    for (i = 1, i < 10, i + 1) foo();
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P14___"))

    def test_P15___(self):
        input = r'''main: function integer()
{
    for (i = foo(), foo(), foo()) foo();
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P15___"))

    def test_P16___(self):
        input = r'''main: function integer()
{
    for (1 = 1, i < 10, i + 1) foo();
}'''
        expect = r'''something else'''
        self.assertTrue(TestParser.test(input, expect, "_P16___"))

    def test_P17___(self):
        input = r'''main: function integer()
{
    for (i = 1, i < 10, i + 1) 
    for (j = 1, j > 10, j + foo()) 
    foo();
}'''
        expect = r'''successful'''
        self.assertTrue(TestParser.test(input, expect, "_P17___"))

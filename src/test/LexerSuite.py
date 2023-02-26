import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def testLexer(self):
        self.assertTrue(TestLexer.test("   ", "<EOF>", 101))
        self.assertTrue(TestLexer.test(" \n ", "<EOF>", 102))
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 103))
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 104))
        self.assertTrue(TestLexer.test("1_2_3", "123,<EOF>", 105))
        self.assertTrue(TestLexer.test("_1_2_3", "_1_2_3,<EOF>", 106))
        self.assertTrue(TestLexer.test("1_2_3_", "123,_,<EOF>", 107))
        self.assertTrue(TestLexer.test("1__2__3", "1,__2__3,<EOF>", 108))
        self.assertTrue(TestLexer.test("1.23", "1.23,<EOF>", 109))
        self.assertTrue(TestLexer.test("0.123", "0.123,<EOF>", 110))
        self.assertTrue(TestLexer.test("123_456.789", "123456.789,<EOF>", 111))
        self.assertTrue(TestLexer.test("1.23e45", "1.23e45,<EOF>", 112))
        self.assertTrue(TestLexer.test("1.23e+45", "1.23e+45,<EOF>", 113))
        self.assertTrue(TestLexer.test("123E-45", "123E-45,<EOF>", 114))
        self.assertTrue(TestLexer.test("0.12", "0.12,<EOF>", 115))
        self.assertTrue(TestLexer.test(".12e1", ".12e1,<EOF>", 116))
        self.assertTrue(TestLexer.test(".0e0", ".0e0,<EOF>", 117))
        self.assertTrue(TestLexer.test(".01", ".,0,1,<EOF>", 118))
        self.assertTrue(TestLexer.test("0.123_456", "0.123,_456,<EOF>", 119))
        self.assertTrue(TestLexer.test("123E456_789", "123E456,_789,<EOF>", 120))
        self.assertTrue(TestLexer.test("123_456E789", "123456E789,<EOF>", 121))
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 122))
        self.assertTrue(TestLexer.test("abc0", "abc0,<EOF>", 123))
        self.assertTrue(TestLexer.test("_abc", "_abc,<EOF>", 124))
        self.assertTrue(TestLexer.test("0_abc", "0,_abc,<EOF>", 125))
        self.assertTrue(TestLexer.test("__abc", "__abc,<EOF>", 126))
        self.assertTrue(TestLexer.test("a b c", "a,b,c,<EOF>", 127))
        self.assertTrue(TestLexer.test("_a_a_", "_a_a_,<EOF>", 128))
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 129))
        self.assertTrue(TestLexer.test("false true", "false,true,<EOF>", 130))
        self.assertTrue(TestLexer.test("true_false", "true_false,<EOF>", 131))
        self.assertTrue(TestLexer.test(""" "Hi" """, "Hi,<EOF>", 132))
        self.assertTrue(TestLexer.test(""" "\\b \\f \\r \\n \\t \\' \\\ " """, "\\b \\f \\r \\n \\t \\' \\\ ,<EOF>", 133))
        self.assertTrue(TestLexer.test(""" "\\"Hey\\"" """, '\\"Hey\\",<EOF>', 134))
        self.assertTrue(TestLexer.test("//A", "<EOF>", 135))
        self.assertTrue(TestLexer.test("/* AAA \n BBB \n CCC */", "<EOF>", 136))
        self.assertTrue(TestLexer.test("auto // auto", "auto,<EOF>", 137))
        self.assertTrue(TestLexer.test("+", "+,<EOF>", 138))
        self.assertTrue(TestLexer.test("-", "-,<EOF>", 139))
        self.assertTrue(TestLexer.test("*", "*,<EOF>", 140))
        self.assertTrue(TestLexer.test("/", "/,<EOF>", 141))
        self.assertTrue(TestLexer.test("%", "%,<EOF>", 142))
        self.assertTrue(TestLexer.test("!", "!,<EOF>", 143))
        self.assertTrue(TestLexer.test("&&", "&&,<EOF>", 144))
        self.assertTrue(TestLexer.test("||", "||,<EOF>", 145))
        self.assertTrue(TestLexer.test("==", "==,<EOF>", 146))
        self.assertTrue(TestLexer.test("!=", "!=,<EOF>", 147))
        self.assertTrue(TestLexer.test("<", "<,<EOF>", 148))
        self.assertTrue(TestLexer.test("<=", "<=,<EOF>", 149))
        self.assertTrue(TestLexer.test(">", ">,<EOF>", 150))
        self.assertTrue(TestLexer.test(">=", ">=,<EOF>", 151))
        self.assertTrue(TestLexer.test("::", "::,<EOF>", 152))
        self.assertTrue(TestLexer.test("(", "(,<EOF>", 153))
        self.assertTrue(TestLexer.test(")", "),<EOF>", 154))
        self.assertTrue(TestLexer.test("[", "[,<EOF>", 155))
        self.assertTrue(TestLexer.test("]", "],<EOF>", 156))
        self.assertTrue(TestLexer.test("{", "{,<EOF>", 157))
        self.assertTrue(TestLexer.test("}", "},<EOF>", 158))
        self.assertTrue(TestLexer.test(".", ".,<EOF>", 159))
        self.assertTrue(TestLexer.test("=", "=,<EOF>", 160))
        self.assertTrue(TestLexer.test(",", ",,<EOF>", 161))
        self.assertTrue(TestLexer.test(":", ":,<EOF>", 162))
        self.assertTrue(TestLexer.test(";", ";,<EOF>", 163))
        self.assertTrue(TestLexer.test("auto", "auto,<EOF>", 164))
        self.assertTrue(TestLexer.test("break", "break,<EOF>", 165))
        self.assertTrue(TestLexer.test("boolean", "boolean,<EOF>", 166))
        self.assertTrue(TestLexer.test("do", "do,<EOF>", 167))
        self.assertTrue(TestLexer.test("else", "else,<EOF>", 168))
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 169))
        self.assertTrue(TestLexer.test("float", "float,<EOF>", 170))
        self.assertTrue(TestLexer.test("for", "for,<EOF>", 171))
        self.assertTrue(TestLexer.test("function", "function,<EOF>", 172))
        self.assertTrue(TestLexer.test("if", "if,<EOF>", 173))
        self.assertTrue(TestLexer.test("integer", "integer,<EOF>", 174))
        self.assertTrue(TestLexer.test("return", "return,<EOF>", 175))
        self.assertTrue(TestLexer.test("string", "string,<EOF>", 176))
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 177))
        self.assertTrue(TestLexer.test("while", "while,<EOF>", 178))
        self.assertTrue(TestLexer.test("void", "void,<EOF>", 179))
        self.assertTrue(TestLexer.test("out", "out,<EOF>", 180))
        self.assertTrue(TestLexer.test("continue", "continue,<EOF>", 181))
        self.assertTrue(TestLexer.test("of", "of,<EOF>", 182))
        self.assertTrue(TestLexer.test("inherit", "inherit,<EOF>", 183))
        self.assertTrue(TestLexer.test("array", "array,<EOF>", 184))

































































































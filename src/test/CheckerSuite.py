import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # def test_001(self):
    #     input = """main1: function void() {}"""
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 1))
    # 
    # def test_002(self):
    #     input = """main: function integer() {
    #                 return 0;
    #             }"""
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 2))
    # 
    # def test_003(self):
    #     input = """main: function void(a: integer) {}"""
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 3))
    # 
    # def test_004(self):
    #     input = """main: function void(a: integer, b: integer) {}
    #                 main2: function boolean() {
    #                     return true;
    #                 }
    #                 A: float = 5;
    #                 main1: function void() {
    #                     A: integer = 5;
    #                 }
    #             """
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 4))
    # 
    # def test_005(self):
    #     input = """main: function void() {}"""
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 5))
    # 
    # def test_006(self):
    #     input = """
    #                 A: integer = 5;
    #                 A: boolean = 5;
    #                 main: function void() {}
    #             """
    #     expect = """Redeclared Variable: A"""
    #     self.assertTrue(TestChecker.test(input, expect, 6))
    # 
    # def test_007(self):
    #     input = """
    #                 A: integer = 5;
    #                 main: function void(a: integer, b: float, c: boolean) {}
    #                 main: function void() {}
    #             """
    #     expect = """Redeclared Function: main"""
    #     self.assertTrue(TestChecker.test(input, expect, 7))
    # 
    # def test_008(self):
    #     input = """
    #                 main: function void() {
    #                     a: integer = 1 + "float";
    #                 }
    #             """
    #     expect = """Type mismatch in expression: BinExpr(+, IntegerLit(1), StringLit(float))"""
    #     self.assertTrue(TestChecker.test(input, expect, 8))
    # 
    # def test_009(self):
    #     input = """
    #                 main: function void() {
    #                     a: integer = "int" :: "float";
    #                 }
    #             """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(::, StringLit(int), StringLit(float)))"""
    #     self.assertTrue(TestChecker.test(input, expect, 9))
    # 
    # def test_010(self):
    #     input = """
    #                 main: function void() {
    #                     a: integer = 5;
    #                     b: boolean = 7;
    #                     c: integer = (a == 4) == b;
    #                 }
    #             """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(b, BooleanType, IntegerLit(7))"""
    #     self.assertTrue(TestChecker.test(input, expect, 10))
    # 
    # def test_011(self):
    #     input = """
    #                 main: function void() {
    #                     a: integer = 5;
    #                     b: boolean = 5;
    #                     c: float = !b + (a == 5);
    #                 }
    #             """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(b, BooleanType, IntegerLit(5))"""
    #     self.assertTrue(TestChecker.test(input, expect, 11))
    # 
    # def test_012(self):
    #     input = """
    #                 main: function void() {
    #                     a: float;
    #                     b: integer;
    #                     c: string;
    #                     d: boolean;
    #                     e: integer = !(((-a + b) < (7 % 5)) == true);
    #                 }
    #             """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(e, IntegerType, UnExpr(!, BinExpr(==, BinExpr(<, BinExpr(+, UnExpr(-, Id(a)), Id(b)), BinExpr(%, IntegerLit(7), IntegerLit(5))), BooleanLit(True))))"""
    #     self.assertTrue(TestChecker.test(input, expect, 12))
    # 
    # def test_013(self):
    #     input = """
    #                 main: function void() {
    #                     a: string = "int" :: "float";
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 13))
    # 
    # def test_014(self):
    #     input = """
    #                 A: integer = 5;
    #                 B: boolean = true || false;
    #                 C: string = "abc" :: "def";
    #                 D: float = 5.0 + A;
    #                 main: function void() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 14))
    # 
    # def test_015(self):
    #     input = """
    #                 A: integer = 5;
    #                 main1: function void(a: integer, b: float, c: boolean) {}
    #                 main: function void() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 15))
    # 
    # def test_016(self):
    #     input = """
    #                 main: function void() {
    #                     a: integer = 2 * 3 + 8 % 5 - 7 / 7;
    #                     b: boolean = (2 == 3) && !(true) || (3 != 8);
    #                     c: float = 2 * 3.5 + 8 % 5 - 7 / 7;
    #                     d: string = ("abc" :: "def") :: "xyz";
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 16))
    # 
    # def test_017(self):
    #     input = """
    #                 main: function void() {
    #                     a: integer = 2 * 3 + 8 % 5 - 7 / 7;
    #                     b: boolean = (2 == 3) && !(true) || (3 != 8);
    #                     c: float = 2 * 3.5 + 8 % 5.5 - 7 / 7;
    #                     d: string = ("abc" :: "def") :: "xyz";
    #                 }
    #             """
    #     expect = """Type mismatch in expression: BinExpr(%, IntegerLit(8), FloatLit(5.5))"""
    #     self.assertTrue(TestChecker.test(input, expect, 17))
    # 
    # def test_018(self):
    #     input = """
    #                 foo: function integer() {
    #                     return 2;
    #                 }
    #                 foo2: function integer() {
    #                     return 3;
    #                 }
    #                 main: function void() {
    #                     a: integer = foo() + foo2();
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 18))
    # 
    # def test_019(self):
    #     input = """
    #                 b: integer = 5;
    #                 c: integer = 6;
    #                 a: integer = b + c;
    # 
    #                 foo: function integer(a: string) {
    #                     return 0;
    #                 }
    # 
    #                 main: function void() {
    #                     a: integer = 7;
    #                     {
    #                         a: boolean = b == c;
    #                         {
    #                             a: float = 1.0 + b;
    #                             {
    #                                 a: string = "abc";
    #                                 {
    #                                     d: integer = foo(a);
    #                                 }
    #                             }
    #                         }
    #                     }
    #                     a: boolean;
    #                 }
    #             """
    #     expect = """Redeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 19))
    # 
    # def test_020(self):
    #     input = """
    #                 b: integer = 5;
    #                 c: integer = 6;
    #                 a: integer = b + c;
    # 
    #                 foo: function void(a: integer) {
    # 
    #                 }
    # 
    #                 main: function void() {
    #                     a: integer = 7;
    #                     {
    #                         a: boolean = b == c;
    #                         {
    #                             a: float = 1.0 + b;
    #                             {
    #                                 a: string = "abc";
    #                                 {
    #                                     d: integer = foo(a);
    #                                 }
    #                             }
    #                         }
    #                     }
    #                 }
    #             """
    #     expect = """Type mismatch in expression: FuncCall(foo, [Id(a)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 20))
    # 
    # def test_021(self):
    #     input = """
    #                 b: integer = 5;
    #                 c: integer = 6;
    #                 a: integer = b + c;
    # 
    #                 main: function void() {
    #                     a: integer = 7;
    #                     {
    #                         a: boolean = b == c;
    #                         {
    #                             a: float = 1.0 + b;
    #                             {
    #                                 a: string = "abc";
    #                                 {
    #                                     printString(a);
    #                                 }
    #                             }
    #                         }
    #                     }
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 21))
    # 
    # def test_022(self):
    #     input = """
    #                 b: integer = 5;
    #                 c: integer = 6;
    #                 a: integer = b + c;
    # 
    #                 main: function void() {
    #                     a: float = b - c;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 22))
    # 
    # def test_023(self):
    #     input = """
    #                 b: integer;
    #                 foo: function void(c: float) {
    #                     a: float = b + c;
    #                 }
    #                 main: function void() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 23))
    # 
    # def test_024(self):
    #     input = """
    #                 b: integer;
    #                 foo: function void() {
    #                     c: integer = 5;
    #                 }
    #                 main: function void() {
    #                     a: integer = b + c;
    #                 }
    #             """
    #     expect = """Undeclared Identifier: c"""
    #     self.assertTrue(TestChecker.test(input, expect, 24))
    # 
    # def test_025(self):
    #     input = """
    #                 b: integer;
    #                 main: function void() {
    #                     c: integer;
    #                     a: integer = b + c;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 25))
    # 
    # def test_026(self):
    #     input = """
    #                 b: integer;
    #                 c: integer;
    #                 main: function void() {
    #                     a: integer = b + c;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 26))
    # 
    # def test_027(self):
    #     input = """
    #                 main: function void() {
    #                     a: integer = b + c;
    #                 }
    #             """
    #     expect = """Undeclared Identifier: b"""
    #     self.assertTrue(TestChecker.test(input, expect, 27))
    # 
    # def test_028(self):
    #     input = """
    #                 a : array[2] of integer = {1, 2};
    #                 main: function void() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 28))
    # 
    # def test_029(self):
    #     input = """
    #                 a : array[2, 2] of integer = {{1, 2}, {3, 4}};
    #                 main: function void() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 29))
    # 
    # def test_030(self):
    #     input = """
    #                 a : array[1] of integer = {1, "c"};
    #                 main: function void() {}
    #             """
    #     expect = """Illegal array literal: ArrayLit([IntegerLit(1), StringLit(c)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 30))
    # 
    # def test_031(self):
    #     input = """
    #                 a : array[1] of integer = {1, 2};
    #                 main: function void() {}
    #             """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 31))
    # 
    # def test_032(self):
    #     input = """
    #                 a : array[2, 2] of integer = {{1, 2}, {"c", "d"}};
    #                 main: function void() {}
    #             """
    #     expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([StringLit(c), StringLit(d)])])"""
    #     self.assertTrue(TestChecker.test(input, expect, 32))
    # 
    # def test_033(self):
    #     input = """
    #                 a : array[2, 2, 2] of integer = {{{1, 2}, {3, 4}}, {{5, 6}, {7, 8}}};
    #                 main: function void() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 33))
    # 
    # def test_034(self):
    #     input = """
    #                 a : array[2, 2, 2] of integer = {{{1,2}, {3, 4}}, {{5.0, 6.1}, {7.8, 9.9}}};
    #                 main: function void() {}
    #             """
    #     expect = """Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)])]), ArrayLit([ArrayLit([FloatLit(5.0), FloatLit(6.1)]), ArrayLit([FloatLit(7.8), FloatLit(9.9)])])])"""
    #     self.assertTrue(TestChecker.test(input, expect, 34))
    # 
    # def test_035(self):
    #     input = """
    #                 a : array[2, 2] of integer = {{1, 2}, {3, 4, 5}};
    #                 main: function void() {}
    #             """
    #     expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4), IntegerLit(5)])])"""
    #     self.assertTrue(TestChecker.test(input, expect, 35))
    # 
    # def test_036(self):
    #     input = """
    #                 a : array[2, 2] of integer = {{1, "c"}, {3, "a", "d"}};
    #                 main: function void() {}
    #             """
    #     expect = """Illegal array literal: ArrayLit([IntegerLit(1), StringLit(c)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 36))
    # 
    # def test_037(self):
    #     input = """
    #                 a : array[2] of boolean = {1, 2};
    #                 main: function void() {}
    #             """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], BooleanType), ArrayLit([IntegerLit(1), IntegerLit(2)]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 37))
    # 
    # def test_038(self):
    #     input = """
    #                 a : array[2] of integer = {1, 2};
    #                 func: function auto(e: integer, b: float, c: string, d: boolean) {
    #                     f: integer = 5;
    #                     g: boolean = true;
    #                     return f;
    #                 }
    #                 main: function void() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 38))
    # 
    # def test_039(self):
    #     input = """
    #                 a: float = 1;
    #                 b: auto = a + 2;
    #                 c: integer = 2.3;
    #                 main: function void() {}
    #             """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FloatLit(2.3))"""
    #     self.assertTrue(TestChecker.test(input, expect, 39))
    # 
    # def test_040(self):
    #     input = """
    #                 foo: function integer(a: integer) {
    #                     return a;
    #                 }
    #                 a, b, c: integer = 3 + 0, a + 1, foo(5);
    #                 main: function void() {
    #                     printInteger(a + b + c);
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 40))
    # 
    # def test_041(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer(a: integer, b: boolean) {
    #                     return a;
    #                 }
    #                 goo: function integer() inherit foo {
    #                     super();
    #                 }
    #             """
    #     expect = """Type mismatch in expression: """
    #     self.assertTrue(TestChecker.test(input, expect, 41))
    # 
    # def test_042(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer(a: integer, b: boolean) {
    #                     return a;
    #                 }
    #                 goo: function integer() inherit foo {
    #                     super(1, true);
    #                     return 3;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 42))
    # 
    # def test_043(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer(a: integer, b: boolean) {
    #                     return a;
    #                 }
    #                 goo: function integer() inherit foo {
    #                     super(1, 2);
    #                 }
    #             """
    #     expect = """Type mismatch in expression: IntegerLit(2)"""
    #     self.assertTrue(TestChecker.test(input, expect, 43))
    # 
    # def test_044(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer(a: integer, b: float) {
    #                     return a;
    #                 }
    #                 goo: function integer() inherit foo {
    #                     super(1, 2);
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 44))
    # 
    # def test_045(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer(a: integer, b: boolean) {
    #                     return a;
    #                 }
    #                 goo: function integer() inherit foo {
    #                     preventDefault();
    #                     return 2;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 45))
    # 
    # def test_046(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer(a: integer, b: boolean) {
    #                     return a;
    #                 }
    #                 goo: function integer() inherit foo {
    #                     preventDefault(1, 2);
    #                 }
    #             """
    #     expect = """Type mismatch in expression: IntegerLit(1)"""
    #     self.assertTrue(TestChecker.test(input, expect, 46))
    # 
    # def test_047(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     return 123;
    #                 }
    #                 goo: function integer() inherit foo {
    #                     super();
    #                     return 2;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 47))
    # 
    # def test_048(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer(a: integer) {
    #                     return 123;
    #                 }
    #                 goo: function integer() inherit foo {
    #                     super(1);
    #                     super(2);
    #                 }
    #             """
    #     expect = """Undeclared Function: super"""
    #     self.assertTrue(TestChecker.test(input, expect, 48))
    # 
    # def test_049(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     if(1 == 2) a = a + 1;
    #                     else {
    #                         return a;
    #                     }
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 49))
    # 
    # def test_050(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     if(1 == 2) return a;
    #                     else {
    #                         return a;
    #                     }
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 50))
    # 
    # def test_051(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     if(1 == 2) {
    #                         a: string = "abc";
    #                     }
    #                     else {
    #                         a: integer = 6;
    #                     }
    #                     return a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 51))
    # 
    # def test_052(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     if(1 == 2) {
    #                         a: string = "abc";
    #                         b: integer;
    #                         return b;
    #                     }
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 52))
    # 
    # def test_053(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     for(a = 5, a < 10, a + 1) {
    #                         a: string = "abc";
    #                         return a;
    #                     }
    #                 }
    #             """
    #     expect = """Type mismatch in statement: ReturnStmt(Id(a))"""
    #     self.assertTrue(TestChecker.test(input, expect, 53))
    # 
    # def test_054(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     for(a = 5, a < 10, a + 1) {
    #                         a: string = "abc";
    #                         b: integer = 4;
    #                         return b;
    #                     }
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 54))
    # 
    # def test_055(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     while (a < 10) {
    #                         a: string = "abc";
    #                     }
    #                     return a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 55))
    # 
    # def test_056(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     while (a < 10) {      
    #                         if(a == 8) {
    #                             return 0;
    #                         }
    #                     }
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 56))
    # 
    # def test_057(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     while (a < 10) {      
    #                         if(a == 8) {
    #                             return a;
    #                         }
    #                         else {
    #                             b: integer = a + 1;
    #                             return b - 1;
    #                         }
    #                     }
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 57))
    # 
    # def test_058(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     while (a < 10) {      
    #                         b: auto = 5;
    #                         for(b = 10, b < 100, b + 2) 
    #                             return a;
    #                     }
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 58))
    # 
    # def test_059(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     do {
    #                         a: string = "abc";
    #                     } while(a < 10);
    #                     return a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 59))
    # 
    # def test_060(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     do {      
    #                         if(a == 8) {
    #                             return 0;
    #                         }
    #                     } while(a < 10);
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 60))
    # 
    # def test_061(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     do {      
    #                         if(a == 8) {
    #                             return a;
    #                         }
    #                         else {
    #                             b: integer = a + 1;
    #                             return b - 1;
    #                         }
    #                     } while (a < 10);
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 61))
    # 
    # def test_062(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     do {      
    #                         b: auto = 5;
    #                         for(b = 10, b < 100, b + 2) 
    #                             return a;
    #                     } while (a < 10);
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 62))
    # 
    # def test_063(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 10;
    #                     if(a == 10) {
    #                         continue;
    #                         return a;
    #                     }
    #                     else {
    #                         return a;
    #                     }
    #                 }
    #             """
    #     expect = """Must in loop: ContinueStmt()"""
    #     self.assertTrue(TestChecker.test(input, expect, 63))
    # 
    # def test_064(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     for(a = 5, a < 10, a + 1) {
    #                         continue;
    #                         a = a + 1;
    #                     }
    #                     return a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 64))
    # 
    # def test_065(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     for(a = 5, a < 10, a + 1) {
    #                         a = a + 1;
    #                         if(a > 7) {
    #                             continue;
    #                         }
    #                         break;
    #                     }
    #                     return a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 65))
    # 
    # def test_066(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     while (a < 10) {
    #                         continue;
    #                         a = a + 1;
    #                         break;
    #                     }
    #                     return a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 66))
    # 
    # def test_067(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     while (a < 10) {
    #                         a = a + 1;
    #                         if(a > 7) {
    #                             continue;
    #                         }
    #                         break;
    #                     }
    #                     return a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 67))
    # 
    # def test_068(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = 5;
    #                     do {
    #                         continue;
    #                         a = a + 1;
    #                         break;
    #                     } while (a < 10);
    #                     return a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 68))
    # 
    # def test_069(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function integer() {
    #                     a: integer = foo2() + foo3(5);
    #                     return a;
    #                 }
    #                 foo2: function integer() {
    #                     return 1;
    #                 }
    #                 foo3: function integer(a: integer) {
    #                     return a - 1;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 69))
    # 
    # def test_070(self):
    #     input = """
    #                 main: function void() {}
    #                 foo2: function integer() {
    #                     return foo();
    #                 }
    #                 foo: function integer() {
    #                     a: integer = foo2() + foo3(5);
    #                     return a;
    #                 }
    #                 foo3: function integer(a: integer) {
    #                     return a - 1;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 70))
    # 
    # def test_071(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function void(inherit a: integer) {}
    #                 foo2: function void(b: integer, b: float) inherit foo {
    #                     super(b);
    #                 }
    #             """
    #     expect = """Redeclared Parameter: b"""
    #     self.assertTrue(TestChecker.test(input, expect, 71))
    # 
    # def test_072(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function void(inherit a: integer) {}
    #                 foo2: function void(a: integer, b: float) inherit foo {
    #                     super(a);
    #                 }
    #             """
    #     expect = """Invalid Parameter: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 72))
    # 
    # def test_073(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function void(inherit a: float) {}
    #                 foo2: function void(b: integer) inherit foo {
    #                     super(b);
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 73))
    # 
    # def test_074(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function void(inherit a: integer) {}
    #                 foo2: function void(inherit b: string) inherit foo {
    #                     super(1);
    #                 }
    #                 foo3: function void(a: string) inherit foo2 {
    #                     preventDefault();
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 74))
    # 
    # def test_075(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function float(a: integer) {
    #                     b: array [2, 3] of float = {{1.0, 2.0, 2.5}, {7.1, 9.3, 10.2}};
    #                     return b[0,0] + b[1];
    #                 }
    #             """
    #     expect = """Type mismatch in expression: BinExpr(+, ArrayCell(b, [IntegerLit(0), IntegerLit(0)]), ArrayCell(b, [IntegerLit(1)]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 75))
    # 
    # def test_076(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function array [3] of float (a: integer) {
    #                     b: array [3, 2] of float = {{1.0, 2.0}, {4.8, 5.7}, {7.1, 9.3}};
    #                     return b[0];
    #                 }
    #             """
    #     expect = """Type mismatch in statement: ReturnStmt(ArrayCell(b, [IntegerLit(0)]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 76))
    # 
    # def test_077(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function array [2] of float (a: integer) {
    #                     b: array [3, 2] of float = {{1.0, 2.0}, {4.8, 5.7}, {7.1, 9.3}};
    #                     return b[0];
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 77))
    # 
    # def test_078(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function void () {
    #                     a: array[0] of string;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 78))
    # 
    # def test_079(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function array [3] of string () {
    #                     a: auto = {"a", "b", "c"};
    #                     return a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 79))
    # 
    # def test_080(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function array [3] of string () {
    #                     a: auto = {"a", "b", "c"};
    #                     b: array [3] of string = a;
    #                     c: array [2,3] of string = {a, b};
    #                     return a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 80))
    # 
    # def test_081(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function array [3] of string () {
    #                     a: auto = {"a", "b", "c"};
    #                     b: auto = a;
    #                     c: auto = {a, b};
    #                     d: auto = {c, {a, a}};
    #                     e: array [2,2,3] of string = d;
    #                     return a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 81))
    # 
    # def test_082(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function array [3] of string () {
    #                     a: auto = {"a", "b", "c"};
    #                     b: auto = a;
    #                     c: auto = {a, b};
    #                     d: auto = {c, {a, a}};
    #                     e: array [2,2,3] of string = d;
    #                     f: array [2,3] of string = e[2];
    #                     return a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 82))
    # 
    # def test_083(self):
    #     input = """
    #                 main: function void() {}
    # 
    #                 foo: function auto () {
    #                     a: auto = {f1(), "string"};
    #                     b: array [2] of string = a;
    #                     c: string = f1();
    #                 }
    # 
    #                 f1: function auto () {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 83))
    # 
    # def test_084(self):
    #     input = """
    #                 main: function void() {}
    #                 f1: function string () {
    #                     return "abc";
    #                 }
    #                 f3: function auto() {
    #                     return "Yoon Jae";
    #                 }
    # 
    #                 foo: function auto () {
    #                     a: auto = {f1(), "string"};
    #                     b: array [2] of string = a;
    #                     c: array [6] of string = { f1(), f2(), f3(), f4(), f5(), f6()};
    #                 }
    #                 f4: function auto() {}
    #                 f2: function string() {
    #                     return "Park Ji Bin the SK";
    #                 }
    #                 f5: function auto() {
    #                     return "Blind 2022";
    #                 }
    #                 f6: function auto() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 84))
    # 
    # def test_085(self):
    #     input = """
    #                 main: function void() {}
    #                 f1: function string () {
    #                     return "abc";
    #                 }
    #                 f3: function auto() {
    #                     return "Yoon Jae";
    #                 }
    # 
    #                 foo: function auto () {
    #                     a: auto = {f1(), "string"};
    #                     b: array [2] of string = a;
    #                     c: auto = { f1(), f2(), f3(), f4(), f5(), f6()};
    #                     d: array [6] of string = c;
    #                 }
    #                 f4: function auto() {}
    #                 f2: function string() {
    #                     return "Park Ji Bin the SK";
    #                 }
    #                 f5: function auto() {
    #                     return "Blind 2022";
    #                 }
    #                 f6: function auto() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 85))
    # 
    # def test_086(self):
    #     input = """
    #                 main: function void() {}
    #                 f1: function string () {
    #                     return "abc";
    #                 }
    #                 f3: function auto() {
    #                     return "Yoon Jae";
    #                 }
    #                 foo: function auto () {
    #                     a: auto = {f1(), "string"};
    #                     b: array [2] of string = a;
    #                     c: auto = ((f1() :: f2()) :: (f3() :: f4())) :: (f5() :: f6());
    #                     d: string = c;
    #                 }
    #                 f4: function auto() {}
    #                 f2: function string() {
    #                     return "Park Ji Bin the SK";
    #                 }
    #                 f5: function auto() {
    #                     return "Blind 2022";
    #                 }
    #                 f6: function auto() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 86))
    # 
    # def test_087(self):
    #     input = """
    #                 main: function void() {}
    # 
    #                 foo: function auto (a: auto) {
    #                     b: integer = a;
    #                     c: integer = f4();
    #                     d: integer = a % f4();
    #                 }
    # 
    #                 f4: function auto() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 87))
    # 
    # def test_088(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function auto (a: auto) {
    #                     b: integer;
    #                     b = a;
    #                     c: integer;
    #                     c = f4();
    #                     d: integer;
    #                     d = a % f4();
    #                 }
    #                 f4: function auto() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 88))
    # 
    # def test_089(self):
    #     input = """
    #                 main: function void() {}
    #                 f4: function auto() {}
    #                 foo: function integer (a: auto) {
    #                     return a;
    #                     b: integer = a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 89))
    # 
    # def test_090(self):
    #     input = """
    #                 main: function void() {}
    #                 f4: function auto() {}
    #                 foo: function auto (a: auto) {
    #                     return 1;
    #                     return a;
    #                     b: integer = a;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 90))
    # 
    # def test_091(self):
    #     input = """
    #                 main: function void() {}
    #                 f4: function void (a: auto, b: auto) {}
    #                 foo: function integer (x: auto) {
    #                     f4(1.0, "a");
    #                     f4(2, "a");
    #                     f4(x, "b");
    #                     f4("c", "d");
    #                 }
    #             """
    #     expect = """Type mismatch in expression: StringLit(c)"""
    #     self.assertTrue(TestChecker.test(input, expect, 91))
    # 
    # def test_092(self):
    #     input = """
    #                 main: function void() {}
    #                 f4: function void (a: auto, b: auto) {}
    #                 foo: function string (x: auto) {
    #                     c: integer;
    #                     foo(c);
    #                     return x;
    #                 }
    #             """
    #     expect = """Type mismatch in statement: ReturnStmt(Id(x))"""
    #     self.assertTrue(TestChecker.test(input, expect, 92))
    # 
    # def test_093(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function boolean (x: auto) {
    #                     c: boolean;
    #                     c = (foo(c) && foo(x)) || f4(c, "a");
    #                     return f4(x, f1());
    #                 }
    #                 f4: function auto (a: auto, b: auto) {}
    #                 f1: function string() {}
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 93))
    # 
    # def test_094(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function auto(a: auto, b: auto) {
    #                     if (b || b) {
    #                         return a :: "abc";
    #                     }
    #                     return 1;
    #                 }
    #             """
    #     expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
    #     self.assertTrue(TestChecker.test(input, expect, 94))
    # 
    # def test_095(self):
    #     input = """
    #                 main: function void() {}
    #                 foo: function auto(a: auto, b: auto) {
    #                     if (b || b) {
    #                         return a && b;
    #                     }
    #                     else {
    #                         c: boolean;
    #                         return b && c;
    #                     }
    #                     return a && b;
    #                 }
    #             """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 95))

    def test_096(self):
        input = """
                    f1: function void() {
                        return;
                    }
                    f2: function integer(inherit a: auto) {
                        return a + 1;
                    }
                    f3: function string(inherit b: string) inherit f2 {
                        preventDefault();
                        return b :: "abc";
                    }
                    f4: function auto(x: auto, y: auto) inherit f3 {
                        super(x);
                        y = 1;
                        return 1;
                    }
                    f9: function array [2] of integer(x: auto, y: auto) inherit f7 {
                        super(x);
                        y = 1;
                        return {y, f2(y)};
                    }
                    main: function void() {}
                    foo: function auto(arg: auto) {
                        a: auto = {f2(1), f6(2)};
                        b: array [2] of integer = a;
        
                        e: auto = f8("a", 1);
                        c: auto = f6(1) + e[0,0];
                        d: integer = c;
        
                        if (d == 5) {
                            return 1;
                        }
                        else {
                            return f6(5);
                        }
                        return f2(d);
                    }
                    f5: function float() {
                        return 0;
                    }
                    f6: function auto (inherit a: auto) {
                        return a + 1;
                    }
                    f7: function auto (inherit b: string) inherit f6 {
                        preventDefault();
                        return {b, "abc"};
                    }
                    f8: function array [1, 2] of integer(x: auto, y: auto) inherit f7 {
                        super(x);
                        y = 1;
                        return {{y, y}};
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 96))

    def test_097(self):
        input = """
                    main: function void() {}
                    a: integer;
                    f1: function string(a: auto) {
                        a = 1;
                        {
                            a: float;
                            {
                                a: string;
                                {
                                    return a;
                                }
                            }
                        }
                        return a;
                    }
                """
        expect = """Type mismatch in statement: ReturnStmt(Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 97))

    def test_098(self):
        input = """
                    main: function void() {
                        a: integer = readInteger();
                        printBoolean(isPrime(a));
                        return;
                    }
                    isPrime: function boolean(n: integer) {
                        if (n <= 2) {
                            return false;
                        }
                        i: integer = 2;
                        for (i = 2, i * i < n, i + 1) {
                            if (n % i == 0) {
                                return false;
                            }
                        }
                        return true;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 98))

    def test_099(self):
        input = """
                    gcd1: function auto(x: auto, y: auto) {
                        if ((x == 0) || (y == 0)) return x + y;
                        if (x > y) return gcd(y, x % y);
                        if (x < y) return gcd(x, y % x);
                    }
                    main: function void() {
                        a: integer = readInteger();
                        b: auto = readInteger();
                        printInteger(gcd1(a, b));
                        printInteger(gcd(a, b));
                    }
                    gcd: function auto(x: auto, y: auto) {
                        if ((x == 0) || (y == 0)) return x + y;
                        if (x > y) return gcd1(y, x % y);
                        if (x < y) return gcd1(x, y % x);
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 99))

    def test_100(self):
        input = """
                    main: function void() {}
                    f1: function auto(a: auto, b: auto) {
                        f2(1, "abc");
                    }
                    f2: function auto(a: auto, b: auto) {
                        f1(a, b);
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 100))

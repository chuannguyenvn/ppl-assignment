import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8051
    # def test_001(self):
    #     input = """
    #     foo: function void(a: float)
    #     {
    #         a  = 1;
    #     }
    # 
    #     bar: function void(a: auto, b: integer)
    #     {
    #         a = a + b;
    #     }
    # 
    #     main: function void()
    #     {
    #         foo(1);
    #         end: auto;
    #     }
    #     """
    #     expect = """Invalid Variable: end"""
    #     self.assertTrue(TestChecker.test(input, expect, 1))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8066
    # def test_002(self):
    #     input = """
    #     main: function void()
    #     {
    #         a: auto = 1.0 != 1.0;
    #     }
    #     """
    #     expect = """Type mismatch in expression: BinExpr(!=, FloatLit(1.0), FloatLit(1.0))"""
    #     self.assertTrue(TestChecker.test(input, expect, 2))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8057 (1)
    # def test_003(self):
    #     input = """
    #     main: function void()
    #     {
    #         a: integer = 5.4;
    #     }
    #     """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(5.4))"""
    #     self.assertTrue(TestChecker.test(input, expect, 3))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8057 (2)
    # def test_004(self):
    #     input = """
    #     main: function void()
    #     {
    #         a: integer;
    #         a = 5.4;
    #     }
    #     """
    #     expect = """Type mismatch in statement: AssignStmt(Id(a), FloatLit(5.4))"""
    #     self.assertTrue(TestChecker.test(input, expect, 4))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8083
    # def test_005(self):
    #     input = """
    #     main: function void()
    #     {
    #         return 1;
    #         end: auto;
    #     }
    #     """
    #     expect = """Invalid Variable: end"""
    #     self.assertTrue(TestChecker.test(input, expect, 5))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7989
    # def test_006(self):
    #     input = """
    #     foo: function void(out x: integer){}
    #     main: function void()
    #     {
    #         foo(2);
    #     }
    #     """
    #     expect = """Type mismatch in ?"""
    #     self.assertTrue(TestChecker.test(input, expect, 6))
    # 
    # def test_007(self):
    #     input = """
    #     foo: function void(out x: integer){}
    #     main: function void()
    #     {
    #         foo(2);
    #     }
    #     """
    #     expect = """Type mismatch in ?"""
    #     self.assertTrue(TestChecker.test(input, expect, 7))
    # 
    # # TODO: https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7991
    # def test_008(self):
    #     input = """
    #                 main: function void() {
    #                     a: integer = 1 + "float";
    #                 }
    #             """
    #     expect = """Type mismatch in expression: BinExpr(+, IntegerLit(1), StringLit(float))"""
    #     self.assertTrue(TestChecker.test(input, expect, 8))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8047
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9221
    # def test_009(self):
    #     input = """
    #     main: function void()
    #     {
    #         a: auto = 2 + 3.4;
    #         b: auto = 1 != true;
    #     }
    #     """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 9))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7988 (1)
    # def test_010(self):
    #     input = """
    #     y: auto = foo();
    #     foo: function integer(){}
    #     main: function void()
    #     {
    #         x = 5;
    #         x: integer;
    #     }
    #     """
    #     expect = """Undeclared Identifier: x"""
    #     self.assertTrue(TestChecker.test(input, expect, 10))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7988 (2)
    # def test_011(self):
    #     input = """
    #     x: auto = foo();
    #     foo: function integer(){}
    #     main: function void()
    #     {
    #         {
    #             x = 5;
    #         }
    #         x: integer;
    #     }
    #     """
    #     expect = """Undeclared Identifier: x"""
    #     self.assertTrue(TestChecker.test(input, expect, 11))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7988 (3)
    # def test_012(self):
    #     input = """
    #     x: auto = foo();
    #     foo: function integer(){}
    #     main: function void()
    #     {
    #         {
    #             x: integer;
    #         }
    #         x = 5;
    #     }
    #     """
    #     expect = """Undeclared Identifier: x"""
    #     self.assertTrue(TestChecker.test(input, expect, 12))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8110
    # def test_013(self):
    #     input = """
    #     main: function void()
    #     {
    #         x = 5;
    #     }
    #     x: auto = 1;
    #     """
    #     expect = """Undeclared Identifier: x"""
    #     self.assertTrue(TestChecker.test(input, expect, 13))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8149 (1)
    # def test_014(self):
    #     input = """
    #     a: function void (p : array [1] of integer) {}
    #     foo: function auto(){}
    #     bar: function auto(){}
    #     goo: function auto(){}
    #     gar: function auto(){}
    #     main: function void()
    #     {
    #         a({1});
    #         b: boolean = foo() == bar();
    #         c: float = goo() + gar();
    #     }
    #     """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 14))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8149 (2)
    # def test_015(self):
    #     input = """
    #     foo: function auto(){}
    #     bar: function auto(){}
    #     goo: function auto(){}
    #     main: function void()
    #     {
    #         a: auto = foo() + bar();
    #         b: integer = foo(); // ?
    #         c: auto = -goo();
    #         d: integer = goo(); // ?
    #     }
    #     """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 15))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8610
    # def test_016(self):
    #     input = """
    #     foo1: function auto(){}
    #     foo2: function auto(){}
    #     a: array [2] of integer = { foo1(), foo2() };
    #     b: integer = foo1();
    #     c: integer = foo2();
    #     main: function void(){}
    #     """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 16))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8106
    # def test_017(self):
    #     input = """
    #     foo: function void(a: auto) {}
    #     bar: function void(a: auto) inherit foo {}
    #     main: function void(){}
    #     """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 17))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7977
    # def test_018(self):
    #     input = """
    #     foo: function void(a: auto)
    #     {
    #         return 1;
    #     }
    #     main: function void(){}
    #     """
    #     expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""  # Hay k có lỗi do k duyệt body, tại hàm k đc gọi?
    #     self.assertTrue(TestChecker.test(input, expect, 18))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8098
    # def test_019(self):
    #     input = """
    #     main: function void()
    #     {
    #         // a: auto = {}; -> Not in testcases
    #         // a: array [0] of integer; -> Not in testcases
    #         a: array [5] of integer = {1, 2, 3};
    #     }
    #     """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 19))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8087
    # def test_020(self):
    #     input = """
    #     main: function void()
    #     {
    #         // a: auto = {}; -> Not in testcases
    #         // a: array [0] of integer; -> Not in testcases
    #         a: array [5] of integer = {1, 2, 3};
    #     }
    #     """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 20))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8399
    # def test_021(self):
    #     input = """
    #     main: function void()
    #     {
    #         a: auto = 1.5 < 2;
    #     }
    #     """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 21))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8317
    # def test_022(self):
    #     input = """
    #     foo: integer = 2;
    #     foo: function void () {}
    #     main: function void() {}
    #     """
    #     expect = """Redeclared Variable: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 22))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8170
    # def test_023(self):
    #     input = """
    #     foo: function auto() { return 10; }
    #     foo2: function void() { a: string = foo(); }
    #     main: function void() {}
    #     """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, FuncCall(foo, []))"""
    #     self.assertTrue(TestChecker.test(input, expect, 23))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8642
    # def test_024(self):
    #     input = """
    #     foo: function integer(inherit x: integer) inherit bar
    #     {
    #         super(2);
    #     }
    # 
    #     bar: function integer(inherit y: integer) inherit foo2
    #     {
    #         super("Hi");
    #     }
    # 
    #     foo2: function integer(inherit z: float){}
    #     """
    #     expect = """Type mismatch in expression: StringLit(Hi)"""
    #     self.assertTrue(TestChecker.test(input, expect, 24))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8646
    # def test_025(self):
    #     input = """
    #     a: float = foo(1, 2) + 1.5;
    #     foo: function auto(a: integer, b: integer)
    #     {
    #         return a + b;
    #     }
    #     b: float = foo(1, 2);
    #     main: function void(){}
    #     """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 25))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8657
    # def test_026(self):
    #     input = """
    #     a: integer = 2.3; //1
    #     b: auto; //2
    #     foo: function void(a: integer, b: float) {} //3
    #     bar: function void() inherit foo {} //4
    #     a: function void() {} //5
    #     main: function void(){}
    #     """
    #     expect = """Invalid Variable: b"""  # "trong khi duyệt sơ bộ mình không cần phải check Redeclared"
    #     self.assertTrue(TestChecker.test(input, expect, 26))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8660
    # def test_027(self):
    #     input = """
    #     x, y: integer = 1, foo(1, 2, 3);
    #     x, y: string;
    #     foo: function integer (x: integer, y: integer, x: integer){}
    #     main: function void(){}
    #     """
    #     expect = """Redeclared Variable: x"""
    #     self.assertTrue(TestChecker.test(input, expect, 27))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8679
    # def test_028(self):
    #     input = """
    #     x: function void() {}
    #     main: function void() inherit x
    #     {
    #         super();
    #     }
    #     """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input, expect, 28))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8703
    # def test_029(self):
    #     input = """
    #     x: auto = {4,5,6};
    #     y: auto = x[1,2];
    #     main: function void() {}
    #     """
    #     expect = """Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 29))
    # 
    # # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8839
    # def test_030(self):
    #     input = """
    #     a: auto = 1;
    #     main: function void()
    #     {
    #         b: auto = a();
    #     }
    #     """
    #     expect = """Undeclared Function: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 30))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8913
    def test_031(self):
        input = """
        a: array [1, 1] of boolean;
        foo: function auto(){}
        main: function void()
        {
            a[foo(), 1+4] = 222;
            b: integer = foo();
            end: auto;
        }
        """
        expect = """Invalid Variable: end"""
        self.assertTrue(TestChecker.test(input, expect, 31))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8943
    def test_032(self):
        input = """
        foo: function integer(){}
        a: auto = foo;
        main: function void()
        {
            a[foo(), 1 + 4] = 222;
            b: integer = foo();
        }
        """
        expect = """Undeclared Identifier: foo"""
        self.assertTrue(TestChecker.test(input, expect, 32))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8936
    def test_033(self):
        input = """
        foo: function auto(){}
        main: function void()
        {
            foo();
            a: boolean = foo();
            end: auto;
        }
        """
        expect = """Invalid Variable: end"""
        self.assertTrue(TestChecker.test(input, expect, 33))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8813 (1)
    def test_034(self):
        input = """
        x: function void (a: auto) {}
        main: function void()
        {
            x();
        }
        """
        expect = """Type mismatch in statement: CallStmt(x, )"""
        self.assertTrue(TestChecker.test(input, expect, 34))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8813 (2)
    def test_035(self):
        input = """
        x: function void (a: auto) {}
        main: function void()
        {
            x(1, 2);
        }
        """
        expect = """Type mismatch in statement: CallStmt(x, IntegerLit(1), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 35))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9108
    def test_036(self):
        input = """
        super: function integer(){}
        main: function void(){}
        """
        expect = """Redeclared Function: super"""
        self.assertTrue(TestChecker.test(input, expect, 36))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9055
    def test_037(self):
        input = """
        foo: function auto () {}
        foo: function auto (a: integer, b: integer ) inherit bar {}
        main: function void() {}
        """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 37))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9057
    def test_038(self):
        input = """
        a: integer = 1;
        foo: function void (b: integer) inherit a {}
        a: function string (inherit c: string) {}
        main: function void () {}
        """
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input, expect, 38))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9107
    def test_039(self):
        input = """
        a: string = 12 :: "str";
        main: function void() {}
        """
        expect = """Type mismatch in expression: BinExpr(::, IntegerLit(12), StringLit(str))"""
        self.assertTrue(TestChecker.test(input, expect, 39))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9036
    def test_040(self):
        input = """
        foo: function integer(a: string){}
        main: function void()
        {
            a: integer = foo();
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 40))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9113
    def test_041(self):
        input = """
        ?
        """
        expect = """ ? """
        self.assertTrue(TestChecker.test(input, expect, 41))
    # CONFLICTING
    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9117
    def test_042(self):
        input = """
        foo: function auto()
        {
            return 1;
            return true;
        }
        main: function void()
        {
            a: boolean = foo();
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 42))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9120
    def test_043(self):
        input = """
        main: function void() {}
        a: float = foo(1, 2) + 1.5;
        foo: function auto(a: integer, b: integer)
        {
            return a + b;
            end: auto;
        }
        """
        expect = """Invalid Variable: end"""
        self.assertTrue(TestChecker.test(input, expect, 43))

    # CONFLICTING
    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9122
    def test_044(self):
        input = """
        main: function void() {}
        foo: function auto(a: string, b: string)
        {
            return a::b;
        }
        a: float = foo("hello", "Hi");
        """
        expect = """Type mismatch in statement: Return(???)"""
        self.assertTrue(TestChecker.test(input, expect, 44))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8969 (1)
    def test_045(self):
        input = """
        main: function void() {}
        foo: function void (inherit a: integer, a: float) inherit bar {}
        """
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 45))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8969 (2)
    def test_046(self):
        input = """
        main: function void() {}
        bar: function void (inherit a: integer) {}
        foo: function void (a: integer) inherit bar
        {
            preventDefault();
            end: auto;
        }
        """
        expect = """Invalid Variable: end"""
        self.assertTrue(TestChecker.test(input, expect, 46))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9208
    def test_047(self):
        input = """
        main: function void() {}
        foo: function void(inherit a: auto)
        {
            a: auto = 1;
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 47))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9291 (1)
    def test_048(self):
        input = """
        main: function void() {}
        foo: function void (b: auto, c: auto)
        {
	        a: string = b + c;
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(+, Id(b), Id(c)))"""
        self.assertTrue(TestChecker.test(input, expect, 48))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9291 (2)
    def test_049(self):
        input = """
        main: function void() {}
        inc : function void (out n : integer, n: float) inherit foo
        {
            super(0.1, 1);
            n: string = 124;
        }
        foo : function auto (inherit n: float, b: integer){}
        """
        expect = """Redeclared Parameter: n"""
        self.assertTrue(TestChecker.test(input, expect, 49))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9146 (wrong)
    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9315
    def test_050(self):
        input = """
        a: auto;
        """
        expect = """Invalid Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 50))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9047
    def test_051(self):
        input = """
        main: function void()
        {
            x: auto = x + 10;
            y: integer = x;
            z: auto = z + z;
            w: string = z;
            t: string = z;
            u: integer = z;
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(u, IntegerType, Id(z))"""
        self.assertTrue(TestChecker.test(input, expect, 51))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9190
    def test_052(self):
        input = """
        main: function void()
        {
            a: integer;
            for (a = 1, 1, a + 1) {}
        }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(a), IntegerLit(1)), IntegerLit(1), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 52))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9192
    def test_053(self):
        input = """
        main: function void() {}
        foo: function string(foo: integer)
        {
            a: integer = foo;
            b: string = foo(a);
            c: auto;
        }
        """
        expect = """Invalid Variable: c"""
        self.assertTrue(TestChecker.test(input, expect, 53))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9354
    def test_054(self):
        input = """
        main: function void()
        {
            a = b;
        }
        """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 54))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9346
    def test_055(self):
        input = """
        main: function void() {}
        M: function void (a: integer) inherit N {}
        N: function void (inherit a: integer) {}
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 55))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9202
    def test_056(self):
        input = """
        main: function void() {}
        x: array [1,2,3] of integer;
        y: auto = x[2 < 3];
        """
        expect = """Type mismatch in expression: BinExpr(<, IntegerLit(2), IntegerLit(3))"""
        self.assertTrue(TestChecker.test(input, expect, 56))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9352
    def test_057(self):
        input = """
        main: function void() {}
        a: array[2] of integer = { {1}, {2} };
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2)])]))"""
        self.assertTrue(TestChecker.test(input, expect, 57))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9239
    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9258
    def test_058(self):
        input = """
        main: function void() {}
        a: array [2, 3, 2] of integer = {{{1, 2}, {1, 2}}, {{1, 2}, {1, "2"}, {1, 2}}};
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])]), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), StringLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])])"""
        self.assertTrue(TestChecker.test(input, expect, 58))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9258
    def test_059(self):
        input = """
        main: function void() {}
        a: auto = { {1 , 2}, { 1,1.5} };
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), FloatLit(1.5)])])"""
        self.assertTrue(TestChecker.test(input, expect, 59))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9390
    def test_060(self):
        input = """
        main: function void() {}
        foo: function auto() {}
        a: float = -foo();
        b: float = foo();
        c: integer = foo();
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 60))

    # CONFLICTING
    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9395
    def test_061(self):
        input = """
        test1 : function string(y : auto)
        {
            y = 2;
            return;
        }
        main: function void()
        {
            test1(true);
        }
        """
        expect = """Type mismatch in statement: Assign(Id(y), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 61))

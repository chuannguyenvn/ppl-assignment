import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8051
    def test_001(self):
        input = """
        foo: function void(a: float)
        {
            a  = 1;
        }

        bar: function void(a: auto, b: integer)
        {
            a = a + b;
        }

        main: function void()
        {
            foo(1);
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 1))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8066
    def test_002(self):
        input = """
        main: function void() 
        {
            a: auto = 1.0 != 1.0;
        }
        """
        expect = """Type mismatch in expression: BinExpr(!=, FloatLit(1.0), FloatLit(1.0))"""
        self.assertTrue(TestChecker.test(input, expect, 2))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8057 (1)
    def test_003(self):
        input = """
        main: function void()
        {
            a: integer = 5.4;
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(5.4))"""
        self.assertTrue(TestChecker.test(input, expect, 3))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8057 (2)
    def test_004(self):
        input = """
        main: function void()
        {
            a: integer;
            a = 5.4;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(a), FloatLit(5.4))"""
        self.assertTrue(TestChecker.test(input, expect, 4))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8083
    def test_005(self):
        input = """
        main: function void()
        {
            return 1;
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 5))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7989
    def test_006(self):
        input = """
        foo: function void(out x: int){}
        main: function void()
        {
            foo(2);
        }
        """
        expect = """Type mismatch in ?"""
        self.assertTrue(TestChecker.test(input, expect, 6))

    def test_007(self):
        input = """
        foo: function void(out x: int){}
        main: function void()
        {
            foo(2);
        }
        """
        expect = """Type mismatch in ?"""
        self.assertTrue(TestChecker.test(input, expect, 7))

    # TODO: https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7991
    def test_008(self):
        input = """
                    main: function void() {
                        a: integer = 1 + "float";
                    }
                """
        expect = """Type mismatch in expression: BinExpr(+, IntegerLit(1), StringLit(float))"""
        self.assertTrue(TestChecker.test(input, expect, 8))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8047
    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9221
    def test_009(self):
        input = """
        main: function void()
        {
            a: auto = 2 + 3.4;
            b: auto = 1 != true;
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 9))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7988 (1)
    def test_010(self):
        input = """
        x: auto = foo();
        foo: function integer(){}
        main: function void()
        {
            x = 5;
            x: integer;
        }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 10))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7988 (2)
    def test_011(self):
        input = """
        x: auto = foo();
        foo: function integer(){}
        main: function void()
        {
            {
                x = 5;
            }
            x: integer;
        }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 11))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7988 (3)
    def test_012(self):
        input = """
        x: auto = foo();
        foo: function integer(){}
        main: function void()
        {
            {
                x: integer;
            }
            x = 5;
        }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 12))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8110
    def test_013(self):
        input = """
        main: function void()
        {
            x = 5;
        }
        x: auto = 1;
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 13))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8149 (1)
    def test_014(self):
        input = """
        a: function void (p : array [1] of integer) {}
        foo: function auto(){}
        bar: function auto(){}
        goo: function auto(){}
        gar: function auto(){}
        main: function void()
        {
            a({1});
            b: boolean = foo() == bar();
            c: float = goo() + gar();
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 14))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8149 (2)
    def test_015(self):
        input = """
        foo: function auto(){}
        bar: function auto(){}
        goo: function auto(){}
        main: function void()
        {
            a: auto = foo() + bar();
            b: integer = foo(); // ?
            c: auto = -goo();
            d: integer = goo(); // ?
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 15))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8610
    def test_016(self):
        input = """
        foo1: function auto(){}
        foo2: function auto(){}
        a: array [2] of integer = { foo1(), foo2() };
        b: integer = foo1();
        c: integer = foo2();
        main: function void(){}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 16))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8106
    def test_017(self):
        input = """
        foo: function void(a: auto) {}
        bar: function void(a: auto) inherit foo {}
        main: function void(){}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 17))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7977
    def test_018(self):
        input = """
        foo: function void(a: auto)
        {
            return 1;
        }
        main: function void(){}
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""  # Hay k có lỗi do k duyệt body, tại hàm k đc gọi?
        self.assertTrue(TestChecker.test(input, expect, 18))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8098
    def test_019(self):
        input = """
        main: function void()
        {
            // a: auto = {}; -> Not in testcases
            // a: array [0] of integer; -> Not in testcases
            a: array [5] of integer = {1, 2, 3};
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 19))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8087
    def test_020(self):
        input = """
        main: function void()
        {
            // a: auto = {}; -> Not in testcases
            // a: array [0] of integer; -> Not in testcases
            a: array [5] of integer = {1, 2, 3};
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 20))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8399
    def test_021(self):
        input = """
        main: function void()
        {
            a: auto = 1.5 < 2;
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 21))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8317
    def test_022(self):
        input = """
        foo: integer = 2;
        foo: function void () {}
        main: function void() {}
        """
        expect = """Redeclared Variable: foo"""
        self.assertTrue(TestChecker.test(input, expect, 22))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8170
    def test_023(self):
        input = """
        foo: function auto() { return 10; }
        foo2: function void() { a: string = foo(); }
        main: function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 23))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8642
    def test_024(self):
        input = """
        foo: function integer(inherit x: integer) inherit bar
        {
            super(2);
        }

        bar: function integer(inherit y: integer) inherit foo2
        {
            super("Hi");
        }

        foo2: function integer(inherit z: float){}
        """
        expect = """Type mismatch in expression: StringLit(Hi)"""
        self.assertTrue(TestChecker.test(input, expect, 24))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8646
    def test_025(self):
        input = """
        a: float = foo(1, 2) + 1.5;
        foo: function auto(a: integer, b: integer)
        {
            return a + b;
        }
        b: float = foo(1, 2);
        main: function void(){}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 25))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8657
    def test_026(self):
        input = """
        a: integer = 2.3; //1
        b: auto; //2
        foo: function void(a: integer, b: float) {} //3
        bar: function void() inherit foo {} //4
        a: function void() {} //5
        main: function void(){}
        """
        expect = """Invalid Variable: b"""  # "trong khi duyệt sơ bộ mình không cần phải check Redeclared"
        self.assertTrue(TestChecker.test(input, expect, 26))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8660
    def test_027(self):
        input = """
        x, y: integer: 1, foo(1, 2, 3);
        x, y: string;
        foo: function integer (x: integer, y: integer, x:integer){}
        main: function void(){}
        """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 27))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8679
    def test_028(self):
        input = """
        x: function void() {}
        main: function void() inherit x
        {
            super();
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 28))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8703
    def test_029(self):
        input = """
        x: auto = {4,5,6};
        y: auto = x[1,2];
        main: function void() {}
        """
        expect = """Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 29))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8839
    def test_030(self):
        input = """
        a: auto = 1;
        main: function void()
        {
            b: auto = a();
        }
        """
        expect = """Undeclared Function: a"""
        self.assertTrue(TestChecker.test(input, expect, 30))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8913
    def test_031(self):
        input = """
        a: array [1, 1] of type boolean;
        foo: function auto(){}
        main: function void()
        {
            a[foo(), 1+4] = 222;
            b: integer = foo();
        }
        """
        expect = """[]"""
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
        }
        """
        expect = """[]"""
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
        foo: function auto (a: integer , b: integer ) inherit bar {}
        main: function void() {}
        """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 37))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9057
    def test_038(self):
        input = """
        a: integer = 1;
        foo: function void (integer b) inherit a {}
        a: function string (inherit string c) {}
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
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 43))

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
        expect = """Type mismatch in statement: Return()"""
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
        }
        """
        expect = """[]"""
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
        expect = """Type mismatch in Variable Declaration: u"""
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
        expect = """Type mismatch in expresison: 1"""
        self.assertTrue(TestChecker.test(input, expect, 52))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9192
    def test_053(self):
        input = """
        main: function void() {}
        foo: function string(foo: integer)
        {
            a: integer = foo;
            b: string = foo();
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
        expect = """Type mismatch in variable decl: c"""
        self.assertTrue(TestChecker.test(input, expect, 60))

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
        expect = """Type mismatch in statement: Assign(y, 2)"""
        self.assertTrue(TestChecker.test(input, expect, 61))

    def test_062(self):
        input = """
                    main: function void() {}
                    foo: function integer() {
                        a: integer = 5;
                        do {      
                            b: auto = 5;
                            for(b = 10, b < 100, b + 2) 
                                return a;
                        } while (a < 10);
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 62))

    def test_063(self):
        input = """
                    main: function void() {}
                    foo: function integer() {
                        a: integer = 10;
                        if(a == 10) {
                            continue;
                            return a;
                        }
                        else {
                            return a;
                        }
                    }
                """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 63))

    def test_064(self):
        input = """
                    main: function void() {}
                    foo: function integer() {
                        a: integer = 5;
                        for(a = 5, a < 10, a + 1) {
                            continue;
                            a = a + 1;
                        }
                        return a;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 64))

    def test_065(self):
        input = """
                    main: function void() {}
                    foo: function integer() {
                        a: integer = 5;
                        for(a = 5, a < 10, a + 1) {
                            a = a + 1;
                            if(a > 7) {
                                continue;
                            }
                            break;
                        }
                        return a;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 65))

    def test_066(self):
        input = """
                    main: function void() {}
                    foo: function integer() {
                        a: integer = 5;
                        while (a < 10) {
                            continue;
                            a = a + 1;
                            break;
                        }
                        return a;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 66))

    def test_067(self):
        input = """
                    main: function void() {}
                    foo: function integer() {
                        a: integer = 5;
                        while (a < 10) {
                            a = a + 1;
                            if(a > 7) {
                                continue;
                            }
                            break;
                        }
                        return a;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 67))

    def test_068(self):
        input = """
                    main: function void() {}
                    foo: function integer() {
                        a: integer = 5;
                        do {
                            continue;
                            a = a + 1;
                            break;
                        } while (a < 10);
                        return a;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 68))

    def test_069(self):
        input = """
                    main: function void() {}
                    foo: function integer() {
                        a: integer = foo2() + foo3(5);
                        return a;
                    }
                    foo2: function integer() {
                        return 1;
                    }
                    foo3: function integer(a: integer) {
                        return a - 1;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 69))

    def test_070(self):
        input = """
                    main: function void() {}
                    foo2: function integer() {
                        return foo();
                    }
                    foo: function integer() {
                        a: integer = foo2() + foo3(5);
                        return a;
                    }
                    foo3: function integer(a: integer) {
                        return a - 1;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 70))

    def test_071(self):
        input = """
                    main: function void() {}
                    foo: function void(inherit a: integer) {}
                    foo2: function void(b: integer, b: float) inherit foo {
                        super(b);
                    }
                """
        expect = """Redeclared Parameter: b"""
        self.assertTrue(TestChecker.test(input, expect, 71))

    def test_072(self):
        input = """
                    main: function void() {}
                    foo: function void(inherit a: integer) {}
                    foo2: function void(a: integer, b: float) inherit foo {
                        super(a);
                    }
                """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 72))

    def test_073(self):
        input = """
                    main: function void() {}
                    foo: function void(inherit a: float) {}
                    foo2: function void(b: integer) inherit foo {
                        super(b);
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 73))

    def test_074(self):
        input = """
                    main: function void() {}
                    foo: function void(inherit a: integer) {}
                    foo2: function void(inherit b: string) inherit foo {
                        super(1);
                    }
                    foo3: function void(a: string) inherit foo2 {
                        preventDefault();
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 74))

    def test_075(self):
        input = """
                    main: function void() {}
                    foo: function float(a: integer) {
                        b: array [2, 3] of float = {{1.0, 2.0, 2.5}, {7.1, 9.3, 10.2}};
                        return b[0,0] + b[1];
                    }
                """
        expect = """Type mismatch in expression: BinExpr(+, ArrayCell(b, [IntegerLit(0), IntegerLit(0)]), ArrayCell(b, [IntegerLit(1)]))"""
        self.assertTrue(TestChecker.test(input, expect, 75))

    def test_076(self):
        input = """
                    main: function void() {}
                    foo: function array [3] of float (a: integer) {
                        b: array [3, 2] of float = {{1.0, 2.0}, {4.8, 5.7}, {7.1, 9.3}};
                        return b[0];
                    }
                """
        expect = """Type mismatch in statement: ReturnStmt(ArrayCell(b, [IntegerLit(0)]))"""
        self.assertTrue(TestChecker.test(input, expect, 76))

    def test_077(self):
        input = """
                    main: function void() {}
                    foo: function array [2] of float (a: integer) {
                        b: array [3, 2] of float = {{1.0, 2.0}, {4.8, 5.7}, {7.1, 9.3}};
                        return b[0];
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 77))

    def test_078(self):
        input = """
                    main: function void() {}
                    foo: function void () {
                        a: array[0] of string;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 78))

    def test_079(self):
        input = """
                    main: function void() {}
                    foo: function array [3] of string () {
                        a: auto = {"a", "b", "c"};
                        return a;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 79))

    def test_080(self):
        input = """
                    main: function void() {}
                    foo: function array [3] of string () {
                        a: auto = {"a", "b", "c"};
                        b: array [3] of string = a;
                        c: array [2,3] of string = {a, b};
                        return a;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 80))

    def test_081(self):
        input = """
                    main: function void() {}
                    foo: function array [3] of string () {
                        a: auto = {"a", "b", "c"};
                        b: auto = a;
                        c: auto = {a, b};
                        d: auto = {c, {a, a}};
                        e: array [2,2,3] of string = d;
                        return a;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 81))

    def test_082(self):
        input = """
                    main: function void() {}
                    foo: function array [3] of string () {
                        a: auto = {"a", "b", "c"};
                        b: auto = a;
                        c: auto = {a, b};
                        d: auto = {c, {a, a}};
                        e: array [2,2,3] of string = d;
                        f: array [2,3] of string = e[2];
                        return a;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 82))

    def test_083(self):
        input = """
                    main: function void() {}

                    foo: function auto () {
                        a: auto = {f1(), "string"};
                        b: array [2] of string = a;
                        c: string = f1();
                    }

                    f1: function auto () {}
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 83))

    def test_084(self):
        input = """
                    main: function void() {}
                    f1: function string () {
                        return "abc";
                    }
                    f3: function auto() {
                        return "Yoon Jae";
                    }

                    foo: function auto () {
                        a: auto = {f1(), "string"};
                        b: array [2] of string = a;
                        c: array [6] of string = { f1(), f2(), f3(), f4(), f5(), f6()};
                    }
                    f4: function auto() {}
                    f2: function string() {
                        return "Park Ji Bin the SK";
                    }
                    f5: function auto() {
                        return "Blind 2022";
                    }
                    f6: function auto() {}
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 84))

    def test_085(self):
        input = """
                    main: function void() {}
                    f1: function string () {
                        return "abc";
                    }
                    f3: function auto() {
                        return "Yoon Jae";
                    }

                    foo: function auto () {
                        a: auto = {f1(), "string"};
                        b: array [2] of string = a;
                        c: auto = { f1(), f2(), f3(), f4(), f5(), f6()};
                        d: array [6] of string = c;
                    }
                    f4: function auto() {}
                    f2: function string() {
                        return "Park Ji Bin the SK";
                    }
                    f5: function auto() {
                        return "Blind 2022";
                    }
                    f6: function auto() {}
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 85))

    def test_086(self):
        input = """
                    main: function void() {}
                    f1: function string () {
                        return "abc";
                    }
                    f3: function auto() {
                        return "Yoon Jae";
                    }
                    foo: function auto () {
                        a: auto = {f1(), "string"};
                        b: array [2] of string = a;
                        c: auto = ((f1() :: f2()) :: (f3() :: f4())) :: (f5() :: f6());
                        d: string = c;
                    }
                    f4: function auto() {}
                    f2: function string() {
                        return "Park Ji Bin the SK";
                    }
                    f5: function auto() {
                        return "Blind 2022";
                    }
                    f6: function auto() {}
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 86))

    def test_087(self):
        input = """
                    main: function void() {}

                    foo: function auto (a: auto) {
                        b: integer = a;
                        c: integer = f4();
                        d: integer = a % f4();
                    }

                    f4: function auto() {}
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 87))

    def test_088(self):
        input = """
                    main: function void() {}
                    foo: function auto (a: auto) {
                        b: integer;
                        b = a;
                        c: integer;
                        c = f4();
                        d: integer;
                        d = a % f4();
                    }
                    f4: function auto() {}
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 88))

    def test_089(self):
        input = """
                    main: function void() {}
                    f4: function auto() {}
                    foo: function integer (a: auto) {
                        return a;
                        b: integer = a;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 89))

    def test_090(self):
        input = """
                    main: function void() {}
                    f4: function auto() {}
                    foo: function auto (a: auto) {
                        return 1;
                        return a;
                        b: integer = a;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 90))

    def test_091(self):
        input = """
                    main: function void() {}
                    f4: function void (a: auto, b: auto) {}
                    foo: function integer (x: auto) {
                        f4(1.0, "a");
                        f4(2, "a");
                        f4(x, "b");
                        f4("c", "d");
                    }
                """
        expect = """Type mismatch in expression: StringLit(c)"""
        self.assertTrue(TestChecker.test(input, expect, 91))

    def test_092(self):
        input = """
                    main: function void() {}
                    f4: function void (a: auto, b: auto) {}
                    foo: function string (x: auto) {
                        c: integer;
                        foo(c);
                        return x;
                    }
                """
        expect = """Type mismatch in statement: ReturnStmt(Id(x))"""
        self.assertTrue(TestChecker.test(input, expect, 92))

    def test_093(self):
        input = """
                    main: function void() {}
                    foo: function boolean (x: auto) {
                        c: boolean;
                        c = (foo(c) && foo(x)) || f4(c, "a");
                        return f4(x, f1());
                    }
                    f4: function auto (a: auto, b: auto) {}
                    f1: function string() {}
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 93))

    def test_094(self):
        input = """
                    main: function void() {}
                    foo: function auto(a: auto, b: auto) {
                        if (b || b) {
                            return a :: "abc";
                        }
                        return 1;
                    }
                """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 94))

    def test_095(self):
        input = """
                    main: function void() {}
                    foo: function auto(a: auto, b: auto) {
                        if (b || b) {
                            return a && b;
                        }
                        else {
                            c: boolean;
                            return b && c;
                        }
                        return a && b;
                    }
                """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 95))

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

import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        input="""main: function integer()\n{\n\n}"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input="""\n    // this is the main function\n    main: function void() // main function is a function that return a void object, which is an object originated from the void\n    { // curly brace denotes the start of the main function\n\t/* main function's main function is\n\tto do some main functions, which are functions\n\tthat main and typically appear in a main function */\n    } // another curly brace informs the function that this is its end\n    // that is all there is to it"""
        expect="""Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        input="""main: function integer()\n    {\n\ta = 1;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input="""\n    main: function integer()\n    {\n\ta = a;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), Id(a))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input="""\n    // this statement suggests that Tai is a meaningless person (void), and everything he said is of utmost untrustworthy (false)\n    Tai /* there is just about a million people with the name "Tai", therefore I deny any personal attack accusation */ : boolean = false; // this statement is also a valid statement, which means it is factual"""
        expect="""Program([\n\tVarDecl(Tai, BooleanType, BooleanLit(False))\n])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input="""\n    a: integer = true || false && true || (!false);"""
        expect="""Program([\n\tVarDecl(a, IntegerType, BinExpr(||, BinExpr(&&, BinExpr(||, BooleanLit(True), BooleanLit(False)), BooleanLit(True)), UnExpr(!, BooleanLit(False))))\n])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input="""\n    main: function integer()\n    {\n\ta = 1 + true * "false" - !((true) + 0.69);\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(+, IntegerLit(1), BinExpr(*, BooleanLit(True), StringLit(false))), UnExpr(!, BinExpr(+, BooleanLit(True), FloatLit(0.69)))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input="""\n    main: function integer()\n    {\n\ta = foo();\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), FuncCall(foo, []))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input="""\n    main: function integer()\n    {\n\ta = foo(1);\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), FuncCall(foo, [IntegerLit(1)]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input="""\n    main: function integer()\n    {\n\ta = foo(((1)));\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), FuncCall(foo, [IntegerLit(1)]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        input="""\n    main: function integer()\n    {\n\ta = foo(foo());\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), FuncCall(foo, [FuncCall(foo, [])]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input="""\n    main: function integer()\n    {\n\ta = {1, 2, 3};\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input="""\n    main: function integer()\n    {\n\ta = {(1), 2 + 3, foo(4), "asdf"};\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(1), BinExpr(+, IntegerLit(2), IntegerLit(3)), FuncCall(foo, [IntegerLit(4)]), StringLit(asdf)]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input="""\n    main: function integer()\n    {\n\ta = 123_456_789;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(123456789))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input="""\n    main: function integer()\n    {\n\ta : array [3] of integer = {1, 2, 3};\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input="""\n    main: function integer()\n    {\n\ta, b, c : array [0, 1, 2, 3, 4] of string;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(a, ArrayType([0, 1, 2, 3, 4], StringType)), VarDecl(b, ArrayType([0, 1, 2, 3, 4], StringType)), VarDecl(c, ArrayType([0, 1, 2, 3, 4], StringType))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input="""\n    main: function integer()\n    {\n\ta, b, c : array [0] of string = 1, 2, 3;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(a, ArrayType([0], StringType), IntegerLit(1)), VarDecl(b, ArrayType([0], StringType), IntegerLit(2)), VarDecl(c, ArrayType([0], StringType), IntegerLit(3))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input="""\n    main: function integer()\n    {\n\tif (1 > 2) a = 1;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(1), IntegerLit(2)), AssignStmt(Id(a), IntegerLit(1)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input="""\n    main: function integer()\n    {\n\tif (1 > 2) foo();\n\telse bar();\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(1), IntegerLit(2)), CallStmt(foo, ), CallStmt(bar, ))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input="""\n    main: function integer()\n    {\n\tif (1 > 2) if (2 > 3) if (3 > 4) if (4 > 5) foo();\n\telse bar();\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(1), IntegerLit(2)), IfStmt(BinExpr(>, IntegerLit(2), IntegerLit(3)), IfStmt(BinExpr(>, IntegerLit(3), IntegerLit(4)), IfStmt(BinExpr(>, IntegerLit(4), IntegerLit(5)), CallStmt(foo, ), CallStmt(bar, )))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input="""\n    main: function integer()\n    {\n\tif (1 > 2) foo(); else if (1 < 2) bar(); else goo();\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(1), IntegerLit(2)), CallStmt(foo, ), IfStmt(BinExpr(<, IntegerLit(1), IntegerLit(2)), CallStmt(bar, ), CallStmt(goo, )))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input="""\n    main: function integer()\n    {\n\tfor (i = 1, i < 10, i + 1) foo();\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(foo, ))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input="""\n    main: function integer()\n    {\n\tfor (i = foo(), foo(), foo()) foo();\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), FuncCall(foo, [])), FuncCall(foo, []), FuncCall(foo, []), CallStmt(foo, ))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input="""\n    main: function integer()\n    {\n\tfor (i = 1, i < 10, i + 1)\n\tfor (j = 1, j > 10, j + foo())\n\tfoo();\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(>, Id(j), IntegerLit(10)), BinExpr(+, Id(j), FuncCall(foo, [])), CallStmt(foo, )))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input="""\n    main: function integer()\n    {\n\tfor (i = 1, i < 10, i + 1) if (true) while (false) return;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BooleanLit(True), WhileStmt(BooleanLit(False), ReturnStmt())))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_326(self):
        input="""\n    main: function integer()\n    {\n\tfor (i = 1, i < 10, i + 1) continue;\n\tcontinue;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), ContinueStmt()), ContinueStmt()]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input="""\n    main: function integer()\n    {\n\twhile (1) {}\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([WhileStmt(IntegerLit(1), BlockStmt([]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
        input="""\n    main: function integer()\n    {\n\twhile (1) foo();\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([WhileStmt(IntegerLit(1), CallStmt(foo, ))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
        input="""\n    main: function integer()\n    {\n\twhile (1) while(a) while(foo()) while ("abc") continue;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([WhileStmt(IntegerLit(1), WhileStmt(Id(a), WhileStmt(FuncCall(foo, []), WhileStmt(StringLit(abc), ContinueStmt()))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
        input="""\n    main: function integer()\n    {\n\tdo {} while (a);\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([DoWhileStmt(Id(a), BlockStmt([]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
        input="""\n    main: function integer()\n    {\n\tdo {do {do {do {} while(a);} while(a);} while(a);} while (a);\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([DoWhileStmt(Id(a), BlockStmt([DoWhileStmt(Id(a), BlockStmt([DoWhileStmt(Id(a), BlockStmt([DoWhileStmt(Id(a), BlockStmt([]))]))]))]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
        input="""\n    main: function integer()\n    {\n\tdo {drug();} while (withdrawing());\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([DoWhileStmt(FuncCall(withdrawing, []), BlockStmt([CallStmt(drug, )]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        input="""\n    main: function integer()\n    {\n\tdo {drug();} while (withdrawing());\n    }"""
        expect="""Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([DoWhileStmt(FuncCall(withdrawing, []), BlockStmt([CallStmt(drug, )]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input="""\n    main: function integer()\n    {\n\tdo {break; continue; return;} while (1);\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([DoWhileStmt(IntegerLit(1), BlockStmt([BreakStmt(), ContinueStmt(), ReturnStmt()]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
        input="""\n    main: function integer()\n    {\n\tbreak;\n\tcontinue;\n\treturn;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([BreakStmt(), ContinueStmt(), ReturnStmt()]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_336(self):
        input="""\n    main: function integer()\n    {\n\tcall(me, maybe);\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([CallStmt(call, Id(me), Id(maybe))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
        input="""\n    main: function integer()\n    {\n\tfractal(69, fractal(69, fractal(69, fractal(69, fractal()))));\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([CallStmt(fractal, IntegerLit(69), FuncCall(fractal, [IntegerLit(69), FuncCall(fractal, [IntegerLit(69), FuncCall(fractal, [IntegerLit(69), FuncCall(fractal, [])])])]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_338(self):
        input="""\n    main: function integer()\n    {\n\t_1();\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([CallStmt(_1, )]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
        input="""\n    main: function integer()\n    {\n\t_1();\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([CallStmt(_1, )]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        input="""\n    main: function integer()\n    {\n\t{}{}{}{}\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([])]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
        input="""\n    main: function integer()\n    {\n\t{}{}{{}}{{{}{}{{}}}}{}{{}}{{}{}}\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([BlockStmt([]), BlockStmt([]), BlockStmt([BlockStmt([])]), BlockStmt([BlockStmt([BlockStmt([]), BlockStmt([]), BlockStmt([BlockStmt([])])])]), BlockStmt([]), BlockStmt([BlockStmt([])]), BlockStmt([BlockStmt([]), BlockStmt([])])]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_342(self):
        input="""\n    main: function integer()\n    {\n\ta, b, c, d: string;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(a, StringType), VarDecl(b, StringType), VarDecl(c, StringType), VarDecl(d, StringType)]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_343(self):
        input="""\n    main: function integer()\n    {\n\ta, b, c, d: auto;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(a, AutoType), VarDecl(b, AutoType), VarDecl(c, AutoType), VarDecl(d, AutoType)]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_344(self):
        input="""\n    main: function integer()\n    {\n\ta: float = true;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(a, FloatType, BooleanLit(True))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
        input="""\n    main: function integer()\n    {\n\ta, b: float = c, d;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(a, FloatType, Id(c)), VarDecl(b, FloatType, Id(d))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_346(self):
        input="""\n    a: integer = "yo";\n    b: string = main();\n    c: float = true :: false; """
        expect="""Program([\n\tVarDecl(a, IntegerType, StringLit(yo))\n\tVarDecl(b, StringType, FuncCall(main, []))\n\tVarDecl(c, FloatType, BinExpr(::, BooleanLit(True), BooleanLit(False)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
        input="""\n    main: integer = -69;\n    main: function integer() { }\n    main: function void() { main: integer = -main(!69);}"""
        expect="""Program([\n\tVarDecl(main, IntegerType, UnExpr(-, IntegerLit(69)))\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([]))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(main, IntegerType, UnExpr(-, FuncCall(main, [UnExpr(!, IntegerLit(69))])))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
        input="""\n    main: function integer()\n    {\n\ta = (1 + 2 * 3 - 4) / (5 % 6) + 7 - (8) % 9 / 0;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(+, BinExpr(/, BinExpr(-, BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(2), IntegerLit(3))), IntegerLit(4)), BinExpr(%, IntegerLit(5), IntegerLit(6))), IntegerLit(7)), BinExpr(/, BinExpr(%, IntegerLit(8), IntegerLit(9)), IntegerLit(0))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
        input="""\n    main: function integer()\n    {\n\ta = ---------------"minus";\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, StringLit(minus)))))))))))))))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
        input="""\n    main: function integer()\n    {\n\ta = 1.001 ---("two" / --3) + four(-5) % six + 7 % 8 * nine(-0.000);\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, BinExpr(-, FloatLit(1.001), UnExpr(-, UnExpr(-, BinExpr(/, StringLit(two), UnExpr(-, UnExpr(-, IntegerLit(3))))))), BinExpr(%, FuncCall(four, [UnExpr(-, IntegerLit(5))]), Id(six))), BinExpr(*, BinExpr(%, IntegerLit(7), IntegerLit(8)), FuncCall(nine, [UnExpr(-, FloatLit(0.0))]))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_351(self):
        input="""\n    main: function integer()\n    {\n\ta = true + false * "yo" / yo % 1_2_3_4_5;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BooleanLit(True), BinExpr(%, BinExpr(/, BinExpr(*, BooleanLit(False), StringLit(yo)), Id(yo)), IntegerLit(12345))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
        input="""\n    main: function integer()\n    {\n\ta = !wtf;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), UnExpr(!, Id(wtf)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
        input="""\n    main: function integer()\n    {\n\ta = !!!!!!!!wtf;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, Id(wtf))))))))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
        input="""\n    main: function integer()\n    {\n\ta = !(!(!(!(!(wtf)))));\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, Id(wtf)))))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_355(self):
        input="""\n    main: function integer()\n    {\n\ta = !hey && !hey || !hey;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BinExpr(&&, UnExpr(!, Id(hey)), UnExpr(!, Id(hey))), UnExpr(!, Id(hey))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
        input="""main: function integer()\n    {\n\ta = !true || false && "true" || !(foo && !!bar);\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BinExpr(&&, BinExpr(||, UnExpr(!, BooleanLit(True)), BooleanLit(False)), StringLit(true)), UnExpr(!, BinExpr(&&, Id(foo), UnExpr(!, UnExpr(!, Id(bar)))))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
        input="""main: function integer()\n    {\n\ta = "my heart" :: "your heart";\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, StringLit(my heart), StringLit(your heart)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
        input="""main: function integer()\n    {\n\ta = ("i love" :: "eating babies") :: "' powdered milk";\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, BinExpr(::, StringLit(i love), StringLit(eating babies)), StringLit(' powdered milk)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
        input="""main: function integer()\n    {\n\ta = ((1 == 2) != 3) < (4 > ((5 <= 6) >= 7));\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(<, BinExpr(!=, BinExpr(==, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr(>, IntegerLit(4), BinExpr(>=, BinExpr(<=, IntegerLit(5), IntegerLit(6)), IntegerLit(7)))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
        input="""main: function integer()\n    {\n\ta = 1 < ("two" >= three(four(5.6, 7 != true)));\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(<, IntegerLit(1), BinExpr(>=, StringLit(two), FuncCall(three, [FuncCall(four, [FloatLit(5.6), BinExpr(!=, IntegerLit(7), BooleanLit(True))])]))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
        input="""main: function integer()\n    {\n\ta = a[0];\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(a, [IntegerLit(0)]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
        input="""main: function integer()\n    {\n\ta = -a[-1];\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), UnExpr(-, ArrayCell(a, [UnExpr(-, IntegerLit(1))])))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input="""main: function integer()\n    {\n\ta = a[one, a[2], a["3"], _1[4 > 5, 6 < 7], _8(nine[0])];\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(a, [Id(one), ArrayCell(a, [IntegerLit(2)]), ArrayCell(a, [StringLit(3)]), ArrayCell(_1, [BinExpr(>, IntegerLit(4), IntegerLit(5)), BinExpr(<, IntegerLit(6), IntegerLit(7))]), FuncCall(_8, [ArrayCell(nine, [IntegerLit(0)])])]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
        input="""main: function integer()\n    {\n\ta = a[a(a[a(a[a()])])];\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(a, [FuncCall(a, [ArrayCell(a, [FuncCall(a, [ArrayCell(a, [FuncCall(a, [])])])])])]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
        input="""main: function integer()\n    {\n\ta = 1 < ("two" >= three + (four(5.6, 7 != true)));\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(<, IntegerLit(1), BinExpr(>=, StringLit(two), BinExpr(+, Id(three), FuncCall(four, [FloatLit(5.6), BinExpr(!=, IntegerLit(7), BooleanLit(True))])))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_366(self):
        input="""\n    main: function integer()\n    {\n\tzero = 1 * 2 + 3 || 4 % five[6] + seven(8, nine[10, 11, twelve[13] && 14]) % 15 == 16 :: (true);\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(zero), BinExpr(::, BinExpr(==, BinExpr(||, BinExpr(+, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr(+, BinExpr(%, IntegerLit(4), ArrayCell(five, [IntegerLit(6)])), BinExpr(%, FuncCall(seven, [IntegerLit(8), ArrayCell(nine, [IntegerLit(10), IntegerLit(11), BinExpr(&&, ArrayCell(twelve, [IntegerLit(13)]), IntegerLit(14))])]), IntegerLit(15)))), IntegerLit(16)), BooleanLit(True)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_367(self):
        input="""\n    main: function integer()\n    {\n\tarr[0] = 1;\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(0)]), IntegerLit(1))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
        input="""\n    main: function integer()\n    {\n\tfor (arr[0] = 1, arr[arr[0]] != 1, arr[arr[arr[0]]] + 1) { }\n    }"""
        expect="""Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(arr, [IntegerLit(0)]), IntegerLit(1)), BinExpr(!=, ArrayCell(arr, [ArrayCell(arr, [IntegerLit(0)])]), IntegerLit(1)), BinExpr(+, ArrayCell(arr, [ArrayCell(arr, [ArrayCell(arr, [IntegerLit(0)])])]), IntegerLit(1)), BlockStmt([]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
        input="""\n    arr: integer = { };\n    """
        expect="""Program([\n\tVarDecl(arr, IntegerType, ArrayLit([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
        input="""\n    arr: function array[0] of integer (arr: array[0, 0, 0] of string) { }\n    """
        expect="""Program([\n\tFuncDecl(arr, ArrayType([0], IntegerType), [Param(arr, ArrayType([0, 0, 0], StringType))], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input="""\n    main: function void ()\n    {\n\tbreak;\n\tcontinue;\n    }\n    """
        expect="""Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([BreakStmt(), ContinueStmt()]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
        input="""\n    main: function void ()\n    {\n\treturn 1;\n    }\n    """
        expect="""Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(IntegerLit(1))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
        input="""\n    main: function void ()\n    {\n\treturn main;\n    }\n    """
        expect="""Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(Id(main))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input="""\n    main: function void ()\n    {\n\treturn;\n    }\n    """
        expect="""Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
        input="""\n    main: function void ()\n    {\n\treturn a[0];\n    }\n    """
        expect="""Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(0)]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input="""\n    main: function void ()\n    {\n\treturn a[/* hey */0];\n    }\n    """
        expect="""Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(0)]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input="""\n    main: function void ()\n    {\n\treturn a[-1];\n    }\n    """
        expect="""Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(ArrayCell(a, [UnExpr(-, IntegerLit(1))]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input="""main: function void()
        {
            f = 12_34.567+e89;
            if (expr1) 
                if (expr2) 
                    stmt1();
                else 
                    stmt2();
        }"""
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(f), BinExpr(+, FloatLit(1234.567), Id(e89))), IfStmt(Id(expr1), IfStmt(Id(expr2), CallStmt(stmt1, ), CallStmt(stmt2, )))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
        input="""a, b, c, d: float = 1.0, 2.0, 3.0, 4.0;\ne, f: integer = 5, 6;\ng, h, i: string = "abc", "def", "ghi";"""
        expect="""Program([
	VarDecl(a, FloatType, FloatLit(1.0))
	VarDecl(b, FloatType, FloatLit(2.0))
	VarDecl(c, FloatType, FloatLit(3.0))
	VarDecl(d, FloatType, FloatLit(4.0))
	VarDecl(e, IntegerType, IntegerLit(5))
	VarDecl(f, IntegerType, IntegerLit(6))
	VarDecl(g, StringType, StringLit(abc))
	VarDecl(h, StringType, StringLit(def))
	VarDecl(i, StringType, StringLit(ghi))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
        input="""main: function auto(a: float, out b: string, inherit c: integer, inherit out d: array [0,  0] of float)\n{\na: integer;\nb, c, d: string;\ne, f, g, h: float = "a", b, 1.2e2, c[1,2,3];\n}"""
        expect="""Program([
	FuncDecl(main, AutoType, [Param(a, FloatType), OutParam(b, StringType), InheritParam(c, IntegerType), InheritOutParam(d, ArrayType([0, 0], FloatType))], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, StringType), VarDecl(c, StringType), VarDecl(d, StringType), VarDecl(e, FloatType, StringLit(a)), VarDecl(f, FloatType, Id(b)), VarDecl(g, FloatType, FloatLit(120.0)), VarDecl(h, FloatType, ArrayCell(c, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input="""a: integer = 10.0;"""
        expect="""Program([
	VarDecl(a, IntegerType, FloatLit(10.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input="""b: float = "c";"""
        expect="""Program([\n\tVarDecl(b, FloatType, StringLit(c))\n])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        input="""a, a, a, a: array [1,2,3,4,5] of float;"""
        expect="""Program([
	VarDecl(a, ArrayType([1, 2, 3, 4, 5], FloatType))
	VarDecl(a, ArrayType([1, 2, 3, 4, 5], FloatType))
	VarDecl(a, ArrayType([1, 2, 3, 4, 5], FloatType))
	VarDecl(a, ArrayType([1, 2, 3, 4, 5], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input="""call: integer = call(1,2,3,4);"""
        expect="""Program([
	VarDecl(call, IntegerType, FuncCall(call, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
        input="""main: integer = foo(foo(foo()));"""
        expect="""Program([\n\tVarDecl(main, IntegerType, FuncCall(foo, [FuncCall(foo, [FuncCall(foo, [])])]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_386(self):
        input="""main: function void(){}"""
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
        input="""a: integer = a / b :: c - d / e && f - g + !(h - k) % - j[--q, ((a >= b) / - c), 1 + "\\n2"]; """
        expect="""Program([
	VarDecl(a, IntegerType, BinExpr(::, BinExpr(/, Id(a), Id(b)), BinExpr(&&, BinExpr(-, Id(c), BinExpr(/, Id(d), Id(e))), BinExpr(+, BinExpr(-, Id(f), Id(g)), BinExpr(%, UnExpr(!, BinExpr(-, Id(h), Id(k))), UnExpr(-, ArrayCell(j, [UnExpr(-, UnExpr(-, Id(q))), BinExpr(/, BinExpr(>=, Id(a), Id(b)), UnExpr(-, Id(c))), BinExpr(+, IntegerLit(1), StringLit(\\n2))])))))))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_388(self):
        input="""main: function auto()
        { 
        if (a) 
            if (b)
                c();
            else 
                d();
            if (e) 
                f();
                if (g)
                    h();
                    else i();
        }
        """
        expect="""Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([IfStmt(Id(a), IfStmt(Id(b), CallStmt(c, ), CallStmt(d, ))), IfStmt(Id(e), CallStmt(f, )), IfStmt(Id(g), CallStmt(h, ), CallStmt(i, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input="""main: function array [0] of integer()
        {
            while(true) 
                while(True) 
                    do 
                    {
                        something();
                        a, b, c, d, e: auto;
                    }
                    while (false);
        }"""
        expect="""Program([
	FuncDecl(main, ArrayType([0], IntegerType), [], None, BlockStmt([WhileStmt(BooleanLit(True), WhileStmt(Id(True), DoWhileStmt(BooleanLit(False), BlockStmt([CallStmt(something, ), VarDecl(a, AutoType), VarDecl(b, AutoType), VarDecl(c, AutoType), VarDecl(d, AutoType), VarDecl(e, AutoType)]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input="""main: function array [0] of integer()
        {
            while(true)
            {
                do
                {
                    something();
                }
                while (something());
            }
        }"""
        expect="""Program([
	FuncDecl(main, ArrayType([0], IntegerType), [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([DoWhileStmt(FuncCall(something, []), BlockStmt([CallStmt(something, )]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input="""main: function array [0] of boolean()
        {
            while (true) 
                if (false == False) 
                    do {something();} 
                    while (false); 
                else False();
        }"""
        expect="""Program([
	FuncDecl(main, ArrayType([0], BooleanType), [], None, BlockStmt([WhileStmt(BooleanLit(True), IfStmt(BinExpr(==, BooleanLit(False), Id(False)), DoWhileStmt(BooleanLit(False), BlockStmt([CallStmt(something, )])), CallStmt(False, )))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input="""main: function array [0,1,2,3] of boolean()
        {
            for (i = 1, 1, 1) break;
        }"""
        expect="""Program([
	FuncDecl(main, ArrayType([0, 1, 2, 3], BooleanType), [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), IntegerLit(1), IntegerLit(1), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input="""main: function void()
        {
            for (a[1,2,3,4,5] = 1, call(), call())
                for (a = "asdf", a, "a")
                {
                    if (a)
                    {
                        while ("c") d = "d";
                    }
                    else b();
                }
        }"""
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]), IntegerLit(1)), FuncCall(call, []), FuncCall(call, []), ForStmt(AssignStmt(Id(a), StringLit(asdf)), Id(a), StringLit(a), BlockStmt([IfStmt(Id(a), BlockStmt([WhileStmt(StringLit(c), AssignStmt(Id(d), StringLit(d)))]), CallStmt(b, ))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input="""a: string = "\\n";"""
        expect="""Program([
	VarDecl(a, StringType, StringLit(\\n))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input="""main: function void()
        {
            break;
            continue;
            return;
            return 1;
            return a[1];
            return "a";
            return "for";
        }"""
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BreakStmt(), ContinueStmt(), ReturnStmt(), ReturnStmt(IntegerLit(1)), ReturnStmt(ArrayCell(a, [IntegerLit(1)])), ReturnStmt(StringLit(a)), ReturnStmt(StringLit(for))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input="""
        main: function void() inherit main {}
        main2: function integer() {} 
        main3: integer; 
        main4: function auto() inherit some_thing {}
        main5: auto = 1;
        main6, main7: auto;
        main8: function auto(a: auto) {}"""
        expect="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([]))
	FuncDecl(main2, IntegerType, [], None, BlockStmt([]))
	VarDecl(main3, IntegerType)
	FuncDecl(main4, AutoType, [], some_thing, BlockStmt([]))
	VarDecl(main5, AutoType, IntegerLit(1))
	VarDecl(main6, AutoType)
	VarDecl(main7, AutoType)
	FuncDecl(main8, AutoType, [Param(a, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input="""global1, global2: integer = 1, 2;
        main: function void(out a: integer)
        {
            for (i = i + 1 / 2 * "3" - 4 || 5, a[foo(), bar(a[0, 0]), foo], rec(rec(rec))))
                if (1 == (2 || (3 + 4) / 5 + ((6 - 7) >= -8)) :: 9)
                    break;
                else continue;
                while (a() :: "b")
                    return c;
                return;
                do {return;}
                while (a[-1]);
                while (a) {}
                do {} while (a);
                call();
                call(1,2,3,4,5,6,7,8,9,0);
                
            for (a = b, c, d)
            {
            
            }
            
            if (true)
                for (a = b, c, d)
                {
                
                }
        }
        """
        expect="""Program([
	VarDecl(global1, IntegerType, IntegerLit(1))
	VarDecl(global2, IntegerType, IntegerLit(2))
	FuncDecl(main, VoidType, [OutParam(a, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(||, BinExpr(-, BinExpr(+, Id(i), BinExpr(*, BinExpr(/, IntegerLit(1), IntegerLit(2)), StringLit(3))), IntegerLit(4)), IntegerLit(5))), ArrayCell(a, [FuncCall(foo, []), FuncCall(bar, [ArrayCell(a, [IntegerLit(0), IntegerLit(0)])]), Id(foo)]), FuncCall(rec, [FuncCall(rec, [Id(rec)])]), IfStmt(BinExpr(::, BinExpr(==, IntegerLit(1), BinExpr(||, IntegerLit(2), BinExpr(+, BinExpr(/, BinExpr(+, IntegerLit(3), IntegerLit(4)), IntegerLit(5)), BinExpr(>=, BinExpr(-, IntegerLit(6), IntegerLit(7)), UnExpr(-, IntegerLit(8)))))), IntegerLit(9)), BreakStmt(), ContinueStmt())), WhileStmt(BinExpr(::, FuncCall(a, []), StringLit(b)), ReturnStmt(Id(c))), ReturnStmt(), DoWhileStmt(ArrayCell(a, [UnExpr(-, IntegerLit(1))]), BlockStmt([ReturnStmt()])), WhileStmt(Id(a), BlockStmt([])), DoWhileStmt(Id(a), BlockStmt([])), CallStmt(call, ), CallStmt(call, IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(0)), ForStmt(AssignStmt(Id(a), Id(b)), Id(c), Id(d), BlockStmt([])), IfStmt(BooleanLit(True), ForStmt(AssignStmt(Id(a), Id(b)), Id(c), Id(d), BlockStmt([])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input="""ex :  function  float  (  inherit  out kI :  boolean  ,  inherit  out Q :  string  )  inherit Nd3w 
        { MPf :  array  [ 7_8_123 , 0 ]  of  float  = 0 - 0.50 + N (  )  + DEA (  )  / s (  )  -  ! 9 || 254_5_2_2_8.1 *  - q ;  }"""
        expect="""Program([
	FuncDecl(ex, FloatType, [InheritOutParam(kI, BooleanType), InheritOutParam(Q, StringType)], Nd3w, BlockStmt([VarDecl(MPf, ArrayType([78123, 0], FloatType), BinExpr(||, BinExpr(-, BinExpr(+, BinExpr(+, BinExpr(-, IntegerLit(0), FloatLit(0.5)), FuncCall(N, [])), BinExpr(/, FuncCall(DEA, []), FuncCall(s, []))), UnExpr(!, IntegerLit(9))), BinExpr(*, FloatLit(2545228.1), UnExpr(-, Id(q)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_399(self):
        input="""main: function void(out a: string) inherit E1
{
    a = false;
    b = a + false;
    c: integer = b + {} + {{true} :: ({})} + {"true"};
    d: string = a[----1];
    e, f: array [1_11_111, 0] of float = !!!!!------11_11_1_1 - 1, {1,.2e1,-0.E+3,.0E-4,1_0_0.500e0};
    g: integer = {a, b(), "c", d - 1, e :: f, g || h(i, !!--j({},{{},{}, a[1]}))};
}
h: auto = {main()};
i: integer = {{1}, {}, {""}, a, call({1}, {}), a[{}]};
j: float = {};
k: auto = .23e12 / .12E1 + true;
l: array [1] of integer = a[{}];
m: auto = a(b[{({})}]);
n: string = {{}, {{}, {} - {{}}}} - {} + ({}) :: {} || !-{} + foo({bar[{}]});
o: function auto(inherit out _1: auto, _2: auto)
{
    p, q, r: auto;
    break;
    break;
    return;
    break;
    continue;
    return true;
    continue;
    break;
    return a[1,{}];
    return a({{{{}}},{}},{},{}) + {} + foo[{}, foo[1, {}]];
    for (i = {}, {}, {})
        do 
        {
            if ({}) foo = ({});
        }
        while ({});
    break;
    for (a[{}] = true, false, {true, false}) while (a[{true}]) a[true] = {foo()};
}
        """
        expect="""Program([
	FuncDecl(main, VoidType, [OutParam(a, StringType)], E1, BlockStmt([AssignStmt(Id(a), BooleanLit(False)), AssignStmt(Id(b), BinExpr(+, Id(a), BooleanLit(False))), VarDecl(c, IntegerType, BinExpr(+, BinExpr(+, BinExpr(+, Id(b), ArrayLit([])), ArrayLit([BinExpr(::, ArrayLit([BooleanLit(True)]), ArrayLit([]))])), ArrayLit([StringLit(true)]))), VarDecl(d, StringType, ArrayCell(a, [UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(1)))))])), VarDecl(e, ArrayType([111111, 0], FloatType), BinExpr(-, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(111111)))))))))))), IntegerLit(1))), VarDecl(f, ArrayType([111111, 0], FloatType), ArrayLit([IntegerLit(1), FloatLit(2.0), UnExpr(-, FloatLit(0.0)), FloatLit(0.0), FloatLit(100.5)])), VarDecl(g, IntegerType, ArrayLit([Id(a), FuncCall(b, []), StringLit(c), BinExpr(-, Id(d), IntegerLit(1)), BinExpr(::, Id(e), Id(f)), BinExpr(||, Id(g), FuncCall(h, [Id(i), UnExpr(!, UnExpr(!, UnExpr(-, UnExpr(-, FuncCall(j, [ArrayLit([]), ArrayLit([ArrayLit([]), ArrayLit([]), ArrayCell(a, [IntegerLit(1)])])])))))]))]))]))
	VarDecl(h, AutoType, ArrayLit([FuncCall(main, [])]))
	VarDecl(i, IntegerType, ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([]), ArrayLit([StringLit()]), Id(a), FuncCall(call, [ArrayLit([IntegerLit(1)]), ArrayLit([])]), ArrayCell(a, [ArrayLit([])])]))
	VarDecl(j, FloatType, ArrayLit([]))
	VarDecl(k, AutoType, BinExpr(+, BinExpr(/, FloatLit(230000000000.0), FloatLit(1.2)), BooleanLit(True)))
	VarDecl(l, ArrayType([1], IntegerType), ArrayCell(a, [ArrayLit([])]))
	VarDecl(m, AutoType, FuncCall(a, [ArrayCell(b, [ArrayLit([ArrayLit([])])])]))
	VarDecl(n, StringType, BinExpr(::, BinExpr(+, BinExpr(-, ArrayLit([ArrayLit([]), ArrayLit([ArrayLit([]), BinExpr(-, ArrayLit([]), ArrayLit([ArrayLit([])]))])]), ArrayLit([])), ArrayLit([])), BinExpr(||, ArrayLit([]), BinExpr(+, UnExpr(!, UnExpr(-, ArrayLit([]))), FuncCall(foo, [ArrayLit([ArrayCell(bar, [ArrayLit([])])])])))))
	FuncDecl(o, AutoType, [InheritOutParam(_1, AutoType), Param(_2, AutoType)], None, BlockStmt([VarDecl(p, AutoType), VarDecl(q, AutoType), VarDecl(r, AutoType), BreakStmt(), BreakStmt(), ReturnStmt(), BreakStmt(), ContinueStmt(), ReturnStmt(BooleanLit(True)), ContinueStmt(), BreakStmt(), ReturnStmt(ArrayCell(a, [IntegerLit(1), ArrayLit([])])), ReturnStmt(BinExpr(+, BinExpr(+, FuncCall(a, [ArrayLit([ArrayLit([ArrayLit([ArrayLit([])])]), ArrayLit([])]), ArrayLit([]), ArrayLit([])]), ArrayLit([])), ArrayCell(foo, [ArrayLit([]), ArrayCell(foo, [IntegerLit(1), ArrayLit([])])]))), ForStmt(AssignStmt(Id(i), ArrayLit([])), ArrayLit([]), ArrayLit([]), DoWhileStmt(ArrayLit([]), BlockStmt([IfStmt(ArrayLit([]), AssignStmt(Id(foo), ArrayLit([])))]))), BreakStmt(), ForStmt(AssignStmt(ArrayCell(a, [ArrayLit([])]), BooleanLit(True)), BooleanLit(False), ArrayLit([BooleanLit(True), BooleanLit(False)]), WhileStmt(ArrayCell(a, [ArrayLit([BooleanLit(True)])]), AssignStmt(ArrayCell(a, [BooleanLit(True)]), ArrayLit([FuncCall(foo, [])]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_400(self):
        input="""mark: float = 10.0;"""
        expect="""Program([\n\tVarDecl(mark, FloatType, FloatLit(10.0))\n])"""
        self.assertTrue(TestAST.test(input, expect, 400))
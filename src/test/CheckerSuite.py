import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_400(self):
        input = """
            main:function void(){
                arr:array[2] of integer;
                arr[1] = 1;
            }
            foo:function auto (a:auto){
                arr:array[2] of integer;
                arr[a] = 1;
                a = 12;
                a = "abc";
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_401(self):
        input = """
            x:string = "abc";
            main:function void(){
                x= "abc"::"abc";
            }
            x:integer = 10;
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402(self):
        input = """
            x:float = 5 + 1.3;
            main:function void(){
                return x+1;
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(BinExpr(+, Id(x), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_403(self):
        input = """
            main:function void(){
                x:integer;
                y:float;
                z:auto = x+y*3/x;
                return z;
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(z))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404(self):
        input = """
            main:function void(){
                x:integer;
                y:float;
                z:auto = x+y*3/z;
                return z;
            }
        """
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_405(self):
        input = """
            x:string;
            y:float = 2 + 2;
            main:function void(){
                x:integer = 5;
                z:auto = x + y;
                t:string = x::"abc";
            }
        """
        expect = "Type mismatch in expression: BinExpr(::, Id(x), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        input = """
            x:string;
            y:float = 2 + 2;
            main:function void(){
                x:integer = 5;
                z:auto = x + y;
            }
            t:string = x::"abc";
            e:float = y + z;
        """
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_407(self):
        input = """
            main:function void(){
                if(true){
                    i:integer;
                    for(i=0,i<10,i+1) if(true) break; else continue;
                    {
                        while(true){
                            break;
                        }
                    }
                    break;
                }
            }
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_408(self):
        input = """
            main:function void() inherit foo{
                super(1,1.0,1);
                printInteger(x);
                printInteger(y);
                printString(t);
            }
            foo:function integer(inherit x:integer, inherit y:float, inherit t:string){
                return x/3;
            }
        """
        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_409(self):
        input = """
            main:function void() inherit foo{
                preventDefault();
                printInteger(x);
                printFloat(y);
                printString(t);
                x:array[5] of integer = {1,2,3,4,5};
            }
            foo:function integer(inherit x:integer, inherit y:float, inherit t:string){
                return x/3;
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_410(self):
        input = """
            main:function void() inherit foo{
                preventDefault();
                printInteger(x);
                printFloat(y);
                printString(t);
                z:array[5] of integer = {1,2,3,4,5.0};
            }
            foo:function integer(inherit x:integer, inherit y:float, inherit t:string){
                return x/3;
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_411(self):
        input = """
            main:function void() inherit foo{
                preventDefault();
                printFloat(f);
            }
            foo:function integer(inherit x:integer, inherit y:float, inherit t:string) inherit foo2{}
            foo2:function float(inherit f:float){
                return f + 2;
            }
        """
        expect = "Undeclared Identifier: f"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_412(self):
        input = """
            foo:function integer(inherit x:integer, inherit y:float, inherit t:string) inherit foo2{
                super(1.2);
            }
            foo2:function float(inherit f:float){
                return f + 2;
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_413(self):
        input = """
            x:string;
            main:function void(x:string, t:string){
                t = x::t;
                return;
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):
        input = """
            x:integer;
            main:function integer(){
                return 0;
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        input = """
            x:integer;
            y:float = x+1;
            main:function void(){
                x:string;
                {
                    x:boolean = true;
                    {
                        x:float = y + 1;
                        {
                            y:string;
                            {
                                y = y::"abc";
                            }
                            x = x*2;
                        }
                        z:auto = 5;
                    }
                    if(x==true){
                        return;
                    }
                    else{
                        continue;
                    }
                }
                x=x::x;
            }
            z:auto=x;
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):
        input = """
            foo:function auto(x:integer){
                return "abc";
            }
            main:function void(){
                x:string = foo(15)::"abc";
                y:float = foo(1) + 1;
            }
        """
        expect = "Type mismatch in expression: BinExpr(+, FuncCall(foo, [IntegerLit(1)]), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        input = """
            foo:function auto(x:integer){
                return;
            }
            main:function void(){
             foo(12);
             x:string = foo(12)::"abc";
             y:integer = foo(1) + 1;
            }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(12)])"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        input = """
            foo:function auto(x:integer){
                x = x + 1;
                return;
            }
            main:function void(){
                foo(foo1(foo1(foo1(12))));
                x:integer = foo1(foo(foo(12))) + 1;
            }
            foo1:function integer(x:integer){
                return x+1;
            }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [FuncCall(foo, [IntegerLit(12)])])"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        input = """
            foo:function auto(x:integer){
                return x;
            }
            main:function void(){
                x:integer = foo1(foo(12)) + 1;
                t:string = foo(12)::"abc";
            }
            foo1:function integer(x:integer){
                return x+1;
            }
        """
        expect = "Type mismatch in expression: BinExpr(::, FuncCall(foo, [IntegerLit(12)]), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        input = """
            foo:function auto(x:integer){
                return "abc";
            }
            main:function void(){
                x:integer = foo1(foo(12)) + 1;
                t:string = foo(12)::"abc";
            }
            foo1:function integer(x:integer){
                return x+1;
            }
        """
        expect = "Type mismatch in expression: FuncCall(foo1, [FuncCall(foo, [IntegerLit(12)])])"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        input = """
            foo:function auto(x:integer){
                return;
            }
            main:function void(){
                foo(12);
                x:string = foo(1);
            }
            foo1:function integer(x:integer){
                return x+1;
            }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        input = """
            foo:function auto(x:integer){
                if (x>1) return "abc"::"abc";
                else return foo(3) + 1;
            }
            main:function void(){
                x:float = 2 + foo();
            }
            foo1:function integer(x:integer){
                return x+1;
            }
        """
        expect = "Type mismatch in expression: BinExpr(+, FuncCall(foo, [IntegerLit(3)]), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        input = """
            foo:function auto(x:integer){
                if (x>1) return foo(2) - 2.0e-4;
                else return 1 + 1;
            }
            main:function void(){
                x:float = 234_567_891 + foo(12);
                x = foo(1)::"abc";
            }
            foo1:function integer(x:integer){
                return x+1;
            }
        """
        expect = "Type mismatch in expression: BinExpr(::, FuncCall(foo, [IntegerLit(1)]), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        input = """
            foo:function auto(x:integer){
                return x % 10;
            }
            main:function void(){
                x:integer = foo1(foo(foo1(12)));
                y:boolean = (foo(1) + foo1(2)) >= 10;
                printBoolean(y || true);
                x = readInteger() + 1;
                y = readBoolean();
                z: auto = readFloat() + x;
                x = z;
            }
            foo1:function auto(x:integer){
                return x+1;
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), Id(z))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        input = """
            x:string;
            main: function void(){
                x:integer = 5;
                t:string = y::"abc";
            }
            y:auto = ((x::x)::x)::"abc";
        """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
        input = """
            x:string;
            main: function void(){
                x:integer = readFloat() + readInteger() + readString() + readBoolean();
                t:string = y::"abc";
            }
            y:auto = ((x::x)::x)::"abc";
        """
        expect = "Type mismatch in expression: BinExpr(+, BinExpr(+, FuncCall(readFloat, []), FuncCall(readInteger, [])), FuncCall(readString, []))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_427(self):
        input = """
            x:string;
            main: function void(){
                x:integer = readInteger()/3 - x*4;
                t:string = y::"abc";
            }
            y:auto = ((x::x)::x)::"abc";
        """
        expect = "Type mismatch in expression: BinExpr(*, Id(x), IntegerLit(4))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
        input = """
             x:string;
            main: function void(){
                z:auto = (!!!true && ---3);
            }
            y:auto = ((x::x)::x)::"abc";
        """
        expect = "Type mismatch in expression: BinExpr(&&, UnExpr(!, UnExpr(!, UnExpr(!, BooleanLit(True)))), UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(3)))))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_429(self):
        input = """
            x:string;
            main: function void(){
                z:auto = !true && false;
                printBoolean(z);
                x:auto = -2 / (readInteger() - 1);
                printFloat(x);
                readInteger(1);
            }
            y:auto = ((x::x)::x)::"abc";
        """
        expect = "Type mismatch in statement: CallStmt(readInteger, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_430(self):
        input = """
            x:string;
            main: function void(){
                z:auto = !true && false;
                printBoolean(z);
                x:auto = -2 / (readInteger() - 1);
                return;
            }
            y:auto = ((x::x)::x)::"abc";
            foo:function integer(x:string, y:float){
                bool:auto = foo1((4+12/7)==(3%10-12));
                x:integer = 5;
                return x + 7;
            }
            foo1:function boolean(bool:boolean){
                bool = true || !false;
                return bool;
            }
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_431(self):
        input = """
            x:string;
            main: function void(){
                z:auto = !true && false;
                printBoolean(z);
                x:auto = -2 / (readInteger() - 1);
                return;
            }
            y:auto = ((x::x)::x)::"abc";
            foo:function integer(x:string, y:float){
                t:integer = 5;
                return t + 7;
            }
            foo:function boolean(bool:boolean){
                bool = true || !false;
                return bool;
            }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_432(self):
        input = """
            main:function void() inherit foo{
                super(13,1.0,"string",1.0);
                printFloat(y);
            }
            foo:function integer(inherit x:integer, inherit y:float, inherit t:string, f:float) inherit foo2{
                super();
                return 0;
            }
            foo2:function float(){
                super();
                return 2.0;
            }
        """
        expect = "Invalid statement in function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_433(self):
        input = """
            main:function void() inherit foo{
                super(13,1.0,true,1.0);
                printFloat(y);
            }
            foo:function integer(inherit x:integer, inherit y:float, inherit t:string, f:float) inherit foo2{
                return 0;
            }
            foo2:function float(){
                return 2.0;
            }
        """
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):
        input = """
            main:function void() inherit foo{
                super(13,1.0,"abc",1.0);
                printFloat(y);
            }
            foo:function integer(inherit x:integer, inherit y:float, inherit t:string, f:float) inherit foo2{
                return 0;
            }
            foo2:function float(inherit f:float){
                return 2.0;
            }
        """
        expect = "Invalid Parameter: f"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        input = """
            main:function void() inherit foo3{
                super(13,1.0,"abc",1.0);
                writeFloat(y);
                foo3(1,2,3);
            }
            foo:function integer(inherit x:integer, inherit y:float, inherit t:string, f:float) inherit foo2{
                return 0;
            }
            foo2:function float(inherit f:float){
                return 2.0;
            }
        """
        expect = "Undeclared Function: foo3"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):
        input = """
            main:function void() inherit foo{
                super(13,1.0,"abc");
                printFloat(y);
            }
            foo:function integer(inherit x:integer, inherit y:float, inherit t:string) inherit foo2{
                preventDefault();
                super((y+f)/2.3);
                super(12);
                return 0;
            }
            foo2:function float(inherit f:float){
                return 2.0;
            }
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):
        input = """
            main:function void(){
                super(1,2,3);
                return;
            }
        """
        expect = "Invalid statement in function: main"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_438(self):
        input = """
            main:function void() inherit foo{
                super(12);
                x:auto = foo(1);
                return;
            }
            foo:function float(x:integer){
                preventDefault();
                return x + 1.2;
            }
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):
        input = """
            main:function void() inherit foo{
                super(12);
                x:auto = foo(1);
                foo2();
                arr:array[2,2] of integer = {{1,2}, {1,2}};
                arr[1,2,3] = 1;
            }
            foo:function float(x:integer){
                return x + 1.2;
            }
            foo2: function void(){}
        """
        expect = "Type mismatch in expression: ArrayCell(arr, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_440(self):
        input = """
            main:function void() inherit foo{
                super(12, 2.2, 3, 4);
                x:auto = foo(1, y, z);
                foo2();
                arr:array[2,2] of integer = {{1,2}, {1,2}};
                t:float = foo(12, y, arr[1,2]);
                foo(12, y, arr[1,2]);
            }
            foo:function float(x:integer, inherit out y:float, inherit out z:integer){
                return x + 1.2;
            }
            foo2: function void(){}
        """
        expect = "Type mismatch in expression: IntegerLit(4)"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_441(self):
        input = """
            x:integer = 3/3;
            t:float = 2 * 6;
            main:function void() inherit foo{
                super(12, t);
                x:auto = foo(1, y, x);
                foo2();
                arr:array[2,2] of integer = {{1,2}, {1,2}};
                t:float = foo(12, x, arr[1,2]);
                t = foo(12, 1.0, 1);
                t = foo(1,1,1);
            }
            foo:function float(x:integer, inherit out y:float, inherit out z:integer){
                return x + 1.2;
            }
            foo2: function void(){}
        """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):
        input = """
            x:integer = 3/3;
            t:float = 2 * 6;
            main:function void(){
                y:float = foo(12, t, x) / 2.3;
                arr:array[2,2] of integer = {{1,2}, {1,2,3}};
            }
            foo:function float(x:integer, inherit out y:float, inherit out z:integer){
                return x + 1.2;
            }
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_443(self):
        input = """
            x:integer = 3/3;
            t:float = 2 * 6;
            main:function void(){
                y:float = foo(12, t, x) / 2.3;
                arr:auto = {{{1,2,3},{1,2,3}},{{1,2,3},{1,2,3}},{{1,2,3},{1,2,3}}};
                x:float = foo(arr[0,0,0]*arr[1,1,1]%arr[2,1,2]-arr[1,1,arr[1,1,2]], foo(arr[0,1,1],2.0,3), 3);
                arr2:auto = arr[2,1];
                x = foo(arr2[2], 2.0, arr2[0]);
                arr3:auto = arr2;
                arr4:auto = arr3[0];
                x = arr4[1];
            }
            foo:function float(x:integer, y:float, z:integer){
                return x + 1.2;
            }
        """
        expect = "Type mismatch in expression: ArrayCell(arr4, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_444(self):
        input = """
            main:function void(){
                arr:array[2,2] of integer = foo();
                x:float = foo() + 1;
            }
            foo:function auto(){
                return {{1,2},{1,2}};
            }
        """
        expect = "Type mismatch in expression: BinExpr(+, FuncCall(foo, []), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
        input = """
             main:function void(){
                arr:array[2,2] of integer = {foo(),foo()};
                x:float = foo() + 1;
            }
            foo:function auto(){
                return {1,2};
            }
        """
        expect = "Type mismatch in expression: BinExpr(+, FuncCall(foo, []), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
        input = """
            main:function void(){
                arr:array[2,2] of integer = {{foo(),foo()},{foo(),foo()}};
                x:float = foo();
                t:boolean = !(-foo());
            }
            foo:function auto(){
                return 1;
            }
        """
        expect = "Type mismatch in expression: UnExpr(!, UnExpr(-, FuncCall(foo, [])))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
        input = """
            main:function void(){
                arr:auto = {};
            }
        """
        expect = "Type mismatch in expression: ArrayLit([])"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
        input = """
            main:function void(){
                arr:array[2] of integer = {{},{}};
            }
        """
        expect = "Type mismatch in expression: ArrayLit([])"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        input = """
            main:function void(){
                arr:array[3] of integer = {1,2,{}};
            }
        """
        expect = "Type mismatch in expression: ArrayLit([])"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        input = """
            main:function void(){
                arr:array[0] of integer = {1,2};
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([0], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        input = """
            main:function void(){
                arr:array[3,2] of integer = {{1,2}, {1,2}, foo()};
                arr2:array[2] of integer = foo();
                arr2[0] = 12 + 3;
                foo();
                foo(1,2);
            }
            foo:function auto(){
                return {1,2};
            }
        """
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(1), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        input = """
            main:function void(){
                arr:array[3,2] of integer = {{1,2}, {1,2}, {1, foo()}};
                x:integer = foo() + 2;
                arr2:array[2] of integer = foo();
            }
            foo:function auto(){
                return 0;
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr2, ArrayType([2], IntegerType), FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        input = """
            main:function void(){
                arr:array[111,222,333] of integer = foo();
                x:integer = arr[12, 219 + 2, arr[34, 56, 111]] + 2;
                arr2:auto = arr[110];
                printInteger(arr2);
            }
            foo:function array[111,222,333] of integer(){}
        """
        expect = "Type mismatch in statement: CallStmt(printInteger, Id(arr2))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
        input = """
            main:function void(){
                arr:array[111,222,333] of integer = foo();
                x:integer = arr[12, 219 + 2, arr[34, 56, 111]] + 2;
                arr2:auto = arr[110];
            }
            foo:function array[111,222,333] of integer(){}
            foo2:function integer(a:auto, b:auto){
                x:integer = a + 1;
                y:string = a::b;
                return x;
            }
        """
        expect = "Type mismatch in expression: BinExpr(::, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_455(self):
        input = """
            main:function void(){
                arr:array[111,222,333] of integer = foo();
                x:integer = arr[12, 219 + 2, arr[34, 56, 111]] + 2;
                arr2:auto = arr[110];
                foo2(12, 12.0);
            }
            foo:function array[111,222,333] of integer(){}
            foo2:function integer(a:auto, b:auto){
                x:integer = a + 1;
                y:string = "abc"::b;
                return x;
            }
        """
        expect = "Type mismatch in expression: BinExpr(::, StringLit(abc), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_456(self):
        input = """
            main:function void(){
                arr:array[111,222,333] of integer = foo();
                x:integer = arr[12, 219 + 2, arr[34, 56, 111]] + 2;
                arr2:auto = arr[110];
            }
            foo:function array[111,222,333] of integer(){}
            foo2:function integer(a:auto, b:auto){
                x:integer = 1;
                x = x + a + b;
                y:string = "abc"::b;
                return x;
            }
        """
        expect = "Type mismatch in expression: BinExpr(::, StringLit(abc), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
        input = """
            foo:string;
            foo:function integer(){
                return 1;
            }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
        input = """
            foo:function integer(){
                return 1;
            }
            foo:string;
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_459(self):
        input = """
            main:function void(){
                main:auto = 5;
                main = main + 12;
                printInteger(main);
                printFloat(main);
                return main;
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(main))"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_460(self):
        input = """
            y:array[2,2] of integer = {{},{}};
            x:integer = "abc";
        """
        expect = "Type mismatch in expression: ArrayLit([])"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_461(self):
        input = """
            foo: function auto(a:auto, b:auto){
                x:integer = a + 1;
                return x + 1;
            }
            main:function void(){
                x:integer = foo(1, 2);
                y:string = foo2("abc", "abc");
                z:auto = x + 1;
                y = y::y;
                y = foo(1, "abc");
            }
            foo2: function auto(a:auto, b:auto){
                y:string = b :: "abc";
            }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(1), StringLit(abc)])"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_462(self):
        input = """
            foo: function auto(a:auto, b:auto){
                return 1;
            }
            main:function void(){
                x:integer = foo(1, 2);
                y:string = foo2("abc", "abc");
                z:auto = x + 1;
                y = y::y;
                y = foo("abc", "abc");
            }
            foo2: function auto(a:auto, b:auto){
                y:string = b :: "abc";
            }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [StringLit(abc), StringLit(abc)])"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):
        input = """
            main:function void(){
                a:array[0,0] of integer = a[10];
                return;
                return 1;
                x:auto;
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):
        input = """
            main:function void(){
                i:integer;
                do{
                    i = 1;
                    break;
                    i = true;
                    return;
                    return 1;
                }while(true);
                if(i>5) continue;
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(i), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_465(self):
        input = """
            main:function void(){
                if(readBoolean() == true){
                    x:auto = true;
                }
                else return;
                if(true) break;
            }
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_466(self):
        input = """
            main:function void(){
                if(readBoolean() == true) return;
                else{
                    x:auto = true;
                }
                x:auto = 5;
                x:float = 1;
            }
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_467(self):
        input = """
            main:function void(){
                a:array[2] of integer;
                x:integer = a["123"];
                if(readBoolean() == true) return;
                else return;
                x:auto = 5;
                x:float = 1;
            }
        """
        expect = "Type mismatch in expression: ArrayCell(a, [StringLit(123)])"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):
        input = """
            main:function void(){
                if(readBoolean() == true){
                    x:integer = 5;
                    x = x + x + x;
                    return;
                    y,z:string = 1,2;
                }
                else{
                    t:string = "abc"::"abc";
                    break;
                }
                x:auto = 5;
                x:float = 1;
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(y, StringType, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        input = """
            main:function void(){
                if(readBoolean() == true){
                    x:integer = 5;
                    x = x + x + x;
                }
                else{
                    t:string = "abc"::"abc";
                    return;
                    break;
                }
                x:auto = 5;
                x:float = 1;
            }
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        input = """
            main:function void(){
                x,y,z:auto = 1,"string", true;
                arr:array[2] of integer = {x,y,z};
                return;
                return str;
            }
        """
        expect = "Illegal array literal: ArrayLit([Id(x), Id(y), Id(z)])"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        input = """
            main:function void(){
                x,y,z:integer = 1,"string", true;
                arr:array[2] of integer = {x,y,z};
                return;
                return str;
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(y, IntegerType, StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        input = """
            foo:function integer(x:string){
                return 1;
            }
            main:function void(){
                foo:string;
                x:auto = foo("abc");
                x = foo;
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), Id(foo))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
        input = """
            main:function void() inherit foo{
                super("abc", true);
                z = z::z;
                t = false;
                x:integer = 5;
                {
                    z:auto = "abc";
                }
                z = "abc";
                z = 1;
            }
            foo:function auto(inherit z:string, inherit t:boolean) inherit foo2{
                
            }
            foo2:function auto(inherit x:integer, inherit y:float){}
        """
        expect = "Type mismatch in statement: AssignStmt(Id(z), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
        input = """
            main:function void() inherit foo{
                super("abc", true);
                z = z::z;
                t = false;
                x:integer = 5;
                y:string;
            }
            foo:function auto(inherit z:string, inherit t:boolean) inherit foo2{
                preventDefault();
            }
            foo2:function auto(inherit x:integer, inherit y:float, inherit x:integer){}
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):
        input = """
            x:string = "abc";
            main:function void(){
                x:auto = 5;
                for(x=0,x<10,x+1) if(x<3) x = x+1; else continue;
                do{break;}while(true);
                while(true) continue;
                if(x+2 <= x) return;
                return 1;
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
        input = """
            x:string;
            y:float = 1 + 1%2;
            main:function void(){
                x:integer = 5;
                {
                    x:boolean = true;
                    while(x){
                        x:auto = 1.0;
                    }
                    if(x) x = x + 1;
                }
            }
        """
        expect = "Type mismatch in expression: BinExpr(+, Id(x), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        input = """
            main:function void(){
                foo(5);
                x:string = foo(5);
            }
            foo:function auto(x:auto){
                return x;
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_478(self):
        input = """
            arr:array[2,2] of integer;
            x:auto = true;
            main:function void(){
                if(x) arr[0,1] = 2;
                return;
            }
            foo:function integer(){
                while(x) arr[0, arr[0,0]] = arr[12,12];
                return;
            }
        """
        expect = "Type mismatch in statement: ReturnStmt()"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        input = """
            arr:array[2,2] of integer;
            x:auto = 5;
            main:function void(){
                if(x) arr[0,1] = 2;
                return;
            }
            foo:function integer(){
                while(x) arr[0, arr[0,0]] = arr[12,12];
                return;
            }
        """
        expect = "Type mismatch in statement: IfStmt(Id(x), AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), IntegerLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_480(self):
        input = """
            arr:array[2,2] of integer;
            x:auto = 5;
            main:function void(){
                if(true) arr[0,1] = 2;
                return;
            }
            foo:function integer(){
                while(x) arr[0, arr[0,0]] = arr[12,12];
                return;
            }
        """
        expect = "Type mismatch in statement: WhileStmt(Id(x), AssignStmt(ArrayCell(arr, [IntegerLit(0), ArrayCell(arr, [IntegerLit(0), IntegerLit(0)])]), ArrayCell(arr, [IntegerLit(12), IntegerLit(12)])))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        input = """
            arr:array[2,2] of integer;
            x:auto = 5;
            main:function void(){
                if(true) arr[0,1] = 2;
                for(x=0, x+1, x+1) break;
                return;
            }
            foo:function integer(){
                while(x) arr[0, arr[0,0]] = arr[12,12];
                return;
            }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(+, Id(x), IntegerLit(1)), BinExpr(+, Id(x), IntegerLit(1)), BreakStmt())"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_482(self):
        input = """
            arr:array[2,2] of integer;
            x:auto = 5;
            main:function void(){
                if(true) arr[0,1] = 2;
                return;
            }
            foo:function integer(){
                do{break;} while(x); 
                arr[0, arr[0,0]] = arr[12,12];
                return;
            }
        """
        expect = "Type mismatch in statement: DoWhileStmt(Id(x), BlockStmt([BreakStmt()]))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_483(self):
        input = """
            main:function void(){
                i:integer = 1;
                for(i=0, i<10, i+1){
                    if(i<=10) printInteger(i);
                    else break;
                }
                if(i>=10) continue;
            }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
        input = """
            main:function void() inherit foo{
                return;
            }
            foo:auto = 5;
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        input = """
            main:function void() inherit foo{
                super(1,2,3);
                y = y::z;
            }
            foo:function auto(inherit x:auto, inherit y:auto, z:auto){
                return x + y + z; 
            }
        """
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        input = """
            main:function void() inherit foo{
                preventDefault();
                x = "abc";
                y = true;
                z: integer = foo(1,2,3) + 1;
                x = x+1;
            }
            foo:function auto(inherit x:auto, inherit y:auto, z:auto){
                return x + y + z; 
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        input = """
            main:function void() inherit foo{
                preventDefault();
                z: integer = foo(1,2,3) + 1;
                x = "abc";
                y = true;
            }
            foo:function auto(inherit x:auto, inherit y:auto, z:auto){
                return x + y + z; 
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_488(self):
        input = """
            main:function void() inherit foo{
                preventDefault();
                foo(1.0,2.0,3.0);
                z: integer = foo(1,2,3) + 1;
                x = "abc";
                y = true;
            }
            foo:function auto(inherit x:auto, inherit y:auto, z:auto){
                return x + y + z; 
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        input = """
            main:function void() inherit foo{
                preventDefault();
                foo(1.0,2.0,3.0);
                z: integer = foo(1,2,3) + 1.0;
                x = "abc";
                y = true;
            }
            foo:function auto(inherit x:auto, inherit y:auto, z:auto){
                return x + y + z; 
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(z, IntegerType, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), FloatLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_490(self):
        input = """
            main:function void() inherit foo{
                preventDefault();
                foo(1.0,2.0,3.0);
                foo();
            }
            foo:function auto(inherit x:auto, inherit y:auto, z:auto){
                return x + y + z; 
            }
        """
        expect = "Type mismatch in statement: CallStmt(foo, )"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = """
            main:function void() inherit foo{
                preventDefault();
                foo(1.0,2.0,3.0);
                foo(1,2,3.0);
                foo(1);
            }
            foo:function auto(inherit x:auto, inherit y:auto, z:auto){
                return x + y + z; 
            }
        """
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        input = """
            main:function void(y:integer) inherit foo{
                preventDefault();
                foo(1.0,2.0,3.0);
            }
            foo:function auto(inherit x:auto, inherit y:auto, z:auto){
                return x + y + z; 
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_493(self):
        input = """
            main:function auto() inherit foo{
                preventDefault();
                foo(1.0,2.0,3.0);
                main();
            }
            foo:function auto(inherit x:auto, inherit y:auto, z:auto){
                return x + y + z; 
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = """
            main:function void(){
                i:integer = 0;
                for(i=1, i<=10, i+1){
                    if(i>10) break;
                    else continue;
                }
                x:auto = x + x;
                return;
                return 1;
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        input = """
             main:function void(){
                i:integer = 0;
                for(i=1, i<=10, i+1){
                    if(i>10) break;
                    else continue;
                }
                return;
                return 1;
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = """
            x:auto = true;
            y:float = 1 + 1;
            main:function void(){
                x:integer = 5;
                {
                    x:string = "abc";
                    printString(x);
                }
                x = x + 1;
                {
                    i:integer;
                    for(i=0,i<10,i+1){
                        x=x+1;
                        if(x>100){
                            x=x*2;
                            continue;
                        }
                        else{
                            x:string = x::x;
                            printString(x);
                        }
                    }
                }
            }
        """
        expect = "Type mismatch in expression: BinExpr(::, Id(x), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
        input = """
            x:auto = true;
            y:float = 1 + 1;
            main:function void(){
                x:integer = 5;
                {
                    x:string = "abc";
                    printString(x);
                }
                x = x + 1;
                {
                    i:integer;
                    for(i=0,i<10,i+1){
                        x=x+1;
                        if(x>100){
                            x=x*2;
                            continue;
                        }
                        else{
                            x:string = "abc"::"abc";
                            printString(x);
                            break;
                        }
                    }
                }
                i = i+1;
            }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_498(self):
        input = """
            foo:function auto(x:integer){
                return;
            }
            main:function void(){
                x:integer;
                x = foo(1);
            }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """
            foo:function auto(x:integer){
                x = foo(2);
                return foo(1);
            }
            main:function auto(){
                x:integer;
                x = foo(1);
                return;
            }
            foo2:function auto(x:integer){
                return "abc";
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 499))
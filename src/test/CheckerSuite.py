import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_101(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 101))

    def test_102(self):
        input = """
    main: function void(){}
    main: function void(){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 102))

    def test_103(self):
        input = """main: function void(a: auto){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 103))

    def test_104(self):
        input = """main: function void(a: integer){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 104))

    def test_105(self):
        input = """main: function string(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 105))

    def test_106(self):
        input = """main: function auto(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 106))

    def test_107(self):
        input = """main: integer = 1;"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 107))

    def test_108(self):
        input = """
    a: integer = 1;
    main: function void(){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 108))

    def test_109(self):
        input = """
    a: integer = "lmao";
    main: function void(){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 109))

    def test_110(self):
        input = """
    a: auto = 1;
    main: function void(){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 110))

    def test_111(self):
        input = """
    a: auto;
    main: function void(){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 111))

    def test_112(self):
        input = """
    a: auto = 1;
    b: integer = 2;
    c: integer = a - b;
    main: function void(){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 112))

    def test_113(self):
        input = """
    a: auto = 1;
    a: integer = 2;
    main: function void(){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 113))

    def test_114(self):
        input = """
    a: auto = 1;
    b: boolean = true;
    c: auto = a * b;
    main: function void(){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 114))

    def test_115(self):
        input = """
    a: auto = 1;
    b: float = 2;
    c: auto = a + b;
    main: function void(){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 115))

    def test_116(self):
        input = """
    a: auto = -1.1;
    b: float = 2.2;
    c: auto = a / b;
    main: function void(){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 116))

    def test_117(self):
        input = """
    a: auto = 1 / 0;
    b: auto = 0 % 0;
    c: auto = a + b;
    main: function void(){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 117))

    def test_118(self):
        input = """
    a: auto = 1;
    b: float = 2;
    c: auto = a + b;
    main: function void(){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 118))

    def test_119(self):
        input = """foo();"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 119))

    def test_120(self):
        input = """
    main: function void(){
    foo();
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 120))

    def test_121(self):
        input = """
    main: function void(){
    main();
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 121))

    def test_122(self):
        input = """
    a: integer;
    main: function void(){
    a: string;
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 122))

    def test_123(self):
        input = """
    a: auto = 1;
    main: function void(){
    a: auto = 2;
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 123))

    def test_124(self):
        input = """
    a: auto = 1;
    main: function void(){
    a: auto = {1, 2, 3};
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 124))

    def test_125(self):
        input = """
    a: auto = 1;
    b: auto = 2;
    main: function void(){
    c: auto = a + b;
    }
    c: auto = "lmao";
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 125))

    def test_126(self):
        input = """
    main: function void(){}
    a: auto = main();
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 126))

    def test_127(self):
        input = """
    main: function void(){}
    foo: function string(){}
    a: auto = foo();
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 127))

    def test_128(self):
        input = """
    main: function void(){}
    foo: function boolean(){}
    a: string = foo();
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 128))

    def test_129(self):
        input = """
    main: function void(){}
    foo: function auto(){}
    a: float = foo();
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 129))

    def test_130(self):
        input = """
    main: function void(){}
    foo: function string(a: string){}
    a: auto = foo(a);
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 130))

    def test_131(self):
        input = """
    main: function void(){}
    foo: function string(a: auto){}
    a: integer;
    b: auto = foo(a);
    c: integer = a;
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 131))

    def test_132(self):
        input = """
    main: function void(){}
    foo: function string(a: auto){}
    a: integer;
    b: auto = foo(a);
    c: string = a;
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 132))

    def test_133(self):
        input = """
    main: function void(){}
    foo: function string(){}
    a: auto = foo(a);
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 133))

    def test_134(self):
        input = """
    main: function void(){}
    foo: function string(){}
    a: integer;
    b: string = foo(a);
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 134))

    def test_135(self):
        input = """
    main: function void(){}
    foo: function void(a: string){}
    a: string = foo(a, a);
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 135))

    def test_136(self):
        input = """
    main: function void(){}
    foo: function string(){}
    foo();
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 136))

    def test_137(self):
        input = """
    main: function void(){}
    foo: function void(a: string){}
    a: string;
    foo(a);
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 137))

    def test_138(self):
        input = """
    main: function void(){}
    foo: function void(a: string, a: integer){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 138))

    def test_139(self):
        input = """
    main: function void(){}
    foo: function void(a: string, main: boolean){}
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 139))

    def test_140(self):
        input = """
    main: function void(){
        if (true)
            main();
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 140))

    def test_141(self):
        input = """
    foo: function void(){}
    main: function void(){
        if (false)
            foo();
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 141))

    def test_142(self):
        input = """
    a: boolean;
    foo: function void(){}
    main: function void(){
        if (a)
            foo();
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 142))

    def test_143(self):
        input = """
    foo: function void(){}
    main: function void(){
        while (true || false)
            foo();
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 143))

    def test_144(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        do
            foo();
        while (foo());
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 144))

    def test_145(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        if (true) if (false) if (foo()) return;
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 145))

    def test_146(self):
        input = """
    foo: function boolean(){}
    bar: function string(){}
    main: function void(){
        if (1 > 0)
            foo();
        else
        {
            bar();
            bar();
            bar();
            return;
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 146))

    def test_147(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        do
            break;
        while (foo());
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 147))

    def test_148(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        while (0 == 0.0)
        {
            continue;
            break;
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 148))

    def test_149(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        a: integer;
        for (a = 1, a < 10, a + 1)
            continue;
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 149))

    def test_150(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        a: string;
        for (a = 1, a < 10, a + 1)
            break;
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 150))

    def test_151(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        a: integer;
        for (a = 1, a < 10, a + 1.1)
            return;
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 151))

    def test_152(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        a: integer;
        for (a = 1, a < 10, a + 1)
        {
            return;
            break;
            continue;
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 152))

    def test_153(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        a: integer;
        for (a = 1, a < 10, a + 1)
            a: boolean = true;
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 153))

    def test_154(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        a: integer;
        for (a = 1, a < 10, a + 1)
        {
            a: boolean = true;
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 154))

    def test_155(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        a: integer;
        for (a = 1, a < 10, a + 1)
        {
            if (a == 1.1) return;
            else continue;
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 155))

    def test_156(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        a: integer;
        b: integer;
        for (a = 1, b < 10, b + 1)
            for (b = 1, a < 10, a + 1)
            {
                a: string = "lmao";
            }
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 156))

    def test_157(self):
        input = """
    foo: function boolean(){}
    main: function void(){
        a: integer;
        b: integer;
        for (a = 1, b < 10, b + 1)
            for (b = 1, a < 10, a + 1)
                if (a != b)
                    while (a % b == 0)
                        for (a = 0, true, 1)
                            return;
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 157))

    def test_158(self):
        input = """
    a: string = "lmao";
    main: function void(){}
    foo: function boolean(b: integer){
        a: auto = 1;
        for (a = 1, b < 10, b + 1)
            for (b = 1, a < 10, a + 1)
            {
                main();
            }
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 158))

    def test_159(self):
        input = """
    a: auto = "lmao";
    main: function void(){}
    foo: function boolean(b: auto){
        a: auto = 2;
        for (a = 1, b < 10, b + 1)
            for (b = 1, a < 10, a + 1)
            {
                main();
                c: auto = foo(a);
            }
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 159))

    def test_160(self):
        input = """
    a: auto = "lmao";
    main: function void(){}
    bar: function auto(){}
    goo: function integer(){}
    foo: function boolean(b: auto){
        a: auto = 2;
        for (a = 1, bar(), goo())
            return;
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 160))

    def test_161(self):
        input = """
    main: function void(){
        continue;
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 161))

    def test_162(self):
        input = """
    main: function void(){
        break;
    }
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 162))

    def test_163(self):
        input = """
    main: function void(){}
    foo: function void(a: float){}
    a: auto = 1 + 2;
    b: auto = a + 1.2;
    foo(b);
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 163))

    def test_164(self):
        input = """
    main: function void(){}
    foo: function void(a: string){}
    a: auto = "asdf";
    b: auto = a :: "lmao";
    foo(b);
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 164))

    def test_165(self):
        input = """
    main: function void(){}
    foo: function void(a: integer){}
    a: auto = (1 + 2) / 0;
    foo(a);
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 165))

    def test_166(self):
        input = """
    main: function void(){}
    foo: function void(a: auto){}
    a: auto = 1 + 2;
    foo(a);
    b: auto = a + 1.2;
    foo(b);
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 166))

    def test_167(self):
        input = """
    main: function void(){}
    foo: function void(a: auto){}
    bar: function integer(){}
    a: auto = bar();
    foo(a);
    b: auto = bar() + 1.2;
    foo(b);
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 167))

    def test_168(self):
        input = """
    main: function void(){}
    foo: function void(a: auto){}
    bar: function integer(){}
    a: auto = 1.2 + bar();
    foo(a);
    b: auto = a + 1.2;
    foo(b);
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 168))

    def test_169(self):
        input = """
    main: function void(){}
    foo: function void(a: auto){}
    bar: function boolean(){}
    a: auto = 1 + 2;
    foo(a);
    b: auto = a + 1.2;
    foo(b);
    """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 169))

    def test_170(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 170))

    def test_171(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 171))

    def test_172(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 172))

    def test_173(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 173))

    def test_174(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 174))

    def test_175(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 175))

    def test_176(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 176))

    def test_177(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 177))

    def test_178(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 178))

    def test_179(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 179))

    def test_180(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 180))

    def test_181(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 181))

    def test_182(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 182))

    def test_183(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 183))

    def test_184(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 184))

    def test_185(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 185))

    def test_186(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 186))

    def test_187(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 187))

    def test_188(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 188))

    def test_189(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 189))

    def test_190(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 190))

    def test_191(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 191))

    def test_192(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 192))

    def test_193(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 193))

    def test_194(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 194))

    def test_195(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 195))

    def test_196(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 196))

    def test_197(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 197))

    def test_198(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 198))

    def test_199(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 199))

    def test_200(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 200))



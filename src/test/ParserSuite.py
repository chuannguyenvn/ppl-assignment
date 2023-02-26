import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_201(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_202(self):
        input = """
main: function integer()
{

}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_203(self):
        input = """
// this is the main function
main: function void() // main function is a function that return a void object, which is an object originated from the void
{ // curly brace denotes the start of the main function
    /* main function's main function is 
    to do some main functions, which are functions
    that main and typically appear in a main function */
} // another curly brace informs the function that this is its end
// that is all there is to it"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_204(self):
        input = """main: function integer()
{
    a = 1;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_205(self):
        input = """
main: function integer()
{
    a = a;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_206(self):
        input = """
main: function integer()
{
    a = a = a;
}"""
        expect = """Error on line 4 col 10: ="""
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        input = """main: function integer()
{
    a = ;
}"""
        expect = """Error on line 3 col 8: ;"""
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_208(self):
        input = """
// this statement suggests that Tai is a meaningless person (void), and everything he said is of utmost untrustworthy (false)
Tai /* there is just about a million people with the name "Tai", therefore I deny any personal attack accusation */ : void = false; // this statement is also a valid statement, which means it is factual"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_209(self):
        input = """
a: integer = true || false && true || (!false);"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_210(self):
        input = """
main: function integer()
{
    a = 1 + true * "false" - !((true) + 0.69);
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_211(self):
        input = """
main: function integer()
{
    a = foo();
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_212(self):
        input = """
main: function integer()
{
    a = foo(1);
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_213(self):
        input = """
main: function integer()
{
    a = foo(((1)));
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_214(self):
        input = """
main: function integer()
{
    a = foo(foo());
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_215(self):
        input = """
main: function integer()
{
    a = {1, 2, 3};
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_216(self):
        input = """
main: function integer()
{
    a = {(1), 2 + 3, foo(4), "asdf"};
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_217(self):
        input = """
main: function integer()
{
    a = 123_456_789;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_218(self):
        input = """
main: function integer()
{
    a : array [3] of integer = {1, 2, 3};
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_219(self):
        input = """
main: function integer() 
{
    a : array [-1] of integer = {1, 2, 3};
}"""
        expect = """Error on line 4 col 15: -"""
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_220(self):
        input = """
main: function integer() 
{
    a : array [1] of void = {1, 2, 3};
}"""
        expect = """Error on line 4 col 21: void"""
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):
        input = """
main: function integer() 
{
    a, b, c : array [0, 1, 2, 3, 4] of string;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_222(self):
        input = """
main: function integer()
{
    a, b, c : array [0] of string = 1, 2, 3;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_223(self):
        input = """
main: function integer()
{
    a, b, c : array [0] of string = 1, 2, 3, 4;
}"""
        expect = """Error on line 4 col 43: ,"""
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_224(self):
        input = """
main: function integer()
{
    a, b, c : array [0] of string = 1, 2;
}"""
        expect = """Error on line 4 col 40: ;"""
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_225(self):
        input = """
main: function integer()
{
    if (1 > 2) a = 1;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_226(self):
        input = """
main: function integer()
{
    if (1 > 2) ;
}"""
        expect = """Error on line 4 col 15: ;"""
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_227(self):
        input = """
main: function integer()
{
    if () foo();
}"""
        expect = """Error on line 4 col 8: )"""
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_228(self):
        input = """
main: function integer()
{
    if foo();
}"""
        expect = """Error on line 4 col 7: foo"""
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_229(self):
        input = """
main: function integer()
{
    if (1 > 2) foo();
    else bar();
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_230(self):
        input = """
main: function integer()
{
    if (1 > 2) foo();
    else ;
}"""
        expect = """Error on line 5 col 9: ;"""
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_231(self):
        input = """
main: function integer()
{
    else foo();
}"""
        expect = """Error on line 4 col 4: else"""
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_232(self):
        input = """
main: function integer()
{
    if (1 > 2) if (2 > 3) if (3 > 4) if (4 > 5) foo();
    else bar();
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_233(self):
        input = """
main: function integer()
{
    if (1 > 2) foo(); else if (1 < 2) bar(); else goo();
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_234(self):
        input = """
main: function integer()
{
    for (i = 1, i < 10, i + 1) foo();
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_235(self):
        input = """
main: function integer()
{
    for (i = foo(), foo(), foo()) foo();
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_236(self):
        input = """
main: function integer()
{
    for (1 = 1, i < 10, i + 1) foo();
}"""
        expect = """Error on line 4 col 9: 1"""
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_237(self):
        input = """
main: function integer()
{
    for (i = 1, i < 10, i + 1) 
    for (j = 1, j > 10, j + foo()) 
    foo();
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_238(self):
        input = """
main: function integer()
{
    for (i = 1, i < 10, i + 1) if (true) while (false) return;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_239(self):
        input = """
main: function integer()
{
    for (i = 1, i < 10, i + 1) continue;
    continue;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_240(self):
        input = """
main: function integer()
{
    for (, , )
}"""
        expect = """Error on line 4 col 9: ,"""
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_241(self):
        input = """
main: function integer()
{
    while (1) {}
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_242(self):
        input = """
main: function integer()
{
    while (1) foo();
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_243(self):
        input = """
main: function integer()
{
    while (1) while(a) while(foo()) while ("abc") continue;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_244(self):
        input = """
main: function integer()
{
    while 
}"""
        expect = """Error on line 5 col 0: }"""
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_245(self):
        input = """
main: function integer()
{
    do {} while (a);
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_246(self):
        input = """
main: function integer()
{
    do {do {do {do {} while(a);} while(a);} while(a);} while (a);
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_247(self):
        input = """
main: function integer()
{
    do {drug();} while (withdrawing());
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_248(self):
        input = """
main: function integer()
{
    do drug() while (withdrawing());
}"""
        expect = """Error on line 4 col 7: drug"""
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_249(self):
        input = """
main: function integer()
{
    do {break; continue; return;} while (1);
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_250(self):
        input = """
main: function integer()
{
    break; 
    continue; 
    return;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_251(self):
        input = """
main: function integer()
{
    call(me, maybe);
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_252(self):
        input = """
main: function integer()
{
    fractal(69, fractal(69, fractal(69, fractal(69, fractal()))));
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_253(self):
        input = """
main: function integer()
{
    _1();
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_254(self):
        input = """
main: function integer()
{
    foo()
}"""
        expect = """Error on line 5 col 0: }"""
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_255(self):
        input = """
main: function integer()
{
    _1();
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_256(self):
        input = """
main: function integer()
{
    {}{}{}{}
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_257(self):
        input = """
main: function integer()
{
    {}{}{{}}{{{}{}{{}}}}{}{{}}{{}{}}
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_258(self):
        input = """
main: function integer()
{
    a, b, c, d: void;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_259(self):
        input = """
main: function integer()
{
    a, b, c, d: auto;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_260(self):
        input = """
main: function integer()
{
    a: float = true;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_261(self):
        input = """
main: function integer()
{
    a, b: void = c, d;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_262(self):
        input = """
main: function integer()
{
    a, b, c: integer = a, b, c, d;
}"""
        expect = """Error on line 4 col 30: ,"""
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_263(self):
        input = """
main: function integer()
{
    a, b, c, d: string = foo(), bar(), goo();
}"""
        expect = """Error on line 4 col 44: ;"""
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_264(self):
        input = """
a: integer = "yo";
b: void = main();
c: float = true :: false; """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_265(self):
        input = """
main: integer = -69;
main: function integer() { }
main: function void() { main: void = -main(!69);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_266(self):
        input = """
main: function integer()
{
    a = (1 + 2 * 3 - 4) / (5 % 6) + 7 - (8) % 9 / 0;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_267(self):
        input = """
main: function integer()
{
    a = ---------------"minus";
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_268(self):
        input = """
main: function integer()
{
    a = 1.001 ---("two" / --3) + four(-5) % six + 7 % 8 * nine(-0.000);
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_269(self):
        input = """
main: function integer()
{
    a = 1 ++ 2;
}"""
        expect = """Error on line 4 col 11: +"""
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_270(self):
        input = """
main: function integer()
{
    -a = 1;
}"""
        expect = """Error on line 4 col 4: -"""
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_271(self):
        input = """
main: function integer()
{
    a = true + false * "yo" / yo % 1_2_3_4_5;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_272(self):
        input = """
main: function integer()
{
    a = !wtf;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_273(self):
        input = """
main: function integer()
{
    a = !!!!!!!!wtf;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_274(self):
        input = """
main: function integer()
{
    a = !(!(!(!(!(wtf)))));
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_275(self):
        input = """
main: function integer()
{
    a = !hey && !hey || !hey;
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_276(self):
        input = """main: function integer()
{
    a = !true || false && "true" || !(foo && !!bar);
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_277(self):
        input = """main: function integer()
{
    a = "my heart" :: "your heart";
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_278(self):
        input = """main: function integer()
{
    a = ("i love" :: "eating babies") :: "' powdered milk";
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_279(self):
        input = """main: function integer()
{
    a = ((1 == 2) != 3) < (4 > ((5 <= 6) >= 7));
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_280(self):
        input = """main: function integer()
{
    a = 1 < ("two" >= three(four(5.6, 7 != true))); 
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_281(self):
        input = """main: function integer()
{
    a = 1 ======= 2;
}"""
        expect = """Error on line 3 col 12: =="""
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_282(self):
        input = """main: function integer()
{
    a = a[0];
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_283(self):
        input = """main: function integer()
{
    a = -a[-1];
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_284(self):
        input = """main: function integer()
{
    a = a[one, a[2], a["3"], _1[4 > 5, 6 < 7], _8(nine[0])];
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_285(self):
        input = """main: function integer()
{
    a = a[1][2];
}"""
        expect = """Error on line 3 col 12: ["""
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_286(self):
        input = """main: function integer()
{
    a = a[a(a[a(a[a()])])];
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        input = """main: function integer()
{
    a = 1 < ("two" >= three + (four(5.6, 7 != true))); 
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        input = """
main: function integer()
{
    zero = 1 * 2 + 3 || 4 % five[6] + seven(8, nine[10, 11, twelve[13] && 14]) % 15 == 16 :: (true);
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_289(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_290(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_291(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_300(self):
        input = """
"""
        expect = """Error on line 2 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 300))

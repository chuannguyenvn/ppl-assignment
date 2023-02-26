import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_101(self):
        self.assertTrue(TestLexer.test("   ", "<EOF>", 101))

    def test_102(self):
        self.assertTrue(TestLexer.test(" ~ ", "Error Token ~", 102))

    def test_103(self):
        self.assertTrue(TestLexer.test(" \n ", "<EOF>", 103))

    def test_104(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 104))

    def test_105(self):
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 105))

    def test_106(self):
        self.assertTrue(TestLexer.test("0000", "0,0,0,0,<EOF>", 106))

    def test_107(self):
        self.assertTrue(TestLexer.test("1_2_3", "123,<EOF>", 107))

    def test_108(self):
        self.assertTrue(TestLexer.test("_1_2_3", "_1_2_3,<EOF>", 108))

    def test_109(self):
        self.assertTrue(TestLexer.test("1_2_3_", "123,_,<EOF>", 109))

    def test_110(self):
        self.assertTrue(TestLexer.test("1__2__3", "1,__2__3,<EOF>", 110))

    def test_111(self):
        self.assertTrue(TestLexer.test("1.23", "1.23,<EOF>", 111))

    def test_112(self):
        self.assertTrue(TestLexer.test("0.123", "0.123,<EOF>", 112))

    def test_113(self):
        self.assertTrue(TestLexer.test("123_456.789", "123456.789,<EOF>", 113))

    def test_114(self):
        self.assertTrue(TestLexer.test("1.23e45", "1.23e45,<EOF>", 114))

    def test_115(self):
        self.assertTrue(TestLexer.test("1.23e+45", "1.23e+45,<EOF>", 115))

    def test_116(self):
        self.assertTrue(TestLexer.test("123E-45", "123E-45,<EOF>", 116))

    def test_117(self):
        self.assertTrue(TestLexer.test("0.12", "0.12,<EOF>", 117))

    def test_118(self):
        self.assertTrue(TestLexer.test(".12e1", ".12e1,<EOF>", 118))

    def test_119(self):
        self.assertTrue(TestLexer.test(".0e0", ".0e0,<EOF>", 119))

    def test_120(self):
        self.assertTrue(TestLexer.test("e0", "e0,<EOF>", 120))

    def test_121(self):
        self.assertTrue(TestLexer.test("e+0", "e,+,0,<EOF>", 121))

    def test_122(self):
        self.assertTrue(TestLexer.test(".01", ".,0,1,<EOF>", 122))

    def test_123(self):
        self.assertTrue(TestLexer.test("0.123_456", "0.123,_456,<EOF>", 123))

    def test_124(self):
        self.assertTrue(TestLexer.test("123E456_789", "123E456,_789,<EOF>", 124))

    def test_125(self):
        self.assertTrue(TestLexer.test("123_456E789", "123456E789,<EOF>", 125))

    def test_126(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 126))

    def test_127(self):
        self.assertTrue(TestLexer.test("abc0", "abc0,<EOF>", 127))

    def test_128(self):
        self.assertTrue(TestLexer.test("_abc", "_abc,<EOF>", 128))

    def test_129(self):
        self.assertTrue(TestLexer.test("0_abc", "0,_abc,<EOF>", 129))

    def test_130(self):
        self.assertTrue(TestLexer.test("__abc", "__abc,<EOF>", 130))

    def test_131(self):
        self.assertTrue(TestLexer.test("a b c", "a,b,c,<EOF>", 131))

    def test_132(self):
        self.assertTrue(TestLexer.test("_a_a_", "_a_a_,<EOF>", 132))

    def test_133(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 133))

    def test_134(self):
        self.assertTrue(TestLexer.test("false true", "false,true,<EOF>", 134))

    def test_135(self):
        self.assertTrue(TestLexer.test("true_false", "true_false,<EOF>", 135))

    def test_136(self):
        self.assertTrue(TestLexer.test(""" "Hi" """, "Hi,<EOF>", 136))

    def test_137(self):
        self.assertTrue(TestLexer.test(""" "Uhhh """, "Unclosed String: Uhhh ", 137))

    def test_138(self):
        self.assertTrue(TestLexer.test(""" "\\b \\f \\r \\n \\t \\' \\\ " """, "\\b \\f \\r \\n \\t \\' \\\ ,<EOF>", 138))

    def test_139(self):
        self.assertTrue(TestLexer.test(""" "\\"Hey\\"" """, '\\"Hey\\",<EOF>', 139))

    def test_140(self):
        self.assertTrue(TestLexer.test(""" "'\''\''''" """, "''''''',<EOF>", 140))

    def test_141(self):
        self.assertTrue(TestLexer.test("// Help me", "<EOF>", 141))

    def test_142(self):
        self.assertTrue(TestLexer.test("/* AAA \n BBB \n CCC */", "<EOF>", 142))

    def test_143(self):
        self.assertTrue(TestLexer.test(""" " ABC // DEF " """, " ABC // DEF ,<EOF>", 143))

    def test_144(self):
        self.assertTrue(TestLexer.test('"<EOF>"', "<EOF>,<EOF>", 144))

    def test_145(self):
        self.assertTrue(TestLexer.test(""" " /* " */ " """, " /* ,*,/,Unclosed String:  ", 145))

    def test_146(self):
        self.assertTrue(TestLexer.test(""" "\\a" """, "Illegal Escape In String: \\a", 146))

    def test_147(self):
        self.assertTrue(TestLexer.test(""" "\\n" """, "\\n,<EOF>", 147))

    def test_148(self):
        self.assertTrue(TestLexer.test(""" "\n" """, "Unclosed String: ", 148))

    def test_149(self):
        self.assertTrue(TestLexer.test("+", "+,<EOF>", 149))

    def test_150(self):
        self.assertTrue(TestLexer.test("-", "-,<EOF>", 150))

    def test_151(self):
        self.assertTrue(TestLexer.test("*", "*,<EOF>", 151))

    def test_152(self):
        self.assertTrue(TestLexer.test("/", "/,<EOF>", 152))

    def test_153(self):
        self.assertTrue(TestLexer.test("%", "%,<EOF>", 153))

    def test_154(self):
        self.assertTrue(TestLexer.test("!", "!,<EOF>", 154))

    def test_155(self):
        self.assertTrue(TestLexer.test("&&", "&&,<EOF>", 155))

    def test_156(self):
        self.assertTrue(TestLexer.test("||", "||,<EOF>", 156))

    def test_157(self):
        self.assertTrue(TestLexer.test("==", "==,<EOF>", 157))

    def test_158(self):
        self.assertTrue(TestLexer.test("!=", "!=,<EOF>", 158))

    def test_159(self):
        self.assertTrue(TestLexer.test("<", "<,<EOF>", 159))

    def test_160(self):
        self.assertTrue(TestLexer.test("<=", "<=,<EOF>", 160))

    def test_161(self):
        self.assertTrue(TestLexer.test(">", ">,<EOF>", 161))

    def test_162(self):
        self.assertTrue(TestLexer.test(">=", ">=,<EOF>", 162))

    def test_163(self):
        self.assertTrue(TestLexer.test("::", "::,<EOF>", 163))

    def test_164(self):
        self.assertTrue(TestLexer.test("(", "(,<EOF>", 164))

    def test_165(self):
        self.assertTrue(TestLexer.test(")", "),<EOF>", 165))

    def test_166(self):
        self.assertTrue(TestLexer.test("[", "[,<EOF>", 166))

    def test_167(self):
        self.assertTrue(TestLexer.test("]", "],<EOF>", 167))

    def test_168(self):
        self.assertTrue(TestLexer.test("{", "{,<EOF>", 168))

    def test_169(self):
        self.assertTrue(TestLexer.test("}", "},<EOF>", 169))

    def test_170(self):
        self.assertTrue(TestLexer.test(".", ".,<EOF>", 170))

    def test_171(self):
        self.assertTrue(TestLexer.test("=", "=,<EOF>", 171))

    def test_172(self):
        self.assertTrue(TestLexer.test(",", ",,<EOF>", 172))

    def test_173(self):
        self.assertTrue(TestLexer.test(":", ":,<EOF>", 173))

    def test_174(self):
        self.assertTrue(TestLexer.test(";", ";,<EOF>", 174))

    def test_175(self):
        self.assertTrue(TestLexer.test("auto // auto", "auto,<EOF>", 175))

    def test_176(self):
        self.assertTrue(TestLexer.test("break", "break,<EOF>", 176))

    def test_177(self):
        self.assertTrue(TestLexer.test("boolean", "boolean,<EOF>", 177))

    def test_178(self):
        self.assertTrue(TestLexer.test("do", "do,<EOF>", 178))

    def test_179(self):
        self.assertTrue(TestLexer.test("else", "else,<EOF>", 179))

    def test_180(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 180))

    def test_181(self):
        self.assertTrue(TestLexer.test("float", "float,<EOF>", 181))

    def test_182(self):
        self.assertTrue(TestLexer.test("for", "for,<EOF>", 182))

    def test_183(self):
        self.assertTrue(TestLexer.test("function", "function,<EOF>", 183))

    def test_184(self):
        self.assertTrue(TestLexer.test("if", "if,<EOF>", 184))

    def test_185(self):
        self.assertTrue(TestLexer.test("integer", "integer,<EOF>", 185))

    def test_186(self):
        self.assertTrue(TestLexer.test("return", "return,<EOF>", 186))

    def test_187(self):
        self.assertTrue(TestLexer.test("string", "string,<EOF>", 187))

    def test_188(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 188))

    def test_189(self):
        self.assertTrue(TestLexer.test("while", "while,<EOF>", 189))

    def test_190(self):
        self.assertTrue(TestLexer.test("void", "void,<EOF>", 190))

    def test_191(self):
        self.assertTrue(TestLexer.test("out", "out,<EOF>", 191))

    def test_192(self):
        self.assertTrue(TestLexer.test("continue", "continue,<EOF>", 192))

    def test_193(self):
        self.assertTrue(TestLexer.test("of", "of,<EOF>", 193))

    def test_194(self):
        self.assertTrue(TestLexer.test("inherit", "inherit,<EOF>", 194))

    def test_195(self):
        self.assertTrue(TestLexer.test("array", "array,<EOF>", 195))

    def test_196(self):
        self.assertTrue(
            TestLexer.test("for(i=while(true)do{1<=2.3;;;},", "for,(,i,=,while,(,true,),do,{,1,<=,2.3,;,;,;,},,,<EOF>", 196))

    def test_197(self):
        self.assertTrue(TestLexer.test("awesome cinematic experience every friday!!!",
                                       "awesome,cinematic,experience,every,friday,!,!,!,<EOF>", 197))

    def test_198(self):
        self.assertTrue(
            TestLexer.test(""" "I love this subject!" /* I don't. */ "I'm craving a good lesson everyday!" /* I'm lying */ """,
                           "I love this subject!,I'm craving a good lesson everyday!,<EOF>", 198))

    def test_199(self):
        self.assertTrue(TestLexer.test(
            """ex :  function  float  (  inherit  out kI :  boolean  ,  inherit  out Q :  void  )  inherit Nd3w { MPf :  array  [ 78 , 0 ]  of  float  = 0 - 0.50 + N (  )  + DEA (  )  / s (  )  -  ! 9 || 254_5_2_2_8. *  -  ! q || "" && mW8n %  !  !  -  - H - gN /  ! t (  )  % FVL *  -  - Q (  )  *  -  !  !  !  - "a" && 83 -  ( Fm :: j )  == x - l (  )  % 3_1_040_6 + W % "" / MT % cMu /  ! "" >  !  !  ! yb *  ! "" / EM <= 0 +  ! R / F (  )  - 8.5E-5967 -  !  - .0488e7 % XTni -  ! j * J ::  - X %  - sb (  )  ||  -  !  ! Y (  )  ;  } """,
            """ex,:,function,float,(,inherit,out,kI,:,boolean,,,inherit,out,Q,:,void,),inherit,Nd3w,{,MPf,:,array,[,78,,,0,],of,float,=,0,-,0.50,+,N,(,),+,DEA,(,),/,s,(,),-,!,9,||,2545228.,*,-,!,q,||,,&&,mW8n,%,!,!,-,-,H,-,gN,/,!,t,(,),%,FVL,*,-,-,Q,(,),*,-,!,!,!,-,a,&&,83,-,(,Fm,::,j,),==,x,-,l,(,),%,310406,+,W,%,,/,MT,%,cMu,/,!,,>,!,!,!,yb,*,!,,/,EM,<=,0,+,!,R,/,F,(,),-,8.5E-5967,-,!,-,.0488e7,%,XTni,-,!,j,*,J,::,-,X,%,-,sb,(,),||,-,!,!,Y,(,),;,},<EOF>""",
            199))

    def test_200(self):
        self.assertTrue(
            TestLexer.test("""
main: function          void ()
{
    a         : auto =    1 + 2 :: 3 * 		4 == 	5;
}
""", "main,:,function,void,(,),{,a,:,auto,=,1,+,2,::,3,*,4,==,5,;,},<EOF>", 200))

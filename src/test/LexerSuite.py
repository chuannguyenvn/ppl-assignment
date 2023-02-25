
import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def testLexer(self):
        self.assertTrue(TestLexer.test("^abc","Error Token ^", 101))
        self.assertTrue(TestLexer.test("##","Error Token #",102))
        self.assertTrue(TestLexer.test("a_b_c","a_b_c,<EOF>",103))
        self.assertTrue(TestLexer.test("AbC","AbC,<EOF>",104))
        self.assertTrue(TestLexer.test("A__________________0","A__________________0,<EOF>",105))
        self.assertTrue(TestLexer.test("A123_456_789","A123_456_789,<EOF>",106))
        self.assertTrue(TestLexer.test("auto","auto,<EOF>",107))
        self.assertTrue(TestLexer.test("autoo","autoo,<EOF>",108))
        self.assertTrue(TestLexer.test("IDENTIFIER","IDENTIFIER,<EOF>",109))
        self.assertTrue(TestLexer.test("main","main,<EOF>",110))
        self.assertTrue(TestLexer.test("01","0,1,<EOF>",111))
        self.assertTrue(TestLexer.test("0","0,<EOF>",112))
        self.assertTrue(TestLexer.test("9","9,<EOF>",113))
        self.assertTrue(TestLexer.test("19","19,<EOF>",114))
        self.assertTrue(TestLexer.test("_123","_123,<EOF>",115))
        self.assertTrue(TestLexer.test("1_2345","12345,<EOF>",116))
        self.assertTrue(TestLexer.test("12_34_56_78","12345678,<EOF>",117))
        self.assertTrue(TestLexer.test("1234_","1234,_,<EOF>",118))
        self.assertTrue(TestLexer.test("0ab","0,ab,<EOF>",119))
        self.assertTrue(TestLexer.test("123__456__789","123,__456__789,<EOF>",120))
        self.assertTrue(TestLexer.test("1_2_3.456","123.456,<EOF>",121))
        self.assertTrue(TestLexer.test("12_3.45_6","123.45,_6,<EOF>",122))
        self.assertTrue(TestLexer.test("123.456","123.456,<EOF>",123))
        self.assertTrue(TestLexer.test("0e0","0e0,<EOF>",124))
        self.assertTrue(TestLexer.test("07e0","0,7e0,<EOF>",125))
        self.assertTrue(TestLexer.test("1_2_3e","123,e,<EOF>",126))
        self.assertTrue(TestLexer.test(".25e+3",".25e+3,<EOF>",127))
        self.assertTrue(TestLexer.test(".25",".,25,<EOF>",128))
        self.assertTrue(TestLexer.test("e10","e10,<EOF>",129))
        self.assertTrue(TestLexer.test("0.25E-3","0.25E-3,<EOF>",130))
        self.assertTrue(TestLexer.test("1.175eE+-3","1.175,eE,+,-,3,<EOF>",131))
        self.assertTrue(TestLexer.test("123E+5","123E+5,<EOF>",132))
        self.assertTrue(TestLexer.test("true","true,<EOF>",133))
        self.assertTrue(TestLexer.test("false","false,<EOF>",134))
        self.assertTrue(TestLexer.test("truee","truee,<EOF>",135))
        self.assertTrue(TestLexer.test(""" "This string \\' contains \\' a tab symbol: \\t" ""","This string \\' contains \\' a tab symbol: \\t,<EOF>",136))
        self.assertTrue(TestLexer.test(""" "This string \\\\ contains \\\\ a backlash symbol: \\\\" ""","This string \\\\ contains \\\\ a backlash symbol: \\\\,<EOF>",137))
        self.assertTrue(TestLexer.test(""" "This string \\t contains \\t a backspace symbol: \\b" ""","This string \\t contains \\t a backspace symbol: \\b,<EOF>",138))
        self.assertTrue(TestLexer.test(""" "This string \\" contains \\" a form feed: \\f and carriage return: \\r" ""","This string \\\" contains \\\" a form feed: \\f and carriage return: \\r,<EOF>",139))
        self.assertTrue(TestLexer.test(""" "Endline symbol endline \\n" ""","Endline symbol endline \\n,<EOF>",140))
        self.assertTrue(TestLexer.test(""" "This string \\' contains \\' a tab symbol: \\t""","Unclosed String: This string \\' contains \\' a tab symbol: \\t",141))
        self.assertTrue(TestLexer.test(""" "This string \\\\ contains \\\\ a backlash symbol: \\\\""","Unclosed String: This string \\\\ contains \\\\ a backlash symbol: \\",142))
        self.assertTrue(TestLexer.test(""" "This string \\t contains \\t a backspace symbol: \\b""","Unclosed String: This string \\t contains \\t a backspace symbol: \\b",143))
        self.assertTrue(TestLexer.test(""" "This string \\" contains \\" a form feed: \\f and carriage return: \\r""","Unclosed String: This string \\\" contains \\\" a form feed: \\f and carriage return: \\r",144))
        self.assertTrue(TestLexer.test(""" "Endline symbol endline \\n""","Unclosed String: Endline symbol endline \\n",145))
        self.assertTrue(TestLexer.test(""" "This string \\' contains \\' a tab symbol: \a" ""","This string \\' contains \\' a tab symbol: \a,<EOF>",146))
        self.assertTrue(TestLexer.test(""" "This string \\\\ contains \\\\ a backlash symbol: \\a" ""","Illegal Escape In String: This string \\\\ contains \\\\ a backlash symbol: \\a",147))
        self.assertTrue(TestLexer.test(""" "This string \\\\\\ contains \\\\\\ a backlash symbol: \q" ""","Illegal Escape In String: This string \\\\\\ ",148))
        self.assertTrue(TestLexer.test(""" "This string \\t contains \\t a backspace symbol: \\q" ""","Illegal Escape In String: This string \\t contains \\t a backspace symbol: \\q",149))
        self.assertTrue(TestLexer.test(""" "This string \\" contains \\" a form feed: \w and carriage return: \r" ""","Illegal Escape In String: This string \\\" contains \\\" a form feed: \\w",150))
        self.assertTrue(TestLexer.test(""" "This string \" contains \" a form feed: \\w and carriage return: \\r" ""","This string ,contains,Illegal Escape In String:  a form feed: \\w",151))
        self.assertTrue(TestLexer.test(""" "This string \\" contains \\" a form feed: \endline and carriage return: \\r" ""","Illegal Escape In String: This string \\\" contains \\\" a form feed: \e",152))
        self.assertTrue(TestLexer.test(""" "This string is illegal \\endline" ""","Illegal Escape In String: This string is illegal \\e",153))
        self.assertTrue(TestLexer.test("+-123*/==79","+,-,123,*,/,==,79,<EOF>",154))
        self.assertTrue(TestLexer.test("9>=3.::<","9,>=,3.,::,<,<EOF>",155))
        self.assertTrue(TestLexer.test("&&&","&&,Error Token &",156))
        self.assertTrue(TestLexer.test(":::","::,:,<EOF>",157))
        self.assertTrue(TestLexer.test("<==","<=,=,<EOF>",158))
        self.assertTrue(TestLexer.test("!=!","!=,!,<EOF>",159))
        self.assertTrue(TestLexer.test("{{{)))","{,{,{,),),),<EOF>",160))
        self.assertTrue(TestLexer.test(";<=12_34true>=:",";,<=,1234,true,>=,:,<EOF>",161))
        self.assertTrue(TestLexer.test("123 > 456","123,>,456,<EOF>",162))
        self.assertTrue(TestLexer.test("{a - [(b] + c) / d % e - f >= {g && h} || j :: k, l {m (n [ p ] ) q } r == s - t ! u && v < 01234 }","{,a,-,[,(,b,],+,c,),/,d,%,e,-,f,>=,{,g,&&,h,},||,j,::,k,,,l,{,m,(,n,[,p,],),q,},r,==,s,-,t,!,u,&&,v,<,0,1234,},<EOF>",163))
        self.assertTrue(TestLexer.test("true1.0e","true1,.,0,e,<EOF>",164))
        self.assertTrue(TestLexer.test("9_Abc","9,_Abc,<EOF>",165))
        self.assertTrue(TestLexer.test(".1234",".,1234,<EOF>",166))
        self.assertTrue(TestLexer.test("true.0e","true,.,0,e,<EOF>",167))
        self.assertTrue(TestLexer.test("0_123_4","0,_123_4,<EOF>",168))
        self.assertTrue(TestLexer.test("\n\\","Error Token \\",169))
        self.assertTrue(TestLexer.test("conti,nue","conti,,,nue,<EOF>",170))
        self.assertTrue(TestLexer.test("integer a, b, c = 1, 2, 3;","integer,a,,,b,,,c,=,1,,,2,,,3,;,<EOF>",171))
        self.assertTrue(TestLexer.test("""float a "abc\\n" - integer || > <==""","float,a,abc\\n,-,integer,||,>,<=,=,<EOF>",172))
        self.assertTrue(TestLexer.test("integer?","integer,Error Token ?",173))
        self.assertTrue(TestLexer.test(""" "What does the fox says - ding ding ding \\" What is that?" ""","What does the fox says - ding ding ding \\\" What is that?,<EOF>",174))
        self.assertTrue(TestLexer.test("{1, 2, 3, 4, 5}","{,1,,,2,,,3,,,4,,,5,},<EOF>",175))
        self.assertTrue(TestLexer.test("""{"Principles", "Of", "Programming", "Language"}""","{,Principles,,,Of,,,Programming,,,Language,},<EOF>",176))
        self.assertTrue(TestLexer.test("x = readInteger();","x,=,readInteger,(,),;,<EOF>",177))
        self.assertTrue(TestLexer.test("autobreak","autobreak,<EOF>",178))
        self.assertTrue(TestLexer.test("aut0br3ak;","aut0br3ak,;,<EOF>",179))
        self.assertTrue(TestLexer.test("ID: [a-zA-Z_][a-zA-Z0-9_]*;","ID,:,[,a,-,zA,-,Z_,],[,a,-,zA,-,Z0,-,9,_,],*,;,<EOF>",180))
        self.assertTrue(TestLexer.test("a?b?c?","a,Error Token ?",181))
        self.assertTrue(TestLexer.test("{while (x < 5) x = x + 1;}","{,while,(,x,<,5,),x,=,x,+,1,;,},<EOF>",182))
        self.assertTrue(TestLexer.test("""foo(x + 2; 4.0 / y ");""","foo,(,x,+,2,;,4.0,/,y,Unclosed String: );",183))
        self.assertTrue(TestLexer.test("","<EOF>",184))
        self.assertTrue(TestLexer.test("                     ","<EOF>",185))
        self.assertTrue(TestLexer.test("// Watch the movie!","<EOF>",186))
        self.assertTrue(TestLexer.test("/* Hello /**/ I am comment block */","I,am,comment,block,*,/,<EOF>",187))
        self.assertTrue(TestLexer.test("// /* I am Tai.","<EOF>",188))
        self.assertTrue(TestLexer.test("// /* \n I am TAI.   ","I,am,TAI,.,<EOF>",189))
        self.assertTrue(TestLexer.test("// Watch \n // The // movie","<EOF>",190))
        self.assertTrue(TestLexer.test("checkPrime: function boolean (n : integer) {","checkPrime,:,function,boolean,(,n,:,integer,),{,<EOF>",191))
        self.assertTrue(TestLexer.test("if (n == 0 || n == 1) return false;","if,(,n,==,0,||,n,==,1,),return,false,;,<EOF>",192))
        self.assertTrue(TestLexer.test("i : integer;","i,:,integer,;,<EOF>",193))
        self.assertTrue(TestLexer.test("for(i = 2, i * i <= n, i = i + 1)","for,(,i,=,2,,,i,*,i,<=,n,,,i,=,i,+,1,),<EOF>",194))
        self.assertTrue(TestLexer.test("if (n % i == 0) return false;  ","if,(,n,%,i,==,0,),return,false,;,<EOF>",195))
        self.assertTrue(TestLexer.test("return true;}","return,true,;,},<EOF>",196))
        self.assertTrue(TestLexer.test("main: function void() {","main,:,function,void,(,),{,<EOF>",197))
        self.assertTrue(TestLexer.test("n : float = 7.5","n,:,float,=,7.5,<EOF>",198))
        self.assertTrue(TestLexer.test("""n = n + string_to_int("1.0");   ""","n,=,n,+,string_to_int,(,1.0,),;,<EOF>",199))
        self.assertTrue(TestLexer.test("checkPrime(n);}","checkPrime,(,n,),;,},<EOF>",100))
        
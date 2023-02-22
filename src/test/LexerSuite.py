
import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_L1__1_(self):
        self.assertTrue(TestLexer.test(r'''^abc''', r'''Error Token ^''', "_L1__1_"))


    def test_L2__2_(self):
        self.assertTrue(TestLexer.test(r'''##''', r'''Error Token #''', "_L2__2_"))


    def test_L3__3_(self):
        self.assertTrue(TestLexer.test(r'''a_b_c''', r'''a_b_c,<EOF>''', "_L3__3_"))


    def test_L4__4_(self):
        self.assertTrue(TestLexer.test(r'''AbC''', r'''AbC,<EOF>''', "_L4__4_"))


    def test_L5__5_(self):
        self.assertTrue(TestLexer.test(r'''A__________________0''', r'''A__________________0,<EOF>''', "_L5__5_"))


    def test_L6__6_(self):
        self.assertTrue(TestLexer.test(r'''A123_456_789''', r'''A123_456_789,<EOF>''', "_L6__6_"))


    def test_L7__7_(self):
        self.assertTrue(TestLexer.test(r'''auto''', r'''auto,<EOF>''', "_L7__7_"))


    def test_L8__8_(self):
        self.assertTrue(TestLexer.test(r'''autoo''', r'''autoo,<EOF>''', "_L8__8_"))


    def test_L9__9_(self):
        self.assertTrue(TestLexer.test(r'''IDENTIFIER''', r'''IDENTIFIER,<EOF>''', "_L9__9_"))


    def test_L10__10_(self):
        self.assertTrue(TestLexer.test(r'''main''', r'''main,<EOF>''', "_L10__10_"))


    def test_L11__11_(self):
        self.assertTrue(TestLexer.test(r'''01''', r'''0,1,<EOF>''', "_L11__11_"))


    def test_L12__12_(self):
        self.assertTrue(TestLexer.test(r'''0''', r'''0,<EOF>''', "_L12__12_"))


    def test_L13__13_(self):
        self.assertTrue(TestLexer.test(r'''9''', r'''9,<EOF>''', "_L13__13_"))


    def test_L14__14_(self):
        self.assertTrue(TestLexer.test(r'''19''', r'''19,<EOF>''', "_L14__14_"))


    def test_L15__15_(self):
        self.assertTrue(TestLexer.test(r'''_123''', r'''_123,<EOF>''', "_L15__15_"))


    def test_L16__16_(self):
        self.assertTrue(TestLexer.test(r'''1_2345''', r'''12345,<EOF>''', "_L16__16_"))


    def test_L17__17_(self):
        self.assertTrue(TestLexer.test(r'''12_34_56_78''', r'''12345678,<EOF>''', "_L17__17_"))


    def test_L18__18_(self):
        self.assertTrue(TestLexer.test(r'''1234_''', r'''1234,_,<EOF>''', "_L18__18_"))


    def test_L19__19_(self):
        self.assertTrue(TestLexer.test(r'''0ab''', r'''0,ab,<EOF>''', "_L19__19_"))


    def test_L20__20_(self):
        self.assertTrue(TestLexer.test(r'''123__456__789''', r'''123,__456__789,<EOF>''', "_L20__20_"))


    def test_L21__21_(self):
        self.assertTrue(TestLexer.test(r'''1_2_3.456''', r'''123.456,<EOF>''', "_L21__21_"))


    def test_L22__22_(self):
        self.assertTrue(TestLexer.test(r'''12_3.45_6''', r'''123.45,_6,<EOF>''', "_L22__22_"))


    def test_L23__23_(self):
        self.assertTrue(TestLexer.test(r'''123.456''', r'''123.456,<EOF>''', "_L23__23_"))


    def test_L24__24_(self):
        self.assertTrue(TestLexer.test(r'''0e0''', r'''0e0,<EOF>''', "_L24__24_"))


    def test_L25__25_(self):
        self.assertTrue(TestLexer.test(r'''07e0''', r'''0,7e0,<EOF>''', "_L25__25_"))


    def test_L26__26_(self):
        self.assertTrue(TestLexer.test(r'''1_2_3e''', r'''123,e,<EOF>''', "_L26__26_"))


    def test_L27__27_(self):
        self.assertTrue(TestLexer.test(r'''.25e+3''', r'''.25e+3,<EOF>''', "_L27__27_"))


    def test_L28__28_(self):
        self.assertTrue(TestLexer.test(r'''.25''', r'''.,25,<EOF>''', "_L28__28_"))


    def test_L29__29_(self):
        self.assertTrue(TestLexer.test(r'''e10''', r'''e10,<EOF>''', "_L29__29_"))


    def test_L30__30_(self):
        self.assertTrue(TestLexer.test(r'''0.25E-3''', r'''0.25E-3,<EOF>''', "_L30__30_"))


    def test_L31__31_(self):
        self.assertTrue(TestLexer.test(r'''1.175eE+-3''', r'''1.175,eE,+,-,3,<EOF>''', "_L31__31_"))


    def test_L32__32_(self):
        self.assertTrue(TestLexer.test(r'''123E+5''', r'''123E+5,<EOF>''', "_L32__32_"))


    def test_L33__33_(self):
        self.assertTrue(TestLexer.test(r'''true''', r'''true,<EOF>''', "_L33__33_"))


    def test_L34__34_(self):
        self.assertTrue(TestLexer.test(r'''false''', r'''false,<EOF>''', "_L34__34_"))


    def test_L35__35_(self):
        self.assertTrue(TestLexer.test(r'''truee''', r'''truee,<EOF>''', "_L35__35_"))


    def test_L36__36_(self):
        self.assertTrue(TestLexer.test(r'''"This string \\' contains \\' a tab symbol: \\t"''', r'''This string \\' contains \\' a tab symbol: \\t,<EOF>''', "_L36__36_"))


    def test_L37__37_(self):
        self.assertTrue(TestLexer.test(r'''"This string \\\\ contains \\\\ a backlash symbol: \\\\"''', r'''This string \\\\ contains \\\\ a backlash symbol: \\\\,<EOF>''', "_L37__37_"))


    def test_L38__38_(self):
        self.assertTrue(TestLexer.test(r'''"This string \\t contains \\t a backspace symbol: \\b"''', r'''This string \\t contains \\t a backspace symbol: \\b,<EOF>''', "_L38__38_"))


    def test_L39__39_(self):
        self.assertTrue(TestLexer.test(r'''"This string \\" contains \\" a form feed: \\f and carriage return: \\r"''', r'''This string \\" contains \\" a form feed: \\f and carriage return: \\r,<EOF>''', "_L39__39_"))


    def test_L40__40_(self):
        self.assertTrue(TestLexer.test(r'''"Endline symbol endline \\n"''', r'''Endline symbol endline \\n,<EOF>''', "_L40__40_"))


    def test_L41__41_(self):
        self.assertTrue(TestLexer.test(r'''"This string \\' contains \\' a tab symbol: \\t''', r'''Unclosed String: This string \\' contains \\' a tab symbol: \\t''', "_L41__41_"))


    def test_L42__42_(self):
        self.assertTrue(TestLexer.test(r'''"This string \\\\ contains \\\\ a backlash symbol: \\\\''', r'''Unclosed String: This string \\\\ contains \\\\ a backlash symbol: \\\\''', "_L42__42_"))


    def test_L43__43_(self):
        self.assertTrue(TestLexer.test(r'''"This string \\t contains \\t a backspace symbol: \\b''', r'''Unclosed String: This string \\t contains \\t a backspace symbol: \\b''', "_L43__43_"))


    def test_L44__44_(self):
        self.assertTrue(TestLexer.test(r'''"This string \\" contains \\" a form feed: \\f and carriage return: \\r''', r'''Unclosed String: This string \\" contains \\" a form feed: \\f and carriage return: \\r''', "_L44__44_"))


    def test_L45__45_(self):
        self.assertTrue(TestLexer.test(r'''"Endline symbol endline \\n''', r'''Unclosed String: Endline symbol endline \\n''', "_L45__45_"))


    def test_L46__54_(self):
        self.assertTrue(TestLexer.test(r'''+-123*/==79''', r'''+,-,123,*,/,==,79,<EOF>''', "_L46__54_"))


    def test_L47__55_(self):
        self.assertTrue(TestLexer.test(r'''9>=3.::<''', r'''9,>=,3.,::,<,<EOF>''', "_L47__55_"))


    def test_L48__56_(self):
        self.assertTrue(TestLexer.test(r'''&&&''', r'''&&,Error Token &''', "_L48__56_"))


    def test_L49__57_(self):
        self.assertTrue(TestLexer.test(r''':::''', r'''::,:,<EOF>''', "_L49__57_"))


    def test_L50__58_(self):
        self.assertTrue(TestLexer.test(r'''<==''', r'''<=,=,<EOF>''', "_L50__58_"))


    def test_L51__59_(self):
        self.assertTrue(TestLexer.test(r'''!=!''', r'''!=,!,<EOF>''', "_L51__59_"))


    def test_L52__60_(self):
        self.assertTrue(TestLexer.test(r'''{{{)))''', r'''{,{,{,),),),<EOF>''', "_L52__60_"))


    def test_L53__61_(self):
        self.assertTrue(TestLexer.test(r''';<=12_34true>=:''', r''';,<=,1234,true,>=,:,<EOF>''', "_L53__61_"))


    def test_L54__62_(self):
        self.assertTrue(TestLexer.test(r'''123 > 456''', r'''123,>,456,<EOF>''', "_L54__62_"))


    def test_L55__63_(self):
        self.assertTrue(TestLexer.test(r'''{a - [(b] + c) / d % e - f >= {g && h} || j :: k, l {m (n [ p ] ) q } r == s - t ! u && v < 01234 }''', r'''{,a,-,[,(,b,],+,c,),/,d,%,e,-,f,>=,{,g,&&,h,},||,j,::,k,,,l,{,m,(,n,[,p,],),q,},r,==,s,-,t,!,u,&&,v,<,0,1234,},<EOF>''', "_L55__63_"))


    def test_L56__64_(self):
        self.assertTrue(TestLexer.test(r'''true1.0e''', r'''true1,.,0,e,<EOF>''', "_L56__64_"))


    def test_L57__65_(self):
        self.assertTrue(TestLexer.test(r'''9_Abc''', r'''9,_Abc,<EOF>''', "_L57__65_"))


    def test_L58__66_(self):
        self.assertTrue(TestLexer.test(r'''.1234''', r'''.,1234,<EOF>''', "_L58__66_"))


    def test_L59__67_(self):
        self.assertTrue(TestLexer.test(r'''true.0e''', r'''true,.,0,e,<EOF>''', "_L59__67_"))


    def test_L60__68_(self):
        self.assertTrue(TestLexer.test(r'''0_123_4''', r'''0,_123_4,<EOF>''', "_L60__68_"))


    def test_L61__70_(self):
        self.assertTrue(TestLexer.test(r'''conti,nue''', r'''conti,,,nue,<EOF>''', "_L61__70_"))


    def test_L62__71_(self):
        self.assertTrue(TestLexer.test(r'''integer a, b, c = 1, 2, 3;''', r'''integer,a,,,b,,,c,=,1,,,2,,,3,;,<EOF>''', "_L62__71_"))


    def test_L63__72_(self):
        self.assertTrue(TestLexer.test(r'''float a "abc\\n" - integer || > <==''', r'''float,a,abc\\n,-,integer,||,>,<=,=,<EOF>''', "_L63__72_"))


    def test_L64__73_(self):
        self.assertTrue(TestLexer.test(r'''integer?''', r'''integer,Error Token ?''', "_L64__73_"))


    def test_L65__74_(self):
        self.assertTrue(TestLexer.test(r'''"What does the fox says - ding ding ding \\" What is that?"''', r'''What does the fox says - ding ding ding \\" What is that?,<EOF>''', "_L65__74_"))


    def test_L66__75_(self):
        self.assertTrue(TestLexer.test(r'''{1, 2, 3, 4, 5}''', r'''{,1,,,2,,,3,,,4,,,5,},<EOF>''', "_L66__75_"))


    def test_L67__76_(self):
        self.assertTrue(TestLexer.test(r'''{"Principles", "Of", "Programming", "Language"}''', r'''{,Principles,,,Of,,,Programming,,,Language,},<EOF>''', "_L67__76_"))


    def test_L68__77_(self):
        self.assertTrue(TestLexer.test(r'''x = readInteger();''', r'''x,=,readInteger,(,),;,<EOF>''', "_L68__77_"))


    def test_L69__78_(self):
        self.assertTrue(TestLexer.test(r'''autobreak''', r'''autobreak,<EOF>''', "_L69__78_"))


    def test_L70__79_(self):
        self.assertTrue(TestLexer.test(r'''aut0br3ak;''', r'''aut0br3ak,;,<EOF>''', "_L70__79_"))


    def test_L71__80_(self):
        self.assertTrue(TestLexer.test(r'''ID: [a-zA-Z_][a-zA-Z0-9_]*;''', r'''ID,:,[,a,-,zA,-,Z_,],[,a,-,zA,-,Z0,-,9,_,],*,;,<EOF>''', "_L71__80_"))


    def test_L72__81_(self):
        self.assertTrue(TestLexer.test(r'''a?b?c?''', r'''a,Error Token ?''', "_L72__81_"))


    def test_L73__82_(self):
        self.assertTrue(TestLexer.test(r'''{while (x < 5) x = x + 1;}''', r'''{,while,(,x,<,5,),x,=,x,+,1,;,},<EOF>''', "_L73__82_"))


    def test_L74__83_(self):
        self.assertTrue(TestLexer.test(r'''foo(x + 2; 4.0 / y ");''', r'''foo,(,x,+,2,;,4.0,/,y,Unclosed String: );''', "_L74__83_"))


    def test_L75__84_(self):
        self.assertTrue(TestLexer.test(r'''''', r'''<EOF>''', "_L75__84_"))


    def test_L76__85_(self):
        self.assertTrue(TestLexer.test(r'''                     ''', r'''<EOF>''', "_L76__85_"))


    def test_L77__86_(self):
        self.assertTrue(TestLexer.test(r'''// Watch the movie!''', r'''<EOF>''', "_L77__86_"))


    def test_L78__87_(self):
        self.assertTrue(TestLexer.test(r'''/* Hello /**/ I am comment block */''', r'''I,am,comment,block,*,/,<EOF>''', "_L78__87_"))


    def test_L79__88_(self):
        self.assertTrue(TestLexer.test(r'''// /* I am Tai.''', r'''<EOF>''', "_L79__88_"))


    def test_L80__89_(self):
        self.assertTrue(TestLexer.test(r'''// /* \n I am TAI.               ''', r'''I,am,TAI,.,<EOF>''', "_L80__89_"))


    def test_L81__90_(self):
        self.assertTrue(TestLexer.test(r'''// Watch \n // The // movie''', r'''<EOF>''', "_L81__90_"))


    def test_L82__91_(self):
        self.assertTrue(TestLexer.test(r'''checkPrime: function boolean (n : integer) {''', r'''checkPrime,:,function,boolean,(,n,:,integer,),{,<EOF>''', "_L82__91_"))


    def test_L83__92_(self):
        self.assertTrue(TestLexer.test(r'''if (n == 0 || n == 1) return false;''', r'''if,(,n,==,0,||,n,==,1,),return,false,;,<EOF>''', "_L83__92_"))


    def test_L84__93_(self):
        self.assertTrue(TestLexer.test(r'''i : integer;''', r'''i,:,integer,;,<EOF>''', "_L84__93_"))


    def test_L85__94_(self):
        self.assertTrue(TestLexer.test(r'''for(i = 2, i * i <= n, i = i + 1)''', r'''for,(,i,=,2,,,i,*,i,<=,n,,,i,=,i,+,1,),<EOF>''', "_L85__94_"))


    def test_L86__95_(self):
        self.assertTrue(TestLexer.test(r'''if (n % i == 0) return false;                 ''', r'''if,(,n,%,i,==,0,),return,false,;,<EOF>''', "_L86__95_"))


    def test_L87__96_(self):
        self.assertTrue(TestLexer.test(r'''return true;}''', r'''return,true,;,},<EOF>''', "_L87__96_"))


    def test_L88__97_(self):
        self.assertTrue(TestLexer.test(r'''main: function void() {''', r'''main,:,function,void,(,),{,<EOF>''', "_L88__97_"))


    def test_L89__98_(self):
        self.assertTrue(TestLexer.test(r'''n : float = 7.5''', r'''n,:,float,=,7.5,<EOF>''', "_L89__98_"))


    def test_L90__99_(self):
        self.assertTrue(TestLexer.test(r'''n = n + string_to_int("1.0");        ''', r'''n,=,n,+,string_to_int,(,1.0,),;,<EOF>''', "_L90__99_"))


    def test_L91__100_(self):
        self.assertTrue(TestLexer.test(r'''checkPrime(n);}''', r'''checkPrime,(,n,),;,},<EOF>''', "_L91__100_"))


    def test_L92___(self):
        self.assertTrue(TestLexer.test(r'''55.''', r'''55.,<EOF>''', "_L92___"))


    def test_L93___(self):
        self.assertTrue(TestLexer.test(r'''55__55''', r'''55,__55,<EOF>''', "_L93___"))


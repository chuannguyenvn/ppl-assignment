# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u0129\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\3\2\6\2D\n\2\r\2\16\2E\3\2\3\2")
        buf.write("\3\3\3\3\5\3L\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\7\5X\n\5\f\5\16\5[\13\5\3\6\5\6^\n\6\3\6\5\6a\n\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\7\7k\n\7\f\7\16\7n\13")
        buf.write("\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\tx\n\t\3\t\3\t\3")
        buf.write("\t\5\t}\n\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\5\13\u008e\n\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u009c\n\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\5\24\u00c5\n\24\3\24\3")
        buf.write("\24\3\24\3\25\3\25\7\25\u00cc\n\25\f\25\16\25\u00cf\13")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\7\26\u00d6\n\26\f\26\16\26")
        buf.write("\u00d9\13\26\3\27\3\27\3\27\5\27\u00de\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\7\30\u00e6\n\30\f\30\16\30\u00e9")
        buf.write("\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u00f1\n\31\f")
        buf.write("\31\16\31\u00f4\13\31\3\32\3\32\3\32\3\32\3\32\3\32\7")
        buf.write("\32\u00fc\n\32\f\32\16\32\u00ff\13\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\7\33\u0107\n\33\f\33\16\33\u010a\13\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\7\34\u0112\n\34\f\34\16\34")
        buf.write("\u0115\13\34\3\35\3\35\3\35\5\35\u011a\n\35\3\36\3\36")
        buf.write("\3\36\5\36\u011f\n\36\3\37\3\37\5\37\u0123\n\37\3 \3 ")
        buf.write("\3!\3!\3!\2\7.\60\62\64\66\"\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@\2\b\b\2\5\5\t\t")
        buf.write("\r\r\17\17\22\22\27\27\3\2 %\3\2\36\37\3\2\30\31\3\2\32")
        buf.write("\33\3\2\61\66\2\u0128\2C\3\2\2\2\4K\3\2\2\2\6M\3\2\2\2")
        buf.write("\bT\3\2\2\2\n]\3\2\2\2\fg\3\2\2\2\16o\3\2\2\2\20q\3\2")
        buf.write("\2\2\22\u0080\3\2\2\2\24\u008d\3\2\2\2\26\u008f\3\2\2")
        buf.write("\2\30\u0094\3\2\2\2\32\u009d\3\2\2\2\34\u00a9\3\2\2\2")
        buf.write("\36\u00af\3\2\2\2 \u00b7\3\2\2\2\"\u00ba\3\2\2\2$\u00bd")
        buf.write("\3\2\2\2&\u00c1\3\2\2\2(\u00c9\3\2\2\2*\u00d2\3\2\2\2")
        buf.write(",\u00dd\3\2\2\2.\u00df\3\2\2\2\60\u00ea\3\2\2\2\62\u00f5")
        buf.write("\3\2\2\2\64\u0100\3\2\2\2\66\u010b\3\2\2\28\u0119\3\2")
        buf.write("\2\2:\u011e\3\2\2\2<\u0122\3\2\2\2>\u0124\3\2\2\2@\u0126")
        buf.write("\3\2\2\2BD\5\4\3\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2")
        buf.write("\2\2FG\3\2\2\2GH\7\2\2\3H\3\3\2\2\2IL\5\6\4\2JL\5\20\t")
        buf.write("\2KI\3\2\2\2KJ\3\2\2\2L\5\3\2\2\2MN\5\f\7\2NO\7)\2\2O")
        buf.write("P\5\16\b\2PQ\7\'\2\2QR\5*\26\2RS\7*\2\2S\7\3\2\2\2TY\5")
        buf.write("\n\6\2UV\7(\2\2VX\5\n\6\2WU\3\2\2\2X[\3\2\2\2YW\3\2\2")
        buf.write("\2YZ\3\2\2\2Z\t\3\2\2\2[Y\3\2\2\2\\^\7\26\2\2]\\\3\2\2")
        buf.write("\2]^\3\2\2\2^`\3\2\2\2_a\7\23\2\2`_\3\2\2\2`a\3\2\2\2")
        buf.write("ab\3\2\2\2bc\7\61\2\2cd\7)\2\2de\5\16\b\2ef\7*\2\2f\13")
        buf.write("\3\2\2\2gl\7\61\2\2hi\7(\2\2ik\7\61\2\2jh\3\2\2\2kn\3")
        buf.write("\2\2\2lj\3\2\2\2lm\3\2\2\2m\r\3\2\2\2nl\3\2\2\2op\t\2")
        buf.write("\2\2p\17\3\2\2\2qr\7\61\2\2rs\7)\2\2st\7\13\2\2tu\5\16")
        buf.write("\b\2uw\7+\2\2vx\5\b\5\2wv\3\2\2\2wx\3\2\2\2xy\3\2\2\2")
        buf.write("y|\7,\2\2z{\7\26\2\2{}\7\61\2\2|z\3\2\2\2|}\3\2\2\2}~")
        buf.write("\3\2\2\2~\177\5\22\n\2\177\21\3\2\2\2\u0080\u0081\5(\25")
        buf.write("\2\u0081\23\3\2\2\2\u0082\u008e\5\26\f\2\u0083\u008e\5")
        buf.write("\26\f\2\u0084\u008e\5\30\r\2\u0085\u008e\5\32\16\2\u0086")
        buf.write("\u008e\5\34\17\2\u0087\u008e\5\36\20\2\u0088\u008e\5 ")
        buf.write("\21\2\u0089\u008e\5\"\22\2\u008a\u008e\5$\23\2\u008b\u008e")
        buf.write("\5&\24\2\u008c\u008e\5(\25\2\u008d\u0082\3\2\2\2\u008d")
        buf.write("\u0083\3\2\2\2\u008d\u0084\3\2\2\2\u008d\u0085\3\2\2\2")
        buf.write("\u008d\u0086\3\2\2\2\u008d\u0087\3\2\2\2\u008d\u0088\3")
        buf.write("\2\2\2\u008d\u0089\3\2\2\2\u008d\u008a\3\2\2\2\u008d\u008b")
        buf.write("\3\2\2\2\u008d\u008c\3\2\2\2\u008e\25\3\2\2\2\u008f\u0090")
        buf.write("\7\61\2\2\u0090\u0091\7\'\2\2\u0091\u0092\5,\27\2\u0092")
        buf.write("\u0093\7*\2\2\u0093\27\3\2\2\2\u0094\u0095\7\f\2\2\u0095")
        buf.write("\u0096\7+\2\2\u0096\u0097\5,\27\2\u0097\u0098\7,\2\2\u0098")
        buf.write("\u009b\5\24\13\2\u0099\u009a\7\7\2\2\u009a\u009c\5\24")
        buf.write("\13\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\31")
        buf.write("\3\2\2\2\u009d\u009e\7\n\2\2\u009e\u009f\7+\2\2\u009f")
        buf.write("\u00a0\7\61\2\2\u00a0\u00a1\7\'\2\2\u00a1\u00a2\5,\27")
        buf.write("\2\u00a2\u00a3\7(\2\2\u00a3\u00a4\5,\27\2\u00a4\u00a5")
        buf.write("\7(\2\2\u00a5\u00a6\5,\27\2\u00a6\u00a7\7,\2\2\u00a7\u00a8")
        buf.write("\5\24\13\2\u00a8\33\3\2\2\2\u00a9\u00aa\7\21\2\2\u00aa")
        buf.write("\u00ab\7+\2\2\u00ab\u00ac\5,\27\2\u00ac\u00ad\7,\2\2\u00ad")
        buf.write("\u00ae\5\24\13\2\u00ae\35\3\2\2\2\u00af\u00b0\7\6\2\2")
        buf.write("\u00b0\u00b1\5(\25\2\u00b1\u00b2\7\21\2\2\u00b2\u00b3")
        buf.write("\7+\2\2\u00b3\u00b4\5\24\13\2\u00b4\u00b5\7,\2\2\u00b5")
        buf.write("\u00b6\7*\2\2\u00b6\37\3\2\2\2\u00b7\u00b8\7\4\2\2\u00b8")
        buf.write("\u00b9\7*\2\2\u00b9!\3\2\2\2\u00ba\u00bb\7\24\2\2\u00bb")
        buf.write("\u00bc\7*\2\2\u00bc#\3\2\2\2\u00bd\u00be\7\16\2\2\u00be")
        buf.write("\u00bf\5,\27\2\u00bf\u00c0\7*\2\2\u00c0%\3\2\2\2\u00c1")
        buf.write("\u00c2\7\61\2\2\u00c2\u00c4\7+\2\2\u00c3\u00c5\5*\26\2")
        buf.write("\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\3")
        buf.write("\2\2\2\u00c6\u00c7\7,\2\2\u00c7\u00c8\7*\2\2\u00c8\'\3")
        buf.write("\2\2\2\u00c9\u00cd\7/\2\2\u00ca\u00cc\5\24\13\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2")
        buf.write("\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3\2\2\2\u00cf\u00cd\3")
        buf.write("\2\2\2\u00d0\u00d1\7\60\2\2\u00d1)\3\2\2\2\u00d2\u00d7")
        buf.write("\5,\27\2\u00d3\u00d4\7(\2\2\u00d4\u00d6\5,\27\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2")
        buf.write("\u00d7\u00d8\3\2\2\2\u00d8+\3\2\2\2\u00d9\u00d7\3\2\2")
        buf.write("\2\u00da\u00de\7\61\2\2\u00db\u00de\5> \2\u00dc\u00de")
        buf.write("\5.\30\2\u00dd\u00da\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00de-\3\2\2\2\u00df\u00e0\b\30\1\2\u00e0")
        buf.write("\u00e1\5\60\31\2\u00e1\u00e7\3\2\2\2\u00e2\u00e3\f\4\2")
        buf.write("\2\u00e3\u00e4\7&\2\2\u00e4\u00e6\5\60\31\2\u00e5\u00e2")
        buf.write("\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7")
        buf.write("\u00e8\3\2\2\2\u00e8/\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea")
        buf.write("\u00eb\b\31\1\2\u00eb\u00ec\5\62\32\2\u00ec\u00f2\3\2")
        buf.write("\2\2\u00ed\u00ee\f\4\2\2\u00ee\u00ef\t\3\2\2\u00ef\u00f1")
        buf.write("\5\62\32\2\u00f0\u00ed\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\61\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f5\u00f6\b\32\1\2\u00f6\u00f7\5\64\33")
        buf.write("\2\u00f7\u00fd\3\2\2\2\u00f8\u00f9\f\4\2\2\u00f9\u00fa")
        buf.write("\t\4\2\2\u00fa\u00fc\5\64\33\2\u00fb\u00f8\3\2\2\2\u00fc")
        buf.write("\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2")
        buf.write("\u00fe\63\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0101\b\33")
        buf.write("\1\2\u0101\u0102\5\66\34\2\u0102\u0108\3\2\2\2\u0103\u0104")
        buf.write("\f\4\2\2\u0104\u0105\t\5\2\2\u0105\u0107\5\66\34\2\u0106")
        buf.write("\u0103\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2")
        buf.write("\u0108\u0109\3\2\2\2\u0109\65\3\2\2\2\u010a\u0108\3\2")
        buf.write("\2\2\u010b\u010c\b\34\1\2\u010c\u010d\58\35\2\u010d\u0113")
        buf.write("\3\2\2\2\u010e\u010f\f\4\2\2\u010f\u0110\t\6\2\2\u0110")
        buf.write("\u0112\58\35\2\u0111\u010e\3\2\2\2\u0112\u0115\3\2\2\2")
        buf.write("\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\67\3\2")
        buf.write("\2\2\u0115\u0113\3\2\2\2\u0116\u0117\7\35\2\2\u0117\u011a")
        buf.write("\58\35\2\u0118\u011a\5:\36\2\u0119\u0116\3\2\2\2\u0119")
        buf.write("\u0118\3\2\2\2\u011a9\3\2\2\2\u011b\u011c\7\31\2\2\u011c")
        buf.write("\u011f\5:\36\2\u011d\u011f\5<\37\2\u011e\u011b\3\2\2\2")
        buf.write("\u011e\u011d\3\2\2\2\u011f;\3\2\2\2\u0120\u0123\5> \2")
        buf.write("\u0121\u0123\5@!\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2")
        buf.write("\2\2\u0123=\3\2\2\2\u0124\u0125\t\7\2\2\u0125?\3\2\2\2")
        buf.write("\u0126\u0127\3\2\2\2\u0127A\3\2\2\2\30EKY]`lw|\u008d\u009b")
        buf.write("\u00c4\u00cd\u00d7\u00dd\u00e7\u00f2\u00fd\u0108\u0113")
        buf.write("\u0119\u011e\u0122")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'break'", "'boolean'", "'do'", 
                     "'else'", "'false'", "'float'", "'for'", "'function'", 
                     "'if'", "'integer'", "'return'", "'string'", "'true'", 
                     "'while'", "'void'", "'out'", "'continue'", "'of'", 
                     "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'::'", "'='", "','", "':'", 
                     "';'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                      "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                      "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", 
                      "CONTINUE", "OF", "INHERIT", "ARRAY", "ADD", "MINUS", 
                      "STAR", "DIV", "MOD", "NOT", "AND_AND", "OR_OR", "EQUAL", 
                      "NOT_EQUAL", "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
                      "DOUBLE_COLON", "ASSIGN", "COMMA", "COLON", "SEMI_COLON", 
                      "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", 
                      "OPEN_BRACE", "CLOSE_BRACE", "IDENTIFIER", "INTEGER_LIT", 
                      "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", "ARRAY_LIT", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_variable_declaration = 2
    RULE_parameter_declaration_list = 3
    RULE_parameter_declaration = 4
    RULE_identifier_list = 5
    RULE_type_specifier = 6
    RULE_function_declaration = 7
    RULE_function_body = 8
    RULE_statement = 9
    RULE_assignment_statement = 10
    RULE_if_statement = 11
    RULE_for_statement = 12
    RULE_while_statement = 13
    RULE_do_while_statement = 14
    RULE_break_statement = 15
    RULE_continue_statement = 16
    RULE_return_statement = 17
    RULE_call_statement = 18
    RULE_block_statement = 19
    RULE_expression_list = 20
    RULE_expression = 21
    RULE_string_expression = 22
    RULE_relational_expression = 23
    RULE_logical_expression = 24
    RULE_adding_expression = 25
    RULE_multiplying_expression = 26
    RULE_negate_expression = 27
    RULE_sign_expression = 28
    RULE_operands = 29
    RULE_literal = 30
    RULE_function_call = 31

    ruleNames =  [ "program", "declaration", "variable_declaration", "parameter_declaration_list", 
                   "parameter_declaration", "identifier_list", "type_specifier", 
                   "function_declaration", "function_body", "statement", 
                   "assignment_statement", "if_statement", "for_statement", 
                   "while_statement", "do_while_statement", "break_statement", 
                   "continue_statement", "return_statement", "call_statement", 
                   "block_statement", "expression_list", "expression", "string_expression", 
                   "relational_expression", "logical_expression", "adding_expression", 
                   "multiplying_expression", "negate_expression", "sign_expression", 
                   "operands", "literal", "function_call" ]

    EOF = Token.EOF
    AUTO=1
    BREAK=2
    BOOLEAN=3
    DO=4
    ELSE=5
    FALSE=6
    FLOAT=7
    FOR=8
    FUNCTION=9
    IF=10
    INTEGER=11
    RETURN=12
    STRING=13
    TRUE=14
    WHILE=15
    VOID=16
    OUT=17
    CONTINUE=18
    OF=19
    INHERIT=20
    ARRAY=21
    ADD=22
    MINUS=23
    STAR=24
    DIV=25
    MOD=26
    NOT=27
    AND_AND=28
    OR_OR=29
    EQUAL=30
    NOT_EQUAL=31
    LESS=32
    LESS_EQUAL=33
    GREATER=34
    GREATER_EQUAL=35
    DOUBLE_COLON=36
    ASSIGN=37
    COMMA=38
    COLON=39
    SEMI_COLON=40
    OPEN_PAREN=41
    CLOSE_PAREN=42
    OPEN_BRACK=43
    CLOSE_BRACK=44
    OPEN_BRACE=45
    CLOSE_BRACE=46
    IDENTIFIER=47
    INTEGER_LIT=48
    FLOAT_LIT=49
    BOOLEAN_LIT=50
    STRING_LIT=51
    ARRAY_LIT=52
    WS=53
    ERROR_CHAR=54
    UNCLOSE_STRING=55
    ILLEGAL_ESCAPE=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MT22Parser.DeclarationContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.declaration()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MT22Parser.IDENTIFIER):
                    break

            self.state = 69
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(MT22Parser.Variable_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(MT22Parser.Function_declarationContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MT22Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.function_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(MT22Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def type_specifier(self):
            return self.getTypedRuleContext(MT22Parser.Type_specifierContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MT22Parser.Expression_listContext,0)


        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = MT22Parser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.identifier_list()
            self.state = 76
            self.match(MT22Parser.COLON)
            self.state = 77
            self.type_specifier()
            self.state = 78
            self.match(MT22Parser.ASSIGN)
            self.state = 79
            self.expression_list()
            self.state = 80
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declaration_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Parameter_declarationContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Parameter_declarationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameter_declaration_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declaration_list" ):
                return visitor.visitParameter_declaration_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declaration_list(self):

        localctx = MT22Parser.Parameter_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameter_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.parameter_declaration()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 83
                self.match(MT22Parser.COMMA)
                self.state = 84
                self.parameter_declaration()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def type_specifier(self):
            return self.getTypedRuleContext(MT22Parser.Type_specifierContext,0)


        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameter_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declaration" ):
                return visitor.visitParameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declaration(self):

        localctx = MT22Parser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 90
                self.match(MT22Parser.INHERIT)


            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 93
                self.match(MT22Parser.OUT)


            self.state = 96
            self.match(MT22Parser.IDENTIFIER)
            self.state = 97
            self.match(MT22Parser.COLON)
            self.state = 98
            self.type_specifier()
            self.state = 99
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.IDENTIFIER)
            else:
                return self.getToken(MT22Parser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_identifier_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier_list" ):
                return visitor.visitIdentifier_list(self)
            else:
                return visitor.visitChildren(self)




    def identifier_list(self):

        localctx = MT22Parser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(MT22Parser.IDENTIFIER)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 102
                self.match(MT22Parser.COMMA)
                self.state = 103
                self.match(MT22Parser.IDENTIFIER)
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_type_specifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_specifier" ):
                return visitor.visitType_specifier(self)
            else:
                return visitor.visitChildren(self)




    def type_specifier(self):

        localctx = MT22Parser.Type_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING) | (1 << MT22Parser.VOID) | (1 << MT22Parser.ARRAY))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.IDENTIFIER)
            else:
                return self.getToken(MT22Parser.IDENTIFIER, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def type_specifier(self):
            return self.getTypedRuleContext(MT22Parser.Type_specifierContext,0)


        def OPEN_PAREN(self):
            return self.getToken(MT22Parser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(MT22Parser.CLOSE_PAREN, 0)

        def function_body(self):
            return self.getTypedRuleContext(MT22Parser.Function_bodyContext,0)


        def parameter_declaration_list(self):
            return self.getTypedRuleContext(MT22Parser.Parameter_declaration_listContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = MT22Parser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(MT22Parser.IDENTIFIER)
            self.state = 112
            self.match(MT22Parser.COLON)
            self.state = 113
            self.match(MT22Parser.FUNCTION)
            self.state = 114
            self.type_specifier()
            self.state = 115
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.OUT) | (1 << MT22Parser.INHERIT) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 116
                self.parameter_declaration_list()


            self.state = 119
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 120
                self.match(MT22Parser.INHERIT)
                self.state = 121
                self.match(MT22Parser.IDENTIFIER)


            self.state = 124
            self.function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_statement(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_function_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_body" ):
                return visitor.visitFunction_body(self)
            else:
                return visitor.visitChildren(self)




    def function_body(self):

        localctx = MT22Parser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_function_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_statement(self):
            return self.getTypedRuleContext(MT22Parser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MT22Parser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MT22Parser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(MT22Parser.While_statementContext,0)


        def do_while_statement(self):
            return self.getTypedRuleContext(MT22Parser.Do_while_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MT22Parser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MT22Parser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MT22Parser.Return_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MT22Parser.Call_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.assignment_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 133
                self.do_while_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 134
                self.break_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 135
                self.continue_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 136
                self.return_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 137
                self.call_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 138
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = MT22Parser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(MT22Parser.IDENTIFIER)
            self.state = 142
            self.match(MT22Parser.ASSIGN)
            self.state = 143
            self.expression()
            self.state = 144
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def OPEN_PAREN(self):
            return self.getToken(MT22Parser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(MT22Parser.CLOSE_PAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MT22Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(MT22Parser.IF)
            self.state = 147
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 148
            self.expression()
            self.state = 149
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 150
            self.statement()
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 151
                self.match(MT22Parser.ELSE)
                self.state = 152
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def OPEN_PAREN(self):
            return self.getToken(MT22Parser.OPEN_PAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def CLOSE_PAREN(self):
            return self.getToken(MT22Parser.CLOSE_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MT22Parser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MT22Parser.FOR)
            self.state = 156
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 157
            self.match(MT22Parser.IDENTIFIER)
            self.state = 158
            self.match(MT22Parser.ASSIGN)
            self.state = 159
            self.expression()
            self.state = 160
            self.match(MT22Parser.COMMA)
            self.state = 161
            self.expression()
            self.state = 162
            self.match(MT22Parser.COMMA)
            self.state = 163
            self.expression()
            self.state = 164
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 165
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def OPEN_PAREN(self):
            return self.getToken(MT22Parser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(MT22Parser.CLOSE_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = MT22Parser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(MT22Parser.WHILE)
            self.state = 168
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 169
            self.expression()
            self.state = 170
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 171
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def OPEN_PAREN(self):
            return self.getToken(MT22Parser.OPEN_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(MT22Parser.CLOSE_PAREN, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_do_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_statement" ):
                return visitor.visitDo_while_statement(self)
            else:
                return visitor.visitChildren(self)




    def do_while_statement(self):

        localctx = MT22Parser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MT22Parser.DO)
            self.state = 174
            self.block_statement()
            self.state = 175
            self.match(MT22Parser.WHILE)
            self.state = 176
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 177
            self.statement()
            self.state = 178
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 179
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MT22Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MT22Parser.BREAK)
            self.state = 182
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MT22Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MT22Parser.CONTINUE)
            self.state = 185
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MT22Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MT22Parser.RETURN)
            self.state = 188
            self.expression()
            self.state = 189
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def OPEN_PAREN(self):
            return self.getToken(MT22Parser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(MT22Parser.CLOSE_PAREN, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MT22Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MT22Parser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(MT22Parser.IDENTIFIER)
            self.state = 192
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 193
                self.expression_list()


            self.state = 196
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 197
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(MT22Parser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MT22Parser.CLOSE_BRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = MT22Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(MT22Parser.OPEN_BRACE)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.OPEN_BRACE) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 200
                self.statement()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
            self.match(MT22Parser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = MT22Parser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expression()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 209
                self.match(MT22Parser.COMMA)
                self.state = 210
                self.expression()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(MT22Parser.LiteralContext,0)


        def string_expression(self):
            return self.getTypedRuleContext(MT22Parser.String_expressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MT22Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.string_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expression(self):
            return self.getTypedRuleContext(MT22Parser.Relational_expressionContext,0)


        def string_expression(self):
            return self.getTypedRuleContext(MT22Parser.String_expressionContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(MT22Parser.DOUBLE_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_string_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expression" ):
                return visitor.visitString_expression(self)
            else:
                return visitor.visitChildren(self)



    def string_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.String_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_string_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.relational_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.String_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_string_expression)
                    self.state = 224
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 225
                    self.match(MT22Parser.DOUBLE_COLON)
                    self.state = 226
                    self.relational_expression(0) 
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Relational_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expression(self):
            return self.getTypedRuleContext(MT22Parser.Logical_expressionContext,0)


        def relational_expression(self):
            return self.getTypedRuleContext(MT22Parser.Relational_expressionContext,0)


        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MT22Parser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(MT22Parser.LESS, 0)

        def LESS_EQUAL(self):
            return self.getToken(MT22Parser.LESS_EQUAL, 0)

        def GREATER(self):
            return self.getToken(MT22Parser.GREATER, 0)

        def GREATER_EQUAL(self):
            return self.getToken(MT22Parser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_relational_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expression" ):
                return visitor.visitRelational_expression(self)
            else:
                return visitor.visitChildren(self)



    def relational_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Relational_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_relational_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.logical_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Relational_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expression)
                    self.state = 235
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 236
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOT_EQUAL) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LESS_EQUAL) | (1 << MT22Parser.GREATER) | (1 << MT22Parser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 237
                    self.logical_expression(0) 
                self.state = 242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expression(self):
            return self.getTypedRuleContext(MT22Parser.Adding_expressionContext,0)


        def logical_expression(self):
            return self.getTypedRuleContext(MT22Parser.Logical_expressionContext,0)


        def AND_AND(self):
            return self.getToken(MT22Parser.AND_AND, 0)

        def OR_OR(self):
            return self.getToken(MT22Parser.OR_OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_logical_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expression" ):
                return visitor.visitLogical_expression(self)
            else:
                return visitor.visitChildren(self)



    def logical_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Logical_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_logical_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.adding_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 246
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 247
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND_AND or _la==MT22Parser.OR_OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 248
                    self.adding_expression(0) 
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expression(self):
            return self.getTypedRuleContext(MT22Parser.Multiplying_expressionContext,0)


        def adding_expression(self):
            return self.getTypedRuleContext(MT22Parser.Adding_expressionContext,0)


        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_adding_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expression" ):
                return visitor.visitAdding_expression(self)
            else:
                return visitor.visitChildren(self)



    def adding_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Adding_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_adding_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.multiplying_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Adding_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                    self.state = 257
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 258
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 259
                    self.multiplying_expression(0) 
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negate_expression(self):
            return self.getTypedRuleContext(MT22Parser.Negate_expressionContext,0)


        def multiplying_expression(self):
            return self.getTypedRuleContext(MT22Parser.Multiplying_expressionContext,0)


        def STAR(self):
            return self.getToken(MT22Parser.STAR, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_multiplying_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expression" ):
                return visitor.visitMultiplying_expression(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Multiplying_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_multiplying_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.negate_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                    self.state = 268
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 269
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.STAR or _la==MT22Parser.DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 270
                    self.negate_expression() 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Negate_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def negate_expression(self):
            return self.getTypedRuleContext(MT22Parser.Negate_expressionContext,0)


        def sign_expression(self):
            return self.getTypedRuleContext(MT22Parser.Sign_expressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_negate_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegate_expression" ):
                return visitor.visitNegate_expression(self)
            else:
                return visitor.visitChildren(self)




    def negate_expression(self):

        localctx = MT22Parser.Negate_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_negate_expression)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(MT22Parser.NOT)
                self.state = 277
                self.negate_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.sign_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def sign_expression(self):
            return self.getTypedRuleContext(MT22Parser.Sign_expressionContext,0)


        def operands(self):
            return self.getTypedRuleContext(MT22Parser.OperandsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_sign_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expression" ):
                return visitor.visitSign_expression(self)
            else:
                return visitor.visitChildren(self)




    def sign_expression(self):

        localctx = MT22Parser.Sign_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_sign_expression)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.match(MT22Parser.MINUS)
                self.state = 282
                self.sign_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.operands()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MT22Parser.LiteralContext,0)


        def function_call(self):
            return self.getTypedRuleContext(MT22Parser.Function_callContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = MT22Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_operands)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def INTEGER_LIT(self):
            return self.getToken(MT22Parser.INTEGER_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MT22Parser.FLOAT_LIT, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(MT22Parser.BOOLEAN_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MT22Parser.STRING_LIT, 0)

        def ARRAY_LIT(self):
            return self.getToken(MT22Parser.ARRAY_LIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MT22Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.IDENTIFIER) | (1 << MT22Parser.INTEGER_LIT) | (1 << MT22Parser.FLOAT_LIT) | (1 << MT22Parser.BOOLEAN_LIT) | (1 << MT22Parser.STRING_LIT) | (1 << MT22Parser.ARRAY_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = MT22Parser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.string_expression_sempred
        self._predicates[23] = self.relational_expression_sempred
        self._predicates[24] = self.logical_expression_sempred
        self._predicates[25] = self.adding_expression_sempred
        self._predicates[26] = self.multiplying_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def string_expression_sempred(self, localctx:String_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def relational_expression_sempred(self, localctx:Relational_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def adding_expression_sempred(self, localctx:Adding_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expression_sempred(self, localctx:Multiplying_expressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         





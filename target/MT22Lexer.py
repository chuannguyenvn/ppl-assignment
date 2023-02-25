# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01fd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\5\5\u0099\n\5\3\5\3\5\3\6\3\6\3\6\7\6\u00a0\n\6")
        buf.write("\f\6\16\6\u00a3\13\6\5\6\u00a5\n\6\3\7\3\7\7\7\u00a9\n")
        buf.write("\7\f\7\16\7\u00ac\13\7\3\b\3\b\5\b\u00b0\n\b\3\b\6\b\u00b3")
        buf.write("\n\b\r\b\16\b\u00b4\3\t\3\t\3\t\3\n\3\n\3\n\5\n\u00bd")
        buf.write("\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00c9")
        buf.write("\n\n\3\13\3\13\5\13\u00cd\n\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\5\f\u00e4\n\f\3\f\5\f\u00e7\n\f\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u00ed\n\f\3\r\3\r\3\r\7\r\u00f2\n\r\f\r\16\r\u00f5")
        buf.write("\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3")
        buf.write("*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\3>\3>\3?\3?\7?\u01b6\n?\f?\16?\u01b9\13")
        buf.write("?\3@\3@\3@\3@\7@\u01bf\n@\f@\16@\u01c2\13@\3@\3@\3A\3")
        buf.write("A\3A\3A\7A\u01ca\nA\fA\16A\u01cd\13A\3A\3A\3A\3A\3A\3")
        buf.write("B\6B\u01d5\nB\rB\16B\u01d6\3B\3B\3C\3C\5C\u01dd\nC\3D")
        buf.write("\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\7G\u01ea\nG\fG\16G\u01ed")
        buf.write("\13G\3G\5G\u01f0\nG\3G\3G\3H\3H\7H\u01f6\nH\fH\16H\u01f9")
        buf.write("\13H\3H\3H\3H\4\u00f3\u01cb\2I\3\2\5\2\7\2\t\2\13\2\r")
        buf.write("\2\17\2\21\3\23\4\25\5\27\2\31\6\33\7\35\b\37\t!\n#\13")
        buf.write("%\f\'\r)\16+\17-\20/\21\61\22\63\23\65\24\67\259\26;\27")
        buf.write("=\30?\31A\32C\33E\34G\35I\36K\37M O!Q\"S#U$W%Y&[\'](_")
        buf.write(")a*c+e,g-i.k/m\60o\61q\62s\63u\64w\65y\2{\2}\66\177\67")
        buf.write("\u00818\u00839\u0085\2\u0087\2\u0089\2\u008b:\u008d;\u008f")
        buf.write("<\3\2\16\3\2\63;\3\2\62;\4\2GGgg\4\2--//\5\2\f\f\16\17")
        buf.write("^^\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\16\17\5\2\13\f\17")
        buf.write("\17\"\"\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\5\3\n\f\16")
        buf.write("\17^^\2\u020f\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2")
        buf.write("\u0083\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\3\u0091\3\2\2\2\5\u0093\3\2\2\2\7\u0095\3\2\2")
        buf.write("\2\t\u0098\3\2\2\2\13\u00a4\3\2\2\2\r\u00a6\3\2\2\2\17")
        buf.write("\u00ad\3\2\2\2\21\u00b6\3\2\2\2\23\u00c8\3\2\2\2\25\u00cc")
        buf.write("\3\2\2\2\27\u00ec\3\2\2\2\31\u00ee\3\2\2\2\33\u00f9\3")
        buf.write("\2\2\2\35\u00fe\3\2\2\2\37\u0104\3\2\2\2!\u010c\3\2\2")
        buf.write("\2#\u010f\3\2\2\2%\u0114\3\2\2\2\'\u011a\3\2\2\2)\u0120")
        buf.write("\3\2\2\2+\u0124\3\2\2\2-\u012d\3\2\2\2/\u0130\3\2\2\2")
        buf.write("\61\u0138\3\2\2\2\63\u013f\3\2\2\2\65\u0146\3\2\2\2\67")
        buf.write("\u014b\3\2\2\29\u0151\3\2\2\2;\u0156\3\2\2\2=\u015a\3")
        buf.write("\2\2\2?\u0163\3\2\2\2A\u0166\3\2\2\2C\u016e\3\2\2\2E\u0174")
        buf.write("\3\2\2\2G\u0176\3\2\2\2I\u0178\3\2\2\2K\u017a\3\2\2\2")
        buf.write("M\u017c\3\2\2\2O\u017e\3\2\2\2Q\u0180\3\2\2\2S\u0183\3")
        buf.write("\2\2\2U\u0186\3\2\2\2W\u0189\3\2\2\2Y\u018c\3\2\2\2[\u018e")
        buf.write("\3\2\2\2]\u0191\3\2\2\2_\u0193\3\2\2\2a\u0196\3\2\2\2")
        buf.write("c\u0199\3\2\2\2e\u019b\3\2\2\2g\u019d\3\2\2\2i\u019f\3")
        buf.write("\2\2\2k\u01a1\3\2\2\2m\u01a3\3\2\2\2o\u01a5\3\2\2\2q\u01a7")
        buf.write("\3\2\2\2s\u01a9\3\2\2\2u\u01ab\3\2\2\2w\u01ad\3\2\2\2")
        buf.write("y\u01af\3\2\2\2{\u01b1\3\2\2\2}\u01b3\3\2\2\2\177\u01ba")
        buf.write("\3\2\2\2\u0081\u01c5\3\2\2\2\u0083\u01d4\3\2\2\2\u0085")
        buf.write("\u01dc\3\2\2\2\u0087\u01de\3\2\2\2\u0089\u01e1\3\2\2\2")
        buf.write("\u008b\u01e4\3\2\2\2\u008d\u01e7\3\2\2\2\u008f\u01f3\3")
        buf.write("\2\2\2\u0091\u0092\t\2\2\2\u0092\4\3\2\2\2\u0093\u0094")
        buf.write("\t\3\2\2\u0094\6\3\2\2\2\u0095\u0096\7a\2\2\u0096\b\3")
        buf.write("\2\2\2\u0097\u0099\5\7\4\2\u0098\u0097\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\5\5\3\2\u009b")
        buf.write("\n\3\2\2\2\u009c\u00a5\7\62\2\2\u009d\u00a1\5\3\2\2\u009e")
        buf.write("\u00a0\5\t\5\2\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2")
        buf.write("\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a5\3")
        buf.write("\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u009c\3\2\2\2\u00a4\u009d")
        buf.write("\3\2\2\2\u00a5\f\3\2\2\2\u00a6\u00aa\7\60\2\2\u00a7\u00a9")
        buf.write("\5\5\3\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\16\3\2\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ad\u00af\t\4\2\2\u00ae\u00b0\t\5\2\2")
        buf.write("\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3")
        buf.write("\2\2\2\u00b1\u00b3\5\5\3\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4")
        buf.write("\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("\20\3\2\2\2\u00b6\u00b7\5\13\6\2\u00b7\u00b8\b\t\2\2\u00b8")
        buf.write("\22\3\2\2\2\u00b9\u00ba\5\13\6\2\u00ba\u00bc\5\r\7\2\u00bb")
        buf.write("\u00bd\5\17\b\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2")
        buf.write("\2\u00bd\u00be\3\2\2\2\u00be\u00bf\b\n\3\2\u00bf\u00c9")
        buf.write("\3\2\2\2\u00c0\u00c1\5\13\6\2\u00c1\u00c2\5\r\7\2\u00c2")
        buf.write("\u00c3\b\n\4\2\u00c3\u00c9\3\2\2\2\u00c4\u00c5\5\13\6")
        buf.write("\2\u00c5\u00c6\5\17\b\2\u00c6\u00c7\b\n\5\2\u00c7\u00c9")
        buf.write("\3\2\2\2\u00c8\u00b9\3\2\2\2\u00c8\u00c0\3\2\2\2\u00c8")
        buf.write("\u00c4\3\2\2\2\u00c9\24\3\2\2\2\u00ca\u00cd\5\65\33\2")
        buf.write("\u00cb\u00cd\5%\23\2\u00cc\u00ca\3\2\2\2\u00cc\u00cb\3")
        buf.write("\2\2\2\u00cd\26\3\2\2\2\u00ce\u00cf\7^\2\2\u00cf\u00ed")
        buf.write("\7)\2\2\u00d0\u00d1\7^\2\2\u00d1\u00ed\7$\2\2\u00d2\u00d3")
        buf.write("\7^\2\2\u00d3\u00ed\7A\2\2\u00d4\u00d5\7^\2\2\u00d5\u00ed")
        buf.write("\7^\2\2\u00d6\u00d7\7^\2\2\u00d7\u00ed\7c\2\2\u00d8\u00d9")
        buf.write("\7^\2\2\u00d9\u00ed\7d\2\2\u00da\u00db\7^\2\2\u00db\u00ed")
        buf.write("\7h\2\2\u00dc\u00dd\7^\2\2\u00dd\u00ed\7p\2\2\u00de\u00df")
        buf.write("\7^\2\2\u00df\u00ed\7t\2\2\u00e0\u00e6\7^\2\2\u00e1\u00e3")
        buf.write("\7\17\2\2\u00e2\u00e4\7\f\2\2\u00e3\u00e2\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e7\7\f\2\2")
        buf.write("\u00e6\u00e1\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00ed\3")
        buf.write("\2\2\2\u00e8\u00e9\7^\2\2\u00e9\u00ed\7v\2\2\u00ea\u00eb")
        buf.write("\7^\2\2\u00eb\u00ed\7x\2\2\u00ec\u00ce\3\2\2\2\u00ec\u00d0")
        buf.write("\3\2\2\2\u00ec\u00d2\3\2\2\2\u00ec\u00d4\3\2\2\2\u00ec")
        buf.write("\u00d6\3\2\2\2\u00ec\u00d8\3\2\2\2\u00ec\u00da\3\2\2\2")
        buf.write("\u00ec\u00dc\3\2\2\2\u00ec\u00de\3\2\2\2\u00ec\u00e0\3")
        buf.write("\2\2\2\u00ec\u00e8\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\30")
        buf.write("\3\2\2\2\u00ee\u00f3\7$\2\2\u00ef\u00f2\5\27\f\2\u00f0")
        buf.write("\u00f2\n\6\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2")
        buf.write("\u00f2\u00f5\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f3\u00f1\3")
        buf.write("\2\2\2\u00f4\u00f6\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7")
        buf.write("\7$\2\2\u00f7\u00f8\b\r\6\2\u00f8\32\3\2\2\2\u00f9\u00fa")
        buf.write("\7c\2\2\u00fa\u00fb\7w\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7q\2\2\u00fd\34\3\2\2\2\u00fe\u00ff\7d\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100\u0101\7g\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7m\2\2\u0103\36\3\2\2\2\u0104\u0105\7d\2\2\u0105\u0106")
        buf.write("\7q\2\2\u0106\u0107\7q\2\2\u0107\u0108\7n\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109\u010a\7c\2\2\u010a\u010b\7p\2\2\u010b \3")
        buf.write("\2\2\2\u010c\u010d\7f\2\2\u010d\u010e\7q\2\2\u010e\"\3")
        buf.write("\2\2\2\u010f\u0110\7g\2\2\u0110\u0111\7n\2\2\u0111\u0112")
        buf.write("\7u\2\2\u0112\u0113\7g\2\2\u0113$\3\2\2\2\u0114\u0115")
        buf.write("\7h\2\2\u0115\u0116\7c\2\2\u0116\u0117\7n\2\2\u0117\u0118")
        buf.write("\7u\2\2\u0118\u0119\7g\2\2\u0119&\3\2\2\2\u011a\u011b")
        buf.write("\7h\2\2\u011b\u011c\7n\2\2\u011c\u011d\7q\2\2\u011d\u011e")
        buf.write("\7c\2\2\u011e\u011f\7v\2\2\u011f(\3\2\2\2\u0120\u0121")
        buf.write("\7h\2\2\u0121\u0122\7q\2\2\u0122\u0123\7t\2\2\u0123*\3")
        buf.write("\2\2\2\u0124\u0125\7h\2\2\u0125\u0126\7w\2\2\u0126\u0127")
        buf.write("\7p\2\2\u0127\u0128\7e\2\2\u0128\u0129\7v\2\2\u0129\u012a")
        buf.write("\7k\2\2\u012a\u012b\7q\2\2\u012b\u012c\7p\2\2\u012c,\3")
        buf.write("\2\2\2\u012d\u012e\7k\2\2\u012e\u012f\7h\2\2\u012f.\3")
        buf.write("\2\2\2\u0130\u0131\7k\2\2\u0131\u0132\7p\2\2\u0132\u0133")
        buf.write("\7v\2\2\u0133\u0134\7g\2\2\u0134\u0135\7i\2\2\u0135\u0136")
        buf.write("\7g\2\2\u0136\u0137\7t\2\2\u0137\60\3\2\2\2\u0138\u0139")
        buf.write("\7t\2\2\u0139\u013a\7g\2\2\u013a\u013b\7v\2\2\u013b\u013c")
        buf.write("\7w\2\2\u013c\u013d\7t\2\2\u013d\u013e\7p\2\2\u013e\62")
        buf.write("\3\2\2\2\u013f\u0140\7u\2\2\u0140\u0141\7v\2\2\u0141\u0142")
        buf.write("\7t\2\2\u0142\u0143\7k\2\2\u0143\u0144\7p\2\2\u0144\u0145")
        buf.write("\7i\2\2\u0145\64\3\2\2\2\u0146\u0147\7v\2\2\u0147\u0148")
        buf.write("\7t\2\2\u0148\u0149\7w\2\2\u0149\u014a\7g\2\2\u014a\66")
        buf.write("\3\2\2\2\u014b\u014c\7y\2\2\u014c\u014d\7j\2\2\u014d\u014e")
        buf.write("\7k\2\2\u014e\u014f\7n\2\2\u014f\u0150\7g\2\2\u01508\3")
        buf.write("\2\2\2\u0151\u0152\7x\2\2\u0152\u0153\7q\2\2\u0153\u0154")
        buf.write("\7k\2\2\u0154\u0155\7f\2\2\u0155:\3\2\2\2\u0156\u0157")
        buf.write("\7q\2\2\u0157\u0158\7w\2\2\u0158\u0159\7v\2\2\u0159<\3")
        buf.write("\2\2\2\u015a\u015b\7e\2\2\u015b\u015c\7q\2\2\u015c\u015d")
        buf.write("\7p\2\2\u015d\u015e\7v\2\2\u015e\u015f\7k\2\2\u015f\u0160")
        buf.write("\7p\2\2\u0160\u0161\7w\2\2\u0161\u0162\7g\2\2\u0162>\3")
        buf.write("\2\2\2\u0163\u0164\7q\2\2\u0164\u0165\7h\2\2\u0165@\3")
        buf.write("\2\2\2\u0166\u0167\7k\2\2\u0167\u0168\7p\2\2\u0168\u0169")
        buf.write("\7j\2\2\u0169\u016a\7g\2\2\u016a\u016b\7t\2\2\u016b\u016c")
        buf.write("\7k\2\2\u016c\u016d\7v\2\2\u016dB\3\2\2\2\u016e\u016f")
        buf.write("\7c\2\2\u016f\u0170\7t\2\2\u0170\u0171\7t\2\2\u0171\u0172")
        buf.write("\7c\2\2\u0172\u0173\7{\2\2\u0173D\3\2\2\2\u0174\u0175")
        buf.write("\7-\2\2\u0175F\3\2\2\2\u0176\u0177\7/\2\2\u0177H\3\2\2")
        buf.write("\2\u0178\u0179\7,\2\2\u0179J\3\2\2\2\u017a\u017b\7\61")
        buf.write("\2\2\u017bL\3\2\2\2\u017c\u017d\7\'\2\2\u017dN\3\2\2\2")
        buf.write("\u017e\u017f\7#\2\2\u017fP\3\2\2\2\u0180\u0181\7(\2\2")
        buf.write("\u0181\u0182\7(\2\2\u0182R\3\2\2\2\u0183\u0184\7~\2\2")
        buf.write("\u0184\u0185\7~\2\2\u0185T\3\2\2\2\u0186\u0187\7?\2\2")
        buf.write("\u0187\u0188\7?\2\2\u0188V\3\2\2\2\u0189\u018a\7#\2\2")
        buf.write("\u018a\u018b\7?\2\2\u018bX\3\2\2\2\u018c\u018d\7>\2\2")
        buf.write("\u018dZ\3\2\2\2\u018e\u018f\7>\2\2\u018f\u0190\7?\2\2")
        buf.write("\u0190\\\3\2\2\2\u0191\u0192\7@\2\2\u0192^\3\2\2\2\u0193")
        buf.write("\u0194\7@\2\2\u0194\u0195\7?\2\2\u0195`\3\2\2\2\u0196")
        buf.write("\u0197\7<\2\2\u0197\u0198\7<\2\2\u0198b\3\2\2\2\u0199")
        buf.write("\u019a\7*\2\2\u019ad\3\2\2\2\u019b\u019c\7+\2\2\u019c")
        buf.write("f\3\2\2\2\u019d\u019e\7]\2\2\u019eh\3\2\2\2\u019f\u01a0")
        buf.write("\7_\2\2\u01a0j\3\2\2\2\u01a1\u01a2\7}\2\2\u01a2l\3\2\2")
        buf.write("\2\u01a3\u01a4\7\177\2\2\u01a4n\3\2\2\2\u01a5\u01a6\7")
        buf.write("\60\2\2\u01a6p\3\2\2\2\u01a7\u01a8\7?\2\2\u01a8r\3\2\2")
        buf.write("\2\u01a9\u01aa\7.\2\2\u01aat\3\2\2\2\u01ab\u01ac\7<\2")
        buf.write("\2\u01acv\3\2\2\2\u01ad\u01ae\7=\2\2\u01aex\3\2\2\2\u01af")
        buf.write("\u01b0\t\7\2\2\u01b0z\3\2\2\2\u01b1\u01b2\t\b\2\2\u01b2")
        buf.write("|\3\2\2\2\u01b3\u01b7\5y=\2\u01b4\u01b6\5{>\2\u01b5\u01b4")
        buf.write("\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7")
        buf.write("\u01b8\3\2\2\2\u01b8~\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba")
        buf.write("\u01bb\7\61\2\2\u01bb\u01bc\7\61\2\2\u01bc\u01c0\3\2\2")
        buf.write("\2\u01bd\u01bf\n\t\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c2")
        buf.write("\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1")
        buf.write("\u01c3\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c4\b@\7\2")
        buf.write("\u01c4\u0080\3\2\2\2\u01c5\u01c6\7\61\2\2\u01c6\u01c7")
        buf.write("\7,\2\2\u01c7\u01cb\3\2\2\2\u01c8\u01ca\13\2\2\2\u01c9")
        buf.write("\u01c8\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01cb\u01c9\3\2\2\2\u01cc\u01ce\3\2\2\2\u01cd\u01cb\3")
        buf.write("\2\2\2\u01ce\u01cf\7,\2\2\u01cf\u01d0\7\61\2\2\u01d0\u01d1")
        buf.write("\3\2\2\2\u01d1\u01d2\bA\7\2\u01d2\u0082\3\2\2\2\u01d3")
        buf.write("\u01d5\t\n\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2")
        buf.write("\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8\3")
        buf.write("\2\2\2\u01d8\u01d9\bB\7\2\u01d9\u0084\3\2\2\2\u01da\u01dd")
        buf.write("\n\13\2\2\u01db\u01dd\5\u0087D\2\u01dc\u01da\3\2\2\2\u01dc")
        buf.write("\u01db\3\2\2\2\u01dd\u0086\3\2\2\2\u01de\u01df\7^\2\2")
        buf.write("\u01df\u01e0\t\f\2\2\u01e0\u0088\3\2\2\2\u01e1\u01e2\7")
        buf.write("^\2\2\u01e2\u01e3\n\f\2\2\u01e3\u008a\3\2\2\2\u01e4\u01e5")
        buf.write("\13\2\2\2\u01e5\u01e6\bF\b\2\u01e6\u008c\3\2\2\2\u01e7")
        buf.write("\u01eb\7$\2\2\u01e8\u01ea\5\u0085C\2\u01e9\u01e8\3\2\2")
        buf.write("\2\u01ea\u01ed\3\2\2\2\u01eb\u01e9\3\2\2\2\u01eb\u01ec")
        buf.write("\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ee")
        buf.write("\u01f0\t\r\2\2\u01ef\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2")
        buf.write("\u01f1\u01f2\bG\t\2\u01f2\u008e\3\2\2\2\u01f3\u01f7\7")
        buf.write("$\2\2\u01f4\u01f6\5\u0085C\2\u01f5\u01f4\3\2\2\2\u01f6")
        buf.write("\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u01fa\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa\u01fb\5")
        buf.write("\u0089E\2\u01fb\u01fc\bH\n\2\u01fc\u0090\3\2\2\2\31\2")
        buf.write("\u0098\u00a1\u00a4\u00aa\u00af\u00b4\u00bc\u00c8\u00cc")
        buf.write("\u00e3\u00e6\u00ec\u00f1\u00f3\u01b7\u01c0\u01cb\u01d6")
        buf.write("\u01dc\u01eb\u01ef\u01f7\13\3\t\2\3\n\3\3\n\4\3\n\5\3")
        buf.write("\r\6\b\2\2\3F\7\3G\b\3H\t")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER_LIT = 1
    FLOAT_LIT = 2
    BOOLEAN_LIT = 3
    STRING_LIT = 4
    AUTO = 5
    BREAK = 6
    BOOLEAN = 7
    DO = 8
    ELSE = 9
    FALSE = 10
    FLOAT = 11
    FOR = 12
    FUNCTION = 13
    IF = 14
    INTEGER = 15
    RETURN = 16
    STRING = 17
    TRUE = 18
    WHILE = 19
    VOID = 20
    OUT = 21
    CONTINUE = 22
    OF = 23
    INHERIT = 24
    ARRAY = 25
    ADD = 26
    MINUS = 27
    STAR = 28
    DIV = 29
    MOD = 30
    NOT = 31
    AND_AND = 32
    OR_OR = 33
    EQUAL = 34
    NOT_EQUAL = 35
    LESS = 36
    LESS_EQUAL = 37
    GREATER = 38
    GREATER_EQUAL = 39
    DOUBLE_COLON = 40
    OPEN_PAREN = 41
    CLOSE_PAREN = 42
    OPEN_BRACK = 43
    CLOSE_BRACK = 44
    OPEN_BRACE = 45
    CLOSE_BRACE = 46
    DOT = 47
    ASSIGN = 48
    COMMA = 49
    COLON = 50
    SEMI_COLON = 51
    IDENTIFIER = 52
    COMMENT_LINE = 53
    COMMENT_BLOCK = 54
    WS = 55
    ERROR_CHAR = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "'.'", "'='", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", "AUTO", 
            "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
            "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ADD", "MINUS", 
            "STAR", "DIV", "MOD", "NOT", "AND_AND", "OR_OR", "EQUAL", "NOT_EQUAL", 
            "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", "DOUBLE_COLON", 
            "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
            "CLOSE_BRACE", "DOT", "ASSIGN", "COMMA", "COLON", "SEMI_COLON", 
            "IDENTIFIER", "COMMENT_LINE", "COMMENT_BLOCK", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTEGER_START", "DIGIT", "UNDERSCORE", "INTEGER_CONTINUE", 
                  "INTEGER_PART", "DECIMAL_PART", "EXPONENT_PART", "INTEGER_LIT", 
                  "FLOAT_LIT", "BOOLEAN_LIT", "ESCAPE_SEQUENCE", "STRING_LIT", 
                  "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADD", "MINUS", "STAR", "DIV", "MOD", "NOT", 
                  "AND_AND", "OR_OR", "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
                  "GREATER", "GREATER_EQUAL", "DOUBLE_COLON", "OPEN_PAREN", 
                  "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
                  "CLOSE_BRACE", "DOT", "ASSIGN", "COMMA", "COLON", "SEMI_COLON", 
                  "IDENTIFIER_START", "IDENTIFIER_CONTINUE", "IDENTIFIER", 
                  "COMMENT_LINE", "COMMENT_BLOCK", "WS", "CHARACTER", "ESCAPE", 
                  "NOT_ESCAPE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.INTEGER_LIT_action 
            actions[8] = self.FLOAT_LIT_action 
            actions[11] = self.STRING_LIT_action 
            actions[68] = self.ERROR_CHAR_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

        if actionIndex == 3:
            self.text = self.text.replace('_','')
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                esc = ['\b', '\t', '\n', '\f', '\r', '\\']
                temp = str(self.text)
                if temp[-1] in esc:
                    raise UncloseString(temp[1:-1])
                else :
                    raise UncloseString(temp[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

                temp = str(self.text)
                raise IllegalEscape(temp[1:])

     



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
        buf.write("\u01db\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\5\5\u0097\n\5\3\5\3\5\3\6\3\6\3\6\7\6\u009e\n\6\f\6\16")
        buf.write("\6\u00a1\13\6\5\6\u00a3\n\6\3\7\3\7\7\7\u00a7\n\7\f\7")
        buf.write("\16\7\u00aa\13\7\3\b\3\b\5\b\u00ae\n\b\3\b\6\b\u00b1\n")
        buf.write("\b\r\b\16\b\u00b2\3\t\3\t\3\t\3\n\3\n\3\n\5\n\u00bb\n")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00c7\n")
        buf.write("\n\3\13\3\13\5\13\u00cb\n\13\3\f\3\f\3\f\3\r\3\r\3\r\7")
        buf.write("\r\u00d3\n\r\f\r\16\r\u00d6\13\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3")
        buf.write("-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3")
        buf.write("\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\7?\u0197")
        buf.write("\n?\f?\16?\u019a\13?\3@\3@\3@\3@\7@\u01a0\n@\f@\16@\u01a3")
        buf.write("\13@\3@\3@\3A\3A\3A\3A\7A\u01ab\nA\fA\16A\u01ae\13A\3")
        buf.write("A\3A\3A\3A\3A\3B\6B\u01b6\nB\rB\16B\u01b7\3B\3B\3C\3C")
        buf.write("\5C\u01be\nC\3D\3D\3D\3E\3E\3E\3F\3F\7F\u01c8\nF\fF\16")
        buf.write("F\u01cb\13F\3F\5F\u01ce\nF\3F\3F\3G\3G\7G\u01d4\nG\fG")
        buf.write("\16G\u01d7\13G\3G\3G\3G\4\u00d4\u01ac\2H\3\2\5\2\7\2\t")
        buf.write("\2\13\2\r\2\17\2\21\3\23\4\25\5\27\2\31\6\33\7\35\b\37")
        buf.write("\t!\n#\13%\f\'\r)\16+\17-\20/\21\61\22\63\23\65\24\67")
        buf.write("\259\26;\27=\30?\31A\32C\33E\34G\35I\36K\37M O!Q\"S#U")
        buf.write("$W%Y&[\'](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64w\65y\2{\2")
        buf.write("}\66\177\67\u00818\u00839\u0085\2\u0087\2\u0089:\u008b")
        buf.write(";\u008d<\3\2\16\3\2\63;\3\2\62;\4\2GGgg\4\2--//\n\2$$")
        buf.write("))^^ddhhppttvv\5\2\f\f\16\17^^\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\4\2\f\f\16\17\5\2\13\f\17\17\"\"\7\2\n\f\16\17$$)")
        buf.write(")^^\5\3\n\f\16\17^^\2\u01e1\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\3\u008f\3\2\2\2\5\u0091\3\2\2\2\7\u0093")
        buf.write("\3\2\2\2\t\u0096\3\2\2\2\13\u00a2\3\2\2\2\r\u00a4\3\2")
        buf.write("\2\2\17\u00ab\3\2\2\2\21\u00b4\3\2\2\2\23\u00c6\3\2\2")
        buf.write("\2\25\u00ca\3\2\2\2\27\u00cc\3\2\2\2\31\u00cf\3\2\2\2")
        buf.write("\33\u00da\3\2\2\2\35\u00df\3\2\2\2\37\u00e5\3\2\2\2!\u00ed")
        buf.write("\3\2\2\2#\u00f0\3\2\2\2%\u00f5\3\2\2\2\'\u00fb\3\2\2\2")
        buf.write(")\u0101\3\2\2\2+\u0105\3\2\2\2-\u010e\3\2\2\2/\u0111\3")
        buf.write("\2\2\2\61\u0119\3\2\2\2\63\u0120\3\2\2\2\65\u0127\3\2")
        buf.write("\2\2\67\u012c\3\2\2\29\u0132\3\2\2\2;\u0137\3\2\2\2=\u013b")
        buf.write("\3\2\2\2?\u0144\3\2\2\2A\u0147\3\2\2\2C\u014f\3\2\2\2")
        buf.write("E\u0155\3\2\2\2G\u0157\3\2\2\2I\u0159\3\2\2\2K\u015b\3")
        buf.write("\2\2\2M\u015d\3\2\2\2O\u015f\3\2\2\2Q\u0161\3\2\2\2S\u0164")
        buf.write("\3\2\2\2U\u0167\3\2\2\2W\u016a\3\2\2\2Y\u016d\3\2\2\2")
        buf.write("[\u016f\3\2\2\2]\u0172\3\2\2\2_\u0174\3\2\2\2a\u0177\3")
        buf.write("\2\2\2c\u017a\3\2\2\2e\u017c\3\2\2\2g\u017e\3\2\2\2i\u0180")
        buf.write("\3\2\2\2k\u0182\3\2\2\2m\u0184\3\2\2\2o\u0186\3\2\2\2")
        buf.write("q\u0188\3\2\2\2s\u018a\3\2\2\2u\u018c\3\2\2\2w\u018e\3")
        buf.write("\2\2\2y\u0190\3\2\2\2{\u0192\3\2\2\2}\u0194\3\2\2\2\177")
        buf.write("\u019b\3\2\2\2\u0081\u01a6\3\2\2\2\u0083\u01b5\3\2\2\2")
        buf.write("\u0085\u01bd\3\2\2\2\u0087\u01bf\3\2\2\2\u0089\u01c2\3")
        buf.write("\2\2\2\u008b\u01c5\3\2\2\2\u008d\u01d1\3\2\2\2\u008f\u0090")
        buf.write("\t\2\2\2\u0090\4\3\2\2\2\u0091\u0092\t\3\2\2\u0092\6\3")
        buf.write("\2\2\2\u0093\u0094\7a\2\2\u0094\b\3\2\2\2\u0095\u0097")
        buf.write("\5\7\4\2\u0096\u0095\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u0099\5\5\3\2\u0099\n\3\2\2\2\u009a")
        buf.write("\u00a3\7\62\2\2\u009b\u009f\5\3\2\2\u009c\u009e\5\t\5")
        buf.write("\2\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a2\u009a\3\2\2\2\u00a2\u009b\3\2\2\2")
        buf.write("\u00a3\f\3\2\2\2\u00a4\u00a8\7\60\2\2\u00a5\u00a7\5\5")
        buf.write("\3\2\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\16\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\u00ad\t\4\2\2\u00ac\u00ae\t\5\2\2\u00ad")
        buf.write("\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2")
        buf.write("\u00af\u00b1\5\5\3\2\u00b0\u00af\3\2\2\2\u00b1\u00b2\3")
        buf.write("\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\20")
        buf.write("\3\2\2\2\u00b4\u00b5\5\13\6\2\u00b5\u00b6\b\t\2\2\u00b6")
        buf.write("\22\3\2\2\2\u00b7\u00b8\5\13\6\2\u00b8\u00ba\5\r\7\2\u00b9")
        buf.write("\u00bb\5\17\b\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2")
        buf.write("\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\b\n\3\2\u00bd\u00c7")
        buf.write("\3\2\2\2\u00be\u00bf\5\13\6\2\u00bf\u00c0\5\r\7\2\u00c0")
        buf.write("\u00c1\b\n\4\2\u00c1\u00c7\3\2\2\2\u00c2\u00c3\5\13\6")
        buf.write("\2\u00c3\u00c4\5\17\b\2\u00c4\u00c5\b\n\5\2\u00c5\u00c7")
        buf.write("\3\2\2\2\u00c6\u00b7\3\2\2\2\u00c6\u00be\3\2\2\2\u00c6")
        buf.write("\u00c2\3\2\2\2\u00c7\24\3\2\2\2\u00c8\u00cb\5\65\33\2")
        buf.write("\u00c9\u00cb\5%\23\2\u00ca\u00c8\3\2\2\2\u00ca\u00c9\3")
        buf.write("\2\2\2\u00cb\26\3\2\2\2\u00cc\u00cd\7^\2\2\u00cd\u00ce")
        buf.write("\t\6\2\2\u00ce\30\3\2\2\2\u00cf\u00d4\7$\2\2\u00d0\u00d3")
        buf.write("\5\27\f\2\u00d1\u00d3\n\7\2\2\u00d2\u00d0\3\2\2\2\u00d2")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d4\u00d2\3\2\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00d4\3")
        buf.write("\2\2\2\u00d7\u00d8\7$\2\2\u00d8\u00d9\b\r\6\2\u00d9\32")
        buf.write("\3\2\2\2\u00da\u00db\7c\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00dd\u00de\7q\2\2\u00de\34\3\2\2\2\u00df\u00e0")
        buf.write("\7d\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3")
        buf.write("\7c\2\2\u00e3\u00e4\7m\2\2\u00e4\36\3\2\2\2\u00e5\u00e6")
        buf.write("\7d\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7n\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec \3\2\2\2\u00ed\u00ee\7f\2\2\u00ee\u00ef")
        buf.write("\7q\2\2\u00ef\"\3\2\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7n\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4\7g\2\2\u00f4$\3")
        buf.write("\2\2\2\u00f5\u00f6\7h\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8")
        buf.write("\7n\2\2\u00f8\u00f9\7u\2\2\u00f9\u00fa\7g\2\2\u00fa&\3")
        buf.write("\2\2\2\u00fb\u00fc\7h\2\2\u00fc\u00fd\7n\2\2\u00fd\u00fe")
        buf.write("\7q\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7v\2\2\u0100(\3")
        buf.write("\2\2\2\u0101\u0102\7h\2\2\u0102\u0103\7q\2\2\u0103\u0104")
        buf.write("\7t\2\2\u0104*\3\2\2\2\u0105\u0106\7h\2\2\u0106\u0107")
        buf.write("\7w\2\2\u0107\u0108\7p\2\2\u0108\u0109\7e\2\2\u0109\u010a")
        buf.write("\7v\2\2\u010a\u010b\7k\2\2\u010b\u010c\7q\2\2\u010c\u010d")
        buf.write("\7p\2\2\u010d,\3\2\2\2\u010e\u010f\7k\2\2\u010f\u0110")
        buf.write("\7h\2\2\u0110.\3\2\2\2\u0111\u0112\7k\2\2\u0112\u0113")
        buf.write("\7p\2\2\u0113\u0114\7v\2\2\u0114\u0115\7g\2\2\u0115\u0116")
        buf.write("\7i\2\2\u0116\u0117\7g\2\2\u0117\u0118\7t\2\2\u0118\60")
        buf.write("\3\2\2\2\u0119\u011a\7t\2\2\u011a\u011b\7g\2\2\u011b\u011c")
        buf.write("\7v\2\2\u011c\u011d\7w\2\2\u011d\u011e\7t\2\2\u011e\u011f")
        buf.write("\7p\2\2\u011f\62\3\2\2\2\u0120\u0121\7u\2\2\u0121\u0122")
        buf.write("\7v\2\2\u0122\u0123\7t\2\2\u0123\u0124\7k\2\2\u0124\u0125")
        buf.write("\7p\2\2\u0125\u0126\7i\2\2\u0126\64\3\2\2\2\u0127\u0128")
        buf.write("\7v\2\2\u0128\u0129\7t\2\2\u0129\u012a\7w\2\2\u012a\u012b")
        buf.write("\7g\2\2\u012b\66\3\2\2\2\u012c\u012d\7y\2\2\u012d\u012e")
        buf.write("\7j\2\2\u012e\u012f\7k\2\2\u012f\u0130\7n\2\2\u0130\u0131")
        buf.write("\7g\2\2\u01318\3\2\2\2\u0132\u0133\7x\2\2\u0133\u0134")
        buf.write("\7q\2\2\u0134\u0135\7k\2\2\u0135\u0136\7f\2\2\u0136:\3")
        buf.write("\2\2\2\u0137\u0138\7q\2\2\u0138\u0139\7w\2\2\u0139\u013a")
        buf.write("\7v\2\2\u013a<\3\2\2\2\u013b\u013c\7e\2\2\u013c\u013d")
        buf.write("\7q\2\2\u013d\u013e\7p\2\2\u013e\u013f\7v\2\2\u013f\u0140")
        buf.write("\7k\2\2\u0140\u0141\7p\2\2\u0141\u0142\7w\2\2\u0142\u0143")
        buf.write("\7g\2\2\u0143>\3\2\2\2\u0144\u0145\7q\2\2\u0145\u0146")
        buf.write("\7h\2\2\u0146@\3\2\2\2\u0147\u0148\7k\2\2\u0148\u0149")
        buf.write("\7p\2\2\u0149\u014a\7j\2\2\u014a\u014b\7g\2\2\u014b\u014c")
        buf.write("\7t\2\2\u014c\u014d\7k\2\2\u014d\u014e\7v\2\2\u014eB\3")
        buf.write("\2\2\2\u014f\u0150\7c\2\2\u0150\u0151\7t\2\2\u0151\u0152")
        buf.write("\7t\2\2\u0152\u0153\7c\2\2\u0153\u0154\7{\2\2\u0154D\3")
        buf.write("\2\2\2\u0155\u0156\7-\2\2\u0156F\3\2\2\2\u0157\u0158\7")
        buf.write("/\2\2\u0158H\3\2\2\2\u0159\u015a\7,\2\2\u015aJ\3\2\2\2")
        buf.write("\u015b\u015c\7\61\2\2\u015cL\3\2\2\2\u015d\u015e\7\'\2")
        buf.write("\2\u015eN\3\2\2\2\u015f\u0160\7#\2\2\u0160P\3\2\2\2\u0161")
        buf.write("\u0162\7(\2\2\u0162\u0163\7(\2\2\u0163R\3\2\2\2\u0164")
        buf.write("\u0165\7~\2\2\u0165\u0166\7~\2\2\u0166T\3\2\2\2\u0167")
        buf.write("\u0168\7?\2\2\u0168\u0169\7?\2\2\u0169V\3\2\2\2\u016a")
        buf.write("\u016b\7#\2\2\u016b\u016c\7?\2\2\u016cX\3\2\2\2\u016d")
        buf.write("\u016e\7>\2\2\u016eZ\3\2\2\2\u016f\u0170\7>\2\2\u0170")
        buf.write("\u0171\7?\2\2\u0171\\\3\2\2\2\u0172\u0173\7@\2\2\u0173")
        buf.write("^\3\2\2\2\u0174\u0175\7@\2\2\u0175\u0176\7?\2\2\u0176")
        buf.write("`\3\2\2\2\u0177\u0178\7<\2\2\u0178\u0179\7<\2\2\u0179")
        buf.write("b\3\2\2\2\u017a\u017b\7*\2\2\u017bd\3\2\2\2\u017c\u017d")
        buf.write("\7+\2\2\u017df\3\2\2\2\u017e\u017f\7]\2\2\u017fh\3\2\2")
        buf.write("\2\u0180\u0181\7_\2\2\u0181j\3\2\2\2\u0182\u0183\7}\2")
        buf.write("\2\u0183l\3\2\2\2\u0184\u0185\7\177\2\2\u0185n\3\2\2\2")
        buf.write("\u0186\u0187\7\60\2\2\u0187p\3\2\2\2\u0188\u0189\7?\2")
        buf.write("\2\u0189r\3\2\2\2\u018a\u018b\7.\2\2\u018bt\3\2\2\2\u018c")
        buf.write("\u018d\7<\2\2\u018dv\3\2\2\2\u018e\u018f\7=\2\2\u018f")
        buf.write("x\3\2\2\2\u0190\u0191\t\b\2\2\u0191z\3\2\2\2\u0192\u0193")
        buf.write("\t\t\2\2\u0193|\3\2\2\2\u0194\u0198\5y=\2\u0195\u0197")
        buf.write("\5{>\2\u0196\u0195\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199~\3\2\2\2\u019a\u0198")
        buf.write("\3\2\2\2\u019b\u019c\7\61\2\2\u019c\u019d\7\61\2\2\u019d")
        buf.write("\u01a1\3\2\2\2\u019e\u01a0\n\n\2\2\u019f\u019e\3\2\2\2")
        buf.write("\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3")
        buf.write("\2\2\2\u01a2\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5")
        buf.write("\b@\7\2\u01a5\u0080\3\2\2\2\u01a6\u01a7\7\61\2\2\u01a7")
        buf.write("\u01a8\7,\2\2\u01a8\u01ac\3\2\2\2\u01a9\u01ab\13\2\2\2")
        buf.write("\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01ad\3")
        buf.write("\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01af\3\2\2\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01af\u01b0\7,\2\2\u01b0\u01b1\7\61\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b3\bA\7\2\u01b3\u0082\3\2\2\2")
        buf.write("\u01b4\u01b6\t\13\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01ba\bB\7\2\u01ba\u0084\3\2\2\2")
        buf.write("\u01bb\u01be\n\f\2\2\u01bc\u01be\5\27\f\2\u01bd\u01bb")
        buf.write("\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be\u0086\3\2\2\2\u01bf")
        buf.write("\u01c0\7^\2\2\u01c0\u01c1\n\6\2\2\u01c1\u0088\3\2\2\2")
        buf.write("\u01c2\u01c3\13\2\2\2\u01c3\u01c4\bE\b\2\u01c4\u008a\3")
        buf.write("\2\2\2\u01c5\u01c9\7$\2\2\u01c6\u01c8\5\u0085C\2\u01c7")
        buf.write("\u01c6\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01c9\u01ca\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9\3")
        buf.write("\2\2\2\u01cc\u01ce\t\r\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01cf")
        buf.write("\3\2\2\2\u01cf\u01d0\bF\t\2\u01d0\u008c\3\2\2\2\u01d1")
        buf.write("\u01d5\7$\2\2\u01d2\u01d4\5\u0085C\2\u01d3\u01d2\3\2\2")
        buf.write("\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6")
        buf.write("\3\2\2\2\u01d6\u01d8\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8")
        buf.write("\u01d9\5\u0087D\2\u01d9\u01da\bG\n\2\u01da\u008e\3\2\2")
        buf.write("\2\26\2\u0096\u009f\u00a2\u00a8\u00ad\u00b2\u00ba\u00c6")
        buf.write("\u00ca\u00d2\u00d4\u0198\u01a1\u01ac\u01b7\u01bd\u01c9")
        buf.write("\u01cd\u01d5\13\3\t\2\3\n\3\3\n\4\3\n\5\3\r\6\b\2\2\3")
        buf.write("E\7\3F\b\3G\t")
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
                  "FLOAT_LIT", "BOOLEAN_LIT", "ESCAPE", "STRING_LIT", "AUTO", 
                  "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", 
                  "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
                  "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                  "ADD", "MINUS", "STAR", "DIV", "MOD", "NOT", "AND_AND", 
                  "OR_OR", "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", "GREATER", 
                  "GREATER_EQUAL", "DOUBLE_COLON", "OPEN_PAREN", "CLOSE_PAREN", 
                  "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", 
                  "DOT", "ASSIGN", "COMMA", "COLON", "SEMI_COLON", "IDENTIFIER_START", 
                  "IDENTIFIER_CONTINUE", "IDENTIFIER", "COMMENT_LINE", "COMMENT_BLOCK", 
                  "WS", "CHARACTER", "NOT_ESCAPE", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
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

     



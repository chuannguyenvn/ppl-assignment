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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u0212\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\7\63\u0152\n\63")
        buf.write("\f\63\16\63\u0155\13\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\5\67\u015e\n\67\3\67\3\67\38\38\38\78\u0165\n8\f")
        buf.write("8\168\u0168\138\58\u016a\n8\39\39\79\u016e\n9\f9\169\u0171")
        buf.write("\139\3:\3:\5:\u0175\n:\3:\6:\u0178\n:\r:\16:\u0179\3;")
        buf.write("\3;\3;\3<\3<\3<\5<\u0182\n<\3<\3<\3<\3<\3<\3<\3<\3<\3")
        buf.write("<\3<\5<\u018e\n<\3=\3=\5=\u0192\n=\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u01a9\n")
        buf.write(">\3>\5>\u01ac\n>\3>\3>\3>\3>\5>\u01b2\n>\3?\3?\3?\7?\u01b7")
        buf.write("\n?\f?\16?\u01ba\13?\3?\3?\3?\3@\3@\3@\3@\5@\u01c3\n@")
        buf.write("\3A\3A\3A\3A\7A\u01c9\nA\fA\16A\u01cc\13A\3A\3A\3B\3B")
        buf.write("\3B\3B\7B\u01d4\nB\fB\16B\u01d7\13B\3B\3B\3C\3C\3C\3C")
        buf.write("\7C\u01df\nC\fC\16C\u01e2\13C\3C\3C\3C\3C\3C\3D\6D\u01ea")
        buf.write("\nD\rD\16D\u01eb\3D\3D\3E\3E\5E\u01f2\nE\3F\3F\3F\3G\3")
        buf.write("G\3G\3H\3H\3H\3I\3I\7I\u01ff\nI\fI\16I\u0202\13I\3I\5")
        buf.write("I\u0205\nI\3I\3I\3J\3J\7J\u020b\nJ\fJ\16J\u020e\13J\3")
        buf.write("J\3J\3J\3\u01e0\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\2c\2e\62g\2")
        buf.write("i\2k\2m\2o\2q\2s\2u\63w\64y\65{\2}\66\177\2\u0081\67\u0083")
        buf.write("8\u00859\u0087:\u0089\2\u008b\2\u008d\2\u008f;\u0091<")
        buf.write("\u0093=\3\2\16\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\5\2\f\f\16\17^^\4\2\f\f\16\17\5\2\13")
        buf.write("\f\17\17\"\"\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\5\3\n")
        buf.write("\f\16\17^^\2\u0227\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2e\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2}\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u009a")
        buf.write("\3\2\2\2\7\u00a0\3\2\2\2\t\u00a8\3\2\2\2\13\u00ab\3\2")
        buf.write("\2\2\r\u00b0\3\2\2\2\17\u00b6\3\2\2\2\21\u00bc\3\2\2\2")
        buf.write("\23\u00c0\3\2\2\2\25\u00c9\3\2\2\2\27\u00cc\3\2\2\2\31")
        buf.write("\u00d4\3\2\2\2\33\u00db\3\2\2\2\35\u00e2\3\2\2\2\37\u00e7")
        buf.write("\3\2\2\2!\u00ed\3\2\2\2#\u00f2\3\2\2\2%\u00f6\3\2\2\2")
        buf.write("\'\u00ff\3\2\2\2)\u0102\3\2\2\2+\u010a\3\2\2\2-\u0110")
        buf.write("\3\2\2\2/\u0112\3\2\2\2\61\u0114\3\2\2\2\63\u0116\3\2")
        buf.write("\2\2\65\u0118\3\2\2\2\67\u011a\3\2\2\29\u011c\3\2\2\2")
        buf.write(";\u011f\3\2\2\2=\u0122\3\2\2\2?\u0125\3\2\2\2A\u0128\3")
        buf.write("\2\2\2C\u012a\3\2\2\2E\u012d\3\2\2\2G\u012f\3\2\2\2I\u0132")
        buf.write("\3\2\2\2K\u0135\3\2\2\2M\u0137\3\2\2\2O\u0139\3\2\2\2")
        buf.write("Q\u013b\3\2\2\2S\u013d\3\2\2\2U\u013f\3\2\2\2W\u0141\3")
        buf.write("\2\2\2Y\u0143\3\2\2\2[\u0145\3\2\2\2]\u0147\3\2\2\2_\u0149")
        buf.write("\3\2\2\2a\u014b\3\2\2\2c\u014d\3\2\2\2e\u014f\3\2\2\2")
        buf.write("g\u0156\3\2\2\2i\u0158\3\2\2\2k\u015a\3\2\2\2m\u015d\3")
        buf.write("\2\2\2o\u0169\3\2\2\2q\u016b\3\2\2\2s\u0172\3\2\2\2u\u017b")
        buf.write("\3\2\2\2w\u018d\3\2\2\2y\u0191\3\2\2\2{\u01b1\3\2\2\2")
        buf.write("}\u01b3\3\2\2\2\177\u01c2\3\2\2\2\u0081\u01c4\3\2\2\2")
        buf.write("\u0083\u01cf\3\2\2\2\u0085\u01da\3\2\2\2\u0087\u01e9\3")
        buf.write("\2\2\2\u0089\u01f1\3\2\2\2\u008b\u01f3\3\2\2\2\u008d\u01f6")
        buf.write("\3\2\2\2\u008f\u01f9\3\2\2\2\u0091\u01fc\3\2\2\2\u0093")
        buf.write("\u0208\3\2\2\2\u0095\u0096\7c\2\2\u0096\u0097\7w\2\2\u0097")
        buf.write("\u0098\7v\2\2\u0098\u0099\7q\2\2\u0099\4\3\2\2\2\u009a")
        buf.write("\u009b\7d\2\2\u009b\u009c\7t\2\2\u009c\u009d\7g\2\2\u009d")
        buf.write("\u009e\7c\2\2\u009e\u009f\7m\2\2\u009f\6\3\2\2\2\u00a0")
        buf.write("\u00a1\7d\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7q\2\2\u00a3")
        buf.write("\u00a4\7n\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7c\2\2\u00a6")
        buf.write("\u00a7\7p\2\2\u00a7\b\3\2\2\2\u00a8\u00a9\7f\2\2\u00a9")
        buf.write("\u00aa\7q\2\2\u00aa\n\3\2\2\2\u00ab\u00ac\7g\2\2\u00ac")
        buf.write("\u00ad\7n\2\2\u00ad\u00ae\7u\2\2\u00ae\u00af\7g\2\2\u00af")
        buf.write("\f\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2\7c\2\2\u00b2")
        buf.write("\u00b3\7n\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5\7g\2\2\u00b5")
        buf.write("\16\3\2\2\2\u00b6\u00b7\7h\2\2\u00b7\u00b8\7n\2\2\u00b8")
        buf.write("\u00b9\7q\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7v\2\2\u00bb")
        buf.write("\20\3\2\2\2\u00bc\u00bd\7h\2\2\u00bd\u00be\7q\2\2\u00be")
        buf.write("\u00bf\7t\2\2\u00bf\22\3\2\2\2\u00c0\u00c1\7h\2\2\u00c1")
        buf.write("\u00c2\7w\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7e\2\2\u00c4")
        buf.write("\u00c5\7v\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7q\2\2\u00c7")
        buf.write("\u00c8\7p\2\2\u00c8\24\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca")
        buf.write("\u00cb\7h\2\2\u00cb\26\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd")
        buf.write("\u00ce\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0\7g\2\2\u00d0")
        buf.write("\u00d1\7i\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7t\2\2\u00d3")
        buf.write("\30\3\2\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6\7g\2\2\u00d6")
        buf.write("\u00d7\7v\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9\7t\2\2\u00d9")
        buf.write("\u00da\7p\2\2\u00da\32\3\2\2\2\u00db\u00dc\7u\2\2\u00dc")
        buf.write("\u00dd\7v\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7k\2\2\u00df")
        buf.write("\u00e0\7p\2\2\u00e0\u00e1\7i\2\2\u00e1\34\3\2\2\2\u00e2")
        buf.write("\u00e3\7v\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5\7w\2\2\u00e5")
        buf.write("\u00e6\7g\2\2\u00e6\36\3\2\2\2\u00e7\u00e8\7y\2\2\u00e8")
        buf.write("\u00e9\7j\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7n\2\2\u00eb")
        buf.write("\u00ec\7g\2\2\u00ec \3\2\2\2\u00ed\u00ee\7x\2\2\u00ee")
        buf.write("\u00ef\7q\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7f\2\2\u00f1")
        buf.write("\"\3\2\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7w\2\2\u00f4")
        buf.write("\u00f5\7v\2\2\u00f5$\3\2\2\2\u00f6\u00f7\7e\2\2\u00f7")
        buf.write("\u00f8\7q\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7v\2\2\u00fa")
        buf.write("\u00fb\7k\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd\7w\2\2\u00fd")
        buf.write("\u00fe\7g\2\2\u00fe&\3\2\2\2\u00ff\u0100\7q\2\2\u0100")
        buf.write("\u0101\7h\2\2\u0101(\3\2\2\2\u0102\u0103\7k\2\2\u0103")
        buf.write("\u0104\7p\2\2\u0104\u0105\7j\2\2\u0105\u0106\7g\2\2\u0106")
        buf.write("\u0107\7t\2\2\u0107\u0108\7k\2\2\u0108\u0109\7v\2\2\u0109")
        buf.write("*\3\2\2\2\u010a\u010b\7c\2\2\u010b\u010c\7t\2\2\u010c")
        buf.write("\u010d\7t\2\2\u010d\u010e\7c\2\2\u010e\u010f\7{\2\2\u010f")
        buf.write(",\3\2\2\2\u0110\u0111\7-\2\2\u0111.\3\2\2\2\u0112\u0113")
        buf.write("\7/\2\2\u0113\60\3\2\2\2\u0114\u0115\7,\2\2\u0115\62\3")
        buf.write("\2\2\2\u0116\u0117\7\61\2\2\u0117\64\3\2\2\2\u0118\u0119")
        buf.write("\7\'\2\2\u0119\66\3\2\2\2\u011a\u011b\7#\2\2\u011b8\3")
        buf.write("\2\2\2\u011c\u011d\7(\2\2\u011d\u011e\7(\2\2\u011e:\3")
        buf.write("\2\2\2\u011f\u0120\7~\2\2\u0120\u0121\7~\2\2\u0121<\3")
        buf.write("\2\2\2\u0122\u0123\7?\2\2\u0123\u0124\7?\2\2\u0124>\3")
        buf.write("\2\2\2\u0125\u0126\7#\2\2\u0126\u0127\7?\2\2\u0127@\3")
        buf.write("\2\2\2\u0128\u0129\7>\2\2\u0129B\3\2\2\2\u012a\u012b\7")
        buf.write(">\2\2\u012b\u012c\7?\2\2\u012cD\3\2\2\2\u012d\u012e\7")
        buf.write("@\2\2\u012eF\3\2\2\2\u012f\u0130\7@\2\2\u0130\u0131\7")
        buf.write("?\2\2\u0131H\3\2\2\2\u0132\u0133\7<\2\2\u0133\u0134\7")
        buf.write("<\2\2\u0134J\3\2\2\2\u0135\u0136\7*\2\2\u0136L\3\2\2\2")
        buf.write("\u0137\u0138\7+\2\2\u0138N\3\2\2\2\u0139\u013a\7]\2\2")
        buf.write("\u013aP\3\2\2\2\u013b\u013c\7_\2\2\u013cR\3\2\2\2\u013d")
        buf.write("\u013e\7}\2\2\u013eT\3\2\2\2\u013f\u0140\7\177\2\2\u0140")
        buf.write("V\3\2\2\2\u0141\u0142\7\60\2\2\u0142X\3\2\2\2\u0143\u0144")
        buf.write("\7?\2\2\u0144Z\3\2\2\2\u0145\u0146\7.\2\2\u0146\\\3\2")
        buf.write("\2\2\u0147\u0148\7<\2\2\u0148^\3\2\2\2\u0149\u014a\7=")
        buf.write("\2\2\u014a`\3\2\2\2\u014b\u014c\t\2\2\2\u014cb\3\2\2\2")
        buf.write("\u014d\u014e\t\3\2\2\u014ed\3\2\2\2\u014f\u0153\5a\61")
        buf.write("\2\u0150\u0152\5c\62\2\u0151\u0150\3\2\2\2\u0152\u0155")
        buf.write("\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154")
        buf.write("f\3\2\2\2\u0155\u0153\3\2\2\2\u0156\u0157\t\4\2\2\u0157")
        buf.write("h\3\2\2\2\u0158\u0159\t\5\2\2\u0159j\3\2\2\2\u015a\u015b")
        buf.write("\7a\2\2\u015bl\3\2\2\2\u015c\u015e\5k\66\2\u015d\u015c")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u0160\5i\65\2\u0160n\3\2\2\2\u0161\u016a\7\62\2\2\u0162")
        buf.write("\u0166\5g\64\2\u0163\u0165\5m\67\2\u0164\u0163\3\2\2\2")
        buf.write("\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3")
        buf.write("\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u0161")
        buf.write("\3\2\2\2\u0169\u0162\3\2\2\2\u016ap\3\2\2\2\u016b\u016f")
        buf.write("\7\60\2\2\u016c\u016e\5i\65\2\u016d\u016c\3\2\2\2\u016e")
        buf.write("\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170r\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0174\t\6\2")
        buf.write("\2\u0173\u0175\t\7\2\2\u0174\u0173\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0178\5i\65\2\u0177")
        buf.write("\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0177\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017at\3\2\2\2\u017b\u017c\5o8\2")
        buf.write("\u017c\u017d\b;\2\2\u017dv\3\2\2\2\u017e\u017f\5o8\2\u017f")
        buf.write("\u0181\5q9\2\u0180\u0182\5s:\2\u0181\u0180\3\2\2\2\u0181")
        buf.write("\u0182\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\b<\3\2")
        buf.write("\u0184\u018e\3\2\2\2\u0185\u0186\5o8\2\u0186\u0187\5q")
        buf.write("9\2\u0187\u0188\b<\4\2\u0188\u018e\3\2\2\2\u0189\u018a")
        buf.write("\5o8\2\u018a\u018b\5s:\2\u018b\u018c\b<\5\2\u018c\u018e")
        buf.write("\3\2\2\2\u018d\u017e\3\2\2\2\u018d\u0185\3\2\2\2\u018d")
        buf.write("\u0189\3\2\2\2\u018ex\3\2\2\2\u018f\u0192\5\35\17\2\u0190")
        buf.write("\u0192\5\r\7\2\u0191\u018f\3\2\2\2\u0191\u0190\3\2\2\2")
        buf.write("\u0192z\3\2\2\2\u0193\u0194\7^\2\2\u0194\u01b2\7)\2\2")
        buf.write("\u0195\u0196\7^\2\2\u0196\u01b2\7$\2\2\u0197\u0198\7^")
        buf.write("\2\2\u0198\u01b2\7A\2\2\u0199\u019a\7^\2\2\u019a\u01b2")
        buf.write("\7^\2\2\u019b\u019c\7^\2\2\u019c\u01b2\7c\2\2\u019d\u019e")
        buf.write("\7^\2\2\u019e\u01b2\7d\2\2\u019f\u01a0\7^\2\2\u01a0\u01b2")
        buf.write("\7h\2\2\u01a1\u01a2\7^\2\2\u01a2\u01b2\7p\2\2\u01a3\u01a4")
        buf.write("\7^\2\2\u01a4\u01b2\7t\2\2\u01a5\u01ab\7^\2\2\u01a6\u01a8")
        buf.write("\7\17\2\2\u01a7\u01a9\7\f\2\2\u01a8\u01a7\3\2\2\2\u01a8")
        buf.write("\u01a9\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01ac\7\f\2\2")
        buf.write("\u01ab\u01a6\3\2\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01b2\3")
        buf.write("\2\2\2\u01ad\u01ae\7^\2\2\u01ae\u01b2\7v\2\2\u01af\u01b0")
        buf.write("\7^\2\2\u01b0\u01b2\7x\2\2\u01b1\u0193\3\2\2\2\u01b1\u0195")
        buf.write("\3\2\2\2\u01b1\u0197\3\2\2\2\u01b1\u0199\3\2\2\2\u01b1")
        buf.write("\u019b\3\2\2\2\u01b1\u019d\3\2\2\2\u01b1\u019f\3\2\2\2")
        buf.write("\u01b1\u01a1\3\2\2\2\u01b1\u01a3\3\2\2\2\u01b1\u01a5\3")
        buf.write("\2\2\2\u01b1\u01ad\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2|")
        buf.write("\3\2\2\2\u01b3\u01b8\7$\2\2\u01b4\u01b7\5{>\2\u01b5\u01b7")
        buf.write("\n\b\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7")
        buf.write("\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2")
        buf.write("\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\7")
        buf.write("$\2\2\u01bc\u01bd\b?\6\2\u01bd~\3\2\2\2\u01be\u01c3\5")
        buf.write("u;\2\u01bf\u01c3\5w<\2\u01c0\u01c3\5y=\2\u01c1\u01c3\5")
        buf.write("}?\2\u01c2\u01be\3\2\2\2\u01c2\u01bf\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3\u0080\3\2\2\2\u01c4")
        buf.write("\u01c5\5S*\2\u01c5\u01ca\5\177@\2\u01c6\u01c7\7.\2\2\u01c7")
        buf.write("\u01c9\5\177@\2\u01c8\u01c6\3\2\2\2\u01c9\u01cc\3\2\2")
        buf.write("\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cd")
        buf.write("\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01ce\5U+\2\u01ce\u0082")
        buf.write("\3\2\2\2\u01cf\u01d0\7\61\2\2\u01d0\u01d1\7\61\2\2\u01d1")
        buf.write("\u01d5\3\2\2\2\u01d2\u01d4\n\t\2\2\u01d3\u01d2\3\2\2\2")
        buf.write("\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3")
        buf.write("\2\2\2\u01d6\u01d8\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8\u01d9")
        buf.write("\bB\7\2\u01d9\u0084\3\2\2\2\u01da\u01db\7\61\2\2\u01db")
        buf.write("\u01dc\7,\2\2\u01dc\u01e0\3\2\2\2\u01dd\u01df\13\2\2\2")
        buf.write("\u01de\u01dd\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0\u01e1\3")
        buf.write("\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01e0")
        buf.write("\3\2\2\2\u01e3\u01e4\7,\2\2\u01e4\u01e5\7\61\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e6\u01e7\bC\7\2\u01e7\u0086\3\2\2\2")
        buf.write("\u01e8\u01ea\t\n\2\2\u01e9\u01e8\3\2\2\2\u01ea\u01eb\3")
        buf.write("\2\2\2\u01eb\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ed")
        buf.write("\3\2\2\2\u01ed\u01ee\bD\7\2\u01ee\u0088\3\2\2\2\u01ef")
        buf.write("\u01f2\n\13\2\2\u01f0\u01f2\5\u008bF\2\u01f1\u01ef\3\2")
        buf.write("\2\2\u01f1\u01f0\3\2\2\2\u01f2\u008a\3\2\2\2\u01f3\u01f4")
        buf.write("\7^\2\2\u01f4\u01f5\t\f\2\2\u01f5\u008c\3\2\2\2\u01f6")
        buf.write("\u01f7\7^\2\2\u01f7\u01f8\n\f\2\2\u01f8\u008e\3\2\2\2")
        buf.write("\u01f9\u01fa\13\2\2\2\u01fa\u01fb\bH\b\2\u01fb\u0090\3")
        buf.write("\2\2\2\u01fc\u0200\7$\2\2\u01fd\u01ff\5\u0089E\2\u01fe")
        buf.write("\u01fd\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe\3\2\2\2")
        buf.write("\u0200\u0201\3\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200\3")
        buf.write("\2\2\2\u0203\u0205\t\r\2\2\u0204\u0203\3\2\2\2\u0205\u0206")
        buf.write("\3\2\2\2\u0206\u0207\bI\t\2\u0207\u0092\3\2\2\2\u0208")
        buf.write("\u020c\7$\2\2\u0209\u020b\5\u0089E\2\u020a\u0209\3\2\2")
        buf.write("\2\u020b\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d")
        buf.write("\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u020c\3\2\2\2\u020f")
        buf.write("\u0210\5\u008dG\2\u0210\u0211\bJ\n\2\u0211\u0094\3\2\2")
        buf.write("\2\33\2\u0153\u015d\u0166\u0169\u016f\u0174\u0179\u0181")
        buf.write("\u018d\u0191\u01a8\u01ab\u01b1\u01b6\u01b8\u01c2\u01ca")
        buf.write("\u01d5\u01e0\u01eb\u01f1\u0200\u0204\u020c\13\3;\2\3<")
        buf.write("\3\3<\4\3<\5\3?\6\b\2\2\3H\7\3I\b\3J\t")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FALSE = 6
    FLOAT = 7
    FOR = 8
    FUNCTION = 9
    IF = 10
    INTEGER = 11
    RETURN = 12
    STRING = 13
    TRUE = 14
    WHILE = 15
    VOID = 16
    OUT = 17
    CONTINUE = 18
    OF = 19
    INHERIT = 20
    ARRAY = 21
    ADD = 22
    MINUS = 23
    STAR = 24
    DIV = 25
    MOD = 26
    NOT = 27
    AND_AND = 28
    OR_OR = 29
    EQUAL = 30
    NOT_EQUAL = 31
    LESS = 32
    LESS_EQUAL = 33
    GREATER = 34
    GREATER_EQUAL = 35
    DOUBLE_COLON = 36
    OPEN_PAREN = 37
    CLOSE_PAREN = 38
    OPEN_BRACK = 39
    CLOSE_BRACK = 40
    OPEN_BRACE = 41
    CLOSE_BRACE = 42
    DOT = 43
    ASSIGN = 44
    COMMA = 45
    COLON = 46
    SEMI_COLON = 47
    IDENTIFIER = 48
    INTEGER_LIT = 49
    FLOAT_LIT = 50
    BOOLEAN_LIT = 51
    STRING_LIT = 52
    ARRAY_LIT = 53
    COMMENT_LINE = 54
    COMMENT_BLOCK = 55
    WS = 56
    ERROR_CHAR = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59

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
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADD", "MINUS", "STAR", "DIV", "MOD", "NOT", "AND_AND", "OR_OR", 
            "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
            "DOUBLE_COLON", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", 
            "OPEN_BRACE", "CLOSE_BRACE", "DOT", "ASSIGN", "COMMA", "COLON", 
            "SEMI_COLON", "IDENTIFIER", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", 
            "STRING_LIT", "ARRAY_LIT", "COMMENT_LINE", "COMMENT_BLOCK", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADD", "MINUS", "STAR", "DIV", "MOD", "NOT", 
                  "AND_AND", "OR_OR", "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
                  "GREATER", "GREATER_EQUAL", "DOUBLE_COLON", "OPEN_PAREN", 
                  "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
                  "CLOSE_BRACE", "DOT", "ASSIGN", "COMMA", "COLON", "SEMI_COLON", 
                  "IDENTIFIER_START", "IDENTIFIER_CONTINUE", "IDENTIFIER", 
                  "INTEGER_START", "DIGIT", "UNDERSCORE", "INTEGER_CONTINUE", 
                  "INTEGER_PART", "DECIMAL_PART", "EXPONENT_PART", "INTEGER_LIT", 
                  "FLOAT_LIT", "BOOLEAN_LIT", "ESCAPE_SEQUENCE", "STRING_LIT", 
                  "ARRAY_ELEMENT", "ARRAY_LIT", "COMMENT_LINE", "COMMENT_BLOCK", 
                  "WS", "CHARACTER", "ESCAPE", "NOT_ESCAPE", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[57] = self.INTEGER_LIT_action 
            actions[58] = self.FLOAT_LIT_action 
            actions[61] = self.STRING_LIT_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
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

     



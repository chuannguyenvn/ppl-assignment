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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01c3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\7\62\u0140\n\62\f\62")
        buf.write("\16\62\u0143\13\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65")
        buf.write("\7\65\u014c\n\65\f\65\16\65\u014f\13\65\5\65\u0151\n\65")
        buf.write("\3\66\3\66\7\66\u0155\n\66\f\66\16\66\u0158\13\66\3\67")
        buf.write("\3\67\5\67\u015c\n\67\3\67\6\67\u015f\n\67\r\67\16\67")
        buf.write("\u0160\38\38\38\39\39\39\59\u0169\n9\39\39\39\39\39\3")
        buf.write("9\39\39\39\39\59\u0175\n9\3:\3:\5:\u0179\n:\3;\3;\3;\3")
        buf.write(";\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\5")
        buf.write(";\u0190\n;\3;\5;\u0193\n;\3;\3;\3;\3;\5;\u0199\n;\3<\3")
        buf.write("<\3<\7<\u019e\n<\f<\16<\u01a1\13<\3<\3<\3<\3=\3=\3=\3")
        buf.write("=\5=\u01aa\n=\3>\3>\3>\3>\7>\u01b0\n>\f>\16>\u01b3\13")
        buf.write(">\3>\3>\3?\6?\u01b8\n?\r?\16?\u01b9\3?\3?\3@\3@\3A\3A")
        buf.write("\3B\3B\2\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\2a\2c\61e\2g\2i\2k\2m\2")
        buf.write("o\62q\63s\64u\2w\65y\2{\66}\67\1778\u00819\u0083:\3\2")
        buf.write("\n\5\2C\\aac|\6\2\62;C\\aac|\4\2\63;aa\4\2\62;aa\4\2G")
        buf.write("Ggg\4\2--//\5\2\f\f\16\17^^\5\2\13\f\17\17\"\"\2\u01d7")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2c\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2w\3")
        buf.write("\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0083\3\2\2\2\3\u0085\3\2\2\2\5\u008a\3\2\2\2\7")
        buf.write("\u0090\3\2\2\2\t\u0098\3\2\2\2\13\u009b\3\2\2\2\r\u00a0")
        buf.write("\3\2\2\2\17\u00a6\3\2\2\2\21\u00ac\3\2\2\2\23\u00b0\3")
        buf.write("\2\2\2\25\u00b9\3\2\2\2\27\u00bc\3\2\2\2\31\u00c4\3\2")
        buf.write("\2\2\33\u00cb\3\2\2\2\35\u00d2\3\2\2\2\37\u00d7\3\2\2")
        buf.write("\2!\u00dd\3\2\2\2#\u00e2\3\2\2\2%\u00e6\3\2\2\2\'\u00ef")
        buf.write("\3\2\2\2)\u00f2\3\2\2\2+\u00fa\3\2\2\2-\u0100\3\2\2\2")
        buf.write("/\u0102\3\2\2\2\61\u0104\3\2\2\2\63\u0106\3\2\2\2\65\u0108")
        buf.write("\3\2\2\2\67\u010a\3\2\2\29\u010c\3\2\2\2;\u010f\3\2\2")
        buf.write("\2=\u0112\3\2\2\2?\u0115\3\2\2\2A\u0118\3\2\2\2C\u011a")
        buf.write("\3\2\2\2E\u011d\3\2\2\2G\u011f\3\2\2\2I\u0122\3\2\2\2")
        buf.write("K\u0125\3\2\2\2M\u0127\3\2\2\2O\u0129\3\2\2\2Q\u012b\3")
        buf.write("\2\2\2S\u012d\3\2\2\2U\u012f\3\2\2\2W\u0131\3\2\2\2Y\u0133")
        buf.write("\3\2\2\2[\u0135\3\2\2\2]\u0137\3\2\2\2_\u0139\3\2\2\2")
        buf.write("a\u013b\3\2\2\2c\u013d\3\2\2\2e\u0144\3\2\2\2g\u0146\3")
        buf.write("\2\2\2i\u0150\3\2\2\2k\u0152\3\2\2\2m\u0159\3\2\2\2o\u0162")
        buf.write("\3\2\2\2q\u0174\3\2\2\2s\u0178\3\2\2\2u\u0198\3\2\2\2")
        buf.write("w\u019a\3\2\2\2y\u01a9\3\2\2\2{\u01ab\3\2\2\2}\u01b7\3")
        buf.write("\2\2\2\177\u01bd\3\2\2\2\u0081\u01bf\3\2\2\2\u0083\u01c1")
        buf.write("\3\2\2\2\u0085\u0086\7c\2\2\u0086\u0087\7w\2\2\u0087\u0088")
        buf.write("\7v\2\2\u0088\u0089\7q\2\2\u0089\4\3\2\2\2\u008a\u008b")
        buf.write("\7d\2\2\u008b\u008c\7t\2\2\u008c\u008d\7g\2\2\u008d\u008e")
        buf.write("\7c\2\2\u008e\u008f\7m\2\2\u008f\6\3\2\2\2\u0090\u0091")
        buf.write("\7d\2\2\u0091\u0092\7q\2\2\u0092\u0093\7q\2\2\u0093\u0094")
        buf.write("\7n\2\2\u0094\u0095\7g\2\2\u0095\u0096\7c\2\2\u0096\u0097")
        buf.write("\7p\2\2\u0097\b\3\2\2\2\u0098\u0099\7f\2\2\u0099\u009a")
        buf.write("\7q\2\2\u009a\n\3\2\2\2\u009b\u009c\7g\2\2\u009c\u009d")
        buf.write("\7n\2\2\u009d\u009e\7u\2\2\u009e\u009f\7g\2\2\u009f\f")
        buf.write("\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3")
        buf.write("\7n\2\2\u00a3\u00a4\7u\2\2\u00a4\u00a5\7g\2\2\u00a5\16")
        buf.write("\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9")
        buf.write("\7q\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab\7v\2\2\u00ab\20")
        buf.write("\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af")
        buf.write("\7t\2\2\u00af\22\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4\7e\2\2\u00b4\u00b5")
        buf.write("\7v\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8")
        buf.write("\7p\2\2\u00b8\24\3\2\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb")
        buf.write("\7h\2\2\u00bb\26\3\2\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1")
        buf.write("\7i\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7t\2\2\u00c3\30")
        buf.write("\3\2\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7")
        buf.write("\7v\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\32\3\2\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7i\2\2\u00d1\34\3\2\2\2\u00d2\u00d3")
        buf.write("\7v\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\36\3\2\2\2\u00d7\u00d8\7y\2\2\u00d8\u00d9")
        buf.write("\7j\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7n\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc \3\2\2\2\u00dd\u00de\7x\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7f\2\2\u00e1\"")
        buf.write("\3\2\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7w\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5$\3\2\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7k\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee&\3\2\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7h\2\2\u00f1(\3\2\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7j\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7v\2\2\u00f9*\3")
        buf.write("\2\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7t\2\2\u00fc\u00fd")
        buf.write("\7t\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7{\2\2\u00ff,\3")
        buf.write("\2\2\2\u0100\u0101\7-\2\2\u0101.\3\2\2\2\u0102\u0103\7")
        buf.write("/\2\2\u0103\60\3\2\2\2\u0104\u0105\7,\2\2\u0105\62\3\2")
        buf.write("\2\2\u0106\u0107\7\61\2\2\u0107\64\3\2\2\2\u0108\u0109")
        buf.write("\7\'\2\2\u0109\66\3\2\2\2\u010a\u010b\7#\2\2\u010b8\3")
        buf.write("\2\2\2\u010c\u010d\7(\2\2\u010d\u010e\7(\2\2\u010e:\3")
        buf.write("\2\2\2\u010f\u0110\7~\2\2\u0110\u0111\7~\2\2\u0111<\3")
        buf.write("\2\2\2\u0112\u0113\7?\2\2\u0113\u0114\7?\2\2\u0114>\3")
        buf.write("\2\2\2\u0115\u0116\7#\2\2\u0116\u0117\7?\2\2\u0117@\3")
        buf.write("\2\2\2\u0118\u0119\7>\2\2\u0119B\3\2\2\2\u011a\u011b\7")
        buf.write(">\2\2\u011b\u011c\7?\2\2\u011cD\3\2\2\2\u011d\u011e\7")
        buf.write("@\2\2\u011eF\3\2\2\2\u011f\u0120\7@\2\2\u0120\u0121\7")
        buf.write("?\2\2\u0121H\3\2\2\2\u0122\u0123\7<\2\2\u0123\u0124\7")
        buf.write("<\2\2\u0124J\3\2\2\2\u0125\u0126\7?\2\2\u0126L\3\2\2\2")
        buf.write("\u0127\u0128\7.\2\2\u0128N\3\2\2\2\u0129\u012a\7<\2\2")
        buf.write("\u012aP\3\2\2\2\u012b\u012c\7=\2\2\u012cR\3\2\2\2\u012d")
        buf.write("\u012e\7*\2\2\u012eT\3\2\2\2\u012f\u0130\7+\2\2\u0130")
        buf.write("V\3\2\2\2\u0131\u0132\7]\2\2\u0132X\3\2\2\2\u0133\u0134")
        buf.write("\7_\2\2\u0134Z\3\2\2\2\u0135\u0136\7}\2\2\u0136\\\3\2")
        buf.write("\2\2\u0137\u0138\7\177\2\2\u0138^\3\2\2\2\u0139\u013a")
        buf.write("\t\2\2\2\u013a`\3\2\2\2\u013b\u013c\t\3\2\2\u013cb\3\2")
        buf.write("\2\2\u013d\u0141\5_\60\2\u013e\u0140\5a\61\2\u013f\u013e")
        buf.write("\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142d\3\2\2\2\u0143\u0141\3\2\2\2\u0144")
        buf.write("\u0145\t\4\2\2\u0145f\3\2\2\2\u0146\u0147\t\5\2\2\u0147")
        buf.write("h\3\2\2\2\u0148\u0151\7\62\2\2\u0149\u014d\5e\63\2\u014a")
        buf.write("\u014c\5g\64\2\u014b\u014a\3\2\2\2\u014c\u014f\3\2\2\2")
        buf.write("\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0151\3")
        buf.write("\2\2\2\u014f\u014d\3\2\2\2\u0150\u0148\3\2\2\2\u0150\u0149")
        buf.write("\3\2\2\2\u0151j\3\2\2\2\u0152\u0156\7\60\2\2\u0153\u0155")
        buf.write("\5g\64\2\u0154\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157l\3\2\2\2\u0158")
        buf.write("\u0156\3\2\2\2\u0159\u015b\t\6\2\2\u015a\u015c\t\7\2\2")
        buf.write("\u015b\u015a\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015e\3")
        buf.write("\2\2\2\u015d\u015f\5g\64\2\u015e\u015d\3\2\2\2\u015f\u0160")
        buf.write("\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write("n\3\2\2\2\u0162\u0163\5i\65\2\u0163\u0164\b8\2\2\u0164")
        buf.write("p\3\2\2\2\u0165\u0166\5i\65\2\u0166\u0168\5k\66\2\u0167")
        buf.write("\u0169\5m\67\2\u0168\u0167\3\2\2\2\u0168\u0169\3\2\2\2")
        buf.write("\u0169\u016a\3\2\2\2\u016a\u016b\b9\3\2\u016b\u0175\3")
        buf.write("\2\2\2\u016c\u016d\5i\65\2\u016d\u016e\5k\66\2\u016e\u016f")
        buf.write("\b9\4\2\u016f\u0175\3\2\2\2\u0170\u0171\5i\65\2\u0171")
        buf.write("\u0172\5m\67\2\u0172\u0173\b9\5\2\u0173\u0175\3\2\2\2")
        buf.write("\u0174\u0165\3\2\2\2\u0174\u016c\3\2\2\2\u0174\u0170\3")
        buf.write("\2\2\2\u0175r\3\2\2\2\u0176\u0179\5\35\17\2\u0177\u0179")
        buf.write("\5\r\7\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("t\3\2\2\2\u017a\u017b\7^\2\2\u017b\u0199\7)\2\2\u017c")
        buf.write("\u017d\7^\2\2\u017d\u0199\7$\2\2\u017e\u017f\7^\2\2\u017f")
        buf.write("\u0199\7A\2\2\u0180\u0181\7^\2\2\u0181\u0199\7^\2\2\u0182")
        buf.write("\u0183\7^\2\2\u0183\u0199\7c\2\2\u0184\u0185\7^\2\2\u0185")
        buf.write("\u0199\7d\2\2\u0186\u0187\7^\2\2\u0187\u0199\7h\2\2\u0188")
        buf.write("\u0189\7^\2\2\u0189\u0199\7p\2\2\u018a\u018b\7^\2\2\u018b")
        buf.write("\u0199\7t\2\2\u018c\u0192\7^\2\2\u018d\u018f\7\17\2\2")
        buf.write("\u018e\u0190\7\f\2\2\u018f\u018e\3\2\2\2\u018f\u0190\3")
        buf.write("\2\2\2\u0190\u0193\3\2\2\2\u0191\u0193\7\f\2\2\u0192\u018d")
        buf.write("\3\2\2\2\u0192\u0191\3\2\2\2\u0193\u0199\3\2\2\2\u0194")
        buf.write("\u0195\7^\2\2\u0195\u0199\7v\2\2\u0196\u0197\7^\2\2\u0197")
        buf.write("\u0199\7x\2\2\u0198\u017a\3\2\2\2\u0198\u017c\3\2\2\2")
        buf.write("\u0198\u017e\3\2\2\2\u0198\u0180\3\2\2\2\u0198\u0182\3")
        buf.write("\2\2\2\u0198\u0184\3\2\2\2\u0198\u0186\3\2\2\2\u0198\u0188")
        buf.write("\3\2\2\2\u0198\u018a\3\2\2\2\u0198\u018c\3\2\2\2\u0198")
        buf.write("\u0194\3\2\2\2\u0198\u0196\3\2\2\2\u0199v\3\2\2\2\u019a")
        buf.write("\u019f\7$\2\2\u019b\u019e\5u;\2\u019c\u019e\n\b\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019e\u01a1\3\2\2\2")
        buf.write("\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2\3")
        buf.write("\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a3\7$\2\2\u01a3\u01a4")
        buf.write("\b<\6\2\u01a4x\3\2\2\2\u01a5\u01aa\5o8\2\u01a6\u01aa\5")
        buf.write("q9\2\u01a7\u01aa\5s:\2\u01a8\u01aa\5w<\2\u01a9\u01a5\3")
        buf.write("\2\2\2\u01a9\u01a6\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01a8")
        buf.write("\3\2\2\2\u01aaz\3\2\2\2\u01ab\u01ac\5[.\2\u01ac\u01b1")
        buf.write("\5y=\2\u01ad\u01ae\7.\2\2\u01ae\u01b0\5y=\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b4\u01b5\5]/\2\u01b5|\3\2\2\2\u01b6\u01b8\t\t\2\2")
        buf.write("\u01b7\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01b7\3")
        buf.write("\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc")
        buf.write("\b?\7\2\u01bc~\3\2\2\2\u01bd\u01be\13\2\2\2\u01be\u0080")
        buf.write("\3\2\2\2\u01bf\u01c0\13\2\2\2\u01c0\u0082\3\2\2\2\u01c1")
        buf.write("\u01c2\13\2\2\2\u01c2\u0084\3\2\2\2\24\2\u0141\u014d\u0150")
        buf.write("\u0156\u015b\u0160\u0168\u0174\u0178\u018f\u0192\u0198")
        buf.write("\u019d\u019f\u01a9\u01b1\u01b9\b\38\2\39\3\39\4\39\5\3")
        buf.write("<\6\b\2\2")
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
    ASSIGN = 37
    COMMA = 38
    COLON = 39
    SEMI_COLON = 40
    OPEN_PAREN = 41
    CLOSE_PAREN = 42
    OPEN_BRACK = 43
    CLOSE_BRACK = 44
    OPEN_BRACE = 45
    CLOSE_BRACE = 46
    IDENTIFIER = 47
    INTEGER_LIT = 48
    FLOAT_LIT = 49
    BOOLEAN_LIT = 50
    STRING_LIT = 51
    ARRAY_LIT = 52
    WS = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'='", "','", "':'", "';'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADD", "MINUS", "STAR", "DIV", "MOD", "NOT", "AND_AND", "OR_OR", 
            "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
            "DOUBLE_COLON", "ASSIGN", "COMMA", "COLON", "SEMI_COLON", "OPEN_PAREN", 
            "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", 
            "IDENTIFIER", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", 
            "ARRAY_LIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADD", "MINUS", "STAR", "DIV", "MOD", "NOT", 
                  "AND_AND", "OR_OR", "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
                  "GREATER", "GREATER_EQUAL", "DOUBLE_COLON", "ASSIGN", 
                  "COMMA", "COLON", "SEMI_COLON", "OPEN_PAREN", "CLOSE_PAREN", 
                  "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", 
                  "IDENTIFIER_START", "IDENTIFIER_CONTINUE", "IDENTIFIER", 
                  "NON_ZERO_DIGIT", "DIGIT", "INTEGER_PART", "DECIMAL_PART", 
                  "EXPONENT_PART", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", 
                  "ESCAPE_SEQUENCE", "STRING_LIT", "ARRAY_ELEMENT", "ARRAY_LIT", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[54] = self.INTEGER_LIT_action 
            actions[55] = self.FLOAT_LIT_action 
            actions[58] = self.STRING_LIT_action 
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
     



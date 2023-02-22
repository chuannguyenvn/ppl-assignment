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
        buf.write("\u01e6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\7")
        buf.write("\62\u0146\n\62\f\62\16\62\u0149\13\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\65\7\65\u0152\n\65\f\65\16\65\u0155\13")
        buf.write("\65\5\65\u0157\n\65\3\66\3\66\7\66\u015b\n\66\f\66\16")
        buf.write("\66\u015e\13\66\3\67\3\67\5\67\u0162\n\67\3\67\6\67\u0165")
        buf.write("\n\67\r\67\16\67\u0166\38\38\38\39\39\39\59\u016f\n9\3")
        buf.write("9\39\39\39\39\39\39\39\39\39\59\u017b\n9\3:\3:\5:\u017f")
        buf.write("\n:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\3;\3;\5;\u0196\n;\3;\5;\u0199\n;\3;\3;\3;\3;\5")
        buf.write(";\u019f\n;\3<\3<\3<\7<\u01a4\n<\f<\16<\u01a7\13<\3<\3")
        buf.write("<\3<\3=\3=\3=\3=\5=\u01b0\n=\3>\3>\3>\3>\7>\u01b6\n>\f")
        buf.write(">\16>\u01b9\13>\3>\3>\3?\6?\u01be\n?\r?\16?\u01bf\3?\3")
        buf.write("?\3@\3@\5@\u01c6\n@\3A\3A\3A\3B\3B\3B\3C\3C\3C\3D\3D\7")
        buf.write("D\u01d3\nD\fD\16D\u01d6\13D\3D\5D\u01d9\nD\3D\3D\3E\3")
        buf.write("E\7E\u01df\nE\fE\16E\u01e2\13E\3E\3E\3E\2\2F\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\2a\2c\61e\2g\2i\2k\2m\2o\62q\63s\64u\2w\65y")
        buf.write("\2{\66}\67\177\2\u0081\2\u0083\2\u00858\u00879\u0089:")
        buf.write("\3\2\r\5\2C\\aac|\6\2\62;C\\aac|\4\2\63;aa\4\2\62;aa\4")
        buf.write("\2GGgg\4\2--//\5\2\f\f\16\17^^\5\2\13\f\17\17\"\"\6\2")
        buf.write("\n\f\16\17$$^^\t\2$$^^ddhhppttvv\5\3\n\f\16\17^^\2\u01fa")
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
        buf.write("\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3")
        buf.write("\2\2\2\2\u0089\3\2\2\2\3\u008b\3\2\2\2\5\u0090\3\2\2\2")
        buf.write("\7\u0096\3\2\2\2\t\u009e\3\2\2\2\13\u00a1\3\2\2\2\r\u00a6")
        buf.write("\3\2\2\2\17\u00ac\3\2\2\2\21\u00b2\3\2\2\2\23\u00b6\3")
        buf.write("\2\2\2\25\u00bf\3\2\2\2\27\u00c2\3\2\2\2\31\u00ca\3\2")
        buf.write("\2\2\33\u00d1\3\2\2\2\35\u00d8\3\2\2\2\37\u00dd\3\2\2")
        buf.write("\2!\u00e3\3\2\2\2#\u00e8\3\2\2\2%\u00ec\3\2\2\2\'\u00f5")
        buf.write("\3\2\2\2)\u00f8\3\2\2\2+\u0100\3\2\2\2-\u0106\3\2\2\2")
        buf.write("/\u0108\3\2\2\2\61\u010a\3\2\2\2\63\u010c\3\2\2\2\65\u010e")
        buf.write("\3\2\2\2\67\u0110\3\2\2\29\u0112\3\2\2\2;\u0115\3\2\2")
        buf.write("\2=\u0118\3\2\2\2?\u011b\3\2\2\2A\u011e\3\2\2\2C\u0120")
        buf.write("\3\2\2\2E\u0123\3\2\2\2G\u0125\3\2\2\2I\u0128\3\2\2\2")
        buf.write("K\u012b\3\2\2\2M\u012d\3\2\2\2O\u012f\3\2\2\2Q\u0131\3")
        buf.write("\2\2\2S\u0133\3\2\2\2U\u0135\3\2\2\2W\u0137\3\2\2\2Y\u0139")
        buf.write("\3\2\2\2[\u013b\3\2\2\2]\u013d\3\2\2\2_\u013f\3\2\2\2")
        buf.write("a\u0141\3\2\2\2c\u0143\3\2\2\2e\u014a\3\2\2\2g\u014c\3")
        buf.write("\2\2\2i\u0156\3\2\2\2k\u0158\3\2\2\2m\u015f\3\2\2\2o\u0168")
        buf.write("\3\2\2\2q\u017a\3\2\2\2s\u017e\3\2\2\2u\u019e\3\2\2\2")
        buf.write("w\u01a0\3\2\2\2y\u01af\3\2\2\2{\u01b1\3\2\2\2}\u01bd\3")
        buf.write("\2\2\2\177\u01c5\3\2\2\2\u0081\u01c7\3\2\2\2\u0083\u01ca")
        buf.write("\3\2\2\2\u0085\u01cd\3\2\2\2\u0087\u01d0\3\2\2\2\u0089")
        buf.write("\u01dc\3\2\2\2\u008b\u008c\7c\2\2\u008c\u008d\7w\2\2\u008d")
        buf.write("\u008e\7v\2\2\u008e\u008f\7q\2\2\u008f\4\3\2\2\2\u0090")
        buf.write("\u0091\7d\2\2\u0091\u0092\7t\2\2\u0092\u0093\7g\2\2\u0093")
        buf.write("\u0094\7c\2\2\u0094\u0095\7m\2\2\u0095\6\3\2\2\2\u0096")
        buf.write("\u0097\7d\2\2\u0097\u0098\7q\2\2\u0098\u0099\7q\2\2\u0099")
        buf.write("\u009a\7n\2\2\u009a\u009b\7g\2\2\u009b\u009c\7c\2\2\u009c")
        buf.write("\u009d\7p\2\2\u009d\b\3\2\2\2\u009e\u009f\7f\2\2\u009f")
        buf.write("\u00a0\7q\2\2\u00a0\n\3\2\2\2\u00a1\u00a2\7g\2\2\u00a2")
        buf.write("\u00a3\7n\2\2\u00a3\u00a4\7u\2\2\u00a4\u00a5\7g\2\2\u00a5")
        buf.write("\f\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8\7c\2\2\u00a8")
        buf.write("\u00a9\7n\2\2\u00a9\u00aa\7u\2\2\u00aa\u00ab\7g\2\2\u00ab")
        buf.write("\16\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae\7n\2\2\u00ae")
        buf.write("\u00af\7q\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1\7v\2\2\u00b1")
        buf.write("\20\3\2\2\2\u00b2\u00b3\7h\2\2\u00b3\u00b4\7q\2\2\u00b4")
        buf.write("\u00b5\7t\2\2\u00b5\22\3\2\2\2\u00b6\u00b7\7h\2\2\u00b7")
        buf.write("\u00b8\7w\2\2\u00b8\u00b9\7p\2\2\u00b9\u00ba\7e\2\2\u00ba")
        buf.write("\u00bb\7v\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7q\2\2\u00bd")
        buf.write("\u00be\7p\2\2\u00be\24\3\2\2\2\u00bf\u00c0\7k\2\2\u00c0")
        buf.write("\u00c1\7h\2\2\u00c1\26\3\2\2\2\u00c2\u00c3\7k\2\2\u00c3")
        buf.write("\u00c4\7p\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6\7g\2\2\u00c6")
        buf.write("\u00c7\7i\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7t\2\2\u00c9")
        buf.write("\30\3\2\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7g\2\2\u00cc")
        buf.write("\u00cd\7v\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf\7t\2\2\u00cf")
        buf.write("\u00d0\7p\2\2\u00d0\32\3\2\2\2\u00d1\u00d2\7u\2\2\u00d2")
        buf.write("\u00d3\7v\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5\7k\2\2\u00d5")
        buf.write("\u00d6\7p\2\2\u00d6\u00d7\7i\2\2\u00d7\34\3\2\2\2\u00d8")
        buf.write("\u00d9\7v\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7w\2\2\u00db")
        buf.write("\u00dc\7g\2\2\u00dc\36\3\2\2\2\u00dd\u00de\7y\2\2\u00de")
        buf.write("\u00df\7j\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7n\2\2\u00e1")
        buf.write("\u00e2\7g\2\2\u00e2 \3\2\2\2\u00e3\u00e4\7x\2\2\u00e4")
        buf.write("\u00e5\7q\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7f\2\2\u00e7")
        buf.write("\"\3\2\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7w\2\2\u00ea")
        buf.write("\u00eb\7v\2\2\u00eb$\3\2\2\2\u00ec\u00ed\7e\2\2\u00ed")
        buf.write("\u00ee\7q\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7v\2\2\u00f0")
        buf.write("\u00f1\7k\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3\7w\2\2\u00f3")
        buf.write("\u00f4\7g\2\2\u00f4&\3\2\2\2\u00f5\u00f6\7q\2\2\u00f6")
        buf.write("\u00f7\7h\2\2\u00f7(\3\2\2\2\u00f8\u00f9\7k\2\2\u00f9")
        buf.write("\u00fa\7p\2\2\u00fa\u00fb\7j\2\2\u00fb\u00fc\7g\2\2\u00fc")
        buf.write("\u00fd\7t\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7v\2\2\u00ff")
        buf.write("*\3\2\2\2\u0100\u0101\7c\2\2\u0101\u0102\7t\2\2\u0102")
        buf.write("\u0103\7t\2\2\u0103\u0104\7c\2\2\u0104\u0105\7{\2\2\u0105")
        buf.write(",\3\2\2\2\u0106\u0107\7-\2\2\u0107.\3\2\2\2\u0108\u0109")
        buf.write("\7/\2\2\u0109\60\3\2\2\2\u010a\u010b\7,\2\2\u010b\62\3")
        buf.write("\2\2\2\u010c\u010d\7\61\2\2\u010d\64\3\2\2\2\u010e\u010f")
        buf.write("\7\'\2\2\u010f\66\3\2\2\2\u0110\u0111\7#\2\2\u01118\3")
        buf.write("\2\2\2\u0112\u0113\7(\2\2\u0113\u0114\7(\2\2\u0114:\3")
        buf.write("\2\2\2\u0115\u0116\7~\2\2\u0116\u0117\7~\2\2\u0117<\3")
        buf.write("\2\2\2\u0118\u0119\7?\2\2\u0119\u011a\7?\2\2\u011a>\3")
        buf.write("\2\2\2\u011b\u011c\7#\2\2\u011c\u011d\7?\2\2\u011d@\3")
        buf.write("\2\2\2\u011e\u011f\7>\2\2\u011fB\3\2\2\2\u0120\u0121\7")
        buf.write(">\2\2\u0121\u0122\7?\2\2\u0122D\3\2\2\2\u0123\u0124\7")
        buf.write("@\2\2\u0124F\3\2\2\2\u0125\u0126\7@\2\2\u0126\u0127\7")
        buf.write("?\2\2\u0127H\3\2\2\2\u0128\u0129\7<\2\2\u0129\u012a\7")
        buf.write("<\2\2\u012aJ\3\2\2\2\u012b\u012c\7?\2\2\u012cL\3\2\2\2")
        buf.write("\u012d\u012e\7.\2\2\u012eN\3\2\2\2\u012f\u0130\7<\2\2")
        buf.write("\u0130P\3\2\2\2\u0131\u0132\7=\2\2\u0132R\3\2\2\2\u0133")
        buf.write("\u0134\7*\2\2\u0134T\3\2\2\2\u0135\u0136\7+\2\2\u0136")
        buf.write("V\3\2\2\2\u0137\u0138\7]\2\2\u0138X\3\2\2\2\u0139\u013a")
        buf.write("\7_\2\2\u013aZ\3\2\2\2\u013b\u013c\7}\2\2\u013c\\\3\2")
        buf.write("\2\2\u013d\u013e\7\177\2\2\u013e^\3\2\2\2\u013f\u0140")
        buf.write("\t\2\2\2\u0140`\3\2\2\2\u0141\u0142\t\3\2\2\u0142b\3\2")
        buf.write("\2\2\u0143\u0147\5_\60\2\u0144\u0146\5a\61\2\u0145\u0144")
        buf.write("\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3\2\2\2\u0147")
        buf.write("\u0148\3\2\2\2\u0148d\3\2\2\2\u0149\u0147\3\2\2\2\u014a")
        buf.write("\u014b\t\4\2\2\u014bf\3\2\2\2\u014c\u014d\t\5\2\2\u014d")
        buf.write("h\3\2\2\2\u014e\u0157\7\62\2\2\u014f\u0153\5e\63\2\u0150")
        buf.write("\u0152\5g\64\2\u0151\u0150\3\2\2\2\u0152\u0155\3\2\2\2")
        buf.write("\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0157\3")
        buf.write("\2\2\2\u0155\u0153\3\2\2\2\u0156\u014e\3\2\2\2\u0156\u014f")
        buf.write("\3\2\2\2\u0157j\3\2\2\2\u0158\u015c\7\60\2\2\u0159\u015b")
        buf.write("\5g\64\2\u015a\u0159\3\2\2\2\u015b\u015e\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015dl\3\2\2\2\u015e")
        buf.write("\u015c\3\2\2\2\u015f\u0161\t\6\2\2\u0160\u0162\t\7\2\2")
        buf.write("\u0161\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0164\3")
        buf.write("\2\2\2\u0163\u0165\5g\64\2\u0164\u0163\3\2\2\2\u0165\u0166")
        buf.write("\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("n\3\2\2\2\u0168\u0169\5i\65\2\u0169\u016a\b8\2\2\u016a")
        buf.write("p\3\2\2\2\u016b\u016c\5i\65\2\u016c\u016e\5k\66\2\u016d")
        buf.write("\u016f\5m\67\2\u016e\u016d\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u0170\3\2\2\2\u0170\u0171\b9\3\2\u0171\u017b\3")
        buf.write("\2\2\2\u0172\u0173\5i\65\2\u0173\u0174\5k\66\2\u0174\u0175")
        buf.write("\b9\4\2\u0175\u017b\3\2\2\2\u0176\u0177\5i\65\2\u0177")
        buf.write("\u0178\5m\67\2\u0178\u0179\b9\5\2\u0179\u017b\3\2\2\2")
        buf.write("\u017a\u016b\3\2\2\2\u017a\u0172\3\2\2\2\u017a\u0176\3")
        buf.write("\2\2\2\u017br\3\2\2\2\u017c\u017f\5\35\17\2\u017d\u017f")
        buf.write("\5\r\7\2\u017e\u017c\3\2\2\2\u017e\u017d\3\2\2\2\u017f")
        buf.write("t\3\2\2\2\u0180\u0181\7^\2\2\u0181\u019f\7)\2\2\u0182")
        buf.write("\u0183\7^\2\2\u0183\u019f\7$\2\2\u0184\u0185\7^\2\2\u0185")
        buf.write("\u019f\7A\2\2\u0186\u0187\7^\2\2\u0187\u019f\7^\2\2\u0188")
        buf.write("\u0189\7^\2\2\u0189\u019f\7c\2\2\u018a\u018b\7^\2\2\u018b")
        buf.write("\u019f\7d\2\2\u018c\u018d\7^\2\2\u018d\u019f\7h\2\2\u018e")
        buf.write("\u018f\7^\2\2\u018f\u019f\7p\2\2\u0190\u0191\7^\2\2\u0191")
        buf.write("\u019f\7t\2\2\u0192\u0198\7^\2\2\u0193\u0195\7\17\2\2")
        buf.write("\u0194\u0196\7\f\2\2\u0195\u0194\3\2\2\2\u0195\u0196\3")
        buf.write("\2\2\2\u0196\u0199\3\2\2\2\u0197\u0199\7\f\2\2\u0198\u0193")
        buf.write("\3\2\2\2\u0198\u0197\3\2\2\2\u0199\u019f\3\2\2\2\u019a")
        buf.write("\u019b\7^\2\2\u019b\u019f\7v\2\2\u019c\u019d\7^\2\2\u019d")
        buf.write("\u019f\7x\2\2\u019e\u0180\3\2\2\2\u019e\u0182\3\2\2\2")
        buf.write("\u019e\u0184\3\2\2\2\u019e\u0186\3\2\2\2\u019e\u0188\3")
        buf.write("\2\2\2\u019e\u018a\3\2\2\2\u019e\u018c\3\2\2\2\u019e\u018e")
        buf.write("\3\2\2\2\u019e\u0190\3\2\2\2\u019e\u0192\3\2\2\2\u019e")
        buf.write("\u019a\3\2\2\2\u019e\u019c\3\2\2\2\u019fv\3\2\2\2\u01a0")
        buf.write("\u01a5\7$\2\2\u01a1\u01a4\5u;\2\u01a2\u01a4\n\b\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4\u01a7\3\2\2\2")
        buf.write("\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a8\3")
        buf.write("\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01a9\7$\2\2\u01a9\u01aa")
        buf.write("\b<\6\2\u01aax\3\2\2\2\u01ab\u01b0\5o8\2\u01ac\u01b0\5")
        buf.write("q9\2\u01ad\u01b0\5s:\2\u01ae\u01b0\5w<\2\u01af\u01ab\3")
        buf.write("\2\2\2\u01af\u01ac\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01b0z\3\2\2\2\u01b1\u01b2\5[.\2\u01b2\u01b7")
        buf.write("\5y=\2\u01b3\u01b4\7.\2\2\u01b4\u01b6\5y=\2\u01b5\u01b3")
        buf.write("\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7")
        buf.write("\u01b8\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01b7\3\2\2\2")
        buf.write("\u01ba\u01bb\5]/\2\u01bb|\3\2\2\2\u01bc\u01be\t\t\2\2")
        buf.write("\u01bd\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01bd\3")
        buf.write("\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2")
        buf.write("\b?\7\2\u01c2~\3\2\2\2\u01c3\u01c6\n\n\2\2\u01c4\u01c6")
        buf.write("\5\u0081A\2\u01c5\u01c3\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6")
        buf.write("\u0080\3\2\2\2\u01c7\u01c8\7^\2\2\u01c8\u01c9\t\13\2\2")
        buf.write("\u01c9\u0082\3\2\2\2\u01ca\u01cb\7^\2\2\u01cb\u01cc\n")
        buf.write("\13\2\2\u01cc\u0084\3\2\2\2\u01cd\u01ce\13\2\2\2\u01ce")
        buf.write("\u01cf\bC\b\2\u01cf\u0086\3\2\2\2\u01d0\u01d4\7$\2\2\u01d1")
        buf.write("\u01d3\5\177@\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6\3\2\2")
        buf.write("\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d8")
        buf.write("\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d9\t\f\2\2\u01d8")
        buf.write("\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01db\bD\t\2")
        buf.write("\u01db\u0088\3\2\2\2\u01dc\u01e0\7$\2\2\u01dd\u01df\5")
        buf.write("\177@\2\u01de\u01dd\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0")
        buf.write("\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e3\3\2\2\2")
        buf.write("\u01e2\u01e0\3\2\2\2\u01e3\u01e4\5\u0083B\2\u01e4\u01e5")
        buf.write("\bE\n\2\u01e5\u008a\3\2\2\2\30\2\u0147\u0153\u0156\u015c")
        buf.write("\u0161\u0166\u016e\u017a\u017e\u0195\u0198\u019e\u01a3")
        buf.write("\u01a5\u01af\u01b7\u01bf\u01c5\u01d4\u01d8\u01e0\13\3")
        buf.write("8\2\39\3\39\4\39\5\3<\6\b\2\2\3C\7\3D\b\3E\t")
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
                  "WS", "Character", "Escape", "IllegalEscape", "ERROR_CHAR", 
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
            actions[54] = self.INTEGER_LIT_action 
            actions[55] = self.FLOAT_LIT_action 
            actions[58] = self.STRING_LIT_action 
            actions[65] = self.ERROR_CHAR_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
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

     



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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\u016d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\3\2\6\2P\n\2\r\2\16\2Q\3\2\3\2\3\3\3\3\5\3X")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4`\n\4\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6r")
        buf.write("\n\6\3\7\3\7\3\7\7\7w\n\7\f\7\16\7z\13\7\3\b\5\b}\n\b")
        buf.write("\3\b\5\b\u0080\n\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t\u0089")
        buf.write("\n\t\f\t\16\t\u008c\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5")
        buf.write("\n\u0095\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\7\f\u00a1\n\f\f\f\16\f\u00a4\13\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\5\r\u00ac\n\r\3\r\3\r\3\r\5\r\u00b1\n\r\3\r")
        buf.write("\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00c1\n\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00cf\n\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\5\27\u00f3\n\27\3\27\3\27\3\30\3\30\3\30\5\30\u00fa\n")
        buf.write("\30\3\30\3\30\3\30\3\31\3\31\3\31\7\31\u0102\n\31\f\31")
        buf.write("\16\31\u0105\13\31\3\31\3\31\3\32\3\32\3\32\7\32\u010c")
        buf.write("\n\32\f\32\16\32\u010f\13\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u0118\n\34\3\35\3\35\3\35\3\35\3\35\5")
        buf.write("\35\u011f\n\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0127")
        buf.write("\n\36\f\36\16\36\u012a\13\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\7\37\u0132\n\37\f\37\16\37\u0135\13\37\3 \3 \3 ")
        buf.write("\3 \3 \3 \7 \u013d\n \f \16 \u0140\13 \3!\3!\3!\5!\u0145")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u014d\n\"\3#\3#\3#\3#")
        buf.write("\3#\5#\u0154\n#\3$\3$\3$\5$\u0159\n$\3%\3%\3%\3%\3%\5")
        buf.write("%\u0160\n%\3&\3&\3&\3&\3\'\3\'\3\'\5\'\u0169\n\'\3\'\3")
        buf.write("\'\3\'\2\5:<>(\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJL\2\b\6\2\t\t\r\r\21\21")
        buf.write("\23\23\3\2$)\3\2\"#\3\2\34\35\3\2\36 \4\2\35\35!!\2\u0175")
        buf.write("\2O\3\2\2\2\4W\3\2\2\2\6_\3\2\2\2\ba\3\2\2\2\nq\3\2\2")
        buf.write("\2\fs\3\2\2\2\16|\3\2\2\2\20\u0085\3\2\2\2\22\u0094\3")
        buf.write("\2\2\2\24\u0096\3\2\2\2\26\u009d\3\2\2\2\30\u00a5\3\2")
        buf.write("\2\2\32\u00b4\3\2\2\2\34\u00c0\3\2\2\2\36\u00c2\3\2\2")
        buf.write("\2 \u00c7\3\2\2\2\"\u00d0\3\2\2\2$\u00dc\3\2\2\2&\u00e2")
        buf.write("\3\2\2\2(\u00ea\3\2\2\2*\u00ed\3\2\2\2,\u00f0\3\2\2\2")
        buf.write(".\u00f6\3\2\2\2\60\u00fe\3\2\2\2\62\u0108\3\2\2\2\64\u0110")
        buf.write("\3\2\2\2\66\u0117\3\2\2\28\u011e\3\2\2\2:\u0120\3\2\2")
        buf.write("\2<\u012b\3\2\2\2>\u0136\3\2\2\2@\u0144\3\2\2\2B\u014c")
        buf.write("\3\2\2\2D\u0153\3\2\2\2F\u0158\3\2\2\2H\u015f\3\2\2\2")
        buf.write("J\u0161\3\2\2\2L\u0165\3\2\2\2NP\5\4\3\2ON\3\2\2\2PQ\3")
        buf.write("\2\2\2QO\3\2\2\2QR\3\2\2\2RS\3\2\2\2ST\7\2\2\3T\3\3\2")
        buf.write("\2\2UX\5\6\4\2VX\5\30\r\2WU\3\2\2\2WV\3\2\2\2X\5\3\2\2")
        buf.write("\2YZ\5\b\5\2Z[\7\65\2\2[`\3\2\2\2\\]\5\n\6\2]^\7\65\2")
        buf.write("\2^`\3\2\2\2_Y\3\2\2\2_\\\3\2\2\2`\7\3\2\2\2ab\5\20\t")
        buf.write("\2bc\7\64\2\2cd\5\22\n\2d\t\3\2\2\2ef\7\66\2\2fg\7\64")
        buf.write("\2\2gh\5\22\n\2hi\7\62\2\2ij\5\64\33\2jr\3\2\2\2kl\7\66")
        buf.write("\2\2lm\7\63\2\2mn\5\n\6\2no\7\63\2\2op\5\64\33\2pr\3\2")
        buf.write("\2\2qe\3\2\2\2qk\3\2\2\2r\13\3\2\2\2sx\5\16\b\2tu\7\63")
        buf.write("\2\2uw\5\16\b\2vt\3\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2")
        buf.write("\2y\r\3\2\2\2zx\3\2\2\2{}\7\32\2\2|{\3\2\2\2|}\3\2\2\2")
        buf.write("}\177\3\2\2\2~\u0080\7\27\2\2\177~\3\2\2\2\177\u0080\3")
        buf.write("\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\7\66\2\2\u0082")
        buf.write("\u0083\7\64\2\2\u0083\u0084\5\22\n\2\u0084\17\3\2\2\2")
        buf.write("\u0085\u008a\7\66\2\2\u0086\u0087\7\63\2\2\u0087\u0089")
        buf.write("\7\66\2\2\u0088\u0086\3\2\2\2\u0089\u008c\3\2\2\2\u008a")
        buf.write("\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\21\3\2\2\2\u008c")
        buf.write("\u008a\3\2\2\2\u008d\u0095\5\24\13\2\u008e\u0095\7\7\2")
        buf.write("\2\u008f\u0095\7\21\2\2\u0090\u0095\7\r\2\2\u0091\u0095")
        buf.write("\7\t\2\2\u0092\u0095\7\23\2\2\u0093\u0095\7\26\2\2\u0094")
        buf.write("\u008d\3\2\2\2\u0094\u008e\3\2\2\2\u0094\u008f\3\2\2\2")
        buf.write("\u0094\u0090\3\2\2\2\u0094\u0091\3\2\2\2\u0094\u0092\3")
        buf.write("\2\2\2\u0094\u0093\3\2\2\2\u0095\23\3\2\2\2\u0096\u0097")
        buf.write("\7\33\2\2\u0097\u0098\7-\2\2\u0098\u0099\5\26\f\2\u0099")
        buf.write("\u009a\7.\2\2\u009a\u009b\7\31\2\2\u009b\u009c\t\2\2\2")
        buf.write("\u009c\25\3\2\2\2\u009d\u00a2\7\3\2\2\u009e\u009f\7\63")
        buf.write("\2\2\u009f\u00a1\7\3\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a4")
        buf.write("\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\27\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a6\7\66\2\2\u00a6")
        buf.write("\u00a7\7\64\2\2\u00a7\u00a8\7\17\2\2\u00a8\u00a9\5\22")
        buf.write("\n\2\u00a9\u00ab\7+\2\2\u00aa\u00ac\5\f\7\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00b0\7,\2\2\u00ae\u00af\7\32\2\2\u00af\u00b1\7\66\2")
        buf.write("\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b3\5\32\16\2\u00b3\31\3\2\2\2\u00b4")
        buf.write("\u00b5\5\60\31\2\u00b5\33\3\2\2\2\u00b6\u00c1\5\36\20")
        buf.write("\2\u00b7\u00c1\5 \21\2\u00b8\u00c1\5\"\22\2\u00b9\u00c1")
        buf.write("\5$\23\2\u00ba\u00c1\5&\24\2\u00bb\u00c1\5(\25\2\u00bc")
        buf.write("\u00c1\5*\26\2\u00bd\u00c1\5,\27\2\u00be\u00c1\5.\30\2")
        buf.write("\u00bf\u00c1\5\60\31\2\u00c0\u00b6\3\2\2\2\u00c0\u00b7")
        buf.write("\3\2\2\2\u00c0\u00b8\3\2\2\2\u00c0\u00b9\3\2\2\2\u00c0")
        buf.write("\u00ba\3\2\2\2\u00c0\u00bb\3\2\2\2\u00c0\u00bc\3\2\2\2")
        buf.write("\u00c0\u00bd\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00bf\3")
        buf.write("\2\2\2\u00c1\35\3\2\2\2\u00c2\u00c3\7\66\2\2\u00c3\u00c4")
        buf.write("\7\62\2\2\u00c4\u00c5\5\64\33\2\u00c5\u00c6\7\65\2\2\u00c6")
        buf.write("\37\3\2\2\2\u00c7\u00c8\7\20\2\2\u00c8\u00c9\7+\2\2\u00c9")
        buf.write("\u00ca\5\64\33\2\u00ca\u00cb\7,\2\2\u00cb\u00ce\5\34\17")
        buf.write("\2\u00cc\u00cd\7\13\2\2\u00cd\u00cf\5\34\17\2\u00ce\u00cc")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf!\3\2\2\2\u00d0\u00d1")
        buf.write("\7\16\2\2\u00d1\u00d2\7+\2\2\u00d2\u00d3\7\66\2\2\u00d3")
        buf.write("\u00d4\7\62\2\2\u00d4\u00d5\5\64\33\2\u00d5\u00d6\7\63")
        buf.write("\2\2\u00d6\u00d7\5\64\33\2\u00d7\u00d8\7\63\2\2\u00d8")
        buf.write("\u00d9\5\64\33\2\u00d9\u00da\7,\2\2\u00da\u00db\5\34\17")
        buf.write("\2\u00db#\3\2\2\2\u00dc\u00dd\7\25\2\2\u00dd\u00de\7+")
        buf.write("\2\2\u00de\u00df\5\64\33\2\u00df\u00e0\7,\2\2\u00e0\u00e1")
        buf.write("\5\34\17\2\u00e1%\3\2\2\2\u00e2\u00e3\7\n\2\2\u00e3\u00e4")
        buf.write("\5\60\31\2\u00e4\u00e5\7\25\2\2\u00e5\u00e6\7+\2\2\u00e6")
        buf.write("\u00e7\5\64\33\2\u00e7\u00e8\7,\2\2\u00e8\u00e9\7\65\2")
        buf.write("\2\u00e9\'\3\2\2\2\u00ea\u00eb\7\b\2\2\u00eb\u00ec\7\65")
        buf.write("\2\2\u00ec)\3\2\2\2\u00ed\u00ee\7\30\2\2\u00ee\u00ef\7")
        buf.write("\65\2\2\u00ef+\3\2\2\2\u00f0\u00f2\7\22\2\2\u00f1\u00f3")
        buf.write("\5\64\33\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\u00f4\3\2\2\2\u00f4\u00f5\7\65\2\2\u00f5-\3\2\2\2\u00f6")
        buf.write("\u00f7\7\66\2\2\u00f7\u00f9\7+\2\2\u00f8\u00fa\5\62\32")
        buf.write("\2\u00f9\u00f8\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb")
        buf.write("\3\2\2\2\u00fb\u00fc\7,\2\2\u00fc\u00fd\7\65\2\2\u00fd")
        buf.write("/\3\2\2\2\u00fe\u0103\7/\2\2\u00ff\u0102\5\34\17\2\u0100")
        buf.write("\u0102\5\6\4\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2")
        buf.write("\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3")
        buf.write("\2\2\2\u0104\u0106\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0107")
        buf.write("\7\60\2\2\u0107\61\3\2\2\2\u0108\u010d\5\64\33\2\u0109")
        buf.write("\u010a\7\63\2\2\u010a\u010c\5\64\33\2\u010b\u0109\3\2")
        buf.write("\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e")
        buf.write("\3\2\2\2\u010e\63\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111")
        buf.write("\5\66\34\2\u0111\65\3\2\2\2\u0112\u0113\58\35\2\u0113")
        buf.write("\u0114\7*\2\2\u0114\u0115\58\35\2\u0115\u0118\3\2\2\2")
        buf.write("\u0116\u0118\58\35\2\u0117\u0112\3\2\2\2\u0117\u0116\3")
        buf.write("\2\2\2\u0118\67\3\2\2\2\u0119\u011a\5:\36\2\u011a\u011b")
        buf.write("\t\3\2\2\u011b\u011c\5:\36\2\u011c\u011f\3\2\2\2\u011d")
        buf.write("\u011f\5:\36\2\u011e\u0119\3\2\2\2\u011e\u011d\3\2\2\2")
        buf.write("\u011f9\3\2\2\2\u0120\u0121\b\36\1\2\u0121\u0122\5<\37")
        buf.write("\2\u0122\u0128\3\2\2\2\u0123\u0124\f\4\2\2\u0124\u0125")
        buf.write("\t\4\2\2\u0125\u0127\5<\37\2\u0126\u0123\3\2\2\2\u0127")
        buf.write("\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2")
        buf.write("\u0129;\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012c\b\37\1")
        buf.write("\2\u012c\u012d\5> \2\u012d\u0133\3\2\2\2\u012e\u012f\f")
        buf.write("\4\2\2\u012f\u0130\t\5\2\2\u0130\u0132\5> \2\u0131\u012e")
        buf.write("\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134=\3\2\2\2\u0135\u0133\3\2\2\2\u0136")
        buf.write("\u0137\b \1\2\u0137\u0138\5@!\2\u0138\u013e\3\2\2\2\u0139")
        buf.write("\u013a\f\4\2\2\u013a\u013b\t\6\2\2\u013b\u013d\5@!\2\u013c")
        buf.write("\u0139\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2")
        buf.write("\u013e\u013f\3\2\2\2\u013f?\3\2\2\2\u0140\u013e\3\2\2")
        buf.write("\2\u0141\u0142\t\7\2\2\u0142\u0145\5@!\2\u0143\u0145\5")
        buf.write("B\"\2\u0144\u0141\3\2\2\2\u0144\u0143\3\2\2\2\u0145A\3")
        buf.write("\2\2\2\u0146\u0147\5D#\2\u0147\u0148\7-\2\2\u0148\u0149")
        buf.write("\5\62\32\2\u0149\u014a\7.\2\2\u014a\u014d\3\2\2\2\u014b")
        buf.write("\u014d\5D#\2\u014c\u0146\3\2\2\2\u014c\u014b\3\2\2\2\u014d")
        buf.write("C\3\2\2\2\u014e\u014f\7+\2\2\u014f\u0150\5\64\33\2\u0150")
        buf.write("\u0151\7,\2\2\u0151\u0154\3\2\2\2\u0152\u0154\5F$\2\u0153")
        buf.write("\u014e\3\2\2\2\u0153\u0152\3\2\2\2\u0154E\3\2\2\2\u0155")
        buf.write("\u0159\5H%\2\u0156\u0159\5L\'\2\u0157\u0159\7\66\2\2\u0158")
        buf.write("\u0155\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0157\3\2\2\2")
        buf.write("\u0159G\3\2\2\2\u015a\u0160\7\3\2\2\u015b\u0160\7\4\2")
        buf.write("\2\u015c\u0160\7\5\2\2\u015d\u0160\7\6\2\2\u015e\u0160")
        buf.write("\5J&\2\u015f\u015a\3\2\2\2\u015f\u015b\3\2\2\2\u015f\u015c")
        buf.write("\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160")
        buf.write("I\3\2\2\2\u0161\u0162\7/\2\2\u0162\u0163\5\62\32\2\u0163")
        buf.write("\u0164\7\60\2\2\u0164K\3\2\2\2\u0165\u0166\7\66\2\2\u0166")
        buf.write("\u0168\7+\2\2\u0167\u0169\5\62\32\2\u0168\u0167\3\2\2")
        buf.write("\2\u0168\u0169\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b")
        buf.write("\7,\2\2\u016bM\3\2\2\2 QW_qx|\177\u008a\u0094\u00a2\u00ab")
        buf.write("\u00b0\u00c0\u00ce\u00f2\u00f9\u0101\u0103\u010d\u0117")
        buf.write("\u011e\u0128\u0133\u013e\u0144\u014c\u0153\u0158\u015f")
        buf.write("\u0168")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'auto'", "'break'", "'boolean'", "'do'", 
                     "'else'", "'false'", "'float'", "'for'", "'function'", 
                     "'if'", "'integer'", "'return'", "'string'", "'true'", 
                     "'while'", "'void'", "'out'", "'continue'", "'of'", 
                     "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "'.'", "'='", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", 
                      "STRING_LIT", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                      "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                      "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", 
                      "CONTINUE", "OF", "INHERIT", "ARRAY", "ADD", "MINUS", 
                      "STAR", "DIV", "MOD", "NOT", "AND_AND", "OR_OR", "EQUAL", 
                      "NOT_EQUAL", "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
                      "DOUBLE_COLON", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", 
                      "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", "DOT", 
                      "ASSIGN", "COMMA", "COLON", "SEMI_COLON", "IDENTIFIER", 
                      "COMMENT_LINE", "COMMENT_BLOCK", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_variable_declaration = 2
    RULE_short_variable_declaration = 3
    RULE_long_variable_declaration = 4
    RULE_parameter_declaration_list = 5
    RULE_parameter_declaration = 6
    RULE_identifier_list = 7
    RULE_type_specifier = 8
    RULE_array_type_specifier = 9
    RULE_dimension_list = 10
    RULE_function_declaration = 11
    RULE_function_body = 12
    RULE_statement = 13
    RULE_assignment_statement = 14
    RULE_if_statement = 15
    RULE_for_statement = 16
    RULE_while_statement = 17
    RULE_do_while_statement = 18
    RULE_break_statement = 19
    RULE_continue_statement = 20
    RULE_return_statement = 21
    RULE_call_statement = 22
    RULE_block_statement = 23
    RULE_expr_list = 24
    RULE_expr = 25
    RULE_string_expr = 26
    RULE_relational_expr = 27
    RULE_logical_expr = 28
    RULE_adding_expr = 29
    RULE_multiplying_expr = 30
    RULE_unary_expr = 31
    RULE_indexing_expr = 32
    RULE_braced_expr = 33
    RULE_operand = 34
    RULE_literal = 35
    RULE_indexed_array_lit = 36
    RULE_function_call = 37

    ruleNames =  [ "program", "declaration", "variable_declaration", "short_variable_declaration", 
                   "long_variable_declaration", "parameter_declaration_list", 
                   "parameter_declaration", "identifier_list", "type_specifier", 
                   "array_type_specifier", "dimension_list", "function_declaration", 
                   "function_body", "statement", "assignment_statement", 
                   "if_statement", "for_statement", "while_statement", "do_while_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "call_statement", "block_statement", "expr_list", "expr", 
                   "string_expr", "relational_expr", "logical_expr", "adding_expr", 
                   "multiplying_expr", "unary_expr", "indexing_expr", "braced_expr", 
                   "operand", "literal", "indexed_array_lit", "function_call" ]

    EOF = Token.EOF
    INTEGER_LIT=1
    FLOAT_LIT=2
    BOOLEAN_LIT=3
    STRING_LIT=4
    AUTO=5
    BREAK=6
    BOOLEAN=7
    DO=8
    ELSE=9
    FALSE=10
    FLOAT=11
    FOR=12
    FUNCTION=13
    IF=14
    INTEGER=15
    RETURN=16
    STRING=17
    TRUE=18
    WHILE=19
    VOID=20
    OUT=21
    CONTINUE=22
    OF=23
    INHERIT=24
    ARRAY=25
    ADD=26
    MINUS=27
    STAR=28
    DIV=29
    MOD=30
    NOT=31
    AND_AND=32
    OR_OR=33
    EQUAL=34
    NOT_EQUAL=35
    LESS=36
    LESS_EQUAL=37
    GREATER=38
    GREATER_EQUAL=39
    DOUBLE_COLON=40
    OPEN_PAREN=41
    CLOSE_PAREN=42
    OPEN_BRACK=43
    CLOSE_BRACK=44
    OPEN_BRACE=45
    CLOSE_BRACE=46
    DOT=47
    ASSIGN=48
    COMMA=49
    COLON=50
    SEMI_COLON=51
    IDENTIFIER=52
    COMMENT_LINE=53
    COMMENT_BLOCK=54
    WS=55
    ERROR_CHAR=56
    UNCLOSE_STRING=57
    ILLEGAL_ESCAPE=58

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
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.declaration()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MT22Parser.IDENTIFIER):
                    break

            self.state = 81
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
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
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

        def short_variable_declaration(self):
            return self.getTypedRuleContext(MT22Parser.Short_variable_declarationContext,0)


        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def long_variable_declaration(self):
            return self.getTypedRuleContext(MT22Parser.Long_variable_declarationContext,0)


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
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.short_variable_declaration()
                self.state = 88
                self.match(MT22Parser.SEMI_COLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.long_variable_declaration()
                self.state = 91
                self.match(MT22Parser.SEMI_COLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Short_variable_declarationContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return MT22Parser.RULE_short_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShort_variable_declaration" ):
                return visitor.visitShort_variable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def short_variable_declaration(self):

        localctx = MT22Parser.Short_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_short_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.identifier_list()
            self.state = 96
            self.match(MT22Parser.COLON)
            self.state = 97
            self.type_specifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Long_variable_declarationContext(ParserRuleContext):
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


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def long_variable_declaration(self):
            return self.getTypedRuleContext(MT22Parser.Long_variable_declarationContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_long_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLong_variable_declaration" ):
                return visitor.visitLong_variable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def long_variable_declaration(self):

        localctx = MT22Parser.Long_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_long_variable_declaration)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(MT22Parser.IDENTIFIER)
                self.state = 100
                self.match(MT22Parser.COLON)
                self.state = 101
                self.type_specifier()
                self.state = 102
                self.match(MT22Parser.ASSIGN)
                self.state = 103
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(MT22Parser.IDENTIFIER)
                self.state = 106
                self.match(MT22Parser.COMMA)
                self.state = 107
                self.long_variable_declaration()
                self.state = 108
                self.match(MT22Parser.COMMA)
                self.state = 109
                self.expr()
                pass


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
        self.enterRule(localctx, 10, self.RULE_parameter_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.parameter_declaration()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 114
                self.match(MT22Parser.COMMA)
                self.state = 115
                self.parameter_declaration()
                self.state = 120
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
        self.enterRule(localctx, 12, self.RULE_parameter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 121
                self.match(MT22Parser.INHERIT)


            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 124
                self.match(MT22Parser.OUT)


            self.state = 127
            self.match(MT22Parser.IDENTIFIER)
            self.state = 128
            self.match(MT22Parser.COLON)
            self.state = 129
            self.type_specifier()
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
        self.enterRule(localctx, 14, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(MT22Parser.IDENTIFIER)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 132
                self.match(MT22Parser.COMMA)
                self.state = 133
                self.match(MT22Parser.IDENTIFIER)
                self.state = 138
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

        def array_type_specifier(self):
            return self.getTypedRuleContext(MT22Parser.Array_type_specifierContext,0)


        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

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
        self.enterRule(localctx, 16, self.RULE_type_specifier)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.array_type_specifier()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(MT22Parser.AUTO)
                pass
            elif token in [MT22Parser.INTEGER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.match(MT22Parser.INTEGER)
                pass
            elif token in [MT22Parser.FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.match(MT22Parser.FLOAT)
                pass
            elif token in [MT22Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.match(MT22Parser.BOOLEAN)
                pass
            elif token in [MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 6)
                self.state = 144
                self.match(MT22Parser.STRING)
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 145
                self.match(MT22Parser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_type_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def OPEN_BRACK(self):
            return self.getToken(MT22Parser.OPEN_BRACK, 0)

        def dimension_list(self):
            return self.getTypedRuleContext(MT22Parser.Dimension_listContext,0)


        def CLOSE_BRACK(self):
            return self.getToken(MT22Parser.CLOSE_BRACK, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_array_type_specifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type_specifier" ):
                return visitor.visitArray_type_specifier(self)
            else:
                return visitor.visitChildren(self)




    def array_type_specifier(self):

        localctx = MT22Parser.Array_type_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_type_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(MT22Parser.ARRAY)
            self.state = 149
            self.match(MT22Parser.OPEN_BRACK)
            self.state = 150
            self.dimension_list()
            self.state = 151
            self.match(MT22Parser.CLOSE_BRACK)
            self.state = 152
            self.match(MT22Parser.OF)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
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


    class Dimension_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.INTEGER_LIT)
            else:
                return self.getToken(MT22Parser.INTEGER_LIT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_dimension_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_list" ):
                return visitor.visitDimension_list(self)
            else:
                return visitor.visitChildren(self)




    def dimension_list(self):

        localctx = MT22Parser.Dimension_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dimension_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MT22Parser.INTEGER_LIT)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 156
                self.match(MT22Parser.COMMA)
                self.state = 157
                self.match(MT22Parser.INTEGER_LIT)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 22, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(MT22Parser.IDENTIFIER)
            self.state = 164
            self.match(MT22Parser.COLON)
            self.state = 165
            self.match(MT22Parser.FUNCTION)
            self.state = 166
            self.type_specifier()
            self.state = 167
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.OUT) | (1 << MT22Parser.INHERIT) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 168
                self.parameter_declaration_list()


            self.state = 171
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 172
                self.match(MT22Parser.INHERIT)
                self.state = 173
                self.match(MT22Parser.IDENTIFIER)


            self.state = 176
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
        self.enterRule(localctx, 24, self.RULE_function_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
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
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.assignment_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.while_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 184
                self.do_while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 185
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 186
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 187
                self.return_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 188
                self.call_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 189
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

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


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
        self.enterRule(localctx, 28, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(MT22Parser.IDENTIFIER)
            self.state = 193
            self.match(MT22Parser.ASSIGN)
            self.state = 194
            self.expr()
            self.state = 195
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

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


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
        self.enterRule(localctx, 30, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(MT22Parser.IF)
            self.state = 198
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 199
            self.expr()
            self.state = 200
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 201
            self.statement()
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 202
                self.match(MT22Parser.ELSE)
                self.state = 203
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


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
        self.enterRule(localctx, 32, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MT22Parser.FOR)
            self.state = 207
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 208
            self.match(MT22Parser.IDENTIFIER)
            self.state = 209
            self.match(MT22Parser.ASSIGN)
            self.state = 210
            self.expr()
            self.state = 211
            self.match(MT22Parser.COMMA)
            self.state = 212
            self.expr()
            self.state = 213
            self.match(MT22Parser.COMMA)
            self.state = 214
            self.expr()
            self.state = 215
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 216
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

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


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
        self.enterRule(localctx, 34, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(MT22Parser.WHILE)
            self.state = 219
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 220
            self.expr()
            self.state = 221
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 222
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

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


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
        self.enterRule(localctx, 36, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MT22Parser.DO)
            self.state = 225
            self.block_statement()
            self.state = 226
            self.match(MT22Parser.WHILE)
            self.state = 227
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 228
            self.expr()
            self.state = 229
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 230
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
        self.enterRule(localctx, 38, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(MT22Parser.BREAK)
            self.state = 233
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
        self.enterRule(localctx, 40, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(MT22Parser.CONTINUE)
            self.state = 236
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

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MT22Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MT22Parser.RETURN)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER_LIT) | (1 << MT22Parser.FLOAT_LIT) | (1 << MT22Parser.BOOLEAN_LIT) | (1 << MT22Parser.STRING_LIT) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.NOT) | (1 << MT22Parser.OPEN_PAREN) | (1 << MT22Parser.OPEN_BRACE) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 239
                self.expr()


            self.state = 242
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

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MT22Parser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(MT22Parser.IDENTIFIER)
            self.state = 245
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER_LIT) | (1 << MT22Parser.FLOAT_LIT) | (1 << MT22Parser.BOOLEAN_LIT) | (1 << MT22Parser.STRING_LIT) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.NOT) | (1 << MT22Parser.OPEN_PAREN) | (1 << MT22Parser.OPEN_BRACE) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 246
                self.expr_list()


            self.state = 249
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 250
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


        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Variable_declarationContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = MT22Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(MT22Parser.OPEN_BRACE)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.OPEN_BRACE) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 255
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 253
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 254
                    self.variable_declaration()
                    pass


                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 260
            self.match(MT22Parser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MT22Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.expr()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 263
                self.match(MT22Parser.COMMA)
                self.state = 264
                self.expr()
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expr(self):
            return self.getTypedRuleContext(MT22Parser.String_exprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.string_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Relational_exprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Relational_exprContext,i)


        def DOUBLE_COLON(self):
            return self.getToken(MT22Parser.DOUBLE_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_string_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expr" ):
                return visitor.visitString_expr(self)
            else:
                return visitor.visitChildren(self)




    def string_expr(self):

        localctx = MT22Parser.String_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_string_expr)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.relational_expr()
                self.state = 273
                self.match(MT22Parser.DOUBLE_COLON)
                self.state = 274
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.relational_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Logical_exprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Logical_exprContext,i)


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
            return MT22Parser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = MT22Parser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_relational_expr)
        self._la = 0 # Token type
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.logical_expr(0)
                self.state = 280
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOT_EQUAL) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LESS_EQUAL) | (1 << MT22Parser.GREATER) | (1 << MT22Parser.GREATER_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 281
                self.logical_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.logical_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expr(self):
            return self.getTypedRuleContext(MT22Parser.Adding_exprContext,0)


        def logical_expr(self):
            return self.getTypedRuleContext(MT22Parser.Logical_exprContext,0)


        def AND_AND(self):
            return self.getToken(MT22Parser.AND_AND, 0)

        def OR_OR(self):
            return self.getToken(MT22Parser.OR_OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_logical_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr" ):
                return visitor.visitLogical_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Logical_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_logical_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.adding_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Logical_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                    self.state = 289
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 290
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND_AND or _la==MT22Parser.OR_OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 291
                    self.adding_expr(0) 
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expr(self):
            return self.getTypedRuleContext(MT22Parser.Multiplying_exprContext,0)


        def adding_expr(self):
            return self.getTypedRuleContext(MT22Parser.Adding_exprContext,0)


        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_adding_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expr" ):
                return visitor.visitAdding_expr(self)
            else:
                return visitor.visitChildren(self)



    def adding_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Adding_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_adding_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 300
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 301
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 302
                    self.multiplying_expr(0) 
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expr(self):
            return self.getTypedRuleContext(MT22Parser.Unary_exprContext,0)


        def multiplying_expr(self):
            return self.getTypedRuleContext(MT22Parser.Multiplying_exprContext,0)


        def STAR(self):
            return self.getToken(MT22Parser.STAR, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_multiplying_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expr" ):
                return visitor.visitMultiplying_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Multiplying_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_multiplying_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.unary_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 311
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STAR) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 313
                    self.unary_expr() 
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Unary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expr(self):
            return self.getTypedRuleContext(MT22Parser.Unary_exprContext,0)


        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def indexing_expr(self):
            return self.getTypedRuleContext(MT22Parser.Indexing_exprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_unary_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expr" ):
                return visitor.visitUnary_expr(self)
            else:
                return visitor.visitChildren(self)




    def unary_expr(self):

        localctx = MT22Parser.Unary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_unary_expr)
        self._la = 0 # Token type
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUS, MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                _la = self._input.LA(1)
                if not(_la==MT22Parser.MINUS or _la==MT22Parser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 320
                self.unary_expr()
                pass
            elif token in [MT22Parser.INTEGER_LIT, MT22Parser.FLOAT_LIT, MT22Parser.BOOLEAN_LIT, MT22Parser.STRING_LIT, MT22Parser.OPEN_PAREN, MT22Parser.OPEN_BRACE, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.indexing_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexing_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def braced_expr(self):
            return self.getTypedRuleContext(MT22Parser.Braced_exprContext,0)


        def OPEN_BRACK(self):
            return self.getToken(MT22Parser.OPEN_BRACK, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def CLOSE_BRACK(self):
            return self.getToken(MT22Parser.CLOSE_BRACK, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_indexing_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexing_expr" ):
                return visitor.visitIndexing_expr(self)
            else:
                return visitor.visitChildren(self)




    def indexing_expr(self):

        localctx = MT22Parser.Indexing_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_indexing_expr)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.braced_expr()
                self.state = 325
                self.match(MT22Parser.OPEN_BRACK)
                self.state = 326
                self.expr_list()
                self.state = 327
                self.match(MT22Parser.CLOSE_BRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.braced_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Braced_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(MT22Parser.OPEN_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(MT22Parser.CLOSE_PAREN, 0)

        def operand(self):
            return self.getTypedRuleContext(MT22Parser.OperandContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_braced_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBraced_expr" ):
                return visitor.visitBraced_expr(self)
            else:
                return visitor.visitChildren(self)




    def braced_expr(self):

        localctx = MT22Parser.Braced_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_braced_expr)
        try:
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OPEN_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(MT22Parser.OPEN_PAREN)
                self.state = 333
                self.expr()
                self.state = 334
                self.match(MT22Parser.CLOSE_PAREN)
                pass
            elif token in [MT22Parser.INTEGER_LIT, MT22Parser.FLOAT_LIT, MT22Parser.BOOLEAN_LIT, MT22Parser.STRING_LIT, MT22Parser.OPEN_BRACE, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MT22Parser.LiteralContext,0)


        def function_call(self):
            return self.getTypedRuleContext(MT22Parser.Function_callContext,0)


        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_operand)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.function_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 341
                self.match(MT22Parser.IDENTIFIER)
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

        def INTEGER_LIT(self):
            return self.getToken(MT22Parser.INTEGER_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MT22Parser.FLOAT_LIT, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(MT22Parser.BOOLEAN_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MT22Parser.STRING_LIT, 0)

        def indexed_array_lit(self):
            return self.getTypedRuleContext(MT22Parser.Indexed_array_litContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MT22Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_literal)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.match(MT22Parser.INTEGER_LIT)
                pass
            elif token in [MT22Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.match(MT22Parser.FLOAT_LIT)
                pass
            elif token in [MT22Parser.BOOLEAN_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 346
                self.match(MT22Parser.BOOLEAN_LIT)
                pass
            elif token in [MT22Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 347
                self.match(MT22Parser.STRING_LIT)
                pass
            elif token in [MT22Parser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 348
                self.indexed_array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(MT22Parser.OPEN_BRACE, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(MT22Parser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_indexed_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array_lit" ):
                return visitor.visitIndexed_array_lit(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array_lit(self):

        localctx = MT22Parser.Indexed_array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_indexed_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(MT22Parser.OPEN_BRACE)
            self.state = 352
            self.expr_list()
            self.state = 353
            self.match(MT22Parser.CLOSE_BRACE)
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

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def OPEN_PAREN(self):
            return self.getToken(MT22Parser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(MT22Parser.CLOSE_PAREN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = MT22Parser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(MT22Parser.IDENTIFIER)
            self.state = 356
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER_LIT) | (1 << MT22Parser.FLOAT_LIT) | (1 << MT22Parser.BOOLEAN_LIT) | (1 << MT22Parser.STRING_LIT) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.NOT) | (1 << MT22Parser.OPEN_PAREN) | (1 << MT22Parser.OPEN_BRACE) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 357
                self.expr_list()


            self.state = 360
            self.match(MT22Parser.CLOSE_PAREN)
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
        self._predicates[28] = self.logical_expr_sempred
        self._predicates[29] = self.adding_expr_sempred
        self._predicates[30] = self.multiplying_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expr_sempred(self, localctx:Logical_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_expr_sempred(self, localctx:Adding_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expr_sempred(self, localctx:Multiplying_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         





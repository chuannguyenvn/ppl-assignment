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
<<<<<<< HEAD
        buf.write("\u0183\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
=======
        buf.write("\u0177\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\6\2R\n\2\r\2\16\2S\3\2\3\2\3\3\3\3")
        buf.write("\5\3Z\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4b\n\4\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6t\n\6\3\7\3\7\3\7\7\7y\n\7\f\7\16\7|\13\7\3\b\5\b\177")
        buf.write("\n\b\3\b\5\b\u0082\n\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t")
        buf.write("\u008b\n\t\f\t\16\t\u008e\13\t\3\n\3\n\3\n\3\n\3\n\3\n")
<<<<<<< HEAD
        buf.write("\3\n\5\n\u0097\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\7\f\u00a3\n\f\f\f\16\f\u00a6\13\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\5\r\u00ae\n\r\3\r\3\r\3\r\5\r\u00b3\n")
        buf.write("\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u00c3\n\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00d1\n\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\5\27\u00f5\n\27\3\27\3\27\3\30\3\30\3\30\5\30\u00fc")
        buf.write("\n\30\3\30\3\30\3\30\3\31\3\31\3\31\7\31\u0104\n\31\f")
        buf.write("\31\16\31\u0107\13\31\3\31\3\31\3\32\3\32\3\32\7\32\u010e")
        buf.write("\n\32\f\32\16\32\u0111\13\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u011a\n\34\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\7\35\u0122\n\35\f\35\16\35\u0125\13\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\7\36\u012d\n\36\f\36\16\36\u0130\13")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0138\n\37\f\37")
        buf.write("\16\37\u013b\13\37\3 \3 \3 \3 \3 \3 \7 \u0143\n \f \16")
        buf.write(" \u0146\13 \3!\3!\3!\5!\u014b\n!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\5\"\u0154\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\7#")
        buf.write("\u0160\n#\f#\16#\u0163\13#\3$\3$\3$\3$\3$\5$\u016a\n$")
        buf.write("\3%\3%\3%\5%\u016f\n%\3&\3&\3&\3&\3&\5&\u0176\n&\3\'\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\5(\u017f\n(\3(\3(\3(\2\78:<>D)\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLN\2\b\6\2\t\t\r\r\21\21\23\23\3\2$)\3\2")
        buf.write("\"#\3\2\34\35\3\2\36 \4\2\35\35!!\2\u018b\2Q\3\2\2\2\4")
        buf.write("Y\3\2\2\2\6a\3\2\2\2\bc\3\2\2\2\ns\3\2\2\2\fu\3\2\2\2")
        buf.write("\16~\3\2\2\2\20\u0087\3\2\2\2\22\u0096\3\2\2\2\24\u0098")
        buf.write("\3\2\2\2\26\u009f\3\2\2\2\30\u00a7\3\2\2\2\32\u00b6\3")
        buf.write("\2\2\2\34\u00c2\3\2\2\2\36\u00c4\3\2\2\2 \u00c9\3\2\2")
        buf.write("\2\"\u00d2\3\2\2\2$\u00de\3\2\2\2&\u00e4\3\2\2\2(\u00ec")
        buf.write("\3\2\2\2*\u00ef\3\2\2\2,\u00f2\3\2\2\2.\u00f8\3\2\2\2")
        buf.write("\60\u0100\3\2\2\2\62\u010a\3\2\2\2\64\u0112\3\2\2\2\66")
        buf.write("\u0119\3\2\2\28\u011b\3\2\2\2:\u0126\3\2\2\2<\u0131\3")
        buf.write("\2\2\2>\u013c\3\2\2\2@\u014a\3\2\2\2B\u0153\3\2\2\2D\u0155")
        buf.write("\3\2\2\2F\u0169\3\2\2\2H\u016e\3\2\2\2J\u0175\3\2\2\2")
        buf.write("L\u0177\3\2\2\2N\u017b\3\2\2\2PR\5\4\3\2QP\3\2\2\2RS\3")
        buf.write("\2\2\2SQ\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\7\2\2\3V\3\3\2")
        buf.write("\2\2WZ\5\6\4\2XZ\5\30\r\2YW\3\2\2\2YX\3\2\2\2Z\5\3\2\2")
        buf.write("\2[\\\5\b\5\2\\]\7\65\2\2]b\3\2\2\2^_\5\n\6\2_`\7\65\2")
        buf.write("\2`b\3\2\2\2a[\3\2\2\2a^\3\2\2\2b\7\3\2\2\2cd\5\20\t\2")
        buf.write("de\7\64\2\2ef\5\22\n\2f\t\3\2\2\2gh\7\66\2\2hi\7\64\2")
        buf.write("\2ij\5\22\n\2jk\7\62\2\2kl\5\64\33\2lt\3\2\2\2mn\7\66")
        buf.write("\2\2no\7\63\2\2op\5\n\6\2pq\7\63\2\2qr\5\64\33\2rt\3\2")
        buf.write("\2\2sg\3\2\2\2sm\3\2\2\2t\13\3\2\2\2uz\5\16\b\2vw\7\63")
        buf.write("\2\2wy\5\16\b\2xv\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2")
        buf.write("\2{\r\3\2\2\2|z\3\2\2\2}\177\7\32\2\2~}\3\2\2\2~\177\3")
        buf.write("\2\2\2\177\u0081\3\2\2\2\u0080\u0082\7\27\2\2\u0081\u0080")
        buf.write("\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0084\7\66\2\2\u0084\u0085\7\64\2\2\u0085\u0086\5\22")
        buf.write("\n\2\u0086\17\3\2\2\2\u0087\u008c\7\66\2\2\u0088\u0089")
        buf.write("\7\63\2\2\u0089\u008b\7\66\2\2\u008a\u0088\3\2\2\2\u008b")
        buf.write("\u008e\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\21\3\2\2\2\u008e\u008c\3\2\2\2\u008f\u0097\5\24")
        buf.write("\13\2\u0090\u0097\7\7\2\2\u0091\u0097\7\21\2\2\u0092\u0097")
        buf.write("\7\r\2\2\u0093\u0097\7\t\2\2\u0094\u0097\7\23\2\2\u0095")
        buf.write("\u0097\7\26\2\2\u0096\u008f\3\2\2\2\u0096\u0090\3\2\2")
        buf.write("\2\u0096\u0091\3\2\2\2\u0096\u0092\3\2\2\2\u0096\u0093")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\23\3\2\2\2\u0098\u0099\7\33\2\2\u0099\u009a\7-\2\2\u009a")
        buf.write("\u009b\5\26\f\2\u009b\u009c\7.\2\2\u009c\u009d\7\31\2")
        buf.write("\2\u009d\u009e\t\2\2\2\u009e\25\3\2\2\2\u009f\u00a4\7")
        buf.write("\3\2\2\u00a0\u00a1\7\63\2\2\u00a1\u00a3\7\3\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2")
        buf.write("\u00a4\u00a5\3\2\2\2\u00a5\27\3\2\2\2\u00a6\u00a4\3\2")
        buf.write("\2\2\u00a7\u00a8\7\66\2\2\u00a8\u00a9\7\64\2\2\u00a9\u00aa")
        buf.write("\7\17\2\2\u00aa\u00ab\5\22\n\2\u00ab\u00ad\7+\2\2\u00ac")
        buf.write("\u00ae\5\f\7\2\u00ad\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2")
        buf.write("\u00ae\u00af\3\2\2\2\u00af\u00b2\7,\2\2\u00b0\u00b1\7")
        buf.write("\32\2\2\u00b1\u00b3\7\66\2\2\u00b2\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\5\32\16")
        buf.write("\2\u00b5\31\3\2\2\2\u00b6\u00b7\5\60\31\2\u00b7\33\3\2")
        buf.write("\2\2\u00b8\u00c3\5\36\20\2\u00b9\u00c3\5 \21\2\u00ba\u00c3")
        buf.write("\5\"\22\2\u00bb\u00c3\5$\23\2\u00bc\u00c3\5&\24\2\u00bd")
        buf.write("\u00c3\5(\25\2\u00be\u00c3\5*\26\2\u00bf\u00c3\5,\27\2")
        buf.write("\u00c0\u00c3\5.\30\2\u00c1\u00c3\5\60\31\2\u00c2\u00b8")
=======
        buf.write("\5\n\u0096\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\7\f\u00a2\n\f\f\f\16\f\u00a5\13\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00ad\n\r\3\r\3\r\3\r\5\r\u00b2\n\r\3")
        buf.write("\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u00c3\n\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00d1\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\5\27\u00f5\n\27\3\27\3\27\3\30\3\30\3\30\5")
        buf.write("\30\u00fc\n\30\3\30\3\30\3\30\3\31\3\31\7\31\u0103\n\31")
        buf.write("\f\31\16\31\u0106\13\31\3\31\3\31\3\32\3\32\3\32\7\32")
        buf.write("\u010d\n\32\f\32\16\32\u0110\13\32\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u0119\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\7\35\u0121\n\35\f\35\16\35\u0124\13\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\7\36\u012c\n\36\f\36\16\36\u012f")
        buf.write("\13\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0137\n\37\f")
        buf.write("\37\16\37\u013a\13\37\3 \3 \3 \3 \3 \3 \7 \u0142\n \f")
        buf.write(" \16 \u0145\13 \3!\3!\3!\5!\u014a\n!\3\"\3\"\3\"\5\"\u014f")
        buf.write("\n\"\3#\3#\3#\3#\3#\3#\5#\u0157\n#\3$\3$\3$\3$\3$\5$\u015e")
        buf.write("\n$\3%\3%\3%\5%\u0163\n%\3&\3&\3&\3&\3&\5&\u016a\n&\3")
        buf.write("\'\3\'\3\'\3\'\3(\3(\3(\5(\u0173\n(\3(\3(\3(\2\68:<>)")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLN\2\7\6\2\t\t\r\r\21\21\23\23\3\2$)\3")
        buf.write("\2\"#\3\2\34\35\3\2\36 \2\u017e\2Q\3\2\2\2\4Y\3\2\2\2")
        buf.write("\6a\3\2\2\2\bc\3\2\2\2\ns\3\2\2\2\fu\3\2\2\2\16~\3\2\2")
        buf.write("\2\20\u0087\3\2\2\2\22\u0095\3\2\2\2\24\u0097\3\2\2\2")
        buf.write("\26\u009e\3\2\2\2\30\u00a6\3\2\2\2\32\u00b5\3\2\2\2\34")
        buf.write("\u00c2\3\2\2\2\36\u00c4\3\2\2\2 \u00c9\3\2\2\2\"\u00d2")
        buf.write("\3\2\2\2$\u00de\3\2\2\2&\u00e4\3\2\2\2(\u00ec\3\2\2\2")
        buf.write("*\u00ef\3\2\2\2,\u00f2\3\2\2\2.\u00f8\3\2\2\2\60\u0100")
        buf.write("\3\2\2\2\62\u0109\3\2\2\2\64\u0111\3\2\2\2\66\u0118\3")
        buf.write("\2\2\28\u011a\3\2\2\2:\u0125\3\2\2\2<\u0130\3\2\2\2>\u013b")
        buf.write("\3\2\2\2@\u0149\3\2\2\2B\u014e\3\2\2\2D\u0156\3\2\2\2")
        buf.write("F\u015d\3\2\2\2H\u0162\3\2\2\2J\u0169\3\2\2\2L\u016b\3")
        buf.write("\2\2\2N\u016f\3\2\2\2PR\5\4\3\2QP\3\2\2\2RS\3\2\2\2SQ")
        buf.write("\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\7\2\2\3V\3\3\2\2\2WZ\5")
        buf.write("\6\4\2XZ\5\30\r\2YW\3\2\2\2YX\3\2\2\2Z\5\3\2\2\2[\\\5")
        buf.write("\b\5\2\\]\7\65\2\2]b\3\2\2\2^_\5\n\6\2_`\7\65\2\2`b\3")
        buf.write("\2\2\2a[\3\2\2\2a^\3\2\2\2b\7\3\2\2\2cd\5\20\t\2de\7\64")
        buf.write("\2\2ef\5\22\n\2f\t\3\2\2\2gh\7\66\2\2hi\7\64\2\2ij\5\22")
        buf.write("\n\2jk\7\62\2\2kl\5\64\33\2lt\3\2\2\2mn\7\66\2\2no\7\63")
        buf.write("\2\2op\5\n\6\2pq\7\63\2\2qr\5\64\33\2rt\3\2\2\2sg\3\2")
        buf.write("\2\2sm\3\2\2\2t\13\3\2\2\2uz\5\16\b\2vw\7\63\2\2wy\5\16")
        buf.write("\b\2xv\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\r\3\2\2")
        buf.write("\2|z\3\2\2\2}\177\7\32\2\2~}\3\2\2\2~\177\3\2\2\2\177")
        buf.write("\u0081\3\2\2\2\u0080\u0082\7\27\2\2\u0081\u0080\3\2\2")
        buf.write("\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084")
        buf.write("\7\66\2\2\u0084\u0085\7\64\2\2\u0085\u0086\5\22\n\2\u0086")
        buf.write("\17\3\2\2\2\u0087\u008c\7\66\2\2\u0088\u0089\7\63\2\2")
        buf.write("\u0089\u008b\7\66\2\2\u008a\u0088\3\2\2\2\u008b\u008e")
        buf.write("\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write("\21\3\2\2\2\u008e\u008c\3\2\2\2\u008f\u0096\5\24\13\2")
        buf.write("\u0090\u0096\7\21\2\2\u0091\u0096\7\r\2\2\u0092\u0096")
        buf.write("\7\t\2\2\u0093\u0096\7\23\2\2\u0094\u0096\7\26\2\2\u0095")
        buf.write("\u008f\3\2\2\2\u0095\u0090\3\2\2\2\u0095\u0091\3\2\2\2")
        buf.write("\u0095\u0092\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3")
        buf.write("\2\2\2\u0096\23\3\2\2\2\u0097\u0098\7\33\2\2\u0098\u0099")
        buf.write("\7-\2\2\u0099\u009a\5\26\f\2\u009a\u009b\7.\2\2\u009b")
        buf.write("\u009c\7\31\2\2\u009c\u009d\t\2\2\2\u009d\25\3\2\2\2\u009e")
        buf.write("\u00a3\7\3\2\2\u009f\u00a0\7\63\2\2\u00a0\u00a2\7\3\2")
        buf.write("\2\u00a1\u009f\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\27\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a6\u00a7\7\66\2\2\u00a7\u00a8\7\64\2\2\u00a8")
        buf.write("\u00a9\7\17\2\2\u00a9\u00aa\5\22\n\2\u00aa\u00ac\7+\2")
        buf.write("\2\u00ab\u00ad\5\f\7\2\u00ac\u00ab\3\2\2\2\u00ac\u00ad")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b1\7,\2\2\u00af")
        buf.write("\u00b0\7\32\2\2\u00b0\u00b2\7\66\2\2\u00b1\u00af\3\2\2")
        buf.write("\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4")
        buf.write("\5\32\16\2\u00b4\31\3\2\2\2\u00b5\u00b6\5\60\31\2\u00b6")
        buf.write("\33\3\2\2\2\u00b7\u00c3\5\36\20\2\u00b8\u00c3\5 \21\2")
        buf.write("\u00b9\u00c3\5\"\22\2\u00ba\u00c3\5$\23\2\u00bb\u00c3")
        buf.write("\5&\24\2\u00bc\u00c3\5(\25\2\u00bd\u00c3\5*\26\2\u00be")
        buf.write("\u00c3\5,\27\2\u00bf\u00c3\5.\30\2\u00c0\u00c3\5\60\31")
        buf.write("\2\u00c1\u00c3\5\4\3\2\u00c2\u00b7\3\2\2\2\u00c2\u00b8")
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
        buf.write("\3\2\2\2\u00c2\u00b9\3\2\2\2\u00c2\u00ba\3\2\2\2\u00c2")
        buf.write("\u00bb\3\2\2\2\u00c2\u00bc\3\2\2\2\u00c2\u00bd\3\2\2\2")
        buf.write("\u00c2\u00be\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c2\u00c0\3")
        buf.write("\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\35\3\2\2\2\u00c4\u00c5")
        buf.write("\7\66\2\2\u00c5\u00c6\7\62\2\2\u00c6\u00c7\5\64\33\2\u00c7")
        buf.write("\u00c8\7\65\2\2\u00c8\37\3\2\2\2\u00c9\u00ca\7\20\2\2")
        buf.write("\u00ca\u00cb\7+\2\2\u00cb\u00cc\5\64\33\2\u00cc\u00cd")
        buf.write("\7,\2\2\u00cd\u00d0\5\34\17\2\u00ce\u00cf\7\13\2\2\u00cf")
        buf.write("\u00d1\5\34\17\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2")
        buf.write("\2\u00d1!\3\2\2\2\u00d2\u00d3\7\16\2\2\u00d3\u00d4\7+")
        buf.write("\2\2\u00d4\u00d5\7\66\2\2\u00d5\u00d6\7\62\2\2\u00d6\u00d7")
        buf.write("\5\64\33\2\u00d7\u00d8\7\63\2\2\u00d8\u00d9\5\64\33\2")
        buf.write("\u00d9\u00da\7\63\2\2\u00da\u00db\5\64\33\2\u00db\u00dc")
        buf.write("\7,\2\2\u00dc\u00dd\5\34\17\2\u00dd#\3\2\2\2\u00de\u00df")
        buf.write("\7\25\2\2\u00df\u00e0\7+\2\2\u00e0\u00e1\5\64\33\2\u00e1")
        buf.write("\u00e2\7,\2\2\u00e2\u00e3\5\34\17\2\u00e3%\3\2\2\2\u00e4")
        buf.write("\u00e5\7\n\2\2\u00e5\u00e6\5\60\31\2\u00e6\u00e7\7\25")
        buf.write("\2\2\u00e7\u00e8\7+\2\2\u00e8\u00e9\5\64\33\2\u00e9\u00ea")
        buf.write("\7,\2\2\u00ea\u00eb\7\65\2\2\u00eb\'\3\2\2\2\u00ec\u00ed")
        buf.write("\7\b\2\2\u00ed\u00ee\7\65\2\2\u00ee)\3\2\2\2\u00ef\u00f0")
        buf.write("\7\30\2\2\u00f0\u00f1\7\65\2\2\u00f1+\3\2\2\2\u00f2\u00f4")
        buf.write("\7\22\2\2\u00f3\u00f5\5\64\33\2\u00f4\u00f3\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\7\65\2")
        buf.write("\2\u00f7-\3\2\2\2\u00f8\u00f9\7\66\2\2\u00f9\u00fb\7+")
        buf.write("\2\2\u00fa\u00fc\5\62\32\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc")
        buf.write("\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\7,\2\2\u00fe")
<<<<<<< HEAD
        buf.write("\u00ff\7\65\2\2\u00ff/\3\2\2\2\u0100\u0105\7/\2\2\u0101")
        buf.write("\u0104\5\34\17\2\u0102\u0104\5\6\4\2\u0103\u0101\3\2\2")
        buf.write("\2\u0103\u0102\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103")
        buf.write("\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0108\3\2\2\2\u0107")
        buf.write("\u0105\3\2\2\2\u0108\u0109\7\60\2\2\u0109\61\3\2\2\2\u010a")
        buf.write("\u010f\5\64\33\2\u010b\u010c\7\63\2\2\u010c\u010e\5\64")
        buf.write("\33\2\u010d\u010b\3\2\2\2\u010e\u0111\3\2\2\2\u010f\u010d")
        buf.write("\3\2\2\2\u010f\u0110\3\2\2\2\u0110\63\3\2\2\2\u0111\u010f")
        buf.write("\3\2\2\2\u0112\u0113\5\66\34\2\u0113\65\3\2\2\2\u0114")
        buf.write("\u0115\58\35\2\u0115\u0116\7*\2\2\u0116\u0117\58\35\2")
        buf.write("\u0117\u011a\3\2\2\2\u0118\u011a\58\35\2\u0119\u0114\3")
        buf.write("\2\2\2\u0119\u0118\3\2\2\2\u011a\67\3\2\2\2\u011b\u011c")
        buf.write("\b\35\1\2\u011c\u011d\5:\36\2\u011d\u0123\3\2\2\2\u011e")
        buf.write("\u011f\f\4\2\2\u011f\u0120\t\3\2\2\u0120\u0122\58\35\5")
        buf.write("\u0121\u011e\3\2\2\2\u0122\u0125\3\2\2\2\u0123\u0121\3")
        buf.write("\2\2\2\u0123\u0124\3\2\2\2\u01249\3\2\2\2\u0125\u0123")
        buf.write("\3\2\2\2\u0126\u0127\b\36\1\2\u0127\u0128\5<\37\2\u0128")
        buf.write("\u012e\3\2\2\2\u0129\u012a\f\4\2\2\u012a\u012b\t\4\2\2")
        buf.write("\u012b\u012d\5<\37\2\u012c\u0129\3\2\2\2\u012d\u0130\3")
        buf.write("\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f;")
        buf.write("\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0132\b\37\1\2\u0132")
        buf.write("\u0133\5> \2\u0133\u0139\3\2\2\2\u0134\u0135\f\4\2\2\u0135")
        buf.write("\u0136\t\5\2\2\u0136\u0138\5> \2\u0137\u0134\3\2\2\2\u0138")
        buf.write("\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2")
        buf.write("\u013a=\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d\b \1\2")
        buf.write("\u013d\u013e\5@!\2\u013e\u0144\3\2\2\2\u013f\u0140\f\4")
        buf.write("\2\2\u0140\u0141\t\6\2\2\u0141\u0143\5@!\2\u0142\u013f")
        buf.write("\3\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144")
        buf.write("\u0145\3\2\2\2\u0145?\3\2\2\2\u0146\u0144\3\2\2\2\u0147")
        buf.write("\u0148\t\7\2\2\u0148\u014b\5@!\2\u0149\u014b\5B\"\2\u014a")
        buf.write("\u0147\3\2\2\2\u014a\u0149\3\2\2\2\u014bA\3\2\2\2\u014c")
        buf.write("\u014d\7\66\2\2\u014d\u014e\5D#\2\u014e\u014f\7-\2\2\u014f")
        buf.write("\u0150\5\62\32\2\u0150\u0151\7.\2\2\u0151\u0154\3\2\2")
        buf.write("\2\u0152\u0154\5F$\2\u0153\u014c\3\2\2\2\u0153\u0152\3")
        buf.write("\2\2\2\u0154C\3\2\2\2\u0155\u0156\b#\1\2\u0156\u0157\7")
        buf.write("-\2\2\u0157\u0158\5\62\32\2\u0158\u0159\7.\2\2\u0159\u0161")
        buf.write("\3\2\2\2\u015a\u015b\f\4\2\2\u015b\u015c\7-\2\2\u015c")
        buf.write("\u015d\5\62\32\2\u015d\u015e\7.\2\2\u015e\u0160\3\2\2")
        buf.write("\2\u015f\u015a\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f")
        buf.write("\3\2\2\2\u0161\u0162\3\2\2\2\u0162E\3\2\2\2\u0163\u0161")
        buf.write("\3\2\2\2\u0164\u0165\7+\2\2\u0165\u0166\5\64\33\2\u0166")
        buf.write("\u0167\7,\2\2\u0167\u016a\3\2\2\2\u0168\u016a\5H%\2\u0169")
        buf.write("\u0164\3\2\2\2\u0169\u0168\3\2\2\2\u016aG\3\2\2\2\u016b")
        buf.write("\u016f\5J&\2\u016c\u016f\5N(\2\u016d\u016f\7\66\2\2\u016e")
        buf.write("\u016b\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016d\3\2\2\2")
        buf.write("\u016fI\3\2\2\2\u0170\u0176\7\3\2\2\u0171\u0176\7\4\2")
        buf.write("\2\u0172\u0176\7\5\2\2\u0173\u0176\7\6\2\2\u0174\u0176")
        buf.write("\5L\'\2\u0175\u0170\3\2\2\2\u0175\u0171\3\2\2\2\u0175")
        buf.write("\u0172\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0174\3\2\2\2")
        buf.write("\u0176K\3\2\2\2\u0177\u0178\7/\2\2\u0178\u0179\5\62\32")
        buf.write("\2\u0179\u017a\7\60\2\2\u017aM\3\2\2\2\u017b\u017c\7\66")
        buf.write("\2\2\u017c\u017e\7+\2\2\u017d\u017f\5\62\32\2\u017e\u017d")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0181\7,\2\2\u0181O\3\2\2\2!SYasz~\u0081\u008c\u0096")
        buf.write("\u00a4\u00ad\u00b2\u00c2\u00d0\u00f4\u00fb\u0103\u0105")
        buf.write("\u010f\u0119\u0123\u012e\u0139\u0144\u014a\u0153\u0161")
        buf.write("\u0169\u016e\u0175\u017e")
=======
        buf.write("\u00ff\7\65\2\2\u00ff/\3\2\2\2\u0100\u0104\7/\2\2\u0101")
        buf.write("\u0103\5\34\17\2\u0102\u0101\3\2\2\2\u0103\u0106\3\2\2")
        buf.write("\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0107")
        buf.write("\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108\7\60\2\2\u0108")
        buf.write("\61\3\2\2\2\u0109\u010e\5\64\33\2\u010a\u010b\7\63\2\2")
        buf.write("\u010b\u010d\5\64\33\2\u010c\u010a\3\2\2\2\u010d\u0110")
        buf.write("\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("\63\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0112\5\66\34\2")
        buf.write("\u0112\65\3\2\2\2\u0113\u0114\58\35\2\u0114\u0115\7*\2")
        buf.write("\2\u0115\u0116\58\35\2\u0116\u0119\3\2\2\2\u0117\u0119")
        buf.write("\58\35\2\u0118\u0113\3\2\2\2\u0118\u0117\3\2\2\2\u0119")
        buf.write("\67\3\2\2\2\u011a\u011b\b\35\1\2\u011b\u011c\5:\36\2\u011c")
        buf.write("\u0122\3\2\2\2\u011d\u011e\f\4\2\2\u011e\u011f\t\3\2\2")
        buf.write("\u011f\u0121\58\35\5\u0120\u011d\3\2\2\2\u0121\u0124\3")
        buf.write("\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u01239")
        buf.write("\3\2\2\2\u0124\u0122\3\2\2\2\u0125\u0126\b\36\1\2\u0126")
        buf.write("\u0127\5<\37\2\u0127\u012d\3\2\2\2\u0128\u0129\f\4\2\2")
        buf.write("\u0129\u012a\t\4\2\2\u012a\u012c\5<\37\2\u012b\u0128\3")
        buf.write("\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e")
        buf.write("\3\2\2\2\u012e;\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0131")
        buf.write("\b\37\1\2\u0131\u0132\5> \2\u0132\u0138\3\2\2\2\u0133")
        buf.write("\u0134\f\4\2\2\u0134\u0135\t\5\2\2\u0135\u0137\5> \2\u0136")
        buf.write("\u0133\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2")
        buf.write("\u0138\u0139\3\2\2\2\u0139=\3\2\2\2\u013a\u0138\3\2\2")
        buf.write("\2\u013b\u013c\b \1\2\u013c\u013d\5@!\2\u013d\u0143\3")
        buf.write("\2\2\2\u013e\u013f\f\4\2\2\u013f\u0140\t\6\2\2\u0140\u0142")
        buf.write("\5@!\2\u0141\u013e\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141")
        buf.write("\3\2\2\2\u0143\u0144\3\2\2\2\u0144?\3\2\2\2\u0145\u0143")
        buf.write("\3\2\2\2\u0146\u0147\7!\2\2\u0147\u014a\5@!\2\u0148\u014a")
        buf.write("\5B\"\2\u0149\u0146\3\2\2\2\u0149\u0148\3\2\2\2\u014a")
        buf.write("A\3\2\2\2\u014b\u014c\7\35\2\2\u014c\u014f\5B\"\2\u014d")
        buf.write("\u014f\5D#\2\u014e\u014b\3\2\2\2\u014e\u014d\3\2\2\2\u014f")
        buf.write("C\3\2\2\2\u0150\u0151\7\66\2\2\u0151\u0152\7-\2\2\u0152")
        buf.write("\u0153\5\62\32\2\u0153\u0154\7.\2\2\u0154\u0157\3\2\2")
        buf.write("\2\u0155\u0157\5F$\2\u0156\u0150\3\2\2\2\u0156\u0155\3")
        buf.write("\2\2\2\u0157E\3\2\2\2\u0158\u0159\7+\2\2\u0159\u015a\5")
        buf.write("\64\33\2\u015a\u015b\7,\2\2\u015b\u015e\3\2\2\2\u015c")
        buf.write("\u015e\5H%\2\u015d\u0158\3\2\2\2\u015d\u015c\3\2\2\2\u015e")
        buf.write("G\3\2\2\2\u015f\u0163\5J&\2\u0160\u0163\5N(\2\u0161\u0163")
        buf.write("\7\66\2\2\u0162\u015f\3\2\2\2\u0162\u0160\3\2\2\2\u0162")
        buf.write("\u0161\3\2\2\2\u0163I\3\2\2\2\u0164\u016a\7\3\2\2\u0165")
        buf.write("\u016a\7\4\2\2\u0166\u016a\7\5\2\2\u0167\u016a\7\6\2\2")
        buf.write("\u0168\u016a\5L\'\2\u0169\u0164\3\2\2\2\u0169\u0165\3")
        buf.write("\2\2\2\u0169\u0166\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u0168")
        buf.write("\3\2\2\2\u016aK\3\2\2\2\u016b\u016c\7/\2\2\u016c\u016d")
        buf.write("\5\62\32\2\u016d\u016e\7\60\2\2\u016eM\3\2\2\2\u016f\u0170")
        buf.write("\7\66\2\2\u0170\u0172\7+\2\2\u0171\u0173\5\62\32\2\u0172")
        buf.write("\u0171\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174\u0175\7,\2\2\u0175O\3\2\2\2 SYasz~\u0081\u008c")
        buf.write("\u0095\u00a3\u00ac\u00b1\u00c2\u00d0\u00f4\u00fb\u0104")
        buf.write("\u010e\u0118\u0122\u012d\u0138\u0143\u0149\u014e\u0156")
        buf.write("\u015d\u0162\u0169\u0172")
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
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
    RULE_expression_list = 24
    RULE_expression = 25
    RULE_string_expression = 26
    RULE_relational_expression = 27
    RULE_logical_expression = 28
    RULE_adding_expression = 29
    RULE_multiplying_expression = 30
    RULE_unary_expression = 31
    RULE_indexing_expression = 32
    RULE_indexing_expression_continue = 33
    RULE_braced_expression = 34
    RULE_operand = 35
    RULE_literal = 36
    RULE_indexed_array_lit = 37
    RULE_function_call = 38

    ruleNames =  [ "program", "declaration", "variable_declaration", "short_variable_declaration", 
                   "long_variable_declaration", "parameter_declaration_list", 
                   "parameter_declaration", "identifier_list", "type_specifier", 
                   "array_type_specifier", "dimension_list", "function_declaration", 
                   "function_body", "statement", "assignment_statement", 
                   "if_statement", "for_statement", "while_statement", "do_while_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "call_statement", "block_statement", "expression_list", 
                   "expression", "string_expression", "relational_expression", 
                   "logical_expression", "adding_expression", "multiplying_expression", 
<<<<<<< HEAD
                   "unary_expression", "indexing_expression", "indexing_expression_continue", 
=======
                   "negate_expression", "sign_expression", "indexing_expression", 
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                   "braced_expression", "operand", "literal", "indexed_array_lit", 
                   "function_call" ]

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
            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                self.declaration()
                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MT22Parser.IDENTIFIER):
                    break

            self.state = 83
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
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
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
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.short_variable_declaration()
                self.state = 90
                self.match(MT22Parser.SEMI_COLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.long_variable_declaration()
                self.state = 93
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
            self.state = 97
            self.identifier_list()
            self.state = 98
            self.match(MT22Parser.COLON)
            self.state = 99
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

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


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
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(MT22Parser.IDENTIFIER)
                self.state = 102
                self.match(MT22Parser.COLON)
                self.state = 103
                self.type_specifier()
                self.state = 104
                self.match(MT22Parser.ASSIGN)
                self.state = 105
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(MT22Parser.IDENTIFIER)
                self.state = 108
                self.match(MT22Parser.COMMA)
                self.state = 109
                self.long_variable_declaration()
                self.state = 110
                self.match(MT22Parser.COMMA)
                self.state = 111
                self.expression()
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
            self.state = 115
            self.parameter_declaration()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 116
                self.match(MT22Parser.COMMA)
                self.state = 117
                self.parameter_declaration()
                self.state = 122
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
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 123
                self.match(MT22Parser.INHERIT)


            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 126
                self.match(MT22Parser.OUT)


            self.state = 129
            self.match(MT22Parser.IDENTIFIER)
            self.state = 130
            self.match(MT22Parser.COLON)
            self.state = 131
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
            self.state = 133
            self.match(MT22Parser.IDENTIFIER)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 134
                self.match(MT22Parser.COMMA)
                self.state = 135
                self.match(MT22Parser.IDENTIFIER)
                self.state = 140
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
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.array_type_specifier()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(MT22Parser.AUTO)
                pass
            elif token in [MT22Parser.INTEGER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.match(MT22Parser.INTEGER)
                pass
            elif token in [MT22Parser.FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.match(MT22Parser.FLOAT)
                pass
            elif token in [MT22Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.match(MT22Parser.BOOLEAN)
                pass
            elif token in [MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 6)
                self.state = 146
                self.match(MT22Parser.STRING)
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 147
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
            self.state = 150
            self.match(MT22Parser.ARRAY)
            self.state = 151
            self.match(MT22Parser.OPEN_BRACK)
            self.state = 152
            self.dimension_list()
            self.state = 153
            self.match(MT22Parser.CLOSE_BRACK)
            self.state = 154
            self.match(MT22Parser.OF)
            self.state = 155
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
            self.state = 157
            self.match(MT22Parser.INTEGER_LIT)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 158
                self.match(MT22Parser.COMMA)
                self.state = 159
                self.match(MT22Parser.INTEGER_LIT)
                self.state = 164
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
            self.state = 165
            self.match(MT22Parser.IDENTIFIER)
            self.state = 166
            self.match(MT22Parser.COLON)
            self.state = 167
            self.match(MT22Parser.FUNCTION)
            self.state = 168
            self.type_specifier()
            self.state = 169
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.OUT) | (1 << MT22Parser.INHERIT) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 170
                self.parameter_declaration_list()


            self.state = 173
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 174
                self.match(MT22Parser.INHERIT)
                self.state = 175
                self.match(MT22Parser.IDENTIFIER)


            self.state = 178
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
            self.state = 180
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
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.assignment_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.while_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 186
                self.do_while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 187
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 188
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 189
                self.return_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 190
                self.call_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 191
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
        self.enterRule(localctx, 28, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(MT22Parser.IDENTIFIER)
            self.state = 195
            self.match(MT22Parser.ASSIGN)
            self.state = 196
            self.expression()
            self.state = 197
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
        self.enterRule(localctx, 30, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(MT22Parser.IF)
            self.state = 200
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 201
            self.expression()
            self.state = 202
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 203
            self.statement()
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 204
                self.match(MT22Parser.ELSE)
                self.state = 205
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
        self.enterRule(localctx, 32, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(MT22Parser.FOR)
            self.state = 209
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 210
            self.match(MT22Parser.IDENTIFIER)
            self.state = 211
            self.match(MT22Parser.ASSIGN)
            self.state = 212
            self.expression()
            self.state = 213
            self.match(MT22Parser.COMMA)
            self.state = 214
            self.expression()
            self.state = 215
            self.match(MT22Parser.COMMA)
            self.state = 216
            self.expression()
            self.state = 217
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 218
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
        self.enterRule(localctx, 34, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MT22Parser.WHILE)
            self.state = 221
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 222
            self.expression()
            self.state = 223
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 224
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

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


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
            self.state = 226
            self.match(MT22Parser.DO)
            self.state = 227
            self.block_statement()
            self.state = 228
            self.match(MT22Parser.WHILE)
            self.state = 229
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 230
            self.expression()
            self.state = 231
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 232
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
            self.state = 234
            self.match(MT22Parser.BREAK)
            self.state = 235
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
            self.state = 237
            self.match(MT22Parser.CONTINUE)
            self.state = 238
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

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


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
            self.state = 240
            self.match(MT22Parser.RETURN)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER_LIT) | (1 << MT22Parser.FLOAT_LIT) | (1 << MT22Parser.BOOLEAN_LIT) | (1 << MT22Parser.STRING_LIT) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.NOT) | (1 << MT22Parser.OPEN_PAREN) | (1 << MT22Parser.OPEN_BRACE) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 241
                self.expression()


            self.state = 244
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
        self.enterRule(localctx, 44, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(MT22Parser.IDENTIFIER)
            self.state = 247
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER_LIT) | (1 << MT22Parser.FLOAT_LIT) | (1 << MT22Parser.BOOLEAN_LIT) | (1 << MT22Parser.STRING_LIT) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.NOT) | (1 << MT22Parser.OPEN_PAREN) | (1 << MT22Parser.OPEN_BRACE) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 248
                self.expression_list()


            self.state = 251
            self.match(MT22Parser.CLOSE_PAREN)
            self.state = 252
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
            self.state = 254
            self.match(MT22Parser.OPEN_BRACE)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.OPEN_BRACE) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 257
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 255
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 256
                    self.variable_declaration()
                    pass


                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 262
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
        self.enterRule(localctx, 48, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.expression()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 265
                self.match(MT22Parser.COMMA)
                self.state = 266
                self.expression()
                self.state = 271
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
        self.enterRule(localctx, 50, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 272
=======
            self.state = 271
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
            self.string_expression()
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

        def relational_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Relational_expressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Relational_expressionContext,i)


        def DOUBLE_COLON(self):
            return self.getToken(MT22Parser.DOUBLE_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_string_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expression" ):
                return visitor.visitString_expression(self)
            else:
                return visitor.visitChildren(self)




    def string_expression(self):

        localctx = MT22Parser.String_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_string_expression)
        try:
<<<<<<< HEAD
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.relational_expression(0)
                self.state = 275
                self.match(MT22Parser.DOUBLE_COLON)
                self.state = 276
=======
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.relational_expression(0)
                self.state = 274
                self.match(MT22Parser.DOUBLE_COLON)
                self.state = 275
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self.relational_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
<<<<<<< HEAD
                self.state = 278
=======
                self.state = 277
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self.relational_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expression(self):
            return self.getTypedRuleContext(MT22Parser.Logical_expressionContext,0)


        def relational_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Relational_expressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Relational_expressionContext,i)


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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_relational_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 282
            self.logical_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 289
=======
            self.state = 281
            self.logical_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 288
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Relational_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expression)
<<<<<<< HEAD
                    self.state = 284
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 285
=======
                    self.state = 283
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 284
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOT_EQUAL) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LESS_EQUAL) | (1 << MT22Parser.GREATER) | (1 << MT22Parser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
<<<<<<< HEAD
                    self.state = 286
                    self.relational_expression(3) 
                self.state = 291
=======
                    self.state = 285
                    self.relational_expression(3) 
                self.state = 290
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_logical_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 293
            self.adding_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 300
=======
            self.state = 292
            self.adding_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 299
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
<<<<<<< HEAD
                    self.state = 295
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 296
=======
                    self.state = 294
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 295
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND_AND or _la==MT22Parser.OR_OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
<<<<<<< HEAD
                    self.state = 297
                    self.adding_expression(0) 
                self.state = 302
=======
                    self.state = 296
                    self.adding_expression(0) 
                self.state = 301
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_adding_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 304
            self.multiplying_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
=======
            self.state = 303
            self.multiplying_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 310
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Adding_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
<<<<<<< HEAD
                    self.state = 306
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 307
=======
                    self.state = 305
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 306
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
<<<<<<< HEAD
                    self.state = 308
                    self.multiplying_expression(0) 
                self.state = 313
=======
                    self.state = 307
                    self.multiplying_expression(0) 
                self.state = 312
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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

        def unary_expression(self):
            return self.getTypedRuleContext(MT22Parser.Unary_expressionContext,0)


        def multiplying_expression(self):
            return self.getTypedRuleContext(MT22Parser.Multiplying_expressionContext,0)


        def STAR(self):
            return self.getToken(MT22Parser.STAR, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_multiplying_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 315
            self.unary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 322
=======
            self.state = 314
            self.negate_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 321
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
<<<<<<< HEAD
                    self.state = 317
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 318
=======
                    self.state = 316
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 317
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STAR) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
<<<<<<< HEAD
                    self.state = 319
                    self.unary_expression() 
                self.state = 324
=======
                    self.state = 318
                    self.negate_expression() 
                self.state = 323
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Unary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expression(self):
            return self.getTypedRuleContext(MT22Parser.Unary_expressionContext,0)


        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def indexing_expression(self):
            return self.getTypedRuleContext(MT22Parser.Indexing_expressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_unary_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expression" ):
                return visitor.visitUnary_expression(self)
            else:
                return visitor.visitChildren(self)




    def unary_expression(self):

        localctx = MT22Parser.Unary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_unary_expression)
        self._la = 0 # Token type
        try:
<<<<<<< HEAD
            self.state = 328
=======
            self.state = 327
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUS, MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
                self.state = 325
                _la = self._input.LA(1)
                if not(_la==MT22Parser.MINUS or _la==MT22Parser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 326
                self.unary_expression()
=======
                self.state = 324
                self.match(MT22Parser.NOT)
                self.state = 325
                self.negate_expression()
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                pass
            elif token in [MT22Parser.INTEGER_LIT, MT22Parser.FLOAT_LIT, MT22Parser.BOOLEAN_LIT, MT22Parser.STRING_LIT, MT22Parser.OPEN_PAREN, MT22Parser.OPEN_BRACE, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
<<<<<<< HEAD
                self.state = 327
                self.indexing_expression()
=======
                self.state = 326
                self.sign_expression()
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
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


    class Indexing_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def indexing_expression_continue(self):
            return self.getTypedRuleContext(MT22Parser.Indexing_expression_continueContext,0)


        def OPEN_BRACK(self):
            return self.getToken(MT22Parser.OPEN_BRACK, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MT22Parser.Expression_listContext,0)


        def CLOSE_BRACK(self):
            return self.getToken(MT22Parser.CLOSE_BRACK, 0)

        def braced_expression(self):
            return self.getTypedRuleContext(MT22Parser.Braced_expressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_indexing_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexing_expression" ):
                return visitor.visitIndexing_expression(self)
            else:
                return visitor.visitChildren(self)




    def indexing_expression(self):

        localctx = MT22Parser.Indexing_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_indexing_expression)
        try:
<<<<<<< HEAD
            self.state = 337
=======
            self.state = 332
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
                self.state = 330
                self.match(MT22Parser.IDENTIFIER)
                self.state = 331
                self.indexing_expression_continue(0)
                self.state = 332
                self.match(MT22Parser.OPEN_BRACK)
                self.state = 333
                self.expression_list()
                self.state = 334
                self.match(MT22Parser.CLOSE_BRACK)
=======
                self.state = 329
                self.match(MT22Parser.MINUS)
                self.state = 330
                self.sign_expression()
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
<<<<<<< HEAD
                self.state = 336
                self.braced_expression()
=======
                self.state = 331
                self.indexing_expression()
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexing_expression_continueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACK(self):
            return self.getToken(MT22Parser.OPEN_BRACK, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MT22Parser.Expression_listContext,0)


        def CLOSE_BRACK(self):
            return self.getToken(MT22Parser.CLOSE_BRACK, 0)

        def indexing_expression_continue(self):
            return self.getTypedRuleContext(MT22Parser.Indexing_expression_continueContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_indexing_expression_continue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexing_expression_continue" ):
                return visitor.visitIndexing_expression_continue(self)
            else:
                return visitor.visitChildren(self)



    def indexing_expression_continue(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Indexing_expression_continueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_indexing_expression_continue, _p)
        try:
<<<<<<< HEAD
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(MT22Parser.OPEN_BRACK)
            self.state = 341
            self.expression_list()
            self.state = 342
            self.match(MT22Parser.CLOSE_BRACK)
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Indexing_expression_continueContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indexing_expression_continue)
                    self.state = 344
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 345
                    self.match(MT22Parser.OPEN_BRACK)
                    self.state = 346
                    self.expression_list()
                    self.state = 347
                    self.match(MT22Parser.CLOSE_BRACK) 
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
=======
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(MT22Parser.IDENTIFIER)
                self.state = 335
                self.match(MT22Parser.OPEN_BRACK)
                self.state = 336
                self.expression_list()
                self.state = 337
                self.match(MT22Parser.CLOSE_BRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.braced_expression()
                pass

>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Braced_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(MT22Parser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(MT22Parser.CLOSE_PAREN, 0)

        def operand(self):
            return self.getTypedRuleContext(MT22Parser.OperandContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_braced_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBraced_expression" ):
                return visitor.visitBraced_expression(self)
            else:
                return visitor.visitChildren(self)




    def braced_expression(self):

        localctx = MT22Parser.Braced_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_braced_expression)
        try:
<<<<<<< HEAD
            self.state = 359
=======
            self.state = 347
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OPEN_PAREN]:
                self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
                self.state = 354
                self.match(MT22Parser.OPEN_PAREN)
                self.state = 355
                self.expression()
                self.state = 356
=======
                self.state = 342
                self.match(MT22Parser.OPEN_PAREN)
                self.state = 343
                self.expression()
                self.state = 344
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self.match(MT22Parser.CLOSE_PAREN)
                pass
            elif token in [MT22Parser.INTEGER_LIT, MT22Parser.FLOAT_LIT, MT22Parser.BOOLEAN_LIT, MT22Parser.STRING_LIT, MT22Parser.OPEN_BRACE, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
<<<<<<< HEAD
                self.state = 358
=======
                self.state = 346
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
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
        self.enterRule(localctx, 70, self.RULE_operand)
        try:
<<<<<<< HEAD
            self.state = 364
=======
            self.state = 352
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
                self.state = 361
=======
                self.state = 349
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
<<<<<<< HEAD
                self.state = 362
=======
                self.state = 350
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self.function_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
<<<<<<< HEAD
                self.state = 363
=======
                self.state = 351
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
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
        self.enterRule(localctx, 72, self.RULE_literal)
        try:
<<<<<<< HEAD
            self.state = 371
=======
            self.state = 359
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
                self.state = 366
=======
                self.state = 354
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self.match(MT22Parser.INTEGER_LIT)
                pass
            elif token in [MT22Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
<<<<<<< HEAD
                self.state = 367
=======
                self.state = 355
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self.match(MT22Parser.FLOAT_LIT)
                pass
            elif token in [MT22Parser.BOOLEAN_LIT]:
                self.enterOuterAlt(localctx, 3)
<<<<<<< HEAD
                self.state = 368
=======
                self.state = 356
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self.match(MT22Parser.BOOLEAN_LIT)
                pass
            elif token in [MT22Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
<<<<<<< HEAD
                self.state = 369
=======
                self.state = 357
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                self.match(MT22Parser.STRING_LIT)
                pass
            elif token in [MT22Parser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 5)
<<<<<<< HEAD
                self.state = 370
=======
                self.state = 358
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
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

        def expression_list(self):
            return self.getTypedRuleContext(MT22Parser.Expression_listContext,0)


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
        self.enterRule(localctx, 74, self.RULE_indexed_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 373
            self.match(MT22Parser.OPEN_BRACE)
            self.state = 374
            self.expression_list()
            self.state = 375
=======
            self.state = 361
            self.match(MT22Parser.OPEN_BRACE)
            self.state = 362
            self.expression_list()
            self.state = 363
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
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

        def expression_list(self):
            return self.getTypedRuleContext(MT22Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = MT22Parser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 377
            self.match(MT22Parser.IDENTIFIER)
            self.state = 378
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER_LIT) | (1 << MT22Parser.FLOAT_LIT) | (1 << MT22Parser.BOOLEAN_LIT) | (1 << MT22Parser.STRING_LIT) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.NOT) | (1 << MT22Parser.OPEN_PAREN) | (1 << MT22Parser.OPEN_BRACE) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 379
                self.expression_list()


            self.state = 382
=======
            self.state = 365
            self.match(MT22Parser.IDENTIFIER)
            self.state = 366
            self.match(MT22Parser.OPEN_PAREN)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER_LIT) | (1 << MT22Parser.FLOAT_LIT) | (1 << MT22Parser.BOOLEAN_LIT) | (1 << MT22Parser.STRING_LIT) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.NOT) | (1 << MT22Parser.OPEN_PAREN) | (1 << MT22Parser.OPEN_BRACE) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 367
                self.expression_list()


            self.state = 370
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
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
        self._predicates[27] = self.relational_expression_sempred
        self._predicates[28] = self.logical_expression_sempred
        self._predicates[29] = self.adding_expression_sempred
        self._predicates[30] = self.multiplying_expression_sempred
        self._predicates[33] = self.indexing_expression_continue_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def relational_expression_sempred(self, localctx:Relational_expressionContext, predIndex:int):
            if predIndex == 0:
<<<<<<< HEAD
                return self.precpred(self._ctx, 2)
         

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def adding_expression_sempred(self, localctx:Adding_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expression_sempred(self, localctx:Multiplying_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def indexing_expression_continue_sempred(self, localctx:Indexing_expression_continueContext, predIndex:int):
            if predIndex == 4:
=======
                return self.precpred(self._ctx, 2)
         

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def adding_expression_sempred(self, localctx:Adding_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expression_sempred(self, localctx:Multiplying_expressionContext, predIndex:int):
            if predIndex == 3:
>>>>>>> 9fd6921 (fix: string concat and relational statement assoc)
                return self.precpred(self._ctx, 2)
         





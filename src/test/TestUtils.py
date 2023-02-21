import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
import pathlib

if not './main/mt22/parser/' in sys.path:
    sys.path.append('./main/mt22/parser/')
if os.path.isdir('../target/main/mt22/parser') and not '../target/main/mt22/parser/' in sys.path:
    sys.path.append('../target/main/mt22/parser/')
from MT22Lexer import MT22Lexer
from MT22Parser import MT22Parser
from lexererr import *
import subprocess
from antlr4.tree.Trees import *

JASMIN_JAR = "./external/jasmin.jar"
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"
RES_DIR = "./test/results/"
DIFF_DIR = "./test/differences/"
Lexer = MT22Lexer
Parser = MT22Parser


class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


def generate_difference_file(testcase_name, input, result, expect):
    diff_filename = DIFF_DIR + str(testcase_name) + ".txt"
    pathlib.Path(diff_filename).touch(exist_ok=True)
    diff = open(diff_filename, "w+")
    diff.write('================================================================================================================================================================================================================================\n')
    diff.write('============== WRONG TESTCASE: ' + testcase_name + ' ==========================================================================================================================================================\n')
    diff.write('================================================================================================================================================================================================================================\n\n\n')
    diff.write("------------------------------------------------\n")
    diff.write("|            Testcase's content                |\n")
    diff.write("------------------------------------------------\n")
    diff.write(input)
    diff.write("\n")
    diff.write("------------------------------------------------\n")
    diff.write("|              Expected output                 |\n")
    diff.write("------------------------------------------------\n")
    diff.write(expect)
    diff.write("\n")
    diff.write("------------------------------------------------\n")
    diff.write("|                Your output                   |\n")
    diff.write("------------------------------------------------\n")
    diff.write(result)
    diff.close()

class TestLexer:
    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        TestLexer.check(SOL_DIR, inputfile, num)
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        if line != expect:
            generate_difference_file(num, input, line, expect)
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        lexer = Lexer(inputfile)
        try:
            TestLexer.printLexeme(dest, lexer)
        except (ErrorToken, UncloseString, IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close()

    @staticmethod
    def printLexeme(dest, lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text + ",")
            TestLexer.printLexeme(dest, lexer)
        else:
            dest.write("<EOF>")


class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)


NewErrorListener.INSTANCE = NewErrorListener()


class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg


def clips_pprint(clips_str: str) -> str:
    LB = "("
    RB = ")"
    TAB = " " * 4
    formatted_clips_str = ""
    tab_count = 0
    for c in clips_str:
        if c == LB:
            formatted_clips_str += os.linesep
            for _i in range(tab_count):
                formatted_clips_str += TAB

            tab_count += 1
        elif c == RB:
            tab_count -= 1
        formatted_clips_str += c

    return formatted_clips_str.strip()


class TestParser:
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        TestParser.check(SOL_DIR, inputfile, num)
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        if line != expect:
            generate_difference_file(num, input, line, expect)
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        lexer = Lexer(inputfile)
        listener = TestParser.createErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        tree_content = Trees.toStringTree(parser.program(), None, parser)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.write('\n\n')
            dest.write(clips_pprint(tree_content))
            dest.close()


class TestAST:
    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        TestAST.check(SOL_DIR, inputfile, num)
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        lexer = Lexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()


class TestChecker:
    @staticmethod
    def test(input, expect, num):
        if type(input) is str:
            inputfile = TestUtil.makeSource(input, num)
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = Parser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input), num)
            asttree = input
        TestChecker.check(SOL_DIR, asttree, num)
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, asttree, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            dest.write(str(list(res)))
        except StaticError as e:
            dest.write(str(e))
        finally:
            dest.close()


class TestCodeGen():
    @staticmethod
    def test(input, expect, num):
        if type(input) is str:
            inputfile = TestUtil.makeSource(input, num)
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = Parser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input), num)
            asttree = input

        TestCodeGen.check(SOL_DIR, asttree, num)

        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, asttree, num):
        codeGen = CodeGenerator()
        path = os.path.join(soldir, str(num))
        if not os.path.isdir(path):
            os.mkdir(path)
        f = open(os.path.join(soldir, str(num) + ".txt"), "w")
        try:
            codeGen.gen(asttree, path)

            subprocess.call("java  -jar " + JASMIN_JAR + " " + path +
                            "/MT22Class.j", shell=True, stderr=subprocess.STDOUT)

            subprocess.run("java -cp ./lib:. MT22Class",
                           shell=True, stdout=f, timeout=10)
        except StaticError as e:
            f.write(str(e))
        except subprocess.TimeoutExpired:
            f.write("Time out\n")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(
                e.cmd, e.returncode, e.output))
        finally:
            f.close()

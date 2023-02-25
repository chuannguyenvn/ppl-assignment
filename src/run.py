import sys
import os
import subprocess
import unittest
import re
import pathlib
from antlr4 import *

for path in ['./test/', './main/mt22/parser/']:
    sys.path.append(path)
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET_DIR = '../target'
GENERATE_DIR = 'main/mt22/parser'

lexer_suite_class_template = """
import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
"""

lexer_suite_test_method_template = """
    def test{0}(self):
        self.assertTrue(TestLexer.test(\'\'\'{1}\'\'\', \'\'\'{2}\'\'\', {3}))

"""

parser_suite_class_template = """
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
"""

parser_suite_test_method_template = """
    def test{0}(self):
        input = \'\'\'{1}\'\'\'
        expect = \'\'\'{2}\'\'\'
        self.assertTrue(TestParser.test(input, expect, {3}))
"""

pathlib.Path('test/LexerTests.txt').touch(exist_ok=True)
pathlib.Path('test/ParserTests.txt').touch(exist_ok=True)
lexer_tests_file = open("test/LexerTests.txt", 'r', encoding='utf-8-sig')
parser_tests_file = open("test/ParserTests.txt", 'r', encoding='utf-8-sig')
lexer_suite_file = open("test/LexerSuite.py", 'w')
parser_suite_file = open("test/ParserSuite.py", 'w')

file_id = 0
file_id_prefix = ''
parsing_test_name = True
parsing_testcase = False
parsing_solution = False

testcase_file = None
solution_file = None

required_dirs = ["./test/testcases/", "./test/outputs/", "./test/solutions/", "./test/differences/"]

for dir in required_dirs:
    if not os.path.exists(dir):
        os.makedirs(dir)


def end_parsing_test_name():
    global parsing_test_name
    global parsing_testcase
    global parsing_solution
    parsing_test_name = False
    parsing_testcase = True
    parsing_solution = False


def end_parsing_testcase():
    global parsing_test_name
    global parsing_testcase
    global parsing_solution
    parsing_test_name = False
    parsing_testcase = False
    parsing_solution = True


def end_parsing_solution():
    global parsing_test_name
    global parsing_testcase
    global parsing_solution
    parsing_test_name = True
    parsing_testcase = False
    parsing_solution = False


def build_filename(filename):
    return '[' + file_id_prefix + str(file_id) + '] ' + filename + '.txt'


def generate_tests_from_file(test_file, file_to_write, starting_template, testcase_template):
    global file_id
    global testcase_file
    global solution_file

    content = starting_template
    formatted_string_elements = ['', '', '', '']
    for line in test_file:
        reached_sep = line.__contains__('```')
        if parsing_test_name:
            if reached_sep:
                filename = re.search('^\s*```\s*(.*)\n?$', line).group(1)
                # testcase_file = open('testcases/' + build_filename(filename), 'w')
                # solution_file = open('solutions/' + build_filename(filename), 'w')
                file_id += 1
                formatted_filename = re.sub("[^\w\d]", '_', build_filename(filename)[:-3])
                formatted_string_elements[0] = formatted_filename
                formatted_string_elements[3] = '"' + formatted_filename + '"'
                end_parsing_test_name()
            continue

        if parsing_testcase:
            if reached_sep:
                end_parsing_testcase()
            else:
                # testcase_file.write(line)
                formatted_string_elements[1] += line
            continue

        if parsing_solution:
            if reached_sep:
                end_parsing_solution()
                content += testcase_template.format(formatted_string_elements[0],
                                                    formatted_string_elements[1][:-1],
                                                    formatted_string_elements[2][:-1],
                                                    formatted_string_elements[3])
                formatted_string_elements = ['', '', '', '']
            else:
                # solution_file.write(line)
                formatted_string_elements[2] += line
            continue
    file_to_write.write(content)


def generate_lexer_tests():
    global file_id
    global file_id_prefix
    file_id = 0
    file_id_prefix = 'L'
    generate_tests_from_file(lexer_tests_file, lexer_suite_file, lexer_suite_class_template, lexer_suite_test_method_template)


def generate_parser_tests():
    global file_id
    global file_id_prefix
    file_id = 0
    file_id_prefix = 'P'
    generate_tests_from_file(parser_tests_file, parser_suite_file, parser_suite_class_template, parser_suite_test_method_template)


def generate_tests():
    generate_lexer_tests()
    generate_parser_tests()
    lexer_suite_file.close()
    parser_suite_file.close()


def main(argv):
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        subprocess.run(["java", "-jar", ANTLR_JAR, "-o", "../target",
                        "-no-listener", "-visitor", "main/mt22/parser/MT22.g4"])
    elif argv[0] == 'clean':
        subprocess.run(["rm", "-rf", TARGET_DIR + "/*"])

    elif argv[0] == 'test':
        if not os.path.isdir(TARGET_DIR + "/" + GENERATE_DIR):
            subprocess.run(["java", "-jar", ANTLR_JAR, "-o", GENERATE_DIR,
                            "-no-listener", "-visitor", "main/mt22/parser/MT22.g4"])
        if not (TARGET_DIR + "/" + GENERATE_DIR) in sys.path:
            sys.path.append(TARGET_DIR + "/" + GENERATE_DIR)
        if len(argv) == 3 and argv[2] == 'spicy':
            generate_tests()
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'LexerSuite':
            from LexerSuite import LexerSuite
            getAndTest(LexerSuite)
        elif argv[1] == 'ParserSuite':
            from ParserSuite import ParserSuite
            getAndTest(ParserSuite)
        else:
            printUsage()
    else:
        printUsage()


def getAndTest(cls):
    suite = unittest.makeSuite(cls)
    test(suite)


def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())


def printUsage():
    print("python3 run.py gen")
    print("python3 run.py test LexerSuite")
    print("python3 run.py test ParserSuite")


if __name__ == "__main__":
    main(sys.argv[1:])

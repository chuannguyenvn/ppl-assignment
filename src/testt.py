import sys
import os
import subprocess
import unittest
import run

for path in ['./test/', './main/mt22/parser/']:
    sys.path.append(path)
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET_DIR = '../target'
GENERATE_DIR = 'main/mt22/parser'

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
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'LexerSuite':
            from src.testt import LexerSuite
            run.getAndTest(LexerSuite)
        elif argv[1] == 'ParserSuite':
            from src.testt import ParserSuite
            run.getAndTest(ParserSuite)
        else:
            printUsage()
    else:
        printUsage()
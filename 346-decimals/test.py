#!/usr/bin/env python3

import re # match()
import os # listdir()
import sys # stderr
from pathlib import Path
from tempfile import NamedTemporaryFile
import subprocess # run shell command

from src import processFromStr as FUNCTION_UNDER_TEST

TESTS_PATH = './examples/'
TESTS_ABS_PATH = Path(TESTS_PATH).resolve()

def printDiff(output, expecting):
    fileA = NamedTemporaryFile(buffering=0)
    fileA.write(bytes(output, 'utf-8'))

    fileB = NamedTemporaryFile(buffering=0)
    fileB.write(bytes(expecting, 'utf-8'))

    subprocess.run(f"diff {fileA.name} {fileB.name} --color=always", shell=True)

def test():
    test_files = os.listdir(TESTS_PATH)

    if not test_files:
        return

    tests = []
    for fname in test_files:
        m = re.match(r'(.*)\.in\.txt', fname)
        if m:
            tests.append(m.group(1))

    if not tests:
        return
        
    for t in tests:
        input = open(f"{TESTS_PATH}/{t}.in.txt", encoding='utf8').read()
        expecting = open(f"{TESTS_PATH}/{t}.out.txt", encoding='utf8').read()
        output = FUNCTION_UNDER_TEST(input)

        if str(output) != expecting:
            print(f"Test '{t}' is failing :", file=sys.stderr)
            printDiff(output, expecting)
            exit(1)

test()

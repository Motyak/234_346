#!/usr/bin/env python3

import sys # read STDIN
import re # regex
import io # redirect print to a var

# depth=3 means we stop at 10^(-3)
DEFAULT_MAX_RECURSION_DEPTH = 3

debug=False

def fn(a, b, maxRecursionDepth = DEFAULT_MAX_RECURSION_DEPTH, _recursionDepth = 0):
    sum_ = sum(a)
    if debug:
        print("\n", "DEBUG", "sum_=", sum_)
        
    remainder = b % sum_
    if debug:
        print("DEBUG", "remainder=", remainder)
        
    if remainder != 0 and _recursionDepth < maxRecursionDepth:
        return fn(a, b * 10, maxRecursionDepth, _recursionDepth + 1)
        
    quotient = b // sum_
    if debug:
        print("DEBUG", "quotient=", quotient)
        
    adjustedQuotient = quotient / 10 ** maxRecursionDepth
    if debug:
        print("DEBUG", "adjustedQuotient=", adjustedQuotient)

    return [a[0] * adjustedQuotient, a[1] * adjustedQuotient, a[2] * adjustedQuotient]

def process(a, b):
    out = io.StringIO()
    for precision in range(0, 9 +1):
        print(precision, " -- ", *[f"{i:.{precision}f}" for i in fn(a, b, precision)], file=out)
    return out.getvalue()[:-1] # get rid of the last '\n' added by print


#######################################################################################
### DO NOT MODIFY BOTTOM PART
#######################################################################################

def parseArgs(str):
    # [<a1>,<a2>,<a3>] <b>
    regex = r"^\[(?P<a1>\d+),(?P<a2>\d+),(?P<a3>\d+)\]\s(?P<b>\d+)$"
    match = re.search(regex, str)

    class args: pass
    args.a = [int(match.group(f"a{i}")) for i in {1, 2, 3}]
    args.b = int(match.group("b"))
    return args

# this is the function under test
def processFromStr(str):
    args = parseArgs(str)
    return process(
        args.a,
        args.b
    )

if __name__ == "__main__":
    userInput = sys.stdin.read()
    res = processFromStr(userInput)
    print(res, end='')

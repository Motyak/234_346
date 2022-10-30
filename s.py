#!/usr/bin/env python3
from itertools import islice
from math import gcd
import sys # argv

def rangeBetween(begin, end):
    assert begin <= end
    res = list()
    if begin == end:
        return res
    for i in range(begin + 1, end):
        res.append(i)
    return res

def generateTriplets():
    a = 1 # will start with 2 on first iteration
    b : int
    c : int
    while True:
        a += 1
        c = 2 * a
        for b in rangeBetween(a, c):
            yield (a,  b, c)

def simplifyFraction(num, denom):
    assert denom != 0, "denominator cannot be zero"
    divisor = gcd(num, denom)
    return (num // divisor, denom // divisor)

def calculateIncreases(triplet: tuple):
    a, b, c = triplet
    aToBIncrease = simplifyFraction(b - a, a)
    str_aToBIncrease = f'{aToBIncrease[0]}/{aToBIncrease[1]}'
    bToCIncrease = simplifyFraction(c - b, b)
    str_bToCIncrease = f'{bToCIncrease[0]}/{bToCIncrease[1]}'

    return (str_aToBIncrease, str_bToCIncrease)

def generateTripletsToIncreases():
    for triplet in generateTriplets():
        yield (triplet, calculateIncreases(triplet))


HOW_MANY_DO_I_GENERATE = int(sys.argv[1])
tripletsToIncreases = list(islice(generateTripletsToIncreases(), HOW_MANY_DO_I_GENERATE))
for triplet, increases in tripletsToIncreases:
    print(triplet, *increases)

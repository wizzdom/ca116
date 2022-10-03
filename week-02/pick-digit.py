#!/usr/bin/env python3

n = int(input())
p = int(input())
length = len(str(n))

digit = n % (10 ** (p + 1))
digit = digit // (10 ** p)
#digit = digit % (10 ** (p - length))

print(digit)

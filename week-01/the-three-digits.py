#!/usr/bin/env python3

n = int(input())

units = n % 10
tens = ((n % 100) - units) // 10
hundreds = ((n % 1000) - tens - units) // 100

print(hundreds)
print(tens)
print(units)

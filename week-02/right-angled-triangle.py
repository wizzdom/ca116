#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

testa = (b * b + c * c) == a * a
testb = (a * a + c * c) == b * b
testc = (a * a + b * b) == c * c

print(testa or testb or testc)

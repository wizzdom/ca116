#!/usr/bin/env python3

n = int(input())
a = 0
b = 1

while a < n:
    print(a)
    c = b
    b = a + b
    a = c

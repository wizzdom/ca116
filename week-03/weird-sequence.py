#!/usr/bin/env python3

x = 0
n = int(input())
i = 0

print(x)
while i < (n - 1):
    x = -x + 2 * (x % 2) - 1
    print(x)
    i = i + 1

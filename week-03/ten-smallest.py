#!/usr/bin/env python3

i = 0
smallest = int(input())

while i < (10 - 1):
    n = int(input())
    if n < smallest:
        smallest = n
    i = i + 1

print(smallest)

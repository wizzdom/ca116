#!/usr/bin/env python3

i = 0
largest = int(input())

while i < (10 - 1):
    n = int(input())
    if largest < n:
        largest = n
    i = i + 1

print(largest)

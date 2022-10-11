#!/usr/bin/env python3

i = 0
sum = 0

while i < 10:
    n = int(input())
    if n < 0:
        sum = sum + (-n % 10)
    else:
        sum = sum + (n % 10)
    i = i + 1
print(sum)

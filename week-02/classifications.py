#!/usr/bin/env python3

n = int(input())

print("first:", 70 <= n)
print("second:", 50 <= n and n <= 69)
print("third:", 40 <= n and n <= 49)
print("fail:", n < 40)

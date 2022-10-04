#!/usr/bin/env python3

x_1 = int(input())
y_1 = int(input())
r_1 = int(input())

x_2 = int(input())
y_2 = int(input())
r_2 = int(input())

dist = ((x_2 - x_1) * (x_2 - x_1) + (y_2 - y_1) * (y_2 - y_1)) ** 0.5

if dist < r_1 + r_2:
    print("yes")
else:
    print("no")

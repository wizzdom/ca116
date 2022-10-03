#!/usr/bin/env python3

month = int(input())
day_of_month = int(input())

day_of_year = (month - 1) * 30 + day_of_month
day_of_week = (day_of_year - 1) % 7 + 1

print(day_of_week)

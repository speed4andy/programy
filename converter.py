#!/usr/bin/env python

import sys

q1 = input("Co chces prevest? decimal/binar? popripade jine?: ")
q2 = int(input("Zadej cislo k prevodu: "))
q3 = input("Nabizim prevod z desitkove do osmickove a sestnactkove, napis patricne cislo k dane soustave: ")

print(q1)
if q1 == "decimal":
    print(q2)
    print("Zadane cislo z desitkove do dvojkove soustavy je: " + bin(q2))     
else:
    if q1 == "jine":
             
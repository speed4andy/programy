#!/usr/bin/env python

import sys

#q1 = input("Co chces prevest? decimal/binar? popripade jine?: ")
q3 = int(input("Nabizim prevod z desitkove(10) do osmickove(8) a sestnactkove(16), napis patricne cislo k dane soustave : "))
q2 = int(input("Zadej cislo k prevodu: "))

print(q3)

if q3 == 10:
    print(q2)
    print("Zadane cislo z desitkove do dvojkove soustavy je: " + bin(q2))
elif q3 == 8:
    print(q2)
    print("Zadane cislo z desitkove do osmickove soustavy je: " + oct(q2))
elif q3 == 16:
    print(q2)
    print("Zadane cislo z desitkove do sestnactkove soustavy je: " + hex(q2))
else:
    print("Toto je spatna volba")  
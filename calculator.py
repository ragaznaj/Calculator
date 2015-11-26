# -*- coding: utf-8 -*-


def sestevek (x, y):

    return x + y

def odstevanje (x, y):

    return  x - y

def mnozenje (x, y):

    return x * y

def deljenje (x, y):

    return x / y

st1 = int(raw_input("vpiši št 1 "))

choice = raw_input("izberi operacijo (+,-,*,/) ")

st2 = int(raw_input("vpisi st 2 " ))



if choice == "+":
    print(sestevek(st1, st2))

elif choice == "-":
    print(odstevanje(st1, st2))

elif choice == "*":
    print(mnozenje(st1, st2))

elif choice == "/":
    print(deljenje(st1, st2))
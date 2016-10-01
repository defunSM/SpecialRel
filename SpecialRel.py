#!/usr/bin/env python
import sys, os, math

c = 299792458

def main():
    print("SpecialRel.py has been loaded.")

def ctometer(a):
    return a * c

def metertoc(a):
    return float(a / c)

def gamma(v):
    return float((1 / math.sqrt((1 - (v**2)))))

def ctogamma(v):
    return float(gamma(metertoc(v)))

def xlorentz(speed, x, t):
    return float(gamma(speed) * (x + speed * t))

def tlorentz(speed, x, t):
    return float(gamma(speed) * (t + speed * x))

def vlorentz(v, w):
    return float((v - w) / (1 - (v * w)))

def timedialation(v, t):
    return float(gamma(v) * t)

def lengthcontraction(v, h):
    return float(h / (gamma(v)))

def spacetimeinterval(x, t):
    return float(math.sqrt((x**2) + (t**2)))

if __name__=="__main__":
    main()

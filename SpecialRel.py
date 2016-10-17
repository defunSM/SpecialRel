#!/usr/bin/env python
import sys, os, math

c = 299792458

def main():
    print("SpecialRel.py has been loaded.")

def ctometer(a):    # Converts the speed that is in terms of c to meters per second.
    return a * c

def metertoc(a):    # Converts the speeed that is in terms of meters per second into terms of c.
    return float(a / c)

def gamma(v):    # Calculates the gamma taking the speed in terms of c.
    return float((1 / math.sqrt((1 - (v**2)))))

def ctogamma(v):  # Calculates the value of gamma based on the speed in terms of meters per second.
    return float(gamma(metertoc(v)))

def xlorentz(speed, x, t):  # Calculates the lorentz transformation for space.
    return float(gamma(speed) * (x - speed * t))

def tlorentz(speed, x, t):  # Calculates the lorentz transformation for time.
    return float(gamma(speed) * (t - speed * x))

def vlorentz(v, w):  # Calculates the lorentz transformation for velocity.
    return float((v - w) / (1 - (v * w)))

def timedialation(v, t):  # Calculates the time dialation based on the velocity and time.
    return float(gamma(v) * t)

def lengthcontraction(v, h):   # Calculates the length contraction based on the velocity and time.
    return float(h / (gamma(v)))

def spacetimeinterval(x, t):   # Calculates the spacetime interval based on the space and time.
    return float(math.sqrt((t**2) -(x**2))))

def spacetimeinterval2(t1, t2, x1, x2):
    return float(math.sqrt((t2 - t1)**2 - (x2 - x1)**2))

def spaceinterval(x1, x2):
    return float(x2 - x1)

def timeinterval(t1, t2):
    return float(t2 - t1)

if __name__=="__main__":
    main()

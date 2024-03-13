"""
Double Derivative Finder
Helping my girlfriend do double derivative for AP Calc BC
03/13/24
author: Quang Huynh
"""

from sympy import *

def main():
    t = symbols("t")
    x = input("Provide x function: ")
    y = input("Provide y function: ")

    dy_dx = diff(y, t)
    dx_dt = diff(x, t)

    dy_dx = dy_dx / dx_dt

    d2y_dx2 = diff(dy_dx, t) / dx_dt

    print("d^2y/dx^2: " + str(d2y_dx2))

    simplified = simplify(d2y_dx2)
    print("Simplified: " + str(simplified))


if __name__ == '__main__':
    main()


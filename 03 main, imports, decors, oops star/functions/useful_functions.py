# import math
from math import sqrt as f

def solve_equation(a, b, c):
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b + f(d)) / (2 * a)
        x2 = (-b - f(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x, x
    else:
        x1 = complex(-b / (2 * a), f(-d) / (2 * a))
        x2 = complex(-b / (2 * a), -f(-d) / (2 * a))
        return x1, x2

if __name__ == "__main__":
    x, y = solve_equation(1, 1, 3)
    print x, y

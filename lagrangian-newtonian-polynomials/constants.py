from sympy import cos

A : float = 0.1
B : float = 0.6

STEPS_COUNT : int = 10

PRECISION  : int = 108

CHECK_POINTS : list[int] = [0.37]

def  FUNCTION(x):
    return x ** 3 - cos(2 * x)
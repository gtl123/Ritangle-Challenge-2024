import sympy as sym
from IPython.display import display, Math
from sympy.abc import *

polynomial1 = 2*x**3 + x**2 - x
polynomial2 = x**3 - x**4 - 4*x**2

display(Math(sym.latex(polynomial1)))

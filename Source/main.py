import sympy as sym
from IPython.display import display, Math
from sympy.abc import x

polynomial1 = 2*x**3 + x**2 - x
polynomial2 = x**3 - x**4 - 4*x**2

display(Math('(%s) + (%s) = %s' % (sym.latex(polynomial1), sym.latex(polynomial2), sym.latex(polynomial1+polynomial2))))

import  sympy

J , w = sympy.symbols('J,W')

J = 0.5*(w **2)

# print(J)

dj_dw = sympy.diff(J,w)
print (dj_dw)

dj_dw.subs([(w,2)])




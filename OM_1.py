def draw_table(xvals, v):

    from matplotlib.pyplot import figure
    figure(num=None, figsize=(16, 2), dpi=300, facecolor='w', edgecolor='k')
    columns = ('X0', 'B', 'r', 'k', 'fn. sk.')

    ax = plt.subplot2grid((2,1), (0,0), colspan=2, rowspan=2)
    ax.table(cellText=xvals,
        colLabels=columns, loc="upper center")
    ax.title.set_text('Rezultatų lentelė {}'.format(v))
    ax.axis("off")
    plt.show()

import numpy as np
import math
import matplotlib.pyplot as plt

# Funkciju skaiciavimo pagalbine funkcija
def f_sk():
    f_sk.counter += 1
# Turio pakelto kvadratu funkcija
def f(val):
    f_sk()
    a, b, c = val
    return -a * b * c
def g(val):
    f_sk()
    a, b, c = val
    return (2 * a * b + 2 * b * c + 2 * c * a - 1)
def hx(val):
    f_sk()
    x, y, z = val
    return -x
def hy(val):
    f_sk()
    x, y, z = val
    return -y
def hz(val):
    f_sk()
    x, y, z = val
    return -z
def grad_norm(val, r):
    return math.sqrt(diffx(val, r)**2 + diffy(val, r)**2 + diffz(val, r)**2)
def diffx(val, r):
    f_sk()
    x, y, z = val
    return -y*z + (2*(2*y+2*z)*(2*y*x+2*x*z+2*y*z-1))/r + min(2*x/r, 0)
def diffy(val, r):
    f_sk()
    x, y, z = val
    return -x*z + (2*(2*x+2*z)*(2*y*x+2*x*z+2*y*z-1))/r + min(2*y/r, 0)
def diffz(val, r):
    f_sk()
    x, y, z = val
    return -x*y + (2*(2*x+2*y)*(2*y*x+2*x*z+2*y*z-1))/r + min(2*z/r, 0)
def B(val, r):
    f_sk()
    x, y, z = val
    return f(val) + 1/r * ((max(hx(val), 0)**2 + max(hy(val), 0)**2 +max(hz(val), 0)**2 + g(val)**2))
def b(val, r):
    f_sk()
    return (max(hx(val), 0)**2+ max(hy(val), 0)**2 + max(hz(val), 0)**2 +g(val)**2)
def gradient_desc(val, r, gamma=1e-3, epsilon=1e-4):
    i = 0
    x, y, z = val
    while abs(grad_norm((x, y, z), r)) >= epsilon:
        x_ = x
        y_ = y
        z_ = z
        x -= diffx((x_, y_, z_), r) * gamma
        y -= diffy((x_, y_, z_), r) * gamma
        z -= diffz((x_, y_, z_), r) * gamma
    return {'x': x, 'y': y, 'z': z, 'B': B((x, y, z), r), 'r': r, 'f_sk': f_sk}
# Funkcija, kuri apibrezia pagrindini skaiciavima
def calculate(X, v, r=1, k=6):
    xvals = []
    X0 = X
    for i in range(0, k):
        f_sk.counter = 0
        answ = gradient_desc(X0, r)
        r = r / 2
        X0 = (round(answ['x'], 5), round(answ['y'], 5), round(answ['z'], 5))
        xvals.append([X0, round(answ['B'], 4), answ['r'], i+1, f_sk.counter])
    draw_table(xvals, v)
    
# Aprasyti pradiniai taskai
X0 = (0, 0, 0)
X0_ = (1e-5, 1e-5, 1e-5)
X1 = (1, 1, 1)
Xm = (0.5, 0, 0.9) # LSP A, B ir C reiksmes

# Skaiciuojamos vertes naudojant skirtingus X taskus
calculate(X0, 'X0')
calculate(X0_, 'X0 (beveik nulinės reikšmės)')
calculate(X1, 'X1')
calculate(Xm, 'Xm')

# Visualizacijai matlab
import matplotlib.pyplot as plt

# kintamasis naudojamas funkcijose skaiciuojant iskvietimus
i = 0

# mano funkcija
def f(x):
   global i
   i += 1
   return 7*x*x-8*x+6

#  pirmos eiles funkcijos isvestine
def df1(x):
   return 14*x-8

#  antros eiles funkcijos isvestine
def df2(x):
   return 14

# aprasomos asys kurias naudosiu vizuolizacijai
def graphAxes():
   axes = plt.gca()
   axes.set_xlim([0,5])
   axes.set_ylim([-3,30])

# vizuolizacijos funkcija
def visualization():
   x = []
   y = []
   for i in range(0, 101):
       x.append(i/10)
       y.append(f(i/10))
   graphAxes()
   plt.plot(x, y, 'k-')


#  Intervalo dalijimo pusiau metodas arba IDPM
def IDPM(interval):
   global i
   visualization()
   i = 0
   j = 0
# Algoritmas pagal skaidres
   l, r = interval 
   xm = (l + r)/2
   L = r - l
   fxm = f(xm)
   plt.plot(xm, fxm, 'md') #Kreipiames i Matlab
   while L >= 0.0001:
       x1 = l + L/4
       x2 = r - L/4
       f1 = f(x1)
       f2 = f(x2)
       plt.plot(x1, f1, 'md') #Kreipiames i Matlab
       plt.plot(x2, f2, 'md') #Kreipiames i Matlab
       if(f1 < fxm):
           r = xm
           xm = x1
           fxm = f1
       elif(f2 < fxm):
           l = xm
           xm = x2
           fxm = f2
       else:
           l = x1
           r = x2

       L = r - l
       #j kintamasis kuris skaičiuoja kiek žingsnių buvo atlikta, naudojamas kai viskas yra false
       j = j + 1
   plt.show()
   return "%.10f" % xm, i, j

# 
# Auksinio pjūvio metodas arba APM
def APM(interval):
   global i
   visualization()
   i = 0
   j = 0
   #Algoritmas is skaidriu
   l, r = interval
   L = r - l
   phi = 0.61803 #Fibonacio skaicius (is skaidriu)
   x1 = r - phi * L
   x2 = l + phi * L
   f1 = f(x1)
   f2 = f(x2)
   while L >= 0.0001:
       plt.plot(x1, f1, 'md')
       plt.plot(x2, f2, 'md')
       if(f2 < f1):
           l = x1
           L = r - l
           x1 = x2
           f1 = f2
           x2 = l + phi * L
           f2 = f(x2)
       else:
           r = x2
           L = r - l
           x2 = x1
           f2 = f1
           x1 = r - phi * L
           f1 = f(x1)
           #Skaiciuojame zingsnius
       j = j + 1
   plt.show()
   return "%.10f" % x1, i, j

# Niutono metodas arba NM
def NM(x0):
   global i
   visualization()
   i = 0
   j = 0
   comp = 0.0001                    # comp skirtas zingsnio dydzio matavimui
   x = x0
   fx = f(x)
   while(abs(df1(x)) > comp):
     df1x = df1(x)
     df2x = df2(x)
     x = x - (df1x/df2x)
     fx = f(x)
     plt.plot(x, fx, 'md')
     j = j + 1
   plt.show()
   return "%.10f" % x, i, j

minimum, funCalls, steps = IDPM([0, 10])
print('Intervalo dalijimo pusiau metodas: \nx: ', minimum,
', funkcijos iškvietimų skaičius: ', funCalls, ', padaryta žingsnių: ', steps)
minimum, funCalls, steps = APM([0, 10])
print('Auksinio pjuvio metodas: \nx: ', minimum,  
', funkcijos iškvietimų skaičius: ', funCalls, ', padaryta žingsnių: ', steps)
minimum, funCalls, steps = NM(5)
print('Niutono metodas: \nx: ', minimum,  
', funkcijos iškvietimų skaičius: ', funCalls, ', padaryta žingsnių: ', steps)
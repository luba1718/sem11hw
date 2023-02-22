import scipy
import numpy as np
from  graph import Graph

list_roots=[]

def func1(x,x1):
    return (-12*(x**4)*np.sin(np.cos(x))-18*(x**3)+5*(x**2)+10*x-30)
t0=1
min=-10
max=0
x1=scipy.optimize.brentq(func1, min,max,args=(t0))


def func2(x,x2,):
    return (-12*(x**4)*np.sin(np.cos(x))-18*(x**3)+5*(x**2)+10*x-30)
t0=1
min=0
max=10
x2=scipy.optimize.brentq(func2, min,max,args=(t0))


list_roots.append(x1)
list_roots.append(x2)
f = lambda x: round(x,2)
list_roots = list(map(f,list_roots))
print(f'Корни функции [x1,x2] = {list_roots}')

list_x = list(range(-200, 200))
f = lambda x: x/100
list_x = list(map(f, list_x))


f = lambda x: -12*(x**4)*np.sin(np.cos(x))-18*(x**3)+5*(x**2)+10*x-30
list_y = list(map(f, list_x))

roots_new=[]
roots_new.append(list_roots[0]-1)
roots_new.append(round((list_roots[0]+list_roots[1])/2,2))
roots_new.append(list_roots[1]+1)

list_y_new=list(map(f,roots_new))

sign=lambda x: ('f(x)>=0 ') if x>0 else 'f(x)<0 '
sign=list(map(sign,list_y_new))


sign_new=[]
sign_new.append(sign[0])
sign_new.append(list_roots[0])
sign_new.append(sign[1])
sign_new.append(list_roots[1])
sign_new.append(sign[2])
print(sign_new)
print(f'На промежутке (-4 , {list_roots[0]}] и [{list_roots[1]}, +4) f(x)>=0 \n\
На промежутке [{list_roots[0]}, {list_roots[1]}] f(x)<0')


min_l=[]
list_x = list(range(-4, 4+1))
f = lambda x:x 
list_x_y = list(map(f, list_x))

for x in list_x_y:
    y=-12*(x**4)*np.sin(np.cos(x))-18*(x**3)+5*(x**2)+10*x-30
    min_l.append(y)
    if x > min_l[-1]:
        print(f'Вершина функции на промежутке от -4 до 4 равна координатам {x,y}')
        break
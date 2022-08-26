
import numpy as np
import matplotlib.pyplot as plt

#%%
zc1 = 2+3j
zc2 = complex(2,3)
print('¿zc1 = zc2?', (zc1 == zc2))
zc1_real = np.real(zc1)

zc1_real = np.real(zc1)
zc1_imag = np.imag(zc1)
zc1_angle= np.angle(zc1)
zc1_conj = np.conj(zc1)

print(zc1)
print('parte real: ', zc1_real)
print('parte imaginaria: ', zc1_imag)
print('angulo en radianes: ', zc1_angle)
print('complejo conjugado: ', zc1_conj)

#%%
# ejercicio 1.01
# a traves de una funcion de numpy
zc1_module = np.absolute(zc1)
print(zc1_module)
# through a method of a complex object
print(zc1.__abs__())

#%%
# ejercicio 1.02
z1 = 4 + 3j
z2 = 2 + 2j

suma = z1+z2
resta = z1-z2
mult = z1*z2
div = z1/z2
print('Suma: ', suma)
print('Resta: ', resta)
print('Multiplicacion: ', mult)
print('Division: ', div)


#%% 
c = 1 + 2j
print('e^c=', np.exp(c))
print('log_natural(c)=', np.log(c))
print('log10(c)', np.log10(c))

#%%
#Logaritmo de cero
print('log(0)', np.log(0))
print('log(inf)', np.log(np.inf))

#%% ejercicio 1.03
c = np.array([[1, 5, 2],[3, 4, 8]])
print(c.shape)

#%% ejercicio 1.04
print(c[:,1])
#%% ejercicio 1.05
a = np.array([1,2,3,4])
#%%
b = a.reshape(2,2)
print(b)
#%% ejercicio 1.6

T=0.01
time = np.arange(-1, 1+T, T)
x_values = []
for t in time:
    x = 2*np.sin(2*np.pi*5*t)
    if x<0:
        x_values.append(-x)
    else:
        x_values.append(x)
plt.plot(time,x_values)
plt.grid()        

        


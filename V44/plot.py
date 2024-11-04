import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.signal import argrelextrema


"""
Plot des Detector-Scans mit Curve fit
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
# Messwerte laden
angle, I = np.genfromtxt('data/Detectorscan.UXD', unpack=True, skip_header=56)

# Berechnung von Mittelwert und Standardabweichung
mean = np.average(angle, weights=I)
sigma = np.sqrt(np.average((angle - mean)**2, weights=I))

# Angepasste Gaußfunktion
def g(x, a, x0, sigma, c):
    return a * np.exp(-((x - x0)**2) / (2 * sigma**2)) + c

# initial guess für curve_fit
initial_guess = [max(I) - min(I), mean, sigma, min(I)]

# curve_fit anpassen
para, pcov = curve_fit(g, angle, I, p0=initial_guess)
a, angle0, sigma, c = para

# Unsicherheiten der Parameter
pcov = np.sqrt(np.diag(pcov))
ua = ufloat(a, pcov[0]) 
uangle0 = ufloat(angle0, pcov[1])
usigma = ufloat(sigma, pcov[2])
uc = ufloat(c, pcov[3])

# FWHM berechnen
ufwhm = 2 * np.sqrt(2 * np.log(2)) * usigma  # FWHM mit Unsicherheiten

# Plotbereich anpassen
xx = np.linspace(min(angle), max(angle), 10000)

# Plot erstellen
plt.plot(angle, I, 'xr', markersize=6, label='measured data points', alpha=0.5)
plt.plot(xx, g(xx, *para), '-b', linewidth=1, label='Ausgleichsfunktion', alpha=0.5)
plt.xlabel(r'$Angle \, (\deg)$')
plt.ylabel(r'$Intensity \, (I)$')
plt.legend(loc="best")
plt.grid(True)
plt.savefig('build/Detektorscan.pdf')

# FWHM und Parameter ausgeben

print("-------------------------------------------")
print("Werte aus Detector-Scan 1:")
print("ua:", ua)
print("uangle0:", uangle0)
print("usigma:", usigma)
print("uc:", uc)
print("FWHM (mit Unsicherheit):", ufwhm)
print("-------------------------------------------")

#plt.show()
plt.clf()

"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""








"""
Plot des ersten Z-scans mit Plateau
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

Zcoord, I = np.genfromtxt('data/Z-Scan-09to09v1.UXD', unpack=True, skip_header=56)




plt.plot(Zcoord, I, 'xr', markersize=6, label='measured data points', alpha=0.5)
plt.axvline(0.3000, linestyle= 'dashed',label='Bereich des Abfalls')
plt.axvline(0.5000, linestyle= 'dashed')
plt.legend(loc="best")
plt.grid(True)

print("Werte aus Z-Scan 1:")
print("Strahlbreite", 0.3+0.5)
print("-------------------------------------------")


plt.savefig('build/Z-Scanv1.pdf')
#plt.show()
plt.clf()


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""



"""
Plot des ersten Rocking scans für Geometriewinkel
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


Zcoord, I = np.genfromtxt('data/Rocking-Scan-1to1v2.UXD', unpack=True, skip_header=56)




plt.plot(Zcoord, I, 'xr', markersize=6, label='measured data points', alpha=0.5)
plt.axvline(-0.5200, linestyle= 'dashed',label='Geometriewinkel')
plt.axvline(0.5200, linestyle= 'dashed')
plt.xlabel(r'$Angle \, (\deg)$')
plt.ylabel(r'$Intensity \, (I)$')
plt.legend(loc="best")
plt.grid(True)

print("Werte aus Rockingscan 1:")
print("Geometriewinkel", 0.52)
print("-------------------------------------------")


plt.savefig('build/RockingScan-1to1.pdf')
#plt.show()
plt.clf()



"""
Plot Refraktivität
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

#eventuell refraktivität auf y achse wie im altprotokoll?????
alpha_i, I = np.genfromtxt('data/Reflektivität.UXD', unpack=True, skip_header=56) 
minimax =[]
minimay =[]

for i in [52, 150]:
    if I[i] < I[i - 1] and I[i] < I[i + 1]:
        minimax.append(alpha_i[i])
        minimay.append(I[i])
        i = i+1
        print(i)
        
#Limit the range to entries 52 to 150 
alpha_i_limited = alpha_i[52:120] 
I_limited = I[52:120] 

# # Identify local minima in the limited range 
local_minima_indices = argrelextrema(I_limited, np.less) 
local_minima_x = alpha_i_limited[local_minima_indices]
local_minima_y = I_limited[local_minima_indices]

plt.plot(alpha_i, I, linestyle= '-', color='red', markersize=6, label='measured refractivity', alpha=0.5)
#plt.plot(alpha_i, I/(1/0.8), linestyle= '-', color='red', markersize=6, label='measured refractivity with correction', alpha=0.5)
#plt.plot(minimax, minimay,'og' , markersize=6, label='measured refractivity', alpha=0.5)
plt.scatter(local_minima_x, local_minima_y, color='blue', label='local minima')


print("Minima für Schichtdicke oder so:")
print("alpha_i_min", local_minima_x)
print("-------------------------------------------")

plt.xlabel(r'Z$\text{-Coordinate}$')
plt.ylabel(r'$Intensity \, (I)$')
plt.legend(loc="best")
plt.grid(True)
plt.yscale('log')

plt.savefig('build/Refraktivitätv1.pdf')

plt.show()
plt.clf()
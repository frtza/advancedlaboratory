import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial as fac

def binom(k, n, p):
	return p**k * (1 - p)**(n - k) * fac(n) / (fac(k) * fac(n - k))

K = np.arange(53)

plt.plot(K[0:15], 100 * binom(K[0:15], 22, 0.250), 'D', ms=3, c='firebrick', markeredgewidth=0, alpha=0.2)
plt.plot(K[4:21], 100 * binom(K[4:21], 22, 0.500), 'D', ms=3, c='goldenrod', markeredgewidth=0, alpha=0.3)

plt.plot(K[15:40], 100 * binom(K[15:40], 52, 0.500), 'o', ms=2, c='steelblue', label=r'Basisabgleich (Alice \& Bob)')
plt.plot( K[0:15], 100 * binom(K[0:15], 52, 0.125),  'o', ms=2, c='firebrick', label=r'Bitfehler (Alice \& Bob)')
plt.plot( K[2:25], 100 * binom(K[2:25], 52, 0.250),  'o', ms=2, c='goldenrod', label=r'Basisabweichung (Eve)')

plt.xlabel(r'$k$')
plt.ylabel(r'$P (c = k)$ $\mathbin{/}$ \unit{\percent}')

plt.legend()

plt.savefig('build/verteilung.pdf')
plt.close()

def _Binom(k, n, p):
	return np.sum(binom(np.arange(k, n + 1), n, p))
def Binom(k, n, p):
	return np.vectorize(_Binom)(k, n, p)

N = np.arange(20, 61)

plt.plot(N, 100 * Binom(20, N, 0.5), 's', ms=2, c='olivedrab', label=r'Basisabgleich (Alice \& Bob)')

plt.xlabel(r'$n$')
plt.ylabel(r'$P (c \geq k)$ $\mathbin{/}$ \unit{\percent}')

plt.legend()

plt.savefig('build/kumuliert.pdf')
plt.close()

with open('build/p20.tex', 'w') as f:
	f.write(f'\\qty{{{100 * Binom(20, 52, 0.5):.2f}}}{{\\percent}}')
with open('build/p23.tex', 'w') as f:
	f.write(f'\\qty{{{100 * binom(23, 52, 0.5):.2f}}}{{\\percent}}')
with open('build/p22.tex', 'w') as f:
	f.write(f'\\qty{{{100 * binom(22, 52, 0.5):.2f}}}{{\\percent}}')
with open('build/p11.tex', 'w') as f:
	f.write(f'\\qty{{{100 * binom(11, 52, 0.25):.2f}}}{{\\percent}}')
with open('build/p4.tex', 'w') as f:
	f.write(f'\\qty{{{100 * binom(4, 52, 0.125):.2f}}}{{\\percent}}')
with open('build/pp11.tex', 'w') as f:
	f.write(f'\\qty{{{100 * binom(11, 22, 0.5):.2f}}}{{\\percent}}')
with open('build/pp4.tex', 'w') as f:
	f.write(f'\\qty{{{100 * binom(4, 22, 0.25):.2f}}}{{\\percent}}')

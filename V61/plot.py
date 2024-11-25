#######################
### Start Theory Curves
#######################


import matplotlib.pyplot as plt
import numpy as np

def g1g2(L, R1, R2):
	return (1 - L / R1) * (1 - L / R2)

l = np.linspace(-200, 3200, 3400)

stab_inf_hr_14_oc = g1g2(l, np.inf, 1400)
stab_10_hr_14_oc = g1g2(l, 1000, 1400)
stab_14_hr_14_oc = g1g2(l, 1400, 1400)

plt.fill_between([-200, 3200], 1, 0, color='none', facecolor='goldenrod', alpha=1/3, label=r'$0 \leq g_1 g_2 \leq 1$')

plt.plot(l, stab_inf_hr_14_oc, label=r'$g_{\text{HR}_\infty} g_{\text{OC}_{\qty{1400}{\milli\meter}}}$')
plt.plot([1400, 1400], [-1, 0], linestyle=(0, (4, 1)), color='olivedrab')
plt.plot(l, stab_10_hr_14_oc, label=r'$g_{\text{HR}_{\qty{1000}{\milli\meter}}} g_{\text{OC}_{\qty{1400}{\milli\meter}}}$')
plt.plot([2400, 2400], [-1, 1], linestyle=(3.5, (4, 1)), color='steelblue')
plt.plot(l, stab_14_hr_14_oc, label=r'$g_{\text{HR}_{\qty{1400}{\milli\meter}}} g_{\text{OC}_{\qty{1400}{\milli\meter}}}$')
plt.plot([2800, 2800], [-1, 1], linestyle=(3.5, (4, 1)), color='firebrick')

plt.plot([], [], linestyle=(1.5, (4, 1)), color='black', label=r'$L_\text{max}$')

plt.xlim(0, 3000)
plt.ylim(-0.5, 2.5)

plt.xlabel(r'$L \mathbin{/} \unit{\milli\meter}$')
plt.ylabel(r'$g_1 g_2$')

plt.legend()

plt.savefig('build/stability.pdf')


#######################
##### End Theory Curves
#######################

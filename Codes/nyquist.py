import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import style
import control
from control import tf
# style.use('seaborn')


systems=[50,60,70,100]







plt.figure()

# mag=20*np.log(mag)
for i in systems:
    sys=tf([i],[1,6,11,6])
    gm,pm,wg,wp= control.margin(sys)
    
    control.nyquist(sys, label=i)


plt.legend()
plt.show()


# plt.show()

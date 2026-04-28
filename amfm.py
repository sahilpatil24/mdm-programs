#amfm
#for fm -> modulation index > 5 for the frequency change to be visible
#t should be having high resolution like 5000 not 300 is quite low

import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
fm = 5
fc = 100
am = 2
ac = 5
t = np.linspace(0,1,5000)
modulation_index = 5

message = np.sin(2 * pi * fm * t)
carrier = ac * np.cos(2 * pi * fc * t)

am_signal = ac * (1 + modulation_index * message) * np.cos(2 * pi * fc * t)
fm_signal = ac * np.cos(2 * pi * fc * t + modulation_index * np.sin(2 * pi * fm * t))


plt.subplot(4,1,1)
plt.plot(t,message)

plt.subplot(4,1,2)
plt.plot(t,carrier)

plt.subplot(4,1,3)
plt.plot(t,am_signal)

plt.subplot(4,1,4)
plt.plot(t,fm_signal)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

#define the variables
fs = 1000
fm = 5
fc = 100
Am = 2
Ac = 5
t = np.linspace(0,1,300)
modulation_index = 0.8

#message and carrier
message = np.sin(2 * np.pi * fm * t) 
carrier = Ac * np.cos(2 * np.pi * fc * t)

am_signal = Ac * (1 + modulation_index * message) * np.cos(2 * np.pi * fc * t)
fm_signal = Ac * np.cos(2 * np.pi * fc * t + modulation_index * np.sin(2 * np.pi * fm * t))

plt.subplot(4,1,1)
plt.title("Message")
plt.plot(t,message)

plt.subplot(4,1,2)
plt.title("Carrier")
plt.plot(t,carrier)
plt.subplot(4,1,3)
plt.title("Am")
plt.plot(t,am_signal)
plt.subplot(4,1,4)
plt.title("Fm")
plt.plot(t,fm_signal)

plt.tight_layout()
plt.show()
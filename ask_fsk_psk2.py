import matplotlib.pyplot as plt
import numpy as np

#define the variables
fs = 1000
fc = 50
f1 = 50
f0 = 20
bit_duration = 0.2
bits = [1,0,1,1,0,1,0]

t = np.linspace(0,0.7,700)

#define message
message = np.repeat(bits,100)
carrier = np.cos(2 * np.pi * fc * t)

#define the 3 signals here
ask = message * carrier
fsk = []
psk = []

#for loop now
for bit in bits:
  t_bit = np.linspace(0,0.1,100)

  if bit == 1:
    fsk_signal = np.sin(2 * np.pi * f0 * t_bit)
    psk_signal = np.sin(2 * np.pi * fc * t_bit + 0)
  else:
    fsk_signal = np.sin(2 * np.pi * f1 * t_bit)
    psk_signal = np.sin(2 * np.pi * fc * t_bit + np.pi)
  fsk.extend(fsk_signal)
  psk.extend(psk_signal)

plt.subplot(5,1,1)
plt.title("Message")
plt.plot(t,message)

plt.subplot(5,1,2)
plt.title("carrier")
plt.plot(t,carrier)

plt.subplot(5,1,3)
plt.title("ask")
plt.plot(t,ask)

plt.subplot(5,1,4)
plt.title("fsk")
plt.plot(t,fsk)

plt.subplot(5,1,5)
plt.title("psk")
plt.plot(t,psk)

plt.tight_layout()
plt.show()
#1
h = [0]*12
d = [0]*8

#2
print("Enter the 7 bit data:")
for i in range(1,8):
  d[i] = int(input())

#3 - copy into h array
h[3],h[5],h[6],h[7],h[9],h[10],h[11] = d[1],d[2],d[3],d[4],d[5],d[6],d[7]

#4 - compute first 4
h[1] = h[3] ^ h[5] ^ h[7] ^ h[9] ^ h[11]
h[2] = h[3] ^ h[6] ^ h[7] ^ h[10] ^ h[11]
h[4] = h[5] ^ h[6] ^ h[7]
h[8] = h[9] ^ h[10] ^ h[11]

#5 - display hamming code
print("The 11 bit hamming code is: ")
for i in range(1,12):
  print(h[i], end="")

#6 - receiver's array compute and all
r = [0]*12

#7
print("Enter the 12 bit receiver's code:")
for i in range(1,12):
  r[i] = int(input())

#8 compute these values
s1 = r[1] ^ r[3] ^ r[5] ^ r[7] ^ r[9] ^ r[11]
s2 = r[2] ^ r[3] ^ r[6] ^ r[7] ^ r[10] ^ r[11]
s4 = r[4] ^ r[5] ^ r[6] ^ r[7]
s8 = r[8] ^ r[9] ^ r[10] ^ r[11]

#error correction
error = s1 + (2 * s2) + (4 * s4) + (8*s8)

if(error == 0):
  print("no error")
else:
  print("err at bit: ", error)
  #flip
  r[error] = 1 - r[error]
  print("The error correction is odone: ")
  for i in range(1,12):
    print(r[i], end="")


#display the data array
print("The 7 bit data is: ")
for i in range(1,8):
  print(d[i], end="")

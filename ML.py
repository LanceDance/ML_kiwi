import numpy as np
import matplotlib.pyplot as plt
import requests
plt.get_backend()
plt.interactive(False)
plt.figure()
plt.interactive(False)
lisx = []
lisy = []

for a in range(-10,10):
        url = 'http://165.227.157.145:8080/api/do_measurement?x=' + str(a)
        # rl = urllib.request.urlopen('http://165.227.157.145:8080/api/do_measurement?x=' + str(a)).read()
        r = requests.get(url)
        c = r.json()
        x = int(c['data']['x'])
        lisx.append(x)
        y = int(c['data']['y'])
        lisy.append(y)

xarr = np.array(lisx)
yarr = np.array(lisy)
matrix = np.column_stack((xarr,yarr))

b = np.minimum(xarr,yarr)
b = matrix[matrix[0][1] != 0].min()
rows = np.where(matrix[:, 1] == b)
peak = matrix[rows]
h = peak[0][0]
k = peak[0][1]
print(peak)
print(b)
print(matrix)
z = np.polyfit(xarr,yarr,0)
# print("{0}x^2 + {1}x^2 ".format(z))
yzero = 0
itemindex = np.where(yarr == 0)
abc = itemindex[0]
xzero = matrix[abc][0][0]

xyz = None
vysledek = (xzero - h)**2


# vysledek = a * (x - h) ** 2 + k
# print(vysledek)
#
# vysledek2 = vysledek * (x - h) ** 2 + k
# print(vysledek2)

# miny = min(yarr)
# print(miny)
# print(matrix)


# ymin = min(lisx)
# xpos = lisy.index(ymin)
# xmin = xarr[xpos]
# ymax = max(lisy)

# xpos = lisy.index(ymax)
# xmas = lisx[xpos]
# print(ymin,xmin)


# vykresleni grafu
plt.axhline(0, color='black')
plt.axvline(0, color='black')
axes = plt.gca()
axes.get_ylim()
plt.plot(xarr, yarr)


plt.show()


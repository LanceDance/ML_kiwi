import numpy as np
import matplotlib.pyplot as plt
import requests
plt.get_backend()
plt.interactive(False)
plt.figure()
plt.interactive(False)
lisx = []
lisy = []

def find_nearest_vector(array, value):
  idx = np.array([np.linalg.norm(y+x) for (y,x) in array-value]).argmin()
  return array[idx]


for i in range(-20,20):
        url = 'http://165.227.157.145:8080/api/do_measurement?x=' + str(i)
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
h = peak.item(0)
k = peak.item(1)
print(h)
print(k)
print(matrix)
z = np.polyfit(xarr,yarr,0)

yzero = find_nearest_vector(matrix,0)

xzero = yzero[0]
yzero = yzero[1]
print(xzero,yzero)

zavorka = (xzero - h) ** 2
print('{}y = a({}x - {}h) ** 2 + {}k'.format(yzero,xzero,h,k))
plt.axhline(0, color='black')
plt.axvline(0, color='black')
axes = plt.gca()
axes.get_ylim()
plt.plot(xarr, yarr)


plt.show()


import numpy as np
import matplotlib.pyplot as plt
import requests
plt.get_backend()
plt.interactive(False)
plt.figure()
plt.interactive(False)
lisx = []
lisy = []


for i in range(-100,100):
        url = 'http://165.227.157.145:8080/api/do_measurement?x=' + str(i)
        # rl = urllib.request.urlopen('http://165.227.157.145:8080/api/do_measurement?x=' + str(a)).read()
        r = requests.get(url)
        c = r.json()

        x = c['data']['x']
        lisx.append(x)
        y = c['data']['y']
        lisy.append(y)


'''
create matrix
'''
xarr = np.array(lisx, dtype=float)
yarr = np.array(lisy, dtype=float)
matrix = np.column_stack((xarr,yarr))


"""
find where x = 0
return array in matrix
"""
get_zero = np.where(matrix == 0)[0]
zero = matrix[get_zero]
zero_x = zero[0][0]
zero_y = round(zero[0][1], 3)
print('Zerox: ' + str(zero_x))
print('Zeroy: ' + str(zero_y))
print(matrix)

'''
find the (h,k) value
'''
c = min(lisy)
xyz = lisy.index(c)
peak = matrix[xyz]
h = round(peak[0], 3)
k = round(peak[1], 3)

print(h, k)

'''
equation
'''
print('f(x) = a(x-h)**2 + k')
print('f(x) = a({} - {}) **2 + {}'.format(zero_x,h,k))


'''
graph
'''

plt.axhline(0, color='black')
plt.axvline(0, color='black')
axes = plt.gca()
axes.get_ylim()

plt.plot(xarr, yarr, 'ro')
plt.savefig('graph.png')
plt.show()


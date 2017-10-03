import numpy
import ast
import matplotlib.pyplot as plt
import requests
matplotlib.use('TkAgg')
lisx = []
lisy = []

for a in range(-10,10):
        url = 'http://165.227.157.145:8080/api/do_measurement?x=' + str(a)
        # rl = urllib.request.urlopen('http://165.227.157.145:8080/api/do_measurement?x=' + str(a)).read()
        r = requests.get(url)
        c = r.json()
        d = c['data']['x']
        lisx.append(d)
        y = c['data']['y']
        lisy.append(y)
print(lisx)
print(lisy)

plt.plot(lisx)
plt.ylabel(lisy)
plt.show()
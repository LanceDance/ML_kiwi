import time
import matplotlib.pyplot as plt
import requests
import numpy as np

lisx = []
lisy = []


start = time.time()
for a in range(-10, 10):
        url = 'http://165.227.157.145:8080/api/do_measurement?x=' + str(a)
        r = requests.get(url)
        c = r.json()
        x = c['data']['x']
        lisx.append(x)
        y = c['data']['y']
        lisy.append(y)
        if x == 0:
                print()
end = time.time()
axes = plt.gca()
ymin, ymax = axes.get_ylim()
# print(lisx)
# print(lisy)
print(end - start)
plt.plot(lisx, lisy)
plt.show()

peak = np.ptp(lisx,lisy)
print(peak)
# plt.savefig('ML.png')
#
# res = numpy.linalg.solve(lisx,lisy)
# print(res)


import json
import numpy as np
import math
from scipy import stats

a = input("Enter file name: \n")
if a.endswith(".json") is False:
    a = a + ".json"
dic = {}

with open(a, 'r') as file:
    dic = json.load(file)

var = len(dic["classes"]["0"][0])
print("Use Ctrl + C to exit!")
while True:
    try:
        vari = []
        result = []
        for i in range(var):
            while True:
                x = input("Enter value of variable " + str(i+1) + "\n")
                if len(x) > 0:
                    try: 
                        x = float(x)
                        vari.append(x)
                        break
                    except: continue
        dic1 = {}
        for l, k in dic["GDA"].items():
            l_lis = l[1:-1].split(',')
            l_tup = tuple(i.strip() for i in l_lis)
            dic1[l_tup] = k
        for i, z in dic1.items():
                v=[]
                phi = z["phi"]
                sigma = z["sigma"]
                c1_mean = z["c1_mean"]
                c2_mean = z["c2_mean"]
                for j, l in enumerate(c1_mean):
                    for m, n in enumerate(vari):
                        if j == m: v.append(n - l)
                j = np.matrix([v], dtype = np.float64)
                P_xy_1 = math.exp(-(np.sum(j*np.linalg.inv(sigma)*j.T)/2))/(((2*math.pi) ** (var/2)) * (np.linalg.det(sigma) ** 0.5))
                v=[]
                for j, l in enumerate(c2_mean):
                    for m, n in enumerate(vari):
                        if j == m: v.append(n - l)
                j = np.matrix([v], dtype = np.float64)
                P_xy_2 = math.exp(-(np.sum(j*np.linalg.inv(sigma)*j.T)/2))/(((2*math.pi) ** (var/2)) * (np.linalg.det(sigma) ** 0.5))
                print(P_xy_1, P_xy_2, phi)
                m2 = P_xy_2*phi
                m1 = P_xy_1*(1-phi)
                if m1 > m2: 
                    print("Value belongs to class", i[0])
                    cla = i[0]
                else:
                    print("Value belong to class", i[1])
                    cla = i[1]
                result.append(cla)
                print(cla)
        array = np.array(result)
        mode = stats.mode(array)
        print("The class is", mode[0])
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        while True:
            ask = input("Exit? y/n \n")
            if ask == 'y' or ask == 'n': break
        if ask == 'y': break
    except KeyError:
       print("\nRun GDA.py!")
       break

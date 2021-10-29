import json
import math
from itertools import combinations
import numpy as np 

a = input("Enter file name: \n")
if a.endswith(".json") is False:
    a = a + ".json"
dic = {}

with open(a, 'r') as file:
    dic = json.load(file)

cl = [i for i in range(len(dic["classes"]))]
var = len(dic["classes"]["0"][0])

ad = {}
cl_c = combinations(cl, 2)
for i in list(cl_c):
    e = 'n'
    print("For classes: ", i)
    c1 = dic["classes"][str(i[0])]
    c2 = dic["classes"][str(i[1])]
    c1_mean = []
    c2_mean = []
    vals_1 = [[] for l in range(var)]
    vals_2 = [[] for l in range(var)]
    for j in c1:
        for p, n in enumerate(j):
            for m, o in enumerate(vals_1):
                if p == m: o.append(n)
    for j in vals_1: c1_mean.append(sum(j)/len(j))
    for j in c2:
        for p, n in enumerate(j):
            for m, o in enumerate(vals_2):
                if p == m: o.append(n)
    for j in vals_2: c2_mean.append(sum(j)/len(j))
    sigma_1 = np.zeros((var, var), dtype = np.float64)
    sigma_2 = np.zeros((var, var), dtype = np.float64)
    print(c1_mean, c2_mean)
    for k in c1:
        v=[]
        for j, l in enumerate(c1_mean):
            for m, n in enumerate(k):
                if j == m: v.append(n - l)
        sigma_1 = np.add(sigma_1, np.matrix([v], dtype = np.float64).T*np.matrix([v], dtype = np.float64))
    for k in c2:
        v=[]
        for j, l in enumerate(c2_mean):
            for m, n in enumerate(k):
                if j == m: v.append(n - l)
        sigma_2 = np.add(sigma_2, np.matrix([v], dtype = np.float64).T*np.matrix([v], dtype = np.float64))
    sigma_1 = np.multiply(sigma_1, 1/(len(c1)+len(c2)))
    sigma_2 = np.multiply(sigma_2, 1/(len(c2)+len(c1)))
    sigma = np.add(sigma_1, sigma_2)
    print(sigma.tolist())
    phi = (len(c2)+1)/(len(c1)+len(c2)+1)
    ad[str(i)] = {}
    ad[str(i)]["phi"] = phi
    ad[str(i)]["sigma"] = sigma.tolist()
    ad[str(i)]["c1_mean"] = c1_mean
    ad[str(i)]["c2_mean"] = c2_mean
while True:
    s_data = input("Save data? y/n\n")
    if s_data == 'y' or s_data == 'n': break
if s_data == 'y':
    add = {}
    with open(a, 'r') as file:
        add = json.load(file)
    add["GDA"] = ad
    with open(a, 'w') as file:
        json.dump(add, file)

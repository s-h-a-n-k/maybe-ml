import json
import numpy as np

a = input("Enter file name: \n")

if a.endswith(".json") is False:
    a = a + ".json"

dic = {}
with open(a, 'r') as file:
    dic = json.load(file)

var = len(dic["classes"]["0"][0])
while True:
    try:
        c_dic = {}
        v_arr = [1]
        cou = 0
        for i in range(var):
            while True:
                b = input("Enter the value of " + str(i) + " variable \n")
                if len(b) > 0:
                    try:
                        b = float(b)
                        v_arr.append(b)
                        break
                    except: continue
                if len(b) == 0: raise KeyboardInterrupt
        v_mat = np.matrix([v_arr], dtype = np.float64)
        for l, k in dic["parameters"].items():
            l_lis = l[1:-1].split(',')
            l_lis = [i.strip() for i in l_lis]
            c1_mean = [1]
            vals_1 = [[] for l in range(var)]
            c1 = dic["classes"][l_lis[0]]
            for j in c1:
                for p, n in enumerate(j):
                    for m, o in enumerate(vals_1):
                        if p == m:
                            o.append(n)
            for j in vals_1:
                c1_mean.append(sum(j)/len(j))
            x1_val = np.sum(np.matrix([c1_mean], dtype = np.float64)*np.matrix(k, dtype = np.float64))
            p_val = np.sum(v_mat*np.matrix(k, dtype = np.float64))
            if p_val*x1_val > 0 : c_dic[l_lis[0]] = c_dic.get(l_lis[0], 0) + 1
            else: c_dic[l_lis[1]] = c_dic.get(l_lis[1], 0) + 1
        ma = 0
        for i, j in c_dic.items():
            if j > ma: 
                ma = j
                m = i
        print("class is", m, "\n")
    except KeyboardInterrupt:
        ask = input("Type 'exit' to Exit\n")
        if ask == "exit": break
        else: continue
    except KeyError:
       print("\nRun logistic_regression.py!")
       break

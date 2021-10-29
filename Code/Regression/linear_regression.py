import json
import numpy as np
import matplotlib.pyplot as plt

a = input("Enter file name: \n")

if a.endswith(".json") is False:
    a = a + ".json"

dic = {}
with open(a, 'r') as file:
    dic = json.load(file)
if type(dic["points"]["0"][0]) is list:
    x = len(dic["points"]["0"][0])
else: x = 1
print(x)
n_p = x + 1
tr = 0
for i in dic["points"].values():
    i[0].insert(0, 1)

again = False
many = False

while True:
    try:
        tr += 1
        print("try:",tr)
        if again == False and many == False:
            p_j = []
            p_j_st = []
            alpha = input("enter alpha \n")
            if len(alpha) == 0:
                alpha = 1
                print("alpha is 1")
            try:
                alpha = float(alpha)
                if alpha <= 0: continue
            except: continue
            for i in range(n_p):
                x = input("Enter start value for parameter " + str(i) + "\n")
                x = float(x)
                p_j.append(x)
                p_j_st.append(x)
        if again == True:
            alpha = alpha/10
            p_j = p_j_st[:]
            again = False
        if many == True:
            alpha = alpha*2
            p_j = p_j_st[:]
            many = False
        cou = 0
        s = True
        p_mat = np.matrix([p_j], dtype = np.float64)
        new_p_j = p_j[:]

        while s == True:
            print(cou, p_j)
            if cou > 1000:
                many = True
                break
            for i in dic["points"].values():
                i_mat = np.matrix([i[0]], dtype = np.float64)
                for j in range(len(new_p_j)):
                    new_p_j[j] -= alpha*(np.sum(p_mat*i_mat.T) - i[1])*i[0][j]
                    if new_p_j[j] == float('inf') or new_p_j[j] == float('-inf') or new_p_j[j] == float('nan'):
                        again = True
                        break
            if again == True: break
            v = 0
            for i in range(n_p):
                if new_p_j[i] - p_j[i] > 0.001 or new_p_j[i] - p_j[i] < -0.001: break
                else:
                    v += 1
            if v == n_p:
                print(p_j, new_p_j)
                s = False
            if s == True:
                p_mat = np.matrix([new_p_j], dtype = np.float64)
                p_j = new_p_j[:]
                cou += 1
        print(p_j)
        if cou < 10: again = True
        if again == True or many == True: continue
        y_j = []
        y_1 = []
        p_mat = np.matrix([p_j], dtype = np.float64)
        x_j = {}
        for i in dic["points"].values():
            i_mat = np.matrix([i[0]], dtype = np.float64)
            y = np.sum(p_mat*i_mat.T)
            y_j.append(y)
            for j, k in enumerate(i[0]):
                if j > 0:
                    try:
                        x_j[j] += [k]
                    except:
                        x_j[j] = [k]
            y_1.append(i[1])
        while True:
            con = input("Proceed to graph? y/n \n")
            if con == 'y' or con == 'n': break
            else: continue
        if con == 'y':
            for i, j in x_j.items():
                plt.title(str(i) + " input variable\nalpha: "+ str(alpha)+ "\ninitial parameters "+ str(p_j_st))
                plt.plot(j, y_1, color='r', label="points")
                plt.plot(j, y_j, color='b', label=str(p_j))
                plt.legend()
                plt.show()
            print("Done!")
            while True:
                ask = input("Update Parameters? y/n\n")
                if ask == 'y':
                    ad = {}
                    with open(a, 'r') as file:
                        ad = json.load(file)
                    ad["parameters"] = p_j
                    with open(a, 'w') as file:
                        json.dump(ad, file)
                    break
                elif ask == 'n': raise KeyboardInterrupt
                else: continue
            raise KeyboardInterrupt
        elif con == 'n':
            tr = 0
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        e = input("Exit? y/n \n")
        if e == 'y': break
        else: 
            tr = 0
            continue

import json
import math
import matplotlib.pyplot as plt
from itertools import combinations
import numpy as np 
from mpl_toolkits import mplot3d

a = input("Enter file name: \n")
if a.endswith(".json") is False:
    a = a + ".json"
dic = {}

with open(a, 'r') as file:
    dic = json.load(file)

cl = [i for i in range(len(dic["classes"]))]
cl_c = combinations(cl, 2)
par = {}
var = len(dic["classes"]["0"][0])

for i in dic["classes"].values():
    for l in i:
        l.insert(0, 1)

ad = {}
print("Ctrl+C to exit \n")
for i in list(cl_c):
    e = 'n'
    print("For classes: ", i)
    c1 = dic["classes"][str(i[0])] 
    c2 = dic["classes"][str(i[1])]
    cou = 0
    small = False
    again = False
    limit = False
    while True:
        try:
            cou += 1
            print("try:", cou)
            if small == False and again == False and limit == False:
                while True:
                    try:
                        lim = input("Enter maximum allowed points on opposite side\n")
                        if len(lim) == 0:
                            lim = 1
                        else:
                            lim = int(lim)
                            if lim >= 0: break
                            else: continue
                    except KeyboardInterrupt: break
                    except:
                        print("Enter a positive integer!")
                        continue
                p_arr = []
                for j in range(var + 1):
                    while True:
                        try:
                            p = input("Enter the value of parameter " + str(j) + "\n")
                            p = float(p)
                        except ValueError: continue
                        break
                    p_arr.append([p])
                while True:
                    try:
                        alpha = input("Enter the value of alpha \n")
                        if len(alpha) == 0:
                            print("alpha is 0.00000001")
                            alpha = 0.00000001
                        alpha = float(alpha)
                        if alpha > 0: break
                    except ValueError: continue
                p_mat_rep = np.matrix(p_arr, dtype=np.float64)
            if small == True:
                alpha = alpha*2
                print("alpha now:", alpha)
                small = False
            if again == True:
                alpha = alpha/2
                print("alpha now:", alpha)
                again = False
            if limit == True:
                alpha = alpha*1.1
                print("alpha now:", alpha)
                limit = False
            p_mat = np.matrix(p_mat_rep)
            new_p_arr = p_mat_rep.tolist()
            coun = 0
            try:
                while True:
                    coun += 1
                    print(coun, p_arr)
                    for l in c1:
                        v_mat = np.matrix([l], dtype = np.float64).T
                        for k in range(var + 1):
                            new_p_arr[k][0] = np.sum(p_mat[k][0]) + alpha*(0 - 1/(1 + math.exp(-np.sum(p_mat.T*v_mat)))*np.sum(v_mat[k][0]))
                    for l in c2:
                        v_mat = np.matrix([l], dtype = np.float64).T
                        for k in range(var + 1):
                            new_p_arr[k][0] = np.sum(p_mat[k][0]) + alpha*(1 - 1/(1 + math.exp(-np.sum(p_mat.T*v_mat)))*np.sum(v_mat[k][0]))
                    print(new_p_arr, p_mat)
                    diff_count = 0
                    for k in range(var + 1):
                        if np.sum(p_mat[k][0]) - new_p_arr[k][0] > 0.0001 or np.sum(p_mat[k][0]) - new_p_arr[k][0] < - 0.0001:
                            break
                        else:
                            print("diff = ", np.sum(p_mat[k][0]) - new_p_arr[k][0])
                            diff_count += 1
                    if diff_count == var + 1: 
                        if coun > 10:
                            c1_mean = []
                            vals_1 = [[] for l in range(var + 1)]
                            for j in c1:
                                for p, n in enumerate(j):
                                    for m, o in enumerate(vals_1):
                                        if p == m:
                                            o.append(n)
                            for j in vals_1:
                                c1_mean.append(sum(j)/len(j))
                            param = np.matrix(new_p_arr, dtype = np.float64)
                            c1_val = np.sum(np.matrix([c1_mean], dtype = np.float64)*param)
                            points = 0
                            for j in c1:
                                v_mat = np.matrix([j], dtype = np.float64).T
                                p_val = np.sum(param.T*v_mat)
                                if c1_val*p_val < 0: points += 1
                            for j in c2:
                                v_mat = np.matrix([j], dtype = np.float64).T
                                p_val = np.sum(param.T*v_mat)
                                if c1_val*p_val > 0: points -= 1
                            if abs(points) > lim:
                                limit = True
                                print(abs(points))
                                break
                            else:
                                print(new_p_arr, coun, abs(points),"Done \n")
                                break
                        else: 
                            print("count:", coun)
                            small = True
                            break
                    p_arr = []
                    p_arr.extend(new_p_arr)
                    p_mat = np.matrix(p_arr, dtype = np.float64)
            except OverflowError:
                again = True
                continue
            if limit == True:
                print("limiting...")
                continue
            if small == True: 
                print("small...")
                continue
            print("Done: ", i, new_p_arr)
            par[i] = new_p_arr
            while True:
                con = input("print figures? y/n \n")
                if con == 'n':
                    cou = 0
                    break
                elif con == 'y':
                    ad[str(i)] = p_arr
                    c_1 = str(i[0])
                    c_2 = str(i[1])
                    c1_p = dic["classes"][c_1]
                    c2_p = dic["classes"][c_2]
                    if var == 3:
                        cla1 = [[],[],[]]
                        cla2 = [[],[],[]]
                        for n in c1_p:
                            cla1[0].append(n[1])
                            cla1[1].append(n[2])
                            cla1[2].append(n[3])
                        fig = plt.figure()
                        ax = plt.axes(projection="3d")
                        ax.scatter3D(cla1[0], cla1[1], cla1[2],color='r', label=c_1 + " n: " + str(len(c1_p)))
                        for n in c2_p:
                            cla2[0].append(n[1])
                            cla2[1].append(n[2])
                            cla2[2].append(n[3])
                        x1l = -np.sum(par[i][0][0])/np.sum(par[i][1][0])
                        x2l = -np.sum(par[i][0][0])/np.sum(par[i][2][0])
                        x3l = -np.sum(par[i][0][0])/np.sum(par[i][3][0])
                        x1m = min(list(l[1] for l in c1)+list(m[1] for m in c1))
                        x2m = max(list(l[2] for l in c1)+list(m[2] for m in c1))
                        x3m = -(np.sum(par[i][0][0]) + np.sum(par[i][1][0])*x1m + np.sum(par[i][2][0])*x2m)/np.sum(par[i][3][0])
                        x2M = min(list(l[2] for l in c1)+list(m[2] for m in c1))
                        x3M = max(list(l[3] for l in c1)+list(m[3] for m in c1))
                        x1M = -(np.sum(par[i][0][0]) + np.sum(par[i][2][0])*x2M + np.sum(par[i][3][0])*x3M)/np.sum(par[i][1][0])
                        x1n = max(list(l[1] for l in c1)+list(m[1] for m in c1))
                        x3n = min(list(l[3] for l in c1)+list(m[3] for m in c1))
                        x2n = -(np.sum(par[i][0][0]) + np.sum(par[i][1][0])*x1n + np.sum(par[i][3][0])*x3n)/np.sum(par[i][2][0])
                        ax.scatter3D(cla2[0], cla2[1], cla2[2], color='b', label=c_2 + " n: " + str(len(c2_p)))
                        ax.set_xlabel("x1")
                        ax.set_ylabel("x2")
                        ax.set_zlabel("x3")
                        ax.plot_trisurf([0, x1l, 0, x1m, x1M, x1n], [x2l, 0, 0, x2m, x2M, x2n], [0, 0, x3l, x3m, x3M, x3n], color='g', alpha=0.5, edgecolor='none')
                        tit = "Classes: " + str(i) + "\n" + "Parameters: " + str(par[i]) + "\n" + "alpha: " + str(alpha) + "\ninitial parameters: " + str(p_mat_rep.tolist())
                        ax.set_title(tit)
                        ax.legend()
                        plt.show()
                    if var == 2:
                        cla1 = [[],[]]
                        cla2 = [[],[]]
                        for n in c1_p:
                            cla1[0].append(n[1])
                            cla1[1].append(n[2])
                        plt.scatter(cla1[0], cla1[1], color='r', label=c_1 + " n: " + str(len(c1_p)))
                        for n in c2_p:
                            cla2[0].append(n[1])
                            cla2[1].append(n[2])
                        x1l = -np.sum(par[i][0][0])/np.sum(par[i][1][0])
                        x2l = -np.sum(par[i][0][0])/np.sum(par[i][2][0])
                        x1m = max(list(l[1] for l in c1)+list(m[1] for m in c1))
                        x2m = -(np.sum(par[i][0][0]) + np.sum(par[i][1][0])*x1m)/np.sum(par[i][2][0])
                        plt.scatter(cla2[0], cla2[1], color='b', label=c_2 + " n: " + str(len(c2_p)))
                        plt.plot([0, x1l, x1m], [x2l, 0, x2m], label="lr_line")
                        tit = "Classes: " + str(i) + "\n" + "Parameters: " + str(par[i]) + "\n" + "alpha: " + str(alpha) + "\ninitial parameters: " + str(p_mat_rep.tolist())
                        plt.title(tit)
                        plt.legend()
                        plt.xlabel("x1")
                        plt.ylabel("x2")
                        plt.show()
                    elif var == 1: 
                        for m in range(var + 1):
                            x1 = []
                            x2 = []
                            x3 = []
                            x4 = []
                            if m > 0:
                                xl = -np.sum(par[i][0][0])/np.sum(par[i][m][0])
                                ep_x1 = 0
                                ep_x2 = 0       
                                for n in c1_p:
                                    x1.append(0)
                                    x2.append(n[m])
                                for z in x2:
                                    if z - xl > 0:
                                        ep_x1 += 1
                                plt.scatter(x1, x2, color='r', label=c_1 + " n: " + str(len(c1_p)) + " o: " + str(ep_x1))
                                for n in c2_p:
                                    x3.append(1)
                                    x4.append(n[m])
                                for z in x4:
                                    if z - xl < 0:
                                        ep_x2 += 1
                                plt.scatter(x3, x4, color='b', label=c_2 + " n: " + str(len(c2_p)) + " o: " + str(ep_x2))
                                plt.plot([-10, 10], [xl, xl], label="Variable: " + str(m))
                                tit = "Classes: " + str(i) + "\n" + "Parameters: " + str(par[i]) + "\n" + "alpha: " + str(alpha) + "\ninitial parameters: " + str(p_mat_rep.tolist())
                                plt.title(tit)
                                plt.legend()
                                plt.show()
                    break
            while True:
                ag = input("try again for " + str(i) + "? y/n \n")
                if ag == 'y' or ag == 'n': break
            if ag == 'n': break
        except KeyboardInterrupt:
            print("alpha:",alpha)
            while True:
                e = input("Exit? y/n \n")
                if e == 'y' or e == 'n': break
            if e == 'y': break
    if e == 'y': break

while True:
    upd = input("Update parameters? y/n \n")
    if upd == 'y' or upd == 'n': break
if upd == 'y':
    add = {}
    with open(a, 'r') as file:
        add = json.load(file)
    add["parameters"] = ad
    with open(a, 'w') as file:
        json.dump(add, file)
print(par)

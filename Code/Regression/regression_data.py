import random
import json

x = input("Enter number of points \n")
xx = input("Enter number of input variables \n")

x = int(x)
xx = int(xx)
xl = []
x_arr = {}
y_arr = []

for i in range(xx):
    x1 = input("Lower limit of " + str(i) + " input variable \n")
    x2 = input("Upper limit of " + str(i) + " input variable \n")
    x1 = int(x1)
    x2 = int(x2)
    xl.append((x1,x2))
    x_arr[i] = []

y1 = input("Enter lower limit of y \n")
y2 = input("Enter upper limit of y \n")
y1 = int(y1)
y2 = int(y2)

for i in range(x):
    xlis = []
    for j in xl:
        x_p = random.uniform(j[0], j[1])
        xlis.append(x_p)
    y_p = random.uniform(y1, y2)
    for i, j in x_arr.items():
        for k in range(len(xlis)):
            if k == i:
                j.append(xlis[k])
                break
    y_arr.append(y_p)

for i in x_arr.values():
    z = random.randint(0, 1)
    if z == 1:
        i.sort()
    else:
        i.sort(reverse=True)
y_arr.sort()

x_coor = []
for i in range(x):
    coor = []
    for j in x_arr.values():
        coor.append(j[i])
    x_coor.append(coor)

dic1 = {}
z = 0
y_arr1 = []
ys = []
print(len(y_arr))
for j, i in enumerate(y_arr):
    if z == 0 or j == len(y_arr) - 1:
        if j == len(y_arr) - 1:
            ys.append(i)
        if x > 90:
            z = random.randint(3,int(x/20))
        else:
            z = random.randint(3, 10)
        if len(ys) > 0:
            random.shuffle(ys)
            for j in ys:
                y_arr1.append(j)
            ys = []
    if z > 0:
        ys.append(i)
        z -= 1
print(len(y_arr1))
for i in range(len(x_coor)):
    dic1[i] = (x_coor[i] , y_arr1[i])

dic = {}
dic["points"] = dic1

j_file = input("Enter dump file name: \n")

with open(j_file + ".json", 'x') as file:
    json.dump(dic, file)

print("Done!")


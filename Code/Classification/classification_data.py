import random
import json

cl = input("Enter the number of classes \n")
cl = int(cl)
x_n = []
x_r = {}

dic1 = {}

x = input("Enter the number of input variables \n")
x = int(x)

for i in range(cl):
    a = input("Enter number of points in class " + str(i) + "\n")
    a = int(a)
    x_n.append(a)
    x_rc = []
    for j in range(x):
        b = input("Enter the lower limit of variable " + str(j) + " for class " + str(i) + "\n")
        b = int(b)
        c = input("Enter the upper limit of variable " + str(j) + " for class " + str(i) + "\n")
        c = int(c)
        x_rc.append([b, c])
    x_r[i] = x_rc
print(x_r)
for n, i in x_r.items():
    points = []
    for j, k in enumerate(x_n):
        if j == n:
            print(i)
            for m in range(k):
                point = []
                for l in i:
                    point.append(random.uniform(l[0], l[1]))
                points.append(point)
    dic1[n] = points

dic = {}
dic["classes"] = dic1

j_file = input("Enter dump file name: \n")

with open(j_file + ".json", 'x') as file:
    json.dump(dic, file)

print("Done!")  

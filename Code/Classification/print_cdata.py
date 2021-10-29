import matplotlib.pyplot as plt
import json

a = input("Enter file name: \n")

if a.endswith(".json") is False:
    a = a + ".json"

dic = {}
with open(a, 'r') as file:
    dic = json.load(file)

color = ['r', 'b', 'g']
for i, j in dic["classes"].items():
    x1 = []
    x2 = []
    for k in j:
        x1.append(k[0])
        x2.append(k[1])
    plt.scatter(x1, x2, c = color[int(i)])
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

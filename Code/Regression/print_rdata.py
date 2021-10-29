import json
import matplotlib.pyplot as plt

a = input("Enter file name: \n")

if a.endswith(".json") is False:
    a = a + ".json"

dic = {}
with open(a, 'r') as file:
    dic = json.load(file)
x = {}
y = []
for i in dic["points"].values():
    for j, k in enumerate(i[0]):
        try:
            x[j] += [k]
        except:
            x[j] = [k]
    y.append(i[1])

for i, j in x.items():
    plt.title(str(i) + " input variable")
    plt.plot(j, y)
    plt.show()

import json

a = input("Enter file name: \n")

if a.endswith(".json") is False:
    a = a + ".json"

dic = {}
with open(a, 'r') as file:
    dic = json.load(file)
while True:
    try:
        p_class = {}
        for j in dic["parameters"]:
            p_value = 0
            for i, j in enumerate(k):
                if i > 0:
                    b = input("Enter the value of " + str(i) + " variable \n")
                    if len(b) == 0: raise KeyboardInterrupt
                    b = float(b)
                    p_value += j*b
                else: p_value += j
            if p_value < 0: p_class[i[0]] += p_class[i[0]].get(0)
            else: p_class[i[0]] += p_class[i[0]].get(0)
    except KeyboardInterrupt:
        ask = input("Type 'exit' to Exit\n")
        if ask == "exit": break
    except ValueError: continue
    except KeyError: 
       print("\nRun linear_regression.py!")
       break

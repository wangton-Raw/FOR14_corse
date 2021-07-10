# Section 3
"""
dic = {}
dic["Carl"] = "B+"
dic["Joe"] = "C"
dic["Sarah"] = "A"
dic["Francine"] = "A"

for key, value in dic.items():
    print(key + ": " + value)
"""

def smooth(values):
    number = values[2] + values[1]

    for i in range(1,len(values)):
        for j in range(len(values)):
            if j-i == 1:
                print(" ")
                print("this is i")
                print(i)
                print(" ")
                print("This is j")
                print(j)
                values[i-1] = (values[i] + values[j])/2
    print(values)




list = [1,2,3,4,5,6,7]

smooth(list)
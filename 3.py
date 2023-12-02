import numpy as np
from matplotlib import pyplot as plt

passDict = dict()
with open("passengers.csv", "r") as file:
    for row in file:
        date, passenger = row.split(",")
        passDict[date] = passenger

passArr = np.array(list(map(int, list(passDict.values())[1:])))
dates = np.array(list(passDict.keys())[1:])

dates1 = [date for date in passDict.keys() if date[:4] in ["1951", "1952", "1953", "1954", "1955"]]
passArr1 = [[date[-2:]] * int(passDict[date]) for date in dates1]
passArr2 = []

for arrList in passArr1:
    passArr2 += arrList

img, axs = plt.subplots(1, 2)
axs[0].plot(dates, passArr)
axs[1].hist(passArr2)
plt.show()

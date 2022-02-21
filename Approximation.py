from cProfile import label
from turtle import color
import numpy as np
import random
import matplotlib.pyplot as plt
import csv
file = open('olympics2021_2.csv')
list = []
csvreader = csv.reader(file)

for row in csvreader:
    first = float(row[0])
    second = float(row[1])
    list.append([first,second])
file.close()

def fourier(x,c):
    fs = [1]
    n=1
    while len(fs) < ncoef:
        fs.append(np.sin(n*x/22.1))
        if len(fs) < ncoef:
            fs.append(np.cos(n*x/22.1))
        n+=1
    return np.dot(np.array(c),np.array(fs))


def getDif(F,c,list):
    diff = 0
    for prediction in  range (len(list)):
        diff+= abs( F(list[prediction][0], c) - 1/70* list[prediction][1])**2
    return diff


nattempts = 10000
successful = 0
attempt = 1
ncoef= 70
P0max= 50
differences = 50
bestt = 50
bestcoeffs=[]

while attempt <= nattempts:
    # print("Attempt {}".format(attempt))
    c = [7]
    while len(c) < ncoef:
        rand = random.uniform(-1,1)
        c.append(rand)
    differences = getDif(fourier,c,list)
    if (differences < bestt) :
        bestcoeffs = c
        successful = attempt
    attempt += 1


c = bestcoeffs
# for i in range (10000):
    # plt.scatter(list[i][0],1/70* list[i][1],color="b")
    # plt.scatter(i/1000, fourier(i/1000,c), color = "r")


print("Attemt {} was successful".format(successful))
f = open("track1.txt", "a")
f.write(str(c))
f.close()


# plt.show()

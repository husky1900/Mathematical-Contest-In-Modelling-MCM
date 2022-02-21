from cProfile import label
from turtle import color
from more_itertools import difference
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
        diff+= abs( F(list[prediction][0], c) - 1/70* list[prediction][1]) 
        print ("fourier: {} , acutal :{}".format(F(list[prediction][0], c), 1/70* list[prediction][1]))
    return diff

# def myfunc(x):
#     return 500

nattempts = 100
successful = 0
attempt = 1
ncoef= 30
P0max= 50
differences = 50
bestt = 50
bestcoeffs=[]

while attempt <= nattempts:
    print("Attempt {}".format(attempt))
    c = [7]
    while len(c) < ncoef:
        rand = random.uniform(-1,1)
        c.append(rand)
    
    # print (fourier(1,c))
    differences = getDif(fourier,c,list)
    # print (differences)
    

    if (differences < bestt) :
        bestcoeffs = c
        print(bestt)
        successful = attempt
    attempt += 1

print(bestcoeffs)
print("Attemt {} was successful".format(successful))
print(bestt)
plt.plot(list[0])

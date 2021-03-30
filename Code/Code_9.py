import numpy as np
import matplotlib.pyplot as plt
import random

def mean(X,Y):
    sum=0
    for i in range(11):
        sum=sum+X[i]*Y[i]
    return sum

X=[2,3,4,5,6,7,8,9,10,11,12]
Y=[1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]
plt.stem(X,Y,linefmt='green',label='Theortical PMF')

X_1=[1,2,3,4,5,6]
X_2=[1,2,3,4,5,6]
print('theortical mean: ',mean(X,Y))


# number of trails
n=1000
Y=[]
c=0
for i in range(n):
    if 2==random.choice(X_1)+random.choice(X_2):
        c=c+1
Y.append(c/n)
c=0
for i in range(n):
    if 3==random.choice(X_1)+random.choice(X_2):
        c=c+1
Y.append(c/n)
c=0
for i in range(n):
    if 4==random.choice(X_1)+random.choice(X_2):
        c=c+1
Y.append(c/n)
c=0
for i in range(n):
    if 5==random.choice(X_1)+random.choice(X_2):
        c=c+1
Y.append(c/n)
c=0
for i in range(n):
    if 6==random.choice(X_1)+random.choice(X_2):
        c=c+1
Y.append(c/n)
c=0
for i in range(n):
    if 7==random.choice(X_1)+random.choice(X_2):
        c=c+1
Y.append(c/n)
c=0
for i in range(n):
    if 8==random.choice(X_1)+random.choice(X_2):
        c=c+1
Y.append(c/n)
c=0
for i in range(n):
    if 9==random.choice(X_1)+random.choice(X_2):
        c=c+1
Y.append(c/n)
c=0
for i in range(n):
    if 10==random.choice(X_1)+random.choice(X_2):
        c=c+1
Y.append(c/n)
c=0
for i in range(n):
    if 11==random.choice(X_1)+random.choice(X_2):
        c=c+1
Y.append(c/n)
c=0
for i in range(n):
    if 12==random.choice(X_1)+random.choice(X_2):
        c=c+1
Y.append(c/n)
print('Experimental mean: ',mean(X,Y))
plt.stem(X,Y,linefmt='red',markerfmt='D',label='Experimental PMF')
plt.xlabel('X')
plt.ylabel('P(X=x)')
plt.title('PMF of X')
plt.legend()
plt.show()  
  


    
    

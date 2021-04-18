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
c=0
Y=[]
 #PMF of X calculation   
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

#PMF calculation of X_1
c=0
y=[]
for i in range(6):
    for j in range(n):
        if i+1==random.choice(X_1):
            c=c+1
    y.append(c/n)
    c=0
Y=[]
for i in range(6):
    sum=0
    for j in range(i+1):
        sum=sum+y[j]
    Y.append(sum)
        
plt.stem(X_1,Y,linefmt='red',markerfmt='D',label='Experimental PMF')
plt.xlabel('X_1')
plt.ylabel('PMF of X_1')
plt.title('PMF of X_1')
plt.legend()
plt.show()
#PMF Calculation of X_2
#PMF of X_1 Calculation
c=0
y=[]
for i in range(6):
    for j in range(n):
        if i+1==random.choice(X_1):
            c=c+1
    y.append(c/n)
    c=0
Y=[]
for i in range(6):
    sum=0
    for j in range(i+1):
        sum=sum+y[j]
    Y.append(sum)
plt.stem(X_1,Y,linefmt='red',markerfmt='D',label='Experimental PMF')
plt.xlabel('X_2')
plt.ylabel('PMF of X_2')
plt.title('PMF of X_2')
plt.legend()
plt.show()

    
    

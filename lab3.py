#sual1
'''a,x=map(int,input().split())
hasil=1
for i in range(x):
    hasil*=a
print(hasil)'''
#sual2
'''a=int(input())
hasil=1
for i in range(1,a+1):
 hasil=hasil*i
print(hasil)'''
#sual3
'''for i in range(0,51,2):
    print(i)'''
#sual4
'''n=int(input())
cem=0
for i in range(1,n+1):
    cem+=i
print(cem)'''
#sual5
'''n=int(input())
x=int(input())
cem=0
for i in range(0,n+1):
 if i%2==0:
     cem+=x**i
 else:
     cem-=x**i
print(cem)'''
#sual6
'''for i in range(100,0,-1):
    print(i)'''
#sual7
'''for i in range(0,11):
    print(i,i**2)'''
#sual8
'''cem=0
hasil=1
for i in range(0,11,2):
    cem+=i
for i in range(1,11,2):
    hasil*=i
print(cem,hasil)'''
#sual9
'''a,b,c=map(int,input().split())
for i in range(a,b+1):
    if i%c==0:
        print(i)'''
#sual10
'''a,b=map(int,input().split())
cut_say=0
tek_say=0
for i in range(a,b+1):
    if i%2==0:
     cut_say+=1
    else:
     tek_say+=1
print(cut_say,tek_say)'''
#sual11
'''from random import *
for i in range(10):
 a=randint(1,100)
 if a%2==0:
    print(a,"cutdur")
 else:
    print(a,"tekdir")'''
#sual12
'''a,b=map(int,input().split())
for i in range(a,b+1):
    print(i,i**2)'''
#sual13
'''import math
a,b=map(int,input().split())
cem=0
for i in range(abs(b)):
    cem+=a
if b<0:
    cem=-cem
print(cem)'''
#sual14
'''n=int(input())
cem=0
j=1
s="3"
for i in range(3,n+1,2):
    cem+=(4/((i-1)*(i)*(i+1)))*j
    s+=str(4)+"/"+str(i-1)+"*"+str(i)+"*"+str(i+1)+"*"+str(j)+" "
    
    j=j*(-1)
print(cem+3)
print(s)'''

#sual15
'''for i in range(10000,99999):
 if i%133==125 and i%134==111:
     print(i)'''
#sual16
'''a,b=map(int,input().split())
ebob=1
for i in range(1,b+1):
        if a%i==0 and b%i==0:
            ebob=i
print(ebob)'''
#sual17
'''a,b=map(int,input().split())
for i in range(a,b+1):
    say=0
    for x in range(1,i+1):
       if i%x==0:
           say+=1
    if say==2:
        print(i)'''
#sual18
'''say=0
for i in range(1,(185//15)+1):
    for j in range(1,(185//17)+1):
        for k in range(1,(185//21)+1):
            if (15*i)+(17*j)+(21*k)==185:
                say+=1
                print(f"15*{i}+17*{j}+21*{k}")
print(say)'''


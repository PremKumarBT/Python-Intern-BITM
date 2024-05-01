'''a=[10,20,30]
print(a)
print(a[0])
print(a[-1])
#print(a[4])
for i in a:
    print(i)
a[1]=-100
print(a)'''

'''b=[10,'prem',250000.75,True,False,True]
print(b)
for i in b:
    print(i,end=' ')
print()

c=[10,'prem',250000.75,True,False,True]
print(c)

print(b == c)

c[1]=(10,20,30)
c[2]=100,200,300
print(c)
print(c[:])
print(c[3:-1])
c[1:3]=(-10,-20,-30,40,50,23,34,54)
print(c)
print(c[:])
'''
'''d=[10,20,30,40,50,60,70,80,90,100]
print(d[:])
print(d[-3:-1])
print(d[3:-1])
print(d[-4:-1])
print(d[0:])
print(d[:-1])
print(d[0:4:2])
print(d[0:7:3])
print(d[0:20:3])'''

'''prem=[]
n=int(input("Enter The Size : "))
for i in range(0,n):
    ele=input("Enter The Elements : ")
    prem.append(ele)
print(prem)'''

'''a=[10,20,30,40,50]
b=[60,70,80,90,100]
c=a+b
print(c)
print(type(c))
print(c*2)
print(max(c))
print(min(c))'''

'''p=[10,25,37,40,57,65]
sum=0
for i in p:
    sum+=i
print(sum)

for i in p:
    if i%10==5:
        print(i)'''
'''a=[10,20,30,40,50,30,50]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)'''

#a=[10,20,30,40,50]
#b=[60,70,80,90,100,20]
'''a=[]
b=[]
c=[]
n=int(input("Enter The Size of a :"))
n1=int(input("Enter The Size of a :"))
for i in range(0,n):
    ele=int(input("Enter The a Elements : "))
    a.append(ele)
for i in range(0,n1):
    ele1=int(input("Enter The b Elements : "))
    b.append(ele1)
for i in a:
    for j in b:
        if i==j:
            print(i)'''
'''a=[]
for i in range(0,5):
    ele=int(input("Enter The Value : "))
    a.append(ele)
'''def prem(yolo):
    if(yolo==1):
        print("Its Not a Prime Number")
    for i in range(1,yolo):
        if(yolo%i==0):
            print("Its not a prime Number")
            break
        else:
            print("Its a prime Number")
            break
for i in a:
    prem(i)'''

'''prem=(10,20,30)
print(prem)
print(type(prem))

a=tuple([10,20,30])
print(a)
print(type(a))
print(len(prem))
#prem[0]=500'''
'''
'''a=[]
for i in range(0,5):
    ele=int(input("Enter The Value : "))
    a.append(ele)
a=tuple(a)
print(a)
print(type(a))
print(max(a))
print(min(a))

def prem(num):
    flag = False
    if num == 1:
        print(num, "is Not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            print(num, "is Not a prime number")
        else:
            print(num, "is a prime number")
for i in a:
    prem(i)

def pre(n):
    if (n%400==0) and (n%4==0):
        print(n,"is a Leap Year")
    elif(n%4==0) and (n%100!=0):
        print(n,"is a Leap Year")
    else:
        print(n,"is not a Leap Year")
for i in a:
    pre(i)'''
'''#List Conprention Method
x,y=[int(x) for x in input().split()]
print(x)
print(y)
#map Method
x,y=map(int,input().split())
print(x)
print(y)

numbers=[10,20,30,40,50]
double_num=[num*2 for num in numbers]
print(double_num)
print(type(double_num))'''


set4={}
print(type(set4))
print()

matrix=[[j for j in range(5)] for i in range(3)]
print(matrix)

'''
'''print(5//8)
print(-4//5)
print(25<<5)
a=5
t=a<20 or a>2 and a==2
print(t)
print(type(t))
b=[10,20,30]
print(5 in b)
print()
print(a is 5)'''

'''if(5>10):
   print("Yes")
else:
    print("No")
    print("Yes")'''

'''email=input("Enter The Email : ")
Pass=int(input("Enter The Pass : "))
uemail="prem@gmail.com"
upass=123456
otp=1234
if(email == uemail):
    if(Pass == upass):
        print("Login Success")        
        print("OTP is sent to Number")
        OTP=int(input("Enter The OTP : "))
        if(OTP==otp):
            print("Transaction Successfull")
        else:
            print("Transaction was UnSuccessfull Due to Incorrect OTP")
    else:
        print("Password is Incorrect")
else:
    print("Email is Incorrect")'''

'''n1=int(input("Enter The N1 : "))
n2=int(input("Enter The N2 : "))
print('N1 is Greater' if n1>n2 else "Both r Equal" if n1==n2 else "N2 is Greater")'''

'''a=10
b=20
c=30
d=40
e=50
print('a is Greater' if (a>b and a>c and a>d and a>e)else ("b is greater" if(b>c and b>d and b>e)else ("c is Greater"if(c>d and c>e)else ("d is greater"if(d>e)else "e is Greater"))))

n=int(input("Enter The Number Of Lemons : "))
print(("Extra Lemons Left ",n-21) if n>21 else (("Still Lemons To Be Buyed ",21-n) if n<21 else ( "Sufficent Lemons" if(n==21) else "Invalid")))

print(chr(3242)+chr(3271)+chr(3246)+chr(32)+chr(3221)+chr(3265)+chr(3246)+chr(3262)+chr(3248))'''

'''for a in range(ord('a'),ord('z')):
    print(chr(a),end=' ')
    print(ord(chr(a)),end=' ')
print()

for i in range(1,6):
    for j in range(1,6):
        print('*',end='')
    print()
    
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()
    
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()
    
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()
    
for i in range(ord('a'),ord('z')):
    for j in range(ord('a'),i+1):
        print(chr(j),end=' ')
    print()

for i in range(0,1):
    print(i,end=' ')'''
    
'''i=0.0
while i<=1:
    print(i,end=' ')
    i=i+0.1'''
    
#for i in range(0,11):
#    print(i/10,end=' ')

'''a=-5
print(abs(a))
print(pow(2,3))

import math
print(math.sqrt(25))
print(math.ceil(-5.1))
print()

def prem():
    print("Hello World")
prem()'''

#def prem(yoo):
#    print(yoo)
#prem('Y88')

'''def prem(yolo):
    if(yolo==1):
        print("Its Not a Prime Number")
    for i in range(1,yolo):
        if(yolo%i==0):
            print("Its a prime Number")
            break
        else:
            print("Its not a prime Number")
            break
prem(1)'''

name = "PREMK"
for i in range(len(name)):
    for j in range(len(name)):
        if i == j or i + j == len(name) - 1 :
            print(name[j], end='')
        else:
            print(' ', end='')
    print()
        

for i in range(len(name)):
    for j in range(len(name)):
        if i == j and i<=2 or (i + j == len(name) + 1 and i<=2) or (j==3 and i>2):
            print(name[i], end='')
            if i== 0 :
                print("    ",name[i],end='')
            if i==1 :
                print("  ",name[i],end='')
        else:
            print(' ', end='')
    print()


for i in range(len(name)):
    for j in range(len(name)):
        if i == 0 or i == len(name) - 1 or i + j == len(name) - 1:
            print(name[j], end='')
        else:
            print(' ', end='')
    print()

name = "PREMK"
n=len(name)

for i in range(n):
    for j in range(n*2):
        if i == j or j == n*2-1-i :
            print(name[i], end='')
        else:
            print(' ', end='')
    print()


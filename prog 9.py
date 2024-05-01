'''n=input("Enter The Binary Number : ").split(',')
for i in range(0,len(n)):
    n[i]=int(n[i],2)
for j in n:
    if j%5==0:
        print(j,bin(j))
'''
'''
a=input("Enter The String: ")
b=0
c=0
for i in a:
    if i.isdigit()==True:
        b+=1
    if i.isalpha()==True:
        c+=1
print("Number Of Digits : ",b)
print("Number Of Alphabet : ",c)
'''
'''
#$#@
a=input("Enter The Password : ")
c=0
for i in range(0,len(a)):
    if ((ord(a[i])>=ord('a')) and (ord(a[i])<=ord('z'))):
        c+=1
    if (ord(a[i])>=ord('A') and ord(a[i])<=ord('Z')):
        c+=1
    if (ord(a[i])>=ord('0') and ord(a[i])<=ord('9')):
        c+=1
    if ord(a[i])==ord('&') or ord(a[i])==ord('$') or ord(a[i])==ord('#'):
        c+=1

print("size = ",c)
if(c>=7 and c<=16):
    if(c==len(a)):
        print("Password Created Successfully")
    else:
        print("UnSuccessfull")
elif c<7:
    print("PassWord Is Weak")
elif c>16:
    print("PassWord Length Reached Max")
'''


'''    
l1=['January','March','May','July','August','October','December']
l2=['April','June','September','November']
l3=['February']
s=input("Enter The Month : ")
if l1.count(s)>=1:
    print(s,"Has 31 Days")
if l2.count(s)>=1:
    print(s,"Has 30 Days")
if l3.count(s)>=1:
    print(s,"Has 28/29 Days")
if (l1.count(s)>=1) or (l1.count(s)>=1) or (l1.count(s)>=1):
    pass
else:
    print("Invalid")
'''
'''
#bitm college's located in ballari? Is't right!!!
s=input("Enter The String : ")
ss=[]
for i in range(0,len(s)):
    ss.append(" ")
print(len(s))
print(len(ss))
for i in range(0,len(s)):
    if s[i].isalpha()==True:
        ss[len(s)-i]=s[i]
    #if ord(s[i])==ord('\'') or ord(s[i])==ord('?') or ord(s[i])==ord('!') or ord(s[i])==ord('*') or ord(s[i])==ord('@') or ord(s[i])==ord('$')
    if ord(s[i])>=ord(' ') and ord(s[i])<=ord('@'):
        ss[i]=s[i]
for i in ss:
    print(i,end='')
'''
'''
#bitm college's located in ballari? Is't right!!!
s=input("Enter The String : ")
ss=[]
for i in range(0,len(s)+1):
    ss.append(s[i])
    if s[len(s)-i-1].isalpha()==True:
        t=s[len(s)-i-1]
i=0
while i<=len(s):
    #ss.append(s[i])
    if s[len(s)-i-1].isalpha()==True:
        t=s[len(s)-i-1]
    i+=1
print(t)
print(len(s))
print(len(ss))
print(ss)
'''

#bitm college's located in ballari? Is't right!!!
s=input("Enter The String : ")
ss=[i for i in s if (i.isalpha()==True)]
ss=ss[::-1]
y=0
t=[]
for i in range(0,len(s)):
    if s[i].isalpha()==True:
        t.append(ss[y])
        y+=1
    if ord(s[i])>=ord(' ') and ord(s[i])<=ord('@'):
        t.append(s[i])
for i in t:
    print(i,end='')

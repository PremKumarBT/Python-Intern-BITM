# Function return Value By Default is String
'''
def prem():
    return 'Prem'
test={'fname': prem,'age':50,'address':'Ballari'}
print('Org Dict : '+str(test))  # print('Org Dict : ',test)
res=test['fname']()
print('Yolo '+str(res))  # print('Yolo ',res)
'''
'''
def prem(a,b):
    print("Res : ",a+b)
test={'fname':prem}
test['fname'](10,20)
'''
'''
for roll in range(1,101):
    if roll == 25 or roll == 50 or roll == 75:
        continue
    else:
        print('allowed to Symposium',roll)
'''
'''
a,b=10,20
a,b=b,a
print(a,b)
'''
'''
email=input("Enter The Email : ")
Pass=int(input("Enter The Pass : "))
uemail=["prem@gmail.com",'bala@gmail.com','yolo@gmail.com']
upass=123456
otp=1234
if (uemail.count(email)>=1):
    if(Pass == upass):
        print("Login Success")        
        print("OTP is sent to Number")
        OTP=int(input("Enter The OTP : "))
        if(OTP==otp):
            print("Transaction Successfull")

            def withdraw(account, amount):
                if amount > account['balance']:
                    print("Insufficient funds!")
                else:
                    account['balance'] -= amount
                    account['transactions'].append(f"Withdrawal: ${amount}")
                    print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

            def deposit(account, amount):
                account['balance'] += amount
                account['transactions'].append(f"Deposit: ${amount}")
                print(f"Deposit successful. Remaining balance: ${account['balance']}")

            def get_balance(account):
                return account['balance']

            def get_transaction_history(account):
                return account['transactions']
            account = {
                'balance': 1000,
                'transactions': []
            }

            choices = {
                '1': deposit,
                '2': withdraw,
                '3': get_balance,
                '4': get_transaction_history
            }
           # count=0
            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. Exit")

                choice = input("Enter your choice: ")
                if choice == '5':
                    print("Exiting program.")
                    break

                if choice in choices:
                    if choice == '1' or choice == '2':
                       # if count==5:
                        #    print("You Have Reached The Maximum Transaction")
                         #   break
                        amount = float(input("Enter amount: "))
                       # count+=1
                        choices[choice](account, amount)
                        #print('Count : ',count)
                    else:
                        print(choices[choice](account))
            else:
                print("Invalid choice. Please try again.")    
        
        else:
            print("Transaction was UnSuccessfull Due to Incorrect OTP")
    else:
        print("Password is Incorrect")
else:
    print("Email is Incorrect")
'''
'''
def prem(num):
    r = 0
    res = 0
    if num == 1:
        print(num, "is Not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) != 0:
                #print(num,"is prime Number")
                temp=int(str(num)[::-1])
                for i in range(2, temp):
                        if (temp % i) != 0:
                            print(num,"is Magical Prime Number")
                            break
                break
            else:
                print(num,"is Not a prime number")
                break        
ele=int(input("Enter The Value : "))
prem(ele)
'''

d=int(input("Enter The Date : ")) 
if(d>0 and d<=31):
    m=int(input("Enter The Month : "))
    if(m>0 and m<=12):
        if(((d<=31) and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12)) or((d<=30) and(m==4 or m== 6 or m==9 or m==11)) or ((d==29) and (m==2))):
            y=int(input("Enter The Year : "))
            if (y>1900 and y<9999):
                c=y//100
                D=y%100
                temp=m
                if m>2:
                    m-=2
                else:
                    m+=1
                if((d==29) and (temp==2)):
                    if (y % 400 == 0) and (y % 100 == 0):
                        f=d+((13*m-1)/5)+D+D/4+(c/4)-2*c
                        fres=int(f%7)
                        day={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
                        print(day[fres+1])
                    elif (y % 4 ==0) and (y % 100 != 0):
                        f=d+((13*m-1)/5)+D+D/4+(c/4)-2*c
                        fres=int(f%7)
                        day={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
                        print(day[fres+1])
                    else:
                        print("Its not a leap year")
                else:
                    f=d+((13*m-1)/5)+D+D/4+(c/4)-2*c
                    fres=int(f%7)
                    day={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
                    print(day[fres])
            else:
                print("Incorrect Year")
        else:
            print("Invalid Date")
    else:
        print("Incorrect Month")
else:
    print("Incorrect Date")
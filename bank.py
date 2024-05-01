import os                    
class Banking:
    def withdraw(self,account, amount):
        if email=='prem@gmail.com':
            if amount > account['balance'][0]:
                print("Insufficient funds!")
            else:
                account['balance'][0] -= amount
                account['transactions'].append(f"Withdrawal: ${amount}")
                print(f"Withdrawal successful. Remaining balance: ${account['balance'][0]}")
                file=open('transactions1.txt','a')
                file.close()
        if email=='balaji@gmail.com':
            if amount > account['balance'][1]:
                print("Insufficient funds!")
            else:
                account['balance'][1] -= amount
                account['transactions'].append(f"Withdrawal: ${amount}")
                print(f"Withdrawal successful. Remaining balance: ${account['balance'][1]}")
                file=open('transactions1.txt','a')
                file.close()
        if email=='royal@gmail.com':
            if amount > account['balance'][2]:
                print("Insufficient funds!")
            else:
                account['balance'][2] -= amount
                account['transactions'].append(f"Withdrawal: ${amount}")
                print(f"Withdrawal successful. Remaining balance: ${account['balance'][2]}")
                file=open('transactions1.txt','a')
                file.close()
            
    def deposit(self,account, amount):
        if email=='prem@gmail.com':
            account['balance'][0] += amount
            account['transactions'].append(f"Deposit: ${amount}")
            print(f"Deposit successful. Remaining balance: ${account['balance'][0]}")
            file=open('transactions1.txt','a')
            file.close()
        if email=='balaji@gmail.com':
            account['balance'][1] += amount
            account['transactions'].append(f"Deposit: ${amount}")
            print(f"Deposit successful. Remaining balance: ${account['balance'][1]}")
            file=open('transactions1.txt','a')
            file.close()
        if email=='royal@gmail.com':
            account['balance'][2] += amount
            account['transactions'].append(f"Deposit: ${amount}")
            print(f"Deposit successful. Remaining balance: ${account['balance'][2]}")
            file=open('transactions1.txt','a')
            file.close()
            
    def get_balance(self,account):
        if email=='prem@gmail.com':
            return account['balance'][0]
        if email=='balaji@gmail.com':
            return account['balance'][1]
        if email=='royal@gmail.com':
            return account['balance'][2]
    def get_transaction_history(self,account):
                temp=str(account['transactions'])
                file=open('transactions1.txt','r+')
                if email=='prem@gmail.com':
                    file.seek(1)
                    file.write("Prem\'s Account : ")
                    file.seek(1026)
                    file.write(temp)
                if email=='balaji@gmail.com':
                    file.seek(7176)
                    file.write("Bala\'s Account : ")
                    file.seek(8200)
                    file.write(temp)
                if email=='royal@gmail.com':
                    file.seek(14350)
                    file.write("Royal\'s Account : ")
                    file.seek(15375)
                    file.write(temp)
                file.close()
                return account['transactions']
                
account = {
            'balance':[1000,1000,1000],
            'transactions': []
          }
email=input("Enter The Email : ")
Pass=input("Enter The Pass : ")
uemail=["prem@gmail.com",'balaji@gmail.com','royal@gmail.com']
upass=['123456','098765','112233']
otp=1234
if (uemail.count(email)>=1):
    if(upass.count(Pass)>=1):
        print("Login Success")        
        print("OTP is sent to Number")
        OTP=int(input("Enter The OTP : "))
        if(OTP==otp):
            print("Transaction Successfull")
            file=open('transactions1.txt','a')
            file.close()
            b=Banking()
            choices = {
                '1': b.deposit,
                '2': b.withdraw,
                '3': b.get_balance,
                '4': b.get_transaction_history
            }
            cemail=email
            count=0
            temp=0
            while True:
                print("\nCurrent User ID : ",email)
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. All Transactions History")
                #print("5. Read All Transaction Done From File")
                print("5. Delete All Transactions and File")
                print("6. Switch User Login")
                print("7. Exit")

                choice = input("Enter your choice: ")
                if choice == '6':
                    email=input("Enter The Email : ") 
                    Pass=input("Enter The Pass : ")
                    if(uemail.count(email)>=1):
                        if(upass.count(Pass)>=1):
                            print("Login Success")        
                            print("OTP is sent to Number")
                            OTP=int(input("Enter The OTP : "))
                            if(OTP==otp):
                                print("Transaction Successfull")
                                count=0
                            else:
                                print("Transaction was UnSuccessfull Due to Incorrect OTP")
                                email=cemail
                                continue
                        else:
                            print("Password is Incorrect")
                            email=cemail
                            continue
                    else:
                        print("Email is Incorrect")
                        email=cemail
                        continue
                    
                if choice == '7':
                    print("Exiting program.")
                    break
                if choice == '5':
                    os.remove("transactions1.txt")
                    print("File Deleted !!")
                '''if choice =='5':
                    #yoo=str(account['transactions'])
                    file=open('transactions1.txt','r')
                    yoo=file.read()
                    print(yoo)
                    file.close()'''
                if choice in choices:
                    if choice == '1' or choice == '2':
                        if count==5:
                            print("You Have Reached The Maximum Transaction")
                            break
                        amount = float(input("Enter amount: "))
                        if choice=='2':
                            temp=amount
                            if temp>10000:
                                print("Withdraw Amount Limit Reached > 10000.0")
                                break
                        count+=1
                        choices[choice](account, amount)
                        print('Count : ',count)
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




'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class professor(person):
    def isprofessor(self):
        return f"{self.name} is a Professor"
sir=professor("Prem",30)
#print(sir)
print(sir.isprofessor())
'''

class a:
     def prem(self,num):
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
                            return "is Magical Prime Number"
                            break
                        else:
                            return "is Not a Magical Prime Number"
                    break
                else:
                    return "is Not a prime number"
                    break        
class b(a):
    def yoo(self,n):
        if (n==0) or (n==1) or (n==9):
            return "is a Neon Number"
        else:
            return "is Not a Neon Number"

class c(a):
    def print_x(self,name):
        for i in range(len(name)):
            for j in range(len(name)):
                if i == j or i + j == len(name) - 1:
                    print(name[j], end='')
                else:
                    print(' ', end='')
            print()
        return ' '
class d(b,c):
    def yolo(self,name):
        return str(name)[::-1]
class BankAccount(a):
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions = []

    def withdraw(shetty, amount):
        if amount > shetty.balance:
            print("Insufficient funds!")
        else:
            shetty.balance -= amount
            shetty.transactions.append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${shetty.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        print(f"Deposit successful. Remaining balance: ${self.balance}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

D=d()
ele=int(input("Enter The Value for Magical No : "))
#A=a()
print(D.prem(ele))
ele1=int(input("Enter The Value for Neon No : "))
#B=b()
print(D.yoo(ele1))
ele2=input("Enter The Name for X Pattern : ")
#C=c()
print(D.print_x(ele2))
ele3=input("Enter The String To Reverse : ")

print(D.yolo(ele3))

f=0
account = BankAccount(1000)
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
    if choice == '3':
        print("Balance : ", account.get_balance())
    if choice == '1': 
        e1=int(input("Enter The Amount : "))
        if f>=5:
            print("Maximum Number Of Transactions Reached")
            break
        account.deposit(e1)
        f+=1
        print("Count : ",f)
    if choice =='2':
        e2=int(input("Enter The Amount : "))
        if e2>10000:
            print("Amount Transaction Should Be < $10000")
            break
        if f>=5:
            print("Maximum Number Of Transactions Reached")
            break
        account.withdraw(e2)
        f+=1
        print("Count : ",f)
        
    if choice == '4':
        print("Transaction History:", account.get_transaction_history())

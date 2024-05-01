'''Everything is in Book '''

# Dictnoary
'''dict={}
print(dict)

emp={"Name":"Prem","Age":35,"Salary":30000}
print(emp)'''
    
'''yoo="Prem"
vowel='aeiou'
prem=[char for char in yoo if char in vowel]
prem1=[char for char in yoo if char not in vowel]
print(prem)
print(prem1)'''

'''name="Prem Kumar"
print(name[::-3])
print()'''

'''fileptr=open("test\prem.txt",'r')
if fileptr:
    print("File is Opened Successfully")'''
    
#print(dir(locals()['__builtins__']))

emp=dict([('Name',"Prem"),("Age",70),('DOB','2004-12-12'),('Aadhar',493831301712),('Debit Card',5272213473652398),('Phone No',8123546706),('PinCode',583104)])
print(emp,sep='#')
print('Name # %s' %emp['Name'])
print('Age # %d' %emp['Age'])
print('DOB # %s' %emp['DOB'])
print('Aadhar No # %d' %emp['Aadhar'])
print('Debit Card # %d' %emp['Debit Card'])
print('Phone No # %d' %emp['Phone No'])
print('PinCode # %d' %emp['PinCode'])
for i in emp.values():
    print(i,end=' ')
print()
for i in emp.items():
    print(i,end='')

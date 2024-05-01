'''
str1=input('Enter The String : ')
list1=[]
list1=str1.split()
word=[list1.count(p) for p in list1]
print(word)
#print(dict(zip(list1,wordfreq)))

'''
'''
ss=input("Enter The String : ")
t=[]
t=ss.split()
for i in range(0,100):
    if t[i].find('s')>=0:
        e=t[i]
        print(e)
'''
'''
s=input("Enter The String")
for i in m.split():
    if 's' in i.lower():
        print(i)        

s=input("Enter The string : ")
res=[char for char in s.split() if 's' in s]
print(res)


mydict ={'balaji':10,'mango':20,'bananna':30,'prem':40}
for key, value in mydict.items():
    if key[0].lower() == 'b':
        print(f"The Value of '{key}' is {value}")
    else:
        print("Key is Not Present!")
'''
'''
l=[int(l) for l in input("Enter The List : ").split()]
e=0
o=0
temp1,temp2,temp3=0,0,0

for i in l:
    if i<=0:
        temp1+=i
    elif (i%2)==0:
            if e<i:
                e=i
            temp2+=i
    elif (i%2)!=0:
            if o<i:
                o=i
            temp3+=i
print("Sum of Negative Numbers : ",temp1)
print("Sum of Even Numbers : ",temp2)
print("Sum of Odd Numbers : ",temp3)
print("Largest Even No :",e)

l=int(input("Enter The List : ").split())
temp1=[num+= for num in l]
print("Largest odd No :",o)'''

# Python Program to Create and Display Linked List

# Create a node
'''
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       
#create a head node and set as null. Here dont be use null. Be use None 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
# Append the data in last
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
 
a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end = '')
a_llist.display()
'''
  # Python Program to Check if Two Lists are Equal

'''
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
 
def is_equal(llist1, llist2):
        current1 = llist1.head
        current2 = llist2.head
        while (current1 and current2):
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next
        if current1 is None and current2 is None:
            return True
        else:
            return False
 
 
llist1 = LinkedList()
llist2 = LinkedList()
 
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    llist1.append(int(data))
 
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    llist2.append(int(data))
 
if is_equal(llist1, llist2):
    print('The two linked lists are the same.')
else:
    print('The two linked list are not the same.', end = '')
''' 
# Python Program to Find Intersection and Union of Two Linked Lists

'''
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
 
    def duplicate(self):
        copy = LinkedList()
        current = self.head
        while current:
            node = Node(current.data)
            copy.insert_at_end(node)
            current = current.next
        return copy
 
    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
 
    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
 
 
def remove_duplicates(llist):
    current1 = llist.head
    while current1:
        current2 = current1.next
        data = current1.data
        while current2:
            temp = current2
            current2 = current2.next
            if temp.data == data:
                llist.remove(temp)
        current1 = current1.next
 
 
def find_union(llist1, llist2):
    if llist1.head is None:
        union = llist2.duplicate()
        remove_duplicates(union)
        return union
    if llist2.head is None:
        union = llist1.duplicate()
        remove_duplicates(union)
        return union
 
    union = llist1.duplicate()
    last_node = union.head
    while last_node.next is not None:
        last_node = last_node.next
    llist2_copy = llist2.duplicate()
    last_node.next = llist2_copy.head
    remove_duplicates(union)
 
    return union
 
 
def find_intersection(llist1, llist2):
    if (llist1.head is None or llist2.head is None):
        return LinkedList()
 
    intersection = LinkedList()
    current1 = llist1.head
    while current1:
        current2 = llist2.head
        data = current1.data
        while current2:
            if current2.data == data:
                node = Node(data)
                intersection.insert_at_end(node)
                break
            current2 = current2.next
        current1 = current1.next
    remove_duplicates(intersection)
 
    return intersection
 
 
a_llist1 = LinkedList()
a_llist2 = LinkedList()
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    node = Node(int(data))
    a_llist1.insert_at_end(node)
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    node = Node(int(data))
    a_llist2.insert_at_end(node)
 
union = find_union(a_llist1, a_llist2)
intersection = find_intersection(a_llist1, a_llist2)
 
print('Their union: ')
union.display()
print()
print('Their intersection: ')
intersection.display()
print()

'''

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
 
def is_equal(llist1, llist2):
        current1 = llist1.head
        current2 = llist2.head
        while (current1 and current2):
            if current1.data <= current2.data:
                return False
            else:
                return True
            current1 = current1.next
            current2 = current2.next
        if current1 is None and current2 is None:
            return False
        else:
            return False
 
 
llist1 = LinkedList()
llist2 = LinkedList()
 
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    llist1.append(int(data))
 
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    llist2.append(int(data))
 
if is_equal(llist1, llist2):
    print('True')
else:
    print('False', end = '')


class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
        
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
 
a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
l=[]
l1=[]
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
    if data%5==0 and data!=0:
        l.append(data)
        l.sort(reverse=True)
    elif data%5!=0 or data==0:
        l1.append(data)
        l1.sort(reverse=True)

print(l+l1)
#print('The linked list: ', end = '')
a_llist.display()

import os
class stadium:
    def __init__(self):
        choices = {
                '1': self.create,
                '2': self.read,
                '3': self.update,
                '4': self.delete,
                '5': self.conduct_safety_audits,
                '6': self.manage_safety_improvements
              }
        while True:
            file=open('stadium.txt','a')
            file.close()
            print("\n1. Creation of Safety Records(Only Initailise)")
            print("2. Reading The Safety Records")
            print("3. Updating The Safety Records")
            print("4. Deletion of Safety Record")
            print("5. Conduct_Safety_Audits")
            print("6. Manage_Safety_Improvements")
            print("7. Delete All The Safety Records in File")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice=='8':
                print("Exiting The Program")
                break
            if choice=='7':
                os.remove("stadium.txt")
                print("File Deleted !!")
            if choice=='1':
                choices[choice]()
            if choice=='2':
                choices[choice]()
                file=open('stadium.txt','r+')
                for i in range(len(mode)):
                    file.write("Record ID : "+str(stadium_id[i]))
                    file.write("\nName : "+name[i])
                    file.write("\nMode :"+mode[i])
                    file.write(f"\nSafety Report of {name[i]}")
                    file.write("\nSafety Measure 1 : "+improvement_data[i][0])
                    file.write("\nSafety Measure 2 : "+improvement_data[i][1])
                    file.write("\nSafety Measure 3 : "+improvement_data[i][2])
                    if len(improvement_data[i])>3:
                        file.write("\nSafety Measure improved : "+str(improvement_data[i][3]) )
                    if improvement_data[i][2]!='-':
                        file.write("\nAll Safety Audits Conducted Successfully... ")
                    else:
                        file.write("\nSafety Audits Was Deleted Successfully... ")
                    file.write("\n-----------------------------------------------------------\n")
            if choice=='3':
                self.e=int(input('Enter The Stadium ID : '))
                if self.e in stadium_id:
                    print("Stadium ID Already Exist")
                else:
                    choices[choice]()
            if choice=='4':
                self.d=int(input("Enter The Stadium ID : "))
                if self.d not in stadium_id:
                    print("Stadium ID Doesn't Exist")
                else:
                    choices[choice]()
            if choice=='5':
                self.y=int(input("Enter The Stadium ID : "))
                if self.y not in stadium_id:
                    print("Create The Stadium ID From Choice 3")
                else:
                    choices[choice]()
            if choice=='6':
                self.z=int(input("Enter The Stadium ID : "))
                if self.z not in stadium_id:
                    print("Create The Stadium ID From Choice 3")
                else:
                    choices[choice]()
    def create(self):
        t=[1,2,3,4,5]
        stadium_id.extend(t)
        r=['Fire Safety','Emergency Evacuation','Venue Operation Centre','Medical','Poice Facilities']
        name.extend(r)
        p=[['Detection & Warning','Fire Fighting Equipment','Contact Near Fire Station'],['Emergency Exit','Evacuation of Disable People','Exit Routes That Provide a Minimum of 30 Minutes of Protection From Fire'],['Fire Alarm Control Panel','Electronic Video Screen Control System','Closed-circuit Television (CCTV)'],['SPECTATOR MEDICAL FACILITIES','FIRST-AID/MEDICAL ROOMS','AMBULANCE PROVISION'],['Sanitary Facilities','CCTV Monitoring','Access to Medical Facilities']]
        improvement_data.extend(p)
        q=["MatchDay Mode","MatchDay Mode","MatchDay Mode","MatchDay Mode","MatchDay Mode"]
        mode.extend(q)
        print("Created The Safety Records of Default")
    def read(self):
        print("Mode\t Stadium_id\t Name ")
        for i in range(len(name)):
            print(f"{mode[i]}\t {stadium_id[i]}\t {name[i]} ")
    def update(self):
        stadium_id.append(self.e)
        n=input("Enter The Name : ")
        name.append(n)
        x=input("Enter The Safety Measure 1 : ")
        y=input("Enter The Safety Measure 2 : ")
        z=input("Enter The Safety Measure 3 : ")
        print("Your Safty Records Has Been Confirmed")
        zz=input("Enter The Match or Non-Match Mode? : ")
        mode.append(zz)
        l=[]
        l.append(x)
        l.append(y)
        l.append(z)
        improvement_data.append(l)
        print("Safety Records List Updated")
    def delete(self):
        for i in range(len(name)):
            if self.d == stadium_id[i]:
                stadium_id[i]=None
                name[i]='-'
                improvement_data[i]=['-','-','-']
                mode[i]='-'
                print("Removed Safety Record Successfully")
    def conduct_safety_audits(self):
        for i in range(len(mode)):
            if self.y==stadium_id[i]:
                print("Name of Safety Audits : ",name[i])
                print(f"The Safety Measure 1 of {name[i]} : ",improvement_data[i][0])
                print(f"The Safety Measure 2 of {name[i]} : ",improvement_data[i][1])
                print(f"The Safety Measure 3 of {name[i]} : ",improvement_data[i][2])
                print(len(improvement_data[i]))
                if len(improvement_data[i])>3:
                    print(f"The Safety Measure 4 of {name[i]} : ",improvement_data[i][3])
                print("\nAll Safety Audits Conducted Successfully... ")
    def manage_safety_improvements(self):
        for i in range(len(mode)):
            if self.z==stadium_id[i]:
                s=input("Enter The Safety Measure To Be Added : ")
                improvement_data[i].append(s)
                print("Safety Measure Updated Successfully...")

stadium_id=[]
name=[]
improvement_data=[]
mode=[]
if __name__ == '__main__':
    c=stadium()


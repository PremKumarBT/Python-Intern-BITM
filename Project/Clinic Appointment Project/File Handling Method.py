import os
class clinic:
    def __init__(self):
        self.i=15
        choices = {
                '1': self.create,
                '2': self.read,
                '3': self.update,
                '4': self.delete,
                '5': self.manage_medical_appointments,
                '6': self.track_health_progress
              }
        while True:
            file=open('clinictest.txt','a')
            file.close()
            print("\n1. Creation of Appointment(Only Initailise)")
            print("2. Reading The Appointment List")
            print("3. Updating The Appointment List")
            print("4. Deletion of Appointment")
            print("5. Manage Medical Appointments")
            print("6. Track Health Progress")
            print("7. Delete All The Appointments and File")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice=='8':
                print("Exiting The Program")
                break
            if choice=='7':
                os.remove("clinictest.txt")
                print("File Deleted !!")
            if choice=='1':
                choices[choice]()
            if choice=='2':
                choices[choice]()
                file=open('clinictest.txt','r+')
                for i in range(len(appoint)):
                    file.write("Athlete ID : "+str(athlete_id[i]))
                    file.write("\nName : "+name[i])
                    file.write("\nAppoint :"+str(appoint[i]))
                    file.write(f"\nProgress Report of {name[i]}")
                    file.write("\nHealth : "+str(progress_data[i][0]))
                    file.write("\nHeartRate : "+str(progress_data[i][1]))
                    file.write("\nStamina : "+str(progress_data[i][2]))
                    if progress_data[i][2]!='-':
                        file.write("\nRecovery Rate : "+str((progress_data[i][0]+progress_data[i][1]+progress_data[i][2])//3))
                    file.write("\n------------------------\n")
            if choice=='3':
                self.e=int(input('Enter The Athlete ID : '))
                if self.e in athlete_id:
                    print("Athlete ID Already Exist")
                else:
                    choices[choice]()
            if choice=='4':
                self.d=int(input("Enter The Athlete ID : "))
                if self.d not in athlete_id:
                    print("Athlete ID Doesn't Exist")
                else:
                    choices[choice]()
            if choice=='5':
                self.y=int(input("Enter The Athlete ID : "))
                if self.y not in athlete_id:
                    print("Create The Athlete ID From Choice 3")
                else:
                    choices[choice]()
            if choice=='6':
                self.z=int(input("Enter The Athlete ID : "))
                if self.z not in athlete_id:
                    print("Create The Athlete ID From Choice 3")
                else:
                    choices[choice]()
    def create(self):
        t=[1000,1001,1002,1003,1004]
        athlete_id.extend(t)
        r=['Raj','Tarun','Shiva','Virat','Joe']
        name.extend(r)
        p=[[98,78,89],[97,81,87],[100,75,92],[87,85,84],[95,81,83]]
        progress_data.extend(p)
        q=["2024-04-10","2024-04-11","2024-04-12","2024-04-13","2024-04-14"]
        appoint.extend(q)
        print("Created The Appointments of Default")
    def read(self):
        print("Appointment\t Athlete_id\t Name ")
        for i in range(len(name)):
            print(f"{appoint[i]}\t {athlete_id[i]}\t\t {name[i]} ")
        
    def update(self):
        athlete_id.append(self.e)
        n=input("Enter The Name : ")
        name.append(n)
        x=int(input("Enter The Health : "))
        y=float(input("Enter The HeartRate : "))
        z=float(input("Enter The Stamina : "))
        print("Your Appointment Has Been Confirmed")
        zz='2024-04-'+str(self.i)
        appoint.append(zz)
        l=[]
        l.append(x)
        l.append(y)
        l.append(z)
        progress_data.append(l)
        self.i+=1
        print("Appointment List Updated")
    def delete(self):
        for i in range(len(name)):
            if self.d == athlete_id[i]:
                athlete_id[i]=None
                name[i]='-'
                progress_data[i]=['-','-','-']
                print("Removed Appointment Successfully")
    def manage_medical_appointments(self):
        o=int(input("Enter The Date of Appointment To Adjust : "))
        for i in range(len(appoint)):
            if ("2024-04-"+str(o))==appoint[i]:
                athlete_id[i],athlete_id[-1],name[i],name[-1],progress_data[i],progress_data[-1]=athlete_id[-1],athlete_id[i],name[-1],name[i],progress_data[-1],progress_data[i]
            elif o>self.i and ("2024-04-"+str(o))!=appoint[i]:
                appoint[-1]="2024-04-"+str(o)
    def track_health_progress(self):
        for i in range(len(appoint)):
            if self.z==athlete_id[i]:
                print("Name of Athlete : ",name[i])
                print(f"Health of {name[i]} : ",progress_data[i][0])
                print(f"HeartRate of {name[i]} : ",progress_data[i][1])
                print(f"Stamina of {name[i]} : ",progress_data[i][2])
                print(f"Recovery Rate : ",(progress_data[i][0]+progress_data[i][1]+progress_data[i][2])//3)
    
athlete_id=[]
name=[]
progress_data=[]
appoint=[]
if __name__ == '__main__':
    c=clinic()
    
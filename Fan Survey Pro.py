import os
class Fan_Class:
    def __init__(self):
        t=[1,2,3,4,5]
        survey_id.extend(t)
        r=['Tanu','Prerana','Rahul','Jaya','Tarun']
        name.extend(r)
        p=[['10','Satisfied','It was Too Hot Seeing Them in Person'],['8','Satisfied','If Sitting Arrangements Was Done In Better Way'],['9','Satisfied','Music Was Super and Full Enjoyed'],['6','Satisfied','Was not Able To See Everything Bec of Too much Crowd and it Was Noisy'],['9','Satisfied','Just Have to Cool Cant Be Melted In Case Of Legends']]
        fan_data.extend(p)
        print("Created The Default Individual Fan Details")
        print(survey_id)
class FanDatabase:
    def create(self):
        s=Fan_Class()
    def read(self,h):
        for i in range(len(name)):
            if h==survey_id[i]:
                print(f"Survey ID : {survey_id[i]}\nName : {name[i]}\nFan Ratings (1-10) : {fan_data[i][0]}")
    def update(self,e):
        survey_id.append(e)
        n=input("Enter The Name : ")
        name.append(n)
        x=input("Enter The Ratings (1-10) : ")
        y=input("Enter Satisfacton and Preferences : ")
        z=input("Enter The FeedBack : ")
        print("Your Fan FeedBack Has Been Confirmed")
        l=[]
        l.append(x)
        l.append(y)
        l.append(z)
        fan_data.append(l)
        print("Survey Records List Updated")
    def delete(self,d):
        for i in range(len(name)):
            if d == survey_id[i]:
                survey_id[i]=None
                name[i]='-'
                fan_data[i]=['-','-','-']
                print("Removed Survey Record Successfully")
class SurveyManager:
    def conduct_fan_surveys(self,Survey_id):
        for i in range(len(name)):
            if Survey_id==survey_id[i]:
                s=input("Enter The FeedBack To Be Added : ")
                fan_data[i].append(s)
                print("Survey FeedBack Managed Successfully...")
class ReportManager:
    def generate_fan_engagement_reports(self,report_id):
        for i in range(len(name)):
            if report_id==survey_id[i]:
                print("Name of Fan : ",name[i])
                print(f"Ratings (1-10) of {name[i]} : ",fan_data[i][0])
                print(f"Fan Satisfaction and Preferences of {name[i]} : ",fan_data[i][1])
                print(f"Fan FeedBack of {name[i]} : ",fan_data[i][2])
                print(len(fan_data[i]))
                if len(fann_data[i])>3:
                    print(f"Extra FeedBacks of {name[i]} : ",fan_data[i][3])
                print("\nFan Engagement Reports Generated Successfully... ")
        
survey_id=[]
name=[]
fan_data=[]
if __name__ == '__main__':
        c=FanDatabase()
        p=SurveyManager()
        q=ReportManager()
        choices = {
                '1': c.create,
                '2': c.read,
                '3': c.update,
                '4': c.delete,
                '5': p.conduct_fan_surveys,
                '6': q.generate_fan_engagement_reports
              }
        while True:
            file=open('fanbase.txt','a')
            file.close()
            print("\n1. Creation of Fan Records(Only Initailise)")
            print("2. Reading The Fan Records")
            print("3. Updating The Fan Records")
            print("4. Deletion of Fan Record")
            print("5. Conduct_Manage_Fan_Surveys")
            print("6. Generate_Fan_Engagement_Reports")
            print("7. Store All Fan Reports On To File")
            print("8. Delete All The Fan Records in File")
            print("9. Exit")
            choice = input("Enter your choice: ")
            if choice=='9':
                print("Exiting The Program")
                break
            if choice=='8':
                os.remove("fanbase.txt")
                print("All File Contents Deleted !!")
            if choice=='7':
                file=open('fanbase.txt','r+')
                for i in range(len(name)):
                    file.write("Survey ID : "+str(survey_id[i]))
                    file.write("\nName : "+name[i])
                    file.write(f"\nFan Survey Report of {name[i]}")
                    file.write("\nRatings (1-10) : "+fan_data[i][0])
                    file.write("\nFan Satisfaction and Preferences : "+fan_data[i][1])
                    file.write("\nFan FeedBack : "+fan_data[i][2])
                    if len(fan_data[i])>3:
                        file.write("\nExtra FeedBacks : "+str(fan_data[i][3]) )
                    if fan_data[i][2]!='-':
                        file.write("\nSurvey Was Conducted Successfully... ")
                    else:
                        file.write("\nSurvey Was Deleted Successfully... ")
                    file.write("\n-----------------------------------------------------------\n")
                print("-----File Created Successfully-----")
            if choice=='1':
                choices[choice]()
            if choice=='2':
                h=int(input("Enter The Survey ID : "))
                if h not in survey_id:
                    print("Survey ID Invalid")
                else:
                    choices[choice](h)
            if choice=='3':
                e=int(input('Enter The Survey ID : '))
                if e in survey_id:
                    print("Survey ID Already Exist")
                else:
                    choices[choice](e)
            if choice=='4':
                d=int(input("Enter The Survey ID : "))
                if d not in survey_id:
                    print("Survey ID Doesn't Exist")
                else:
                    choices[choice](d)
            if choice=='5':
                y=int(input("Enter The Survey ID : "))
                if y not in survey_id:
                    print("Create The Survey ID From Choice 3")
                else:
                    choices[choice](y)
            if choice=='6':
                z=int(input("Enter The Survey ID : "))
                if z not in survey_id:
                    print("Create The Survey ID From Choice 3")
                else:
                    choices[choice](z)


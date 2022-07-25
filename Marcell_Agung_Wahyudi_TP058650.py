#Marcell Agung Wahyudi
#TP058650

#-----------------------------------------------------------------------

#Admin Data
ad_nm = "Admin"
ad_pw = "Admin69"

#Admin Function, Add Records of : a. Coaches
def coach_record():
    coach_data = ["ID", "name", "datejoined", "dateterminated", "hourlyrate", "phone", "address", "SPcode", "SPname", "sportcode", "sportname", "rating"]
    print("\nAdd Records of Coach :")
    confirm = 1
    while (confirm == 1):
        coach_data[0] = input ("Coach ID \t\t: ")
        coach_data[1] = input ("Coach Name \t\t: ")
        coach_data[2] = input ("Date Joined \t\t: ")
        coach_data[3] = input ("Date Terminated \t: ")
        coach_data[4] = input ("Hourly Rate (Rm/H) \t: ")
        coach_data[5] = input ("Phone  \t\t\t: ")
        coach_data[6] = input ("Address \t\t: ")
        coach_data[7] = input ("Sport Center Code \t: ")
        coach_data[8] = input ("Sport Center Name \t: ")
        coach_data[9] = input ("Sport Code \t\t: ")
        coach_data[10] = input ("Sport Name \t\t: ")
        coach_data[11] = input ("Rating \t\t\t: ")
        verify = input ("\nEnter an input :\n'1' to Save and exit program\n'2' to Save and add another Record \n'3' to Save and go back to Admin Function\n'anything' to redo\n'b' to go back\n\n")
        coach_database = open("coachdatabase.txt", "a")
        if (verify == "1"):
            confirm = 0
            print ("\nRecord Saved")
            coach_database.write(coach_data[0]+"\t"+coach_data[1]+"\t"+coach_data[2]+"\t"+coach_data[3]+"\t"+coach_data[4]+"\t"+coach_data[5]+"\t"+coach_data[6]+"\t"+coach_data[7]+"\t"+coach_data[8]+"\t"+coach_data[9]+"\t"+coach_data[10]+"\t"+coach_data[11]+"\t1"+"\n")
            coach_database.close()
        if (verify == "2"):
            print ("\nRecord Saved")
            coach_database.write(coach_data[0]+"\t"+coach_data[1]+"\t"+coach_data[2]+"\t"+coach_data[3]+"\t"+coach_data[4]+"\t"+coach_data[5]+"\t"+coach_data[6]+"\t"+coach_data[7]+"\t"+coach_data[8]+"\t"+coach_data[9]+"\t"+coach_data[10]+"\t"+coach_data[11]+"\t1"+"\n")
            coach_database.close()
        if (verify == "3"):
            confirm = 0
            print ("\nRecord Saved")
            coach_database.write(coach_data[0]+"\t"+coach_data[1]+"\t"+coach_data[2]+"\t"+coach_data[3]+"\t"+coach_data[4]+"\t"+coach_data[5]+"\t"+coach_data[6]+"\t"+coach_data[7]+"\t"+coach_data[8]+"\t"+coach_data[9]+"\t"+coach_data[10]+"\t"+coach_data[11]+"\t1"+"\n")
            coach_database.close()
            admin_function()
        elif (verify == "b"):
            confirm = 0
            add_records()

#Admin Function, Add Records of : b. Sports
def sport_record():
    sport_data = ["id", "name", "center", "coach", "fees"]
    print("\nAdd Records of Sport : ")
    while True:
        sport_data[0] = input("Sport ID\t: ")
        sport_data[1] = input("Sport Name \t: ")
        sport_data[2] = input("Sport Center \t: ")
        sport_data[3] = input("Sport Coach \t: ")
        sport_data[4] = input("Sport Fees (RM)\t: ")
        verify = input ("\nEnter an input :\n'1' to Save and exit program\n'2' to Save and add another Record \n'3' to Save and go back to Admin Function\n'anything' to redo\n'b' to go back\n\n")
        sport_database = open("sportdatabase.txt", "a")
        if (verify == "1"):
            print ("\nRecord Saved")
            sport_database.write("\n"+sport_data[0]+"\t"+sport_data[1]+"\t"+sport_data[2]+"\t"+sport_data[3]+"\t"+sport_data[4])
            sport_database.close()
            break
        if (verify == "2"):
            print ("\nRecord Saved")
            sport_database.write("\n"+sport_data[0]+"\t"+sport_data[1]+"\t"+sport_data[2]+"\t"+sport_data[3]+"\t"+sport_data[4])
            sport_database.close()
        if (verify == "3"):
            print ("\nRecord Saved")
            sport_database.write("\n"+sport_data[0]+"\t"+sport_data[1]+"\t"+sport_data[2]+"\t"+sport_data[3]+"\t"+sport_data[4])
            sport_database.close()
            admin_function()
            break
        elif (verify == "b"):
            add_records()
            break

#Admin Function, Add Records of : c. Sport Schedules
def sportschedule_record():
    schedule_data = ["sport","time", "date", "coach"]
    print("\nAdd Records of Sport Schedule : ")
    while True:
        schedule_data[0] = input("Sport \t: ")
        schedule_data[1] = input("Date \t: ")
        schedule_data[2] = input("Time \t: ")
        schedule_data[3] = input("Coach \t: ")
        verify = input ("\nEnter an input :\n'1' to Save and exit program\n'2' to Save and add another Record \n'3' to Save and go back to Admin Function\n'anything' to redo\n'b' to go back\n\n")
        schedule_database = open("scheduledatabase.txt", "a")
        if (verify == "1"):
            print ("\nRecord Saved")
            schedule_database.write("\n"+schedule_data[0]+"\t"+schedule_data[1]+"\t"+schedule_data[2]+"\t"+schedule_data[3])
            schedule_database.close()
            break
        if (verify == "2"):
            print ("\nRecord Saved")
            schedule_database.write("\n"+schedule_data[0]+"\t"+schedule_data[1]+"\t"+schedule_data[2]+"\t"+schedule_data[3])
            schedule_database.close()
        if (verify == "3"):
            print ("\nRecord Saved")
            schedule_database.write("\n"+schedule_data[0]+"\t"+schedule_data[1]+"\t"+schedule_data[2]+"\t"+schedule_data[3])
            schedule_database.close()
            admin_function()
            break
        elif (verify == "b"):
            add_records()
            break

#Admin Function, Add Records
def add_records():
    while True:
        record = input("\nSelect something to be recorded : \na. Coach \nb. Sport \nc. Sport Schedule \nd. Go Back\n\n")
        if (record == "a"):
            coach_record()
            break
        elif (record == "b"):
            sport_record()
            break
        elif (record == "c"):
            sportschedule_record()
            break
        elif (record == "d"):
            admin_function()
            break
        else:
            print ("\nInvalid Input, please select a, b, c, or d.")

#Admin Function, Display Records of : a. Coaches
def dcoach_record():
    coach_data = open("coachdatabase.txt")
    for coaches in coach_data:
        order = coaches.split()
        print("\nCoach ID \t\t: ",order[0])
        print("Coach Name \t\t: ",order[1])
        print("Date Joined \t\t: ",order[2])
        print("Date Terminated \t: ",order[3])
        print("Hourly Rate (Rm/H) \t: ",order[4])
        print("Phone  \t\t\t: ",order[5])
        print("Address \t\t: ",order[6])
        print("Sport Center Code \t: ",order[7])
        print("Sport Center Name \t: ",order[8])
        print("Sport Code \t\t: ",order[9])
        print("Sport Name \t\t: ",order[10])
        print("Rating \t\t\t: ",order[11])
        print("Total Reviewers \t: ",order[12])
    coach_data.close()
    
#Admin Function, Display Records of : b. Sports
def dsport_record():
    sport_data = open("sportdatabase.txt")
    for sports in sport_data:
        order = sports.split()
        print("\nSport Code \t: ",order[0])
        print("Sport Type \t: ",order[1])
        print("Sport Center \t: ",order[2])
        print("Coach \t\t: ",order[3])
        print("Sport Fee \t: ",order[4])
    sport_data.close()

#Admin Function, Display Records of : c. Registered Students
def dregisteredstudent_record():
    student_data = open("studentdatabase.txt")
    for students in student_data:
        order = students.split()
        print("\nStudent ID\t: ",order[0])
        print("Username \t: ",order[1])
        print("Email \t\t: ",order[2])
        print("Place of Birth \t: ",order[3])
        print("Date of Birth \t: ",order[4])
        print("Password \t: ",order[5])
    student_data.close()
    
#Admin Function, Display Records
def display_records():
    while True:
        record = input("\nSelect a record to be displayed : \na. Coach \nb. Sport \nc. Registered Students \nd. Go Back\n\n")
        if (record == "a"):
            dcoach_record()
            break
        elif (record == "b"):
            dsport_record()
            break
        elif (record == "c"):
            dregisteredstudent_record()
            break
        elif (record == "d"):
            admin_function()
            break
        else:
            print ("\nInvalid Input, please select a, b, c, or d.")

#Admin Function, Search Specific Records of : a. Coach by Coach ID
def search_coachID():
    found = False
    print ("Search Specific Records of Coach by Coach ID \nEnter 'b' to go Back")
    while (found == False):
        coachID = input("\nEnter a Coach ID : ")
        coach_data = open("coachdatabase.txt")
        for coaches in coach_data:
            order = coaches.split()
            if(coachID == order[0]):
                print("Coach ID \t\t: ",order[0])
                print("Coach Name \t\t: ",order[1])
                print("Date Joined \t\t: ",order[2])
                print("Date Terminated \t: ",order[3])
                print("Hourly Rate (Rm/H) \t: ",order[4])
                print("Phone  \t\t\t: ",order[5])
                print("Address \t\t: ",order[6])
                print("Sport Center Code \t: ",order[7])
                print("Sport Center Name \t: ",order[8])
                print("Sport Code \t\t: ",order[9])
                print("Sport Name \t\t: ",order[10])
                print("Rating \t\t\t: ",order[11])
                print("Total Reviewers \t: ",order[12])
                found = True
        coach_data.close()
        if (coachID == "b"):
            found = True
            search_records()
        elif (found == False):
            print ("Invalid Coach ID, please retry or Enter 'b' to go back")

#Admin Function, Search Specific Records of : b. Coach by overall performance (Rating)
def search_coachRating():
    print ("Search Specific Records of Coach by Coach Rating \nEnter 'b' to go Back")
    found = False
    counter = 1
    while (found == False):
        coachRating = input("\nEnter Rating : ")
        coach_data = open("coachdatabase.txt")
        for coaches in coach_data:
            order = coaches.split()
            if (coachRating == order[11]):
                print("\n["+str(counter)+"]")
                print("Coach ID \t\t: ",order[0])
                print("Coach Name \t\t: ",order[1])
                print("Date Joined \t\t: ",order[2])
                print("Date Terminated \t: ",order[3])
                print("Hourly Rate (Rm/H) \t: ",order[4])
                print("Phone  \t\t\t: ",order[5])
                print("Address \t\t: ",order[6])
                print("Sport Center Code \t: ",order[7])
                print("Sport Center Name \t: ",order[8])
                print("Sport Code \t\t: ",order[9])
                print("Sport Name \t\t: ",order[10])
                print("Rating \t\t\t: ",order[11])
                print("Total Reviewers \t: ",order[12])
                counter += 1
                found = True
        coach_data.close()
        if (coachRating == "b"):
            found = True
            search_records()
        elif (found == False):
            print ("Invalid Coach Rating, please retry or Enter 'b' to go back")

#Admin Function, Search Specific Records of : c. Sport by Sport ID
def search_sportID():
    found = False
    while (found == False):
        sportID = input("\nEnter 'b' to go back \nEnter a Sport ID : ")
        sport_data = open("sportdatabase.txt")
        for sports in sport_data:
            order = sports.split()
            if (sportID == order[0]):
                print("\nSport Code \t: ",order[0])
                print("Sport Type \t: ",order[1])
                print("Sport Center \t: ",order[2])
                print("Coach \t\t: ",order[3])
                print("Sport Fee \t: ",order[4])
                found = True
        sport_data.close()
        if (sportID == "b"):
            found = True   
            search_records()
        elif (found == False):
            print ("Invalid Sport ID, please retry or Enter 'b' to go back")
        

#Admin Function, Search Specific Records of : d. Student by Student ID
def search_studentID():
    found = False
    while (found == False):
        studentID = input("\nEnter 'b' to go back \nEnter a Student ID : ")
        student_data = open("studentdatabase.txt")
        for students in student_data:
            order = students.split()
            if (studentID == order[0]):
                order = students.split()
                print("\nStudent ID\t: ",order[0])
                print("Username \t: ",order[1])
                print("Email \t\t: ",order[2])
                print("Place of Birth \t: ",order[3])
                print("Date of Birth \t: ",order[4])
                print("Password \t: ",order[5])
                found = True
            elif (studentID == "b"):
                student_data.close()
                found = True
  
#Admin Function, Search Specific Records
def search_records():
    while True:
        record = input("\nSelect a record to be searched : \na. Coach by Coach ID \nb. Coach by Overall Performance (Rating) \nc. Sport by Sport ID \nd. Student by Student ID \ne. Go Back \n\n")
        if (record == "a"):
            search_coachID()
            break
        elif (record == "b"):
            search_coachRating()
            break
        elif (record == "c"):
            search_sportID()
            break
        elif (record == "d"):
            search_studentID()
            break
        elif (record == "e"):
            admin_function()
            break
        else:
            print ("\nInvalid Input, please select a, b, c, d or e.")

#Admin Function, Sort and Display Records of : a. Coaches in ascending order by names.
def coachNames():
    question = input("\nDisplaying Coaches by Names in Ascending Order, enter 1 to Continue or 0 to go back : ")
    if (question == "1"):
        coach_database = open("coachdatabase.txt")
        sort_name = open("sortname.txt", "w")
        for coach_records in coach_database:
            coach_details = coach_records.split()
            sort_name.write(coach_details[1]+"\t"+coach_details[0]+"\t"+coach_details[2]+"\t"+coach_details[3]+"\t"+coach_details[4]+"\t"+coach_details[5]+"\t"+coach_details[6]+"\t"+coach_details[7]+"\t"+coach_details[8]+"\t"+coach_details[9]+"\t"+coach_details[10]+"\t"+coach_details[11]+"\t"+coach_details[12]+"\n")
        coach_database.close()
    elif (question == "0"):
        sortdisplay_records()      
    sort_name.close()
    sort_name = open("sortname.txt")
    readl = sort_name.readlines()
    n = len(readl)
    x = ""
    for i in range (n-1):
        for j in range (0, n-i-1):
            if readl[j] > readl [j+1]:
                x = readl[j]
                readl[j] = readl[j+1]
                readl[j+1] = x
    with open("sortname.txt", "w") as file:
        file.writelines (readl)
        file.close
    sort_name.close()
    sort = open("sortname.txt")
    for sort_records in sort:
        sort_records = sort_records.strip("\n")
        sort_details = sort_records.split()
        print("\nCoach ID \t\t: ",sort_details[1])
        print("Coach Name \t\t: ",sort_details[0])
        print("Date Joined \t\t: ",sort_details[2])
        print("Date Terminated \t: ",sort_details[3])
        print("Hourly Rate (Rm/H) \t: ",sort_details[4])
        print("Phone  \t\t\t: ",sort_details[5])
        print("Address \t\t: ",sort_details[6])
        print("Sport Center Code \t: ",sort_details[7])
        print("Sport Center Name \t: ",sort_details[8])
        print("Sport Code \t\t: ",sort_details[9])
        print("Sport Name \t\t: ",sort_details[10])
        print("Rating \t\t\t: ",sort_details[11])
        print("Total Reviewers \t: ",sort_details[12])

#Admin Function, Sort and Display Records of : b. Coaches Hourly Pay Rate in Ascending Order.
def coachPayRate():
    question = input("\nDisplaying Coaches by Hourly Pay Rate in Ascending Order, enter 1 to Continue or 0 to go back : ")
    if (question == "1"):
        coach_database = open("coachdatabase.txt", "r")
        sort_pay = open("sortpay.txt", "w")
        for coach_records in coach_database:
            coach_details = coach_records.split()
            sort_pay.write(coach_details[4]+"\t"+coach_details[0]+"\t"+coach_details[1]+"\t"+coach_details[2]+"\t"+coach_details[3]+"\t"+coach_details[5]+"\t"+coach_details[6]+"\t"+coach_details[7]+"\t"+coach_details[8]+"\t"+coach_details[9]+"\t"+coach_details[10]+"\t"+coach_details[11]+"\t"+coach_details[12]+"\n")
        coach_database.close()
    elif (question == "0"):
        sortdisplay_records()      
    sort_pay.close()
    sort_pay = open("sortpay.txt", "r")
    readl = sort_pay.readlines()
    n = len(readl)
    y = ""
    for i in range (n-1):
        for j in range (0, n-i-1):
            if readl[j] > readl [j+1]:
                y = readl[j]
                readl[j] = readl[j+1]
                readl[j+1] = y
    with open("sortpay.txt", "w") as file:
        file.writelines (readl)
        file.close
    sort_pay.close()
    sort = open("sortpay.txt")
    for sort_records in sort:
        sort_records = sort_records.strip("\n")
        sort_details = sort_records.split()
        print("\nCoach ID \t\t: ",sort_details[1])
        print("Hourly Rate (Rm/H) \t: ",sort_details[0])
        print("Coach Name \t\t: ",sort_details[2])
        print("Date Joined \t\t: ",sort_details[3])
        print("Date Terminated \t: ",sort_details[4])
        print("Phone  \t\t\t: ",sort_details[5])
        print("Address \t\t: ",sort_details[6])
        print("Sport Center Code \t: ",sort_details[7])
        print("Sport Center Name \t: ",sort_details[8])
        print("Sport Code \t\t: ",sort_details[9])
        print("Sport Name \t\t: ",sort_details[10])
        print("Rating \t\t\t: ",sort_details[11])
        print("Total Reviewers \t: ",sort_details[12])           

#Admin Function, Sort and Display Records of : c. Coaches Overall Performance in Ascending Order.
def coachRating():
    question = input("\nDisplaying Coaches by Overall Performance in Ascending Order, enter 1 to Continue or 0 to go back : ")
    if (question == "1"):
        coach_database = open("coachdatabase.txt", "r")
        sort_rate = open("sortrate.txt", "w")
        for coach_records in coach_database:
            coach_details = coach_records.split()
            sort_rate.write(coach_details[11]+"\t"+coach_details[0]+"\t"+coach_details[1]+"\t"+coach_details[2]+"\t"+coach_details[3]+"\t"+coach_details[4]+"\t"+"\t"+coach_details[5]+"\t"+coach_details[6]+"\t"+coach_details[7]+"\t"+coach_details[8]+"\t"+coach_details[9]+"\t"+coach_details[10]+"\t"+coach_details[12]+"\n")
        coach_database.close()
    elif (question == "0"):
        sortdisplay_records()      
    sort_rate.close()
    sort_rate = open("sortrate.txt", "r")
    readl = sort_rate.readlines()
    n = len(readl)
    z = ""
    for i in range (n-1):
        for j in range (0, n-i-1):
            if readl[j] > readl [j+1]:
                z = readl[j]
                readl[j] = readl[j+1]
                readl[j+1] = z
    with open("sortrate.txt", "w") as file:
        file.writelines (readl)
        file.close
    sort_rate.close()
    sort = open("sortrate.txt")
    for sort_records in sort:
        sort_records = sort_records.strip("\n")
        sort_details = sort_records.split()
        print("\nCoach ID \t\t: ",sort_details[1])
        print("Rating \t\t\t: ",sort_details[0])
        print("Total Reviewers \t: ",sort_details[12])  
        print("Coach Name \t\t: ",sort_details[2])
        print("Date Joined \t\t: ",sort_details[3])
        print("Date Terminated \t: ",sort_details[4])
        print("Hourly Rate (Rm/H) \t: ",sort_details[5])
        print("Phone  \t\t\t: ",sort_details[6])
        print("Address \t\t: ",sort_details[7])
        print("Sport Center Code \t: ",sort_details[8])
        print("Sport Center Name \t: ",sort_details[9])
        print("Sport Code \t\t: ",sort_details[10])
        print("Sport Name \t\t: ",sort_details[11])


#Admin Function, Sort and Display Records
def sortdisplay_records():
    while True:
        record = input("\nSelect a record to be Sorted and Displayed : \na. Coach in Ascending Order by Names \nb. Coaches Hourly Pay Rate in Ascending Order \nc. Coaches Overall Performance in Ascending Order \nd. Go Back\n\n")
        if (record == "a"):
            coachNames()
            break
        elif (record == "b"):
            coachPayRate()
            break
        elif (record == "c"):
            coachRating()
            break
        elif (record == "d"):
            admin_function()
            break
        else:
            print ("\nInvalid Input, please select a, b, c, or d.")

#Admin Function, Modify Records of : a. Coach
def modifyCoach():
    print ("\nModify Records of Coach")
    counter = 0
    coach_data = open("coachdatabase.txt")
    for data in coach_data:
            print("[",counter+1,"]",data)
            counter += 1
    coach_data.close()
    coach_data = ["ID", "name", "datejoined", "dateterminated", "hourlyrate", "phone", "address", "SPcode", "SPname", "sportcode", "sportname", "rating", "reviewers"]
    while True:
        line = int(input("\nSelect a line to be modified : "))
        coach_modify = open("coachdatabase.txt")
        coach_modify_line = coach_modify.readlines()
        coach_data[0] = input ("Coach ID \t\t: ")
        coach_data[1] = input ("Coach Name \t\t: ")
        coach_data[2] = input ("Date Joined \t\t: ")
        coach_data[3] = input ("Date Terminated \t: ")
        coach_data[4] = input ("Hourly Rate  (RM/H)\t: ")
        coach_data[5] = input ("Phone  \t\t\t: ")
        coach_data[6] = input ("Address \t\t: ")
        coach_data[7] = input ("Sport Center Code \t: ")
        coach_data[8] = input ("Sport Center Name \t: ")
        coach_data[9] = input ("Sport Code \t\t: ")
        coach_data[10] = input ("Sport Name \t\t: ")
        coach_data[11] = input ("Rating \t\t\t: ")
        verify = input ("\nEnter an input :\n'1' to Save and exit program\n'2' to Save and Modify another Record \n'3' to Save and go back to Admin Function\n'anything' to redo\n'b' to go back\n\n")
        if (verify == "1"):
            print("Record Modified Successfully")
            coach_modify_line[line-1] = coach_data[0]+"\t\t"+coach_data[1]+"\t"+coach_data[2]+"\t"+coach_data[3]+"\t"+coach_data[4]+"\t\t"+coach_data[5]+"\t"+coach_data[6]+"\t"+coach_data[7]+"\t"+coach_data[8]+"\t"+coach_data[9]+"\t\t"+coach_data[10]+"\t"+coach_data[11]+"\t1"+"\n"
            coach_modify = open("coachdatabase.txt", "w")
            coach_modify.writelines(coach_modify_line)
            coach_modify.close()
            break
        elif (verify == "2"):
            print("Record Modified Successfully")
            coach_modify_line[line-1] = coach_data[0]+"\t\t"+coach_data[1]+"\t"+coach_data[2]+"\t"+coach_data[3]+"\t"+coach_data[4]+"\t\t"+coach_data[5]+"\t"+coach_data[6]+"\t"+coach_data[7]+"\t"+coach_data[8]+"\t"+coach_data[9]+"\t\t"+coach_data[10]+"\t"+coach_data[11]+"\t1"+"\n"
            coach_modify = open("coachdatabase.txt", "w")
            coach_modify.writelines(coach_modify_line)
            coach_modify.close()
        elif (verify == "3"):
            print("Record Modified Successfully")
            coach_modify_line[line-1] = coach_data[0]+"\t\t"+coach_data[1]+"\t"+coach_data[2]+"\t"+coach_data[3]+"\t"+coach_data[4]+"\t\t"+coach_data[5]+"\t"+coach_data[6]+"\t"+coach_data[7]+"\t"+coach_data[8]+"\t"+coach_data[9]+"\t\t"+coach_data[10]+"\t"+coach_data[11]+"\t1"+"\n"
            coach_modify = open("coachdatabase.txt", "w")
            coach_modify.writelines(coach_modify_line)
            coach_modify.close()
            admin_function()
            break
        elif (verify == "b"):
            modifyRecords()
            break

#Admin Function, Modify Records of : b. Sport
def modifySport():
    print ("\nModify Records of Sport")
    sport_data = open("sportdatabase.txt")
    counter = 1
    for sports in sport_data:
        print("[",counter,"]",sports)
        counter +=1
    sport_data.close()
    sport_data = ["id", "name", "center", "coach", "fees"]
    while True:
        line = int(input("\nSelect a line to be modified : "))
        sport_modify = open("sportdatabase.txt")
        sport_modify_line = sport_modify.readlines()
        sport_data[0] = input("Sport ID\t: ")
        sport_data[1] = input("Sport Name \t: ")
        sport_data[2] = input("Sport Center \t: ")
        sport_data[3] = input("Sport Coach \t: ")
        sport_data[4] = input("Sport Fees (RM)\t: ")
        verify = input ("\nEnter an input :\n'1' to Save and exit program\n'2' to Save and Modify another Record \n'3' to Save and go back to Admin Function\n'anything' to redo\n'b' to go back\n\n")
        if (verify == "1"):
            print ("\nRecord Modified Successfully")
            sport_modify_line[line-1] = sport_data[0]+"\t\t"+sport_data[1]+"\t"+sport_data[2]+"\t"+sport_data[3]+"\t"+sport_data[4]+"\n"
            sport_modify = open("sportdatabase.txt", "w")
            sport_modify.writelines(sport_modify_line)
            sport_modify.close()
            break
        elif (verify == "2"):
            print ("\nRecord Modified Successfully")
            sport_modify_line[line-1] = sport_data[0]+"\t\t"+sport_data[1]+"\t"+sport_data[2]+"\t"+sport_data[3]+"\t"+sport_data[4]+"\n"
            sport_modify = open("sportdatabase.txt", "w")
            sport_modify.writelines(sport_modify_line)
            sport_modify.close()
        elif (verify == "3"):
            print ("\nRecord Modified Successfully")
            sport_modify_line[line-1] = sport_data[0]+"\t\t"+sport_data[1]+"\t"+sport_data[2]+"\t"+sport_data[3]+"\t"+sport_data[4]+"\n"
            sport_modify = open("sportdatabase.txt", "w")
            sport_modify.writelines(sport_modify_line)
            sport_modify.close()
            admin_function()
            break
        elif (verify == "b"):
            modifyRecords()
            break
        
#Admin Fucntion, Modify Records of : c. Sport Schedule
def modifySportSchedule():
    print ("\nModify Records of Sport Schedule")
    schedule_data = open("scheduledatabase.txt")
    counter = 1
    for schedules in schedule_data:
        print("[",counter,"]",schedules)
        counter += 1
    schedule_data.close()
    schedule_data = ["sport", "time", "date", "coach"] 
    while True:
        line = int(input("\nSelect a line to be modified : "))
        schedule_modify = open("scheduledatabase.txt")
        schedule_modify_line = schedule_modify.readlines()
        schedule_data[0] = input("Sport \t: ")
        schedule_data[1] = input("Date \t: ")
        schedule_data[2] = input("Time \t: ")
        schedule_data[3] = input("Coach \t: ")
        verify = input ("\nEnter an input :\n'1' to Save and exit program\n'2' to Save and Modify another Record \n'3' to Save and go back to Admin Function\n'anything' to redo\n'b' to go back\n\n")
        if (verify == "1"):
            print ("\nRecord Modified Successfully")
            schedule_modify_line[line-1] = schedule_data[0]+"\t"+schedule_data[1]+"\t"+schedule_data[2]+"\t"+schedule_data[3]+"\n"
            schedule_modify = open("scheduledatabase.txt", "w")
            schedule_modify.writelines(schedule_modify_line)
            schedule_modify.close()
            break
        if (verify == "2"):
            print ("\nRecord Modified Successfully")
            schedule_modify_line[line-1] = schedule_data[0]+"\t"+schedule_data[1]+"\t"+schedule_data[2]+"\t"+schedule_data[3]+"\n"
            schedule_modify = open("scheduledatabase.txt", "w")
            schedule_modify.writelines(schedule_modify_line)
            schedule_modify.close()
        if (verify == "3"):
            print ("\nRecord Modified Successfully")
            schedule_modify_line[line-1] = schedule_data[0]+"\t"+schedule_data[1]+"\t"+schedule_data[2]+"\t"+schedule_data[3]+"\n"
            schedule_modify = open("scheduledatabase.txt", "w")
            schedule_modify.writelines(schedule_modify_line)
            schedule_modify.close()
            admin_function()
            break
        elif (verify == "b"):
            modifyRecords()
            break     

#Admin Function, Modify Records
def modifyRecords():
    while True:
        record = input("\nSelect a Record to be Modified : \na. Coach \nb. Sport \nc. Sport Schedule \nd. Go Back\n\n")
        if (record == "a"):
            modifyCoach()
            break
        elif (record == "b"):
            modifySport()
            break
        elif (record == "c"):
            modifySportSchedule()
            break
        elif (record == "d"):
            admin_function()
            break
        else:
            print ("\nInvalid Input, please select a, b, c, or d.")

#Admin Function : General
def admin_function():
    while True:
        option = int(input("\nPlease select Admin function : \n1. Add Records \n2. Display Records \n3. Search Spesific Records \n4. Sort and Display Records \n5. Modify Records \n6. Back to main menu \n\n"))
        if (option == 1):
            add_records()
            break
        elif (option == 2):
            display_records()
            break
        elif (option == 3):
            search_records()
            break
        elif (option == 4):
            sortdisplay_records()
            break
        elif (option == 5):
            modifyRecords()
            break
        elif (option == 6):
            main_menu()
            break
        else:
            print("\nInvalid Input, Please Try Again")

#Admin Login Function
def admin_login():
    print ("\nAdmin Login \nType 'b' on username or password to go back")
    while True:
        adLoginnm = input("Enter admin username : ")
        adLoginpw = input("Enter admin password : ")
        if (adLoginnm == "b" or adLoginpw == "b"):
            main_menu()
            break
        elif (adLoginnm == ad_nm and adLoginpw == ad_pw):
            print ("\nLogin Successful")
            admin_function()
            break
        else:
            print("\nInvalid Username or Password")

#----------------------------------------------------------------------
#Student Function, View Details of : a. Coach
#same like admins'~
    
#Student Function, View Details of : b. Self-Record
def self_record_detail():
    print("Details of Self, Enter 'b' on Username or Passsword to go back")
    confirm = 1
    while (confirm == 1):
        selfrecord = open("studentdatabase.txt")
        inputid = input("Please Confirm your Username : ")
        inputpw = input("Please Confirm Your Password : ")
        for password in selfrecord:
            order = password.split()
            if (inputpw == order[5] and inputid == order[1]):
                print("\nStudent ID \t\t: ", order[0])
                print("Username \t\t: ", order[1])
                print("Email \t\t\t: ", order[2])
                print("Place of Birth \t\t: ", order[3])
                print("Date of Birth \t\t: ", order[4])
                selfrecord.close()
                confirm = 0
                break
            elif (inputid == "b" or inputpw == "b"):
                confirm = 0
                view_details_student()
        if (inputid == "b" or inputpw == "b"):
            confirm = 0
            view_details_student()
        elif(confirm == 1):
            print("Invalid Password, Please re-enter your password, or type 'b' to go back")
        
#Student Function, View Details of : c. Registered Sport Schedule
def sport_schedule():
    sportschedule = open("scheduledatabase.txt")
    counter = 1
    for schedule in sportschedule:
        order = schedule.split()
        print("\n["+str(counter)+"]")
        print("Sport Type \t: ", order[0])
        print("Date \t\t: ",order[1])
        print("Time \t\t: ",order[2])
        print("Sport Coach \t: ",order[3])
        counter +=1
    sportschedule.close()

#Student Function, View Details
def view_details_student():
    while True:
        record = input("\nSelect a detail to be displayed : \na. Coach \nb. Self-Record \nc. Sport Schedule \nd. Go Back\n\n")
        if (record == "a"):
            dcoach_record()
            break
        elif (record == "b"):
            self_record_detail()
            break
        elif (record == "c"):
            sport_schedule()
            break
        elif (record == "d"):
            student_function()
            break
        else:
            print ("\nInvalid Input, please select a, b, c, or d.")

#Student Function, Modify Self Record
def modify_self_record():
    student_data = ["studentID", "username", "email", "place of birth", "dateofbirth", "password"]
    login = False
    counter = 0
    print("Modify Self Record, Enter 'b' on Username or Password to go back")
    while (login == False):
        studentnm = input("\nPlease Confirm your Username : ")
        studentpw = input("Please Confirm your Password : ")
        student_modify = open("studentdatabase.txt")
        for password in student_modify:
            order = password.split()
            if (studentnm == order[1] and studentpw == order[5]): 
                login = True
                break
            elif(studentnm == "b" or studentpw == "b"):
                student_function()
                break
            else:
                counter += 1
        if (login == False):
            print("Invalid Username or Password, Please Retry or Enter 'b' on Username or Password to go back.")
        student_modify.close()
    while (login == True):
        student_modify = open("studentdatabase.txt")
        student_modify_line = student_modify.readlines()
        student_data[0] = input("\nStudent ID \t: ")
        student_data[1] = input("Username \t: ") 
        student_data[2] = input("Email \t\t: ")
        student_data[3] = input("Place of Birth \t: ")
        student_data[4] = input("Date of Birth \t: ")
        student_data[5] = input("Password \t: ")
        verify = input ("\nEnter an input :\n'1' to Save and exit program\n'2' to Save and go back to Student Function\n'anything' to redo\n'b' to go back and cancel modify\n\n")
        if (verify == "1"):
            print ("\nRecord Modified Successfully")
            student_modify_line[counter] = student_data[0]+"\t"+student_data[1]+"\t"+student_data[2]+"\t"+student_data[3]+"\t"+student_data[4]+"\t"+student_data[5]+"\n"
            student_modify = open("studentdatabase.txt", "w")
            student_modify.writelines(student_modify_line)
            student_modify.close()
            break
        elif (verify == "2"):
            print ("\nRecord Modified Successfully")
            student_modify_line[counter] = student_data[0]+"\t"+student_data[1]+"\t"+student_data[2]+"\t"+student_data[3]+"\t"+student_data[4]+"\t"+student_data[5]+"\n"
            student_modify = open("studentdatabase.txt", "w")
            student_modify.writelines(student_modify_line)
            student_modify.close()
            student_function()
            break                    
        elif (verify == "b"):
            student_modify.close()
            student_function()
            break
        else:
            login = True
    
#Student Function, Provide Feedback and Star to Coach
def feedback_and_star():
    coaches = open("coachdatabase.txt")
    print ("\nProvide Feedback and Star to Coach, Enter 'b' to go back \nList of Coaches : ")
    for names in coaches:
        order = names.split()
        print(order[1])
    coaches.close()
    found = False
    while True:
        coachname = input("\nEnter a Coach name : ")
        coachdata = open("coachdatabase.txt")
        for coaches in coachdata:
            order = coaches.split()
            if (coachname == order[1]):
                found = True
                print("\nCoach ID \t\t: ",order[0])
                print("Coach Name \t\t: ",order[1])
                print("Date Joined \t\t: ",order[2])
                print("Date Terminated \t: ",order[3])
                print("Hourly Rate (Rm/H) \t: ",order[4])
                print("Phone  \t\t\t: ",order[5])
                print("Address \t\t: ",order[6])
                print("Sport Center Code \t: ",order[7])
                print("Sport Center Name \t: ",order[8])
                print("Sport Code \t\t: ",order[9])
                print("Sport Name \t\t: ",order[10])
                print("Rating \t\t\t: ",order[11])
                print("Total Reviewers \t: ", order[12])
                coachdata.close()
                break
        if (found == True):
            coachdata = open("coachdatabase.txt")
            counter = 0
            coaches = coachdata.readlines()
            for lines in coaches:
                counter += 1
                if coachname in lines:
                    order = lines.split()
                    rating = int(input("Enter Your Rating (1-5)\t:  "))
                    if (rating >= 1 and rating <= 5):
                        totalrating = rating + float(order[11]) * float(order[12])
                        order[12] = float(order[12]) + 1
                        order[11] = totalrating/float(order[12])
                        order[12] = str(order[12])
                        order[11] = str(order[11])
                    else:
                        print("Invalid Input, Please enter 1-5")
                        student_function()
                        break
                    order[12] = order[12] + "\n"
                    success = '\t'.join(order)
                    coaches[counter-1] = success
                    with open("coachdatabase.txt", "w") as file:
                        file.writelines(coaches)
                    print("Rating Successfully Updated, Updated Rating : ", order[11])
                    break
            coachdata.close()
            break
        elif (coachname == "b"):
            student_function()
            break
        else:
            print("Invalid Coach Name, Enter 'b' to go back")

#Student Function : General 
def student_function():
    while True:
        option = int(input("\nPlease select Student function : \n1. View Details \n2. Modify Self Record \n3. Provide feedback and Star to Coach \n4. Back to main menu \n\n"))
        if (option == 1):
            view_details_student()
            break
        elif (option == 2):
            modify_self_record()
            break
        elif (option == 3):
            feedback_and_star()
            break
        elif (option == 4):
            main_menu()
            break
        else:
            print("\nInvalid Input, Please Try Again")   

#Student Login Function
def student_login():
    studentLogin = False
    print("\nStudent Login \nType 'b' on Username or Password to go back")
    while (studentLogin == False):
        student_data = open("studentdatabase.txt")
        studentnm = input("Enter student username \t: ")
        studentpw = input("Enter student password \t: ")
        if (studentnm == "b" or studentpw == "b"):
            main_menu()
            break
        for student_records in student_data:
            order = student_records.split()
            if (studentnm == order[1] and studentpw == order[5]):
                print ("\nLogin Successful")
                studentLogin = True
                student_data.close()
                student_function()
                break
        if (studentLogin == False):
            print ("\nInvalid Username or Password\nEnter 'b' to go back")


#----------------------------------------------------------------------              
#Public Function, View Details of : a. Sport
#The same as admins'~

#Public Function, View Details of : b. Sport Schedule
#The same as student's~

#Public Function, Register
def register():
    student_data = ["studentID","username", "email", "place of birth", "dateofbirth", "password", "confirmedpassword"]
    print("\nStudent Registration \nEnter 'b' on StudentID or Password to go back")
    while True:
        student_data[0] = input("\nStudent ID \t\t: ")
        student_data[1] = input("Username \t\t: ")
        student_data[2] = input("Email \t\t\t: ")
        student_data[3] = input("Place of Birth \t\t: ")
        student_data[4] = input("Date of Birth \t\t: ")
        student_data[5] = input("Password \t\t: ")
        student_data[6] = input("Confirm your Password \t: ")
        if (student_data[6] == student_data[5]):
            student_registration = open("studentdatabase.txt", "a")
            student_registration.write("\n"+student_data[0]+"\t"+student_data[1]+"\t"+student_data[2]+"\t"+student_data[3]+"\t"+student_data[4]+"\t"+student_data[5])
            student_registration.close()
            print("Registration Successful \nProceeding to Student Login Function")
            student_login()
            break
        elif (student_data[0] == "b" or student_data[5] == "b"):
            public_function()
            break
        else:
            print("\nPassword doesn't match, Please try again \nor type 'b' on StudentID or Password to go back")



#Public Function, View Details
def view_detail_public():
    while True:
        record = input("\nSelect a detail to be displayed : \na. Sport \nb. Sport Schedule \nc. Back to main menu\n\n")
        if (record == "a"):
            dsport_record()
            break
        elif (record == "b"):
            sport_schedule()
            break
        elif (record == "c"):
            public_function()
            break
        else:
            print ("\nInvalid Input, please select a, b, c, or d.")

#Public Function : General
def public_function():
    while True:
        option = input("\nPlease select Public function : \n1. View Details \n2. Register as Student \n3. Back to Main Menu \n\n")
        if (option == "1"):
            view_detail_public()
            break
        elif (option == "2"):
            register()
            break
        elif (option == "3"):
            main_menu()
            break
        else:
            print("\nInvalid Input, Please Try Again")

#----------------------------------------------------------------------              
#Main Menu Function
def main_menu():
    print ("\nWelcome to Sport Academy")
    while True:
        profile = input("Select a Profile : \n1. Admin \n2. Student  \n3. Public (Un-Registered) \n4. Exit Program \n\n")    
        if (profile == "1"):
            admin_login()
            break
        elif (profile == "2"):
            student_login()
            break
        elif (profile == "3"):
            public_function()
            break
        elif(profile == "4"):
            print("")
            break
        else:
            print("\nInvalid Input")
main_menu()

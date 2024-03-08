import sqlite3
import matplotlib.pyplot as plt
connection = sqlite3.connect('eSports_management.db')
cursor = connection.cursor()
print("eSports_Management")
print("Opened_database_Successfully")

def tableCols(conn,table): return list(map(lambda x: x[0], conn.execute(f"select * from {table}").description))

connection.execute('''CREATE TABLE if not exists Registration_Details
                 (Team_Name        Char(60)             NOT NULL,
                  Team_Number      int(12) PRIMARY KEY NOT NULL,
                  Registration_ID  Char(60)             NOT NULL,
                  Team_origin      Char(60)             NOT NULL,
                  Team_email       Char(60)             NOT NULL)
                  ''')
print ("Registration_Details Table Created Successfully")

connection.execute('''CREATE TABLE if not exists Team_Details
                  (Team_Number               Int      PRIMARY KEY  NOT NULL,
                   Team_Leader               Char(60)              NOT NULL,
                   Team_platform             Char(60)              NOT NULL,
                   Team_tier                 Int                   NOT NULL,
                   Team_strength             Char(60)              NOT NULL,
                   Tournaments_played        Int                   NOT NULL,
                   Tournaments_won           Int                   NOT NULL,
                   Team_Experience           Int                   NOT NULL)
                   ''')
print ("Team_Details Table Created Successfully")

connection.execute('''CREATE TABLE if not exists Platform_Details
                  (eSport_Name               Char(60)    PRIMARY KEY  NOT NULL,
                   Match_type                Char(60)                 NOT NULL,
                   Number_of_teams           Int(12)                  NOT NULL,
                   Match_difficulty          Int(12)                  NOT NULL,
                   Participation_amount      Int(12)                  NOT NULL,
                   Winning_amount            Int(12)                  NOT NULL,
                   Tier_required             Int(12)                  NOT NULL)
                   ''')
print ("Platform_Details Table Created Successfully")
connection.commit()
sql1 = "select * FROM Registration_Details"
cursor.execute(sql1)

sql2 = "select * FROM Team_Details"
cursor.execute(sql2)

sql3 = "Select * FROM Platform_Details"
cursor.execute(sql3)
print("Record Shown")

TeamNumber = []
TeamOrigin = []
TeamNumber = []
TeamTier= []
MatchType = []
NumberofTeams = []
menu1 = int(input("Choose your table you want to work on : 1 for Registration_Details, 2 for Team_Details, 3 for Platform_Details:"))
if(menu1==1):
    print("Welcome to Registration_Details Table")
    menu2 = int(input("enter 1 for inserting, 2 for Deleting , 3 for Updating , 4 for showing Data"))
    if (menu2 == 1):
        cursor = connection.execute("SELECT * FROM Registration_Details")
        cols = tableCols(connection,"Registration_Details")
        print("Records of table Registration_Details \n ----")
        for row in cursor:
            for entry in range(len(row)):
                print(f"{cols[entry]}: {row[entry]}")
            print("----")
        tname = input("Enter Team_Name:")
        tno = input("Enter Team_Number:")
        rid = input("Enter Registration_ID:")
        torigin = input("Enter Team_origin:")
        temail = input("Enter Team_email:")
        connection.execute("""INSERT INTO Registration_Details (Team_Name, Team_Number, Registration_ID, Team_origin, Team_email) VALUES (?,?,?,?,?)""",(tname, tno, rid, torigin, temail))
        connection.commit()
        print("Record Inserted")
    elif (menu2 == 2):
        cursor = connection.execute("SELECT * FROM Registration_Details")
        cols = tableCols(connection,"Registration_Details")
        print("Records of table Registration_Details \n ----")
        for row in cursor:
            for entry in range(len(row)):
                print(f"{cols[entry]}: {row[entry]}")
            print("----")
        tno = input("Enter Team_Number to delete data")
        connection.execute("DELETE FROM Registration_Details WHERE Team_Number = ?",(tno,))
        connection.commit()
        print ("Total number of rows deleted:", connection.total_changes)
    elif (menu2 == 3):
        cursor = connection.execute("SELECT * FROM Registration_Details")
        cols = tableCols(connection,"Registration_Details")
        print("Records of table Registration_Details \n ----")
        for row in cursor:
            for entry in range(len(row)):
                print(f"{cols[entry]}: {row[entry]}")
            print("----")
        tno = (int(input("Enter Team_Number to update data")))
        tname = input("Enter Team_Name to change data")
        connection.execute("UPDATE Registration_Details SET Team_Name = ? WHERE Team_Number = ?",(tname,tno))
        connection.commit()
        print("Total row updated:",connection.total_changes)
    elif (menu2 == 4):
        cursor = connection.execute("SELECT * FROM Registration_Details")
        cols = tableCols(connection,"Registration_Details")
        print("Records of table Registration_Details \n ----")
        for row in cursor:
            for entry in range(len(row)):
                print(f"{cols[entry]}: {row[entry]}")
            print("----")
            TeamNumber.append(row[1])
            TeamOrigin.append(row[3])

        plt.bar(TeamNumber,TeamOrigin)
        plt.show()

elif(menu1==2):
     print("Welcome to Team_Details Table")
     menu2 = int(input("enter 1 for inserting, 2 for Deleting , 3 for Updating , 4 for showing Data"))
     if (menu2 == 1):
         cursor = connection.execute("SELECT * FROM Team_Details")
         cols = tableCols(connection,"Team_Details")
         print("Records of table Team_Details \n ----")
         for row in cursor:
             for entry in range(len(row)):
                  print(f"{cols[entry]}: {row[entry]}")
             print("----")
         tno = input("Enter Team_Number:")
         tleader = input("Enter Team_Leader:")
         tplatform = input("Enter Team_platform:")
         ttier = input("Enter Team_tier:")
         tstrength = input("Enter Team_Strength:")
         tsplayed = input("Enter Tournaments_Played:")
         tswon = input("Enter Tournaments_Won:")
         texp = input("Enter Team_Experience:")
         connection.execute("""INSERT INTO Team_Details (Team_Number, Team_Leader, Team_platform, Team_tier, Team_Strength, Tournaments_Played, Tournaments_Won, Team_Experience) VALUES (?,?,?,?,?,?,?,?)""",(tno, tleader, tplatform, ttier, tstrength, tsplayed, tswon, texp))
         connection.commit()
         print("Record Inserted")
     elif (menu2 == 2):
         cursor = connection.execute("SELECT * FROM Team_Details")
         cols = tableCols(connection,"Team_Details")
         print("Records of table Team_Details \n ----")
         for row in cursor:
             for entry in range(len(row)):
                  print(f"{cols[entry]}: {row[entry]}")
             print("----")
         tno = input("Enter Team_Number to delete data")
         connection.execute("DELETE FROM Team_Details WHERE Team_Number = ?",(tno,))
         connection.commit()
         print ("Total number of rows deleted:", connection.total_changes)
     elif (menu2 == 3):
         cursor = connection.execute("SELECT * FROM Team_Details")
         cols = tableCols(connection,"Team_Details")
         print("Records of table Team_Details \n ----")
         for row in cursor:
             for entry in range(len(row)):
                  print(f"{cols[entry]}: {row[entry]}")
             print("----")
         tno = input("Enter Team_Number to update data")
         tleader = input("Enter Team_Leader to change data")
         connection.execute("UPDATE Team_Details SET Team_Leader = ? WHERE Team_Number = ?",(tleader,tno))
         connection.commit()
         print("Total row updated:",connection.total_changes)
     elif (menu2 == 4):
         
         cursor = connection.execute("SELECT * FROM Team_Details")
         cols = tableCols(connection,"Team_Details")
         print("Records of table Team_Details \n ----")
         for row in cursor:
             for entry in range(len(row)):
                  print(f"{cols[entry]}: {row[entry]}")
             print("----")
             TeamNumber.append(row[0])
             TeamTier.append(row[3])
         plt.bar(TeamNumber,TeamTier)
         plt.show()

elif(menu1==3):
     print("Welcome to Platform_Details Table")
     menu2 = int(input("enter 1 for inserting, 2 for Deleting , 3 for Updating , 4 for showing Data"))
     if (menu2 == 1):
         cursor = connection.execute("SELECT * FROM Platform_Details")
         cols = tableCols(connection,"Platform_Details")
         print("Records of table Platform_Details \n ----")
         for row in cursor:
             
             for entry in range(len(row)):
                 print(f"{cols[entry]}: {row[entry]}")
             print("----")
         esname = input("Enter eSport_Name:")
         mtype = input("Enter Match_Type:")
         nteams = input("Enter Number_of_Teams:")
         mdifficulty = input("Enter Match_Difficulty:")
         pamount = input("Enter Participation_Amount:")
         wamount = input("Enter Winning_Amount:")
         tierreq = input("Enter Tier_required:")
         connection.execute("""INSERT INTO Platform_Details (eSport_Name, Match_Type, Number_of_Teams, Match_Difficulty, Participation_Amount, Winning_Amount, Tier_required) VALUES (?,?,?,?,?,?,?)""",(esname, mtype, nteams, mdifficulty, pamount, wamount, tierreq))
         connection.commit()
         print("Record Inserted")
     elif (menu2 == 2):
         cursor = connection.execute("SELECT * FROM Platform_Details")
         cols = tableCols(connection,"Platform_Details")
         print("Records of table Platform_Details \n ----")
         for row in cursor:
             
             for entry in range(len(row)):
                 print(f"{cols[entry]}: {row[entry]}")
             print("----")
         esname = input("Enter eSport_Name to delete date")
         connection.execute("DELETE FROM Platform_Details WHERE eSport_Name = ?",(esname,))
         connection.commit()
         print ("Total number of rows deleted:", connection.total_changes)
     elif (menu2 == 3):
         cursor = connection.execute("SELECT * FROM Platform_Details")
         cols = tableCols(connection,"Platform_Details")
         print("Records of table Platform_Details \n ----")
         for row in cursor:
             
             for entry in range(len(row)):
                 print(f"{cols[entry]}: {row[entry]}")
             print("----")
         esname = input("Enter eSport_Name to update data")
         nteams = input("Enter Number_of_Teams to change data")
         connection.execute("UPDATE Platform_Details SET Number_of_Teams = ? WHERE eSport_Name = ?",(nteams,esname))
         connection.commit()
         print("Total row updated:",connection.total_changes)
     elif (menu2 == 4):
         cursor = connection.execute("SELECT * FROM Platform_Details")
         cols = tableCols(connection,"Platform_Details")
         print("Records of table Platform_Details \n ----")
         for row in cursor:
             
             for entry in range(len(row)):
                 print(f"{cols[entry]}: {row[entry]}")
             print("----")
             MatchType.append(row[1])
             NumberofTeams.append(row[2])
         plt.barh(MatchType,NumberofTeams)
         plt.show()

else:
    print("Invalid Input")

import pymysql


connection = pymysql.connect("localhost","root","","_insta_db_" )
cursor = connection.cursor()
#sql=raw_input("Enter The command")
#cursor.execute(sql)
#data=cursor.fetchall()
#print(data)

sqlout=""
print("\n 1.Max Likes \n 2.Min Likes \n 3.Who liked most\n 4.Music pictures \n 5.Popular Tag \n 6.Most liked User \n 7.Old Tagging \n 8.Delete Inactive Users")
choice=int(input("select your option"))
if (choice==1):
    sqlout="select pictue_id from likeed where count(*)>"
    print("pictue_id with max like")
elif (choice==2): 
    sqlout="select pictue_id from likeed where count(*)>"
    print("pictue_id with max like")
elif (choice==3):
    sqlout="select pictue_id from likeed where count(*)>"
    print("user_id with most like")
elif (choice==4):
    sqlout="select pictue_id from likeed where count(*)>"
    print("pictures related to music are")
elif (choice==5):
    sqlout="select pictue_id from likeed where count(*)>"
    print("the name of most popular tag")
elif (choice==6):
    sqlout="select pictue_id from likeed where count(*)>"
    print("Most liked User is")
elif (choice==7):
    sqlout="select pictue_id from likeed where count(*)>"
    print("Tagged Successfully")
elif (choice==8):
    sqlout="select pictue_id from likeed where count(*)>"
    print("Deleted inactive user")
else :
    print("Invalid choice")
    exit

      
cursor.execute(sqlout)
for row in cursor.fetchall():
     print(row)
          
     
     
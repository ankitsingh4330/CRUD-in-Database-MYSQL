'''from connection import get_connection

con = get_connection()
cursor = con.cursor()

username = input("Enter Username: ")
email = input("Enter Email: ")
password = input("Enter Password: ")

query = "INSERT INTO user (username,email,password) VALUES (%s,%s,%s)"
values = (username,email,password)

cursor.execute(query,values)
con.commit()

print("Record Inserted Successfully")

con.close()
'''

from connection import get_connection

con=get_connection()
cursor=con.cursor()

username = input("Enter Username: ")
email = input("Enter Email: ")
password = input("Enter Password: ")

query="INSERT INTO user(username,email,password) VALUES(%s,%s,%s)"
values=(username,email,password)

cursor.execute(query,values)
con.commit()

print("Succesfully")
con.close()
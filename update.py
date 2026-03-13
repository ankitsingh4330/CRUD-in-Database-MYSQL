from connection import get_connection

con = get_connection()
cursor = con.cursor()

id = input("Enter ID to Update: ")
username = input("Enter New Username: ")
email = input("Enter New Email: ")
password = input("Enter New Password: ")

query = "UPDATE user SET username=%s,email=%s,password=%s WHERE id=%s"
values = (username,email,password,id)

cursor.execute(query,values)
con.commit()

print("Record Updated Successfully")

con.close()
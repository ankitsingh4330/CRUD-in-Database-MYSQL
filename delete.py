from connection import get_connection

con = get_connection()
cursor = con.cursor()

id = input("Enter ID to Delete: ")

query = "DELETE FROM user WHERE id=%s"
values = (id,)

cursor.execute(query,values)
con.commit()

print("Record Deleted Successfully")

con.close()
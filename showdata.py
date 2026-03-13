from connection import get_connection

con = get_connection()
cursor = con.cursor()

query = "SELECT * FROM user"
cursor.execute(query)

rows = cursor.fetchall()

for r in rows:
    print("ID:",r[0],"Username:",r[1],"Email:",r[2],"Password:",r[3])

con.close()
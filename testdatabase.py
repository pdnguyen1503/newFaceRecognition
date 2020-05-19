import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="nguyenpc", passwd="nguyen1503", database="FaceBase")
cursor = connection.cursor()

# queries for retrievint all rows
peoples = "Select * from People;"

#executing the quires
cursor.execute(peoples)
rows = cursor.fetchall()
for row in rows:
   print(row)


#commiting the connection then closing it.
connection.commit()
connection.close()
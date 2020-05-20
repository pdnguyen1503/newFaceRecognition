import pymysql

def insertOrUpdate(Id,Name):
    connection = pymysql.connect(host="localhost", user="nguyenpc", passwd="nguyen1503", database="FaceBase")
    cursor = connection.cursor()
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor.execute(cmd)
    data = cursor.fetchall()
    print(data)
    isRecordExist=0
    for row in data:
        isRecordExist=1

    print(isRecordExist)

    if isRecordExist == 1:
        cmd="UPDATE People SET Name="+"'"+str(Name)+"'"+" WHERE ID="+str(Id) + ";"
    else:
        cmd="INSERT INTO People(ID,Name) Values("+str(Id)+","+"'"+str(Name)+"'"+");"
    print(cmd)
    cursor.execute(cmd)
    connection.commit()
    connection.close()
    
id=raw_input('enter your id: ')
name=raw_input('enter your name: ')
insertOrUpdate(id,name)
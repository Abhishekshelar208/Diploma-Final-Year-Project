import mysql.connector

conn = mysql.connector.connect(username='root', password='Abhi@1234',host='localhost',database='face_recognizer',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()

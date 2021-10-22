import mysql.connector


# ;7(KtnU2rgXD_veK

mydb = mysql.connector.connect(
    host= "localhost",
    user= "aplikasi",
    password= ";7(KtnU2rgXD_veK"
)

mycursor = mydb.cursor()

def insert(username, firstname, lastname, password):
    mycursor = mydb.cursor()
    sql = "INSERT INTO users(username, firstname, lastname, password) VALUES (%s, %s)"
    val = (username, firstname, lastname, password)

    mycursor.execute(sql, val)

    mydb.commit()

    rows = mycursor.rowcount
    print(mycursor.rowcount, "baris berhasil ditambahkan")
    return rows

# insert("giovanni", "Giovanni", "Mikail", ";7(KtnU2rgXD_veK")

def getall():
    mycursor = mydb.cursor()
    sql = "SELECT username, firstname, lastname, password FROM users"
    mycursor.execite(sql)
    return mycursor.fetchall()

users = getall()

print(users[1][3])
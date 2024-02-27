import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="221-15-4949",
    database="company"
)

def showTheWholeTable():
    mycursor.execute("SELECT * FROM employee")
    myresult = mycursor.fetchall()

    for row in myresult:
        print(row)

# def showListofTable():
#     mycursor.execute("SHOW TABLES")
#     for tb in mycursor:
#         print(tb)

def searchForIndividualDataset():
    query = int(input("Enter the ID you want to search: "))
    mycursor.execute("SELECT * FROM employee")
    myresult = mycursor.fetchall()

    for row in myresult:
        if row[0] == query:
            print(row)
            
# def searchForIndividualDatasetusingWhere():
#     query = input("Enter the mode list you want to see: ")
#     sqlFormula2 = "SELECT * FROM employee WHERE mode = %s"
#     mycursor.execute(sqlFormula2, (query,))

#     myresult = mycursor.fetchall()

#     for row in myresult:
#         print(row)
        
def insertIntoDatabase():
    n = int(input("Enter the number of rows to insert: "))

    while n>0:
        n -= 1
        sqlFormula = "INSERT INTO employee(customer_name, mode, city) VALUES (%s, %s, %s)"  # Corrected the SQL statement and placeholders

        c_name = input("Enter the name of the customer: ")
        c_mode = input("Enter transaction mode: ")
        c_city = input("Enter the city: ")

        cust = (c_name, c_mode, c_city)

        mycursor.execute(sqlFormula, cust)
        mydb.commit()

        print("Inserted Successfully...")
        
def updateAnyDataByTheCustomerID():
    id = int(input("Enter the ID you want to update: "))
    column = input("Enter which column you want to update: ")
    what = input("Enter the updated data: ")

    if column.lower() not in ['customer_id', 'customer_name', 'mode', 'city']:
        print("Invalid column name!")
    else:
        sqlFormula3 = "UPDATE employee SET {} = %s WHERE customer_id = %s".format(column)
        mycursor.execute(sqlFormula3, (what, id))

        mydb.commit()
        
def deleteAnyRowByCustomerID():
    id = int(input("Enter the ID you want to delete: "))
    mycursor.execute("SELECT * FROM employee WHERE customer_id = %s", (id,))
    result = mycursor.fetchone()

    if result:
        sqlFormula4 = "DELETE FROM employee WHERE customer_id = %s"
        mycursor.execute(sqlFormula4, (id,))
        mydb.commit()
        print("Record deleted successfully.")
    else:
        print("ID not found in the database.")
        
 
mycursor = mydb.cursor()


while True:
    print("-------------------------------")
    print("Enter 1 to Insert Data In Database")
    print("Enter 2 to Show The Table In Database")
    print("Enter 3 to Search Data In Database")
    print("Enter 4 to Update Data In Database")
    print("Enter 5 to Delete Data In Database")
    print("Enter 0 to Break from Database")
    print("-------------------------------\n\n")
    num = int(input("Enter your command: "))
    match num:
        case 0:
            break
        case 1:
            insertIntoDatabase()
        case 2:
            showTheWholeTable()
        case 3:
            searchForIndividualDataset() 
        case 4:
            updateAnyDataByTheCustomerID()
        case 5:
            deleteAnyRowByCustomerID()
        case _:
            print("Wrong Input")
    

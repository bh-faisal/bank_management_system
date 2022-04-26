import mysql.connector
mydb=mysql.connector.connect(host='Localhost', user='root' , password= 'bhfaisal273614', database='BANK_MANAGEMENT', auth_plugin='mysql_native_password')

def main():
    print('''
                1. OPEN NEW ACCOUNT
                2. DEPOSIT AMOUNT
                3. WITHORAW AMOUNT
                4. BALANCE ENQUIRY
                5. DISPLAY CUSTOMER DETAILS
                6. CLOSE AN ACCOUNT''')
    choice = input("Enter the task you want to perform: ")
    if (choice=='1'):
        OpenAcc()
    elif (choice=='2'):
        DepoAmo()
    elif(choice=='3'):
        WitndrawAmount()
    elif(choice=='4'):
        BalEnq()
    elif(choice=='5'):
        DisDetails()
    elif(choice=='6'):
        CloseAcc()
    else:
        print("Invalid choice")
        main()
main()        
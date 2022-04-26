import mysql.connector
mydb=mysql.connector.connect(host='Localhost', user='root' , password= 'bhfaisal273614', database='BANK_MANAGEMENT', auth_plugin='mysql_native_password')

def OpenAcc():
    n=input ("Enter The Name: ")
    ac=input("Enter The Account No: ")
    db=input ("Enter The Date Of Birth: ")
    add=input("Enter The Address: ")
    cn=input ("Enter The Contact Number: ")
    ob=int(input("Enter Opening Balalne: "))
    data1=(n,ac,db,add,cn,ob)
    data2= (n,ac,ob)
    sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values  (%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print ("Data Entered Successfully..")
    main()

def DepoAmo():
    amount = int(input("Enter the amount you want to deposit: "))
    ac = input ("Enter The Account No: ")
    a='select balance from amount where AccNo = %s'
    data= (ac, )
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0] + amount
    d= (t,ac)
    sql=('update amount set balance where AccNo=%s')
    x.execute(sql,d)
    mydb.commit()
    main()

def WitndrawAmount():
    amount = int(input ("Enter the amount you want to withdraw: "))
    ac = input ("Enter The Account No: ")
    a = 'select balance from amount where AccNo=%s'
    data = (ac, )
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = ('update amount set balance where AccNo=%s')
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit ()
    main()
    
def BalEnq():
    ac=input("Enter the account no: ")
    a='select * from amount where AccNo=%s'
    data= (ac,)
    x=mydb.cursor()
    x.execute(a, data)
    result = x.fetchone ()
    print("Balance for account:" ,ac, "is",result[-1])
    main()

def DisDetails():
    ac = input("Enter the account no: ")
    a = 'select * from account where AccNo=%s' 
    data = (ac,)
    x = mydb.cursor()
    x.execute (a, data)
    result = x. fetchone()
    for i in result:
        print(i)
    main()

def CloseAcc():
    input("Enter the account no: ")
    sql1='delete from account where AccNo=%s'
    sql2='delete from amount where AccNo=%s'
    data (ac,)
    x=mydb.cursor()
    x.execute (sql1.data)
    x.execute (sql2.data)
    myab.commit ()
    main()   


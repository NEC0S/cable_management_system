def menu():
    print('1.YES')
    print('2.NO')
    ch=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
    while ch==1:
        print('WELECOME TO ROYAL CABLE CONNECTION CENTER') 
        print('1.SIGN IN')
        print('2.SIGN UP')
        print('3.DELETE ACCOUNT')
        print('4.EXIT')
        ch1=int(input('ENTER YOUR CHOICE:'))
        if ch1==1:
            a=checking()
            if a==True:
                print('WELCOME')
                akhil()
            else:
                
                
                continue
        elif ch1==2:
            a=checking_1()
            if a==True:
                print('WELCOME')
                akhil()
            else:
                print('PASSWORD ALREADY EXISTS')
                continue
            
            
        elif ch1==3:
            c=checking_2()
            if c==True:
                print('ACCOUNT DELETED')
                continue
            else:
                print('YOUR PASSWAORD OR USER_NAME IS INCORRECT')
                continue
        elif ch==4:
            print('THANK YOU')
            break
        else:
            print('ERROR 404:PAGE NOT FOUND')
            break
def akhil():
     import mysql.connector as sql
     conn=sql.connect(host="localhost",user="root",passwd="manager",database="cable")
     if conn.is_connected():
          print("connected successfully")
          
     c1=conn.cursor()
     c1.execute('use cable')

     print("1.ADD DETAILS")
     print("2.MAINTAINANCE")
     print("3.SUGGESTION")
     print("4.EXIT")
     choice=int(input("ENTER  UR CHOICE:"))
     if choice==1:
          v_code=int(input("ENTER  UR CODE_NO:"))
          v_name=input("ENTER UR NAME:")
          v_phone_no=int(input("ENTER UR PHONE_NO:"))
          v_year=int(input("ENTER THE YEAR U STARTED USING OUR CENTER:"))
          v_address=input("ENTER UR ADDRESS(CITY OR VILLAGE NAME):")
          v_SQL_insert="insert into customer_profile values("+str(v_code)+",'"+v_name+"',"+str(v_phone_no)+","+str(v_year)+",'"+v_address+"')"
          c1.execute(v_SQL_insert)
          print("DETAILS ADDED")
          conn.commit()
     if choice==2:
          v_code=int(input("ENTER  UR CODE_NO:"))
          v_name=input("ENTER UR NAME:")
          v_fees=int(input("ENTER CHARGES:"))
          v_rating=float(input("ENTER RATING(out of 10):"))
          v_SQL2_insert="insert into maintenance values("+str(v_code)+",'"+v_name+"',"+str(v_fees)+","+str(v_rating)+")"
          c1.execute(v_SQL2_insert)
          print("DETAILS ADDED")
          conn.commit()

     if choice==3:
          v_code=int(input("ENTER CODE_NO:"))
          v_name=input("ENTER UR NAME:")
          v_suggestion=input("ENTER UR SUGGESTION FOR US:")
          v_SQL3_insert="insert into suggestion values("+str(v_code)+",'"+v_name+"','"+v_suggestion+"')"
          c1.execute(v_SQL3_insert)
          print("DETAILS ADDED")
          conn.commit()

     if choice==4:
          quit()
def checking_2():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='manager',database='cable')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==a:
            b1="delete from user_accounts where password = '{}'".format(b)
            cursor.execute(b1)
            return True
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')
        

def checking_1():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='manager',database='cable')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    c=input('RE-ENTER YOUR PASS WORD:')
    if b==c:
         try:
            c1="insert into user_accounts values('{}','{}')".format(a,b)
            cursor.execute(c1)
            print('WELCOME')
            return True
         except:
              return False
    else:
        print('BOTH PASSWORDS ARE NOT MATCHING')


def checking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='manager',database='cable')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==a:
            
            return True
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')

menu()

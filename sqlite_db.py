import sqlite3
conn = sqlite3.connect("sqlite_db.db")

while True:

    us = int(input('''
    1.INSERT THE DATA BASE
    2.DELETE THE DATA BASE
    3.UPDATE/MODIFY THE DTABASE
    4.SEARCH THE DATA BASE
    5.SHOW THE DATA BASE
    6.END THE THE DATA BASE  
    '''))
    if us == 1 and us < 7:
        try:
            I_ID = input("ENTER THE ID :")
            I_NAME = input("ENTER THE NAME OF STUDENT :")
            I_DEPARTMENT = input("ENTER THE NAME OF DEPARTMENT :")
            I_EN = input("ENTER THE STUDENT ENROLLMENT NUMBER:")

            conn.execute(" INSERT INTO  Student(ID,NAME,DEPARTMENT,ENRO_NO) VALUES (?, ?, ?, ?)",
                         (I_ID, I_NAME, I_DEPARTMENT, I_EN))
            conn.commit()  # update,delete data
            conn.close()
            print(" ----DATA SUCCESFULLU INSERTED----")
        except:
            print(" ----DATA DOES NOT INSERTED----")

    elif us == 2 and us < 7:
        try:
            ID = input("enter the ID foR delete:")
            conn.execute("DELETE FROM Student where ID="+ID)
            conn.commit()
            conn.close()
            print(" ----DATA SUCCESFULLU DELETED----")
        except:
            print(" ----DATA DOES NOT DELETED----")
    elif us == 3 and us < 7:
        try:
            I_ID = input("ENTER THE ID FOR UPDATION  :")
            I_NAME = input("ENTER THE NAME OF STUDENTFOR UPDATION  :")
            I_DEPARTMENT = input("ENTER THE NAME OF DEPARTMENT FOR UPDATION :")
            I_EN = input("ENTER THE STUDENT ENROLLMENT NUMBER FOR UPDATION :")
            update_query = """Update Student set NAME = ?, DEPARTMENT =? ,ENRO_NO=? where id = ?"""
            data = (I_NAME, I_DEPARTMENT, I_EN, I_ID)
            conn.execute(update_query, data)
            conn.commit()
            conn.close()
            print(" ----DATA SUCCESFULLU UPDATED----")
        except:
            print(" ----DATA DOES NOT  UPDATED----")
    elif us == 4 and us < 7:
        try:
            ID = input("Enter the id for searching:  ")
            data = conn.execute("SELECT *FROM Student where ID ='"+ID+"'")
            for n in data:
                # print(n)
                print(n[0], n[1], n[2], n[3])
        except:
            print("YOU SEARCH DATA IS NOT SHOW BECAUSE YOU  ARE WRONG ID ENTER....")
    elif us == 5 and us < 7:
        try:
            data = conn.execute("SELECT *FROM Student")
            for n in data:
                # print(n)
                print(n[0], n[1], n[2], n[3])
        except:
            print("PLEASE ENTER THE PERFECT NUMBER FOR SHOW DATA ")
    elif us == 6 and us < 7:
        break
    else:
        print("PLEASE ENTER THE PERFECT NUMBER")

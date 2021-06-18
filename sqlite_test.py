import sqlite3
import csv

with open('./file/WK_M_EMPLOYEE.csv',encoding='UTF-8-sig') as reder_csv_file:
    reader = csv.DictReader(reder_csv_file,fieldnames = ['EMPLOYEE_ID','EMPLOYEE_NAME','WORK_LOCATION','DATE','YARE','aaa','MAIL_ADDLESS','bbb','ccc','ddd'])

    conn = sqlite3.connect('C:\\pg\\sqlite3\\testdb')
    curs = conn.cursor()
    for row in reader:
        curs.execute('INSERT INTO WK_M_EMPLOYEE ("EMPLOYEE_ID","EMPLOYEE_NAME","WORK_LOCATION","MAIL_ADDLESS") values(?,?,?,?)',[int(row['EMPLOYEE_ID']),row['EMPLOYEE_NAME'],row['WORK_LOCATION'],row['MAIL_ADDLESS']])
    conn.commit()
    conn.close()
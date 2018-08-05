# pymysql  ติดตั้งเพิ่มด้วย pip
import pymysql

if __name__ == '__main__':
    con = pymysql.connect(host='localhost',user='root',passwd='112233',db='h07477',port=3306)
    #print(con)
    cursor = con.cursor(pymysql.cursors.DictCursor)
    sql = """ select * from patient """
    numrows = cursor.execute(sql)
    print(numrows)
    rows = cursor.fetchall()
    for row in rows:
        print(row['fname'] , row['lname'])
    con.close()

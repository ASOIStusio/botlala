
import pyodbc as p



conn = p.connect (
    "Driver = {SQL Server Native 11.0};"
    "Server = DESKTOP-BKNN6JL;"
    "Database = base;"
    "Trusted_Connection = yes;"
)

def create(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("update list set b = ? where a = ?",
                  ('dsad',31)
    )
    conn.commit()






read(conn)


# import psycopg2 as p
# connect = p.connect(dbname='list' ,user='postgres', password='1478' )
# 
# rows = cursor.ferchall()
# print(rows)
#insert into list(id,name,id_chat,status,track) values ('','sanya','418871128',false,'instsanya')
#select * from list
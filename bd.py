import psycopg2 as p
connect = p.connect("dbname=list user=postgres password=1478 ")
cursor = connect.cursor()
cursor.execute("select * from list")
rows = cursor.ferchall()
print(rows)
#insert into list(id,name,id_chat,status,track) values ('','sanya','418871128',false,'instsanya')
#select * from list
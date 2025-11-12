import psycopg2 

#sudo systemctl start postgresql

connect = psycopg2.connect("dbname=alunos_db user=postgres")

cur = connect.cursor()
cur.execute("CREATE TABLE Ana (id serial PRIMARY KEY, num integer, data varchar);")

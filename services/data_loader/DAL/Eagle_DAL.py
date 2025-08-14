import mysql.connector
from DAL.DAL import DAL
from Models.Person import Person

class Eagle_DAL:
    
    def __init__(self,host,user,password, dbname ,table_name):
        db= DAL(host,user,password, dbname)
        self.table_name = table_name
        self.conn = db.get_conn()
   

    def Select(self):
        cursor =self.conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def add(self , person):
        cursor = self.conn.cursor()
        query  = f"""INSERT INTO {self.table_name} (first_name, last_name) VALUES (%s, %s) """
        cursor.execute(query, (person.first_name, person.last_name))

        self.conn.commit()
        cursor.close()

    def edit(self, person):
        cursor = self.conn.cursor()
        query = f"""UPDATE {self.table_name} SET first_name = %s, last_name = %s WHERE id = %s """
        cursor.execute(query, (person.first_name, person.last_name, person.id))
         
        self.conn.commit()
        cursor.close()



    def delete(self ,person):
        cursor = self.conn.cursor()
        query =f"""DELETE FROM {self.table_name} WHERE id = %s"""
        cursor.execute(query, (person.id ,))
        self.conn.commit()
        cursor.close()               

    def c(self):
        self.conn.close()
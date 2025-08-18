import pymongo
from DAL.DAL import DAL
from Models.Person import Person

class Eagle_DAL:
    
    def __init__(self,host,user,password, dbname ,collecsion_conn):
        db= DAL(host,user,password, dbname)
        self.collecsion_conn = collecsion_conn
        conn = db.get_conn()
        self.collecsion = conn[collecsion_conn]

   
# ---------------------------------------------------------------------------------------

    def Select(self):
        result = self.collecsion.find()
        return [x for x in result]
# ---------------------------------------------------------------------------------------
    def add(self , person):

        new_person = {"id":person.id , "first_name" :person.first_name , "last_name": person.last_name}

        self.collecsion.insert_one(new_person)
        
# ---------------------------------------------------------------------------------------

    def edit(self, person):
        myquery ={"id":person.id}
        newvalues = {"$set" : {"first_name" :person.first_name , "last_name": person.last_name}}

        self.collecsion.update_one(myquery , newvalues)
        


# ---------------------------------------------------------------------------------------

    def delete(self ,person):
        self.collecsion.delete_one({"id":person.id})
               

    def c(self):
        pass
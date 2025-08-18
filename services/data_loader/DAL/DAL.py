import pymongo
class DAL:
    def __init__(self ,host,user,password, dbname) -> None:

        myclient = pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:27017/")
        self.conn = myclient[dbname]     

    def get_conn(self):
        return self.conn
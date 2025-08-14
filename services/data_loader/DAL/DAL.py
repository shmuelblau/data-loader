import mysql.connector
class DAL:
    def __init__(self ,host,user,password, dbname) -> None:

        self.conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=dbname,
        port=3306,
        auth_plugin='mysql_native_password'
    )
       

    def get_conn(self):
        return self.conn
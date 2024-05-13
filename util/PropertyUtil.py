class PropertyUtil:
        #passes the parameters required for making connection with database in the form of string 
    @staticmethod
    def getPropertyString():
        host = 'localhost'
        database = 'cars'
        user = 'root'
        password = 'Priyanshu2003'
        return host, database, user, password

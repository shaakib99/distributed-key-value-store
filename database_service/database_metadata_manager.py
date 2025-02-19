from database_service.mysql_database import MySQLDatabase
from database_service.mysql_database import Base


id_remaining = [i for i in range(1, 2001)]

class DatabaseMetadataManager:
    def __init__(self):
        self.databases = [
        {
            "host": "mysql://root:root@localhost:3306/test",
            "type": "mysql",
            "key_start": 1,
            "key_end": 1000
        },
        {
            "host": "mysql://root:root@localhost:3307/test",
            "type": "mysql",
            "key_start": 1001,
            "key_end": 2000
        }
    ]


    def get_db(self,key: str) -> "MySQLDatabase":
        for db in self.databases:
            if db["key_start"] <= int(key) <= db["key_end"]:
                if db["type"] == "mysql":
                    return MySQLDatabase.get_instance(db["host"])
        raise Exception("Database not found")
    
    def create_tables(self):
        for db in self.databases:
            if db["type"] == "mysql":
                instance = MySQLDatabase.get_instance(db["host"])
                Base.metadata.create_all(instance.engine)
    
    def get_all_db(self):
        databases = []
        for db in self.databases:
            if db["type"] == "mysql":
                databases.append(MySQLDatabase.get_instance(db["host"]))
        return databases 
    
    def get_key(self):
        if id_remaining:
            return id_remaining.pop(0)
        raise Exception("No more keys available")
    
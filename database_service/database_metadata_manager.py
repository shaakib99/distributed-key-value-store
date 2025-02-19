from database_service.mysql_database import MySQLDatabase
from functools import cache

dbs = [
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

id_remaining = [i for i in range(1, 2001)]

class DatabaseMetadataManager:
    def __init__(self):
        pass

    @cache
    def get_db(self,key: str):
        for db in dbs:
            if db["key_start"] <= int(key) <= db["key_end"]:
                if db["type"] == "mysql":
                    return db
                    return MySQLDatabase.get_instance(db["host"])
        raise Exception("Database not found")
    
    def get_key(self):
        if id_remaining:
            return id_remaining.pop(0)
        raise Exception("No more keys available")
    
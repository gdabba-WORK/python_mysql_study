import mysql
from mysql.connector.pooling import MySQLConnectionPool


class ExplicitlyConnectionPool(object):
    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        else:
            self.__cnxPool = MySQLConnectionPool(pool_name="myPool", pool_size=5, option_files="db_config.conf")

    @classmethod
    def get_instance(cls, *args, **kargs):
        if cls.INSTANCE is None:
            cls.INSTANCE = ExplicitlyConnectionPool()
            # cls.INSTANCE = cls(*args, **kargs)
        return cls.INSTANCE

    def get_connection(self):
        return self.__cnxPool.get_connection()

    @classmethod
    def pool_close(cls):
        cls.INSTANCE = None


def get_implicitly_connection(_pool_size):
    return mysql.connector.connect(pool_name="myPool", pool_size=_pool_size, option_files='db_config.conf')

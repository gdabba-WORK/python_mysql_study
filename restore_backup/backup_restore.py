from mysql.connector import errorcode, Error
from connection_pool.connection_pool_study02 import ExplicitlyConnectionPool
from ddl_extern.read_ddl import read_ddl_file


class BackupRestore:
    def __init__(self):
        self._db = read_ddl_file()

    def data_backup(self):
        try:
            sql = read_ddl_file()
            conn = ExplicitlyConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self._db['database_name']))
            print("CREATE DATABASE {}".format(self._db['database_name']))
        except Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                cursor.execute("DROP DATABASE {}".format(self._db['database_name']))
                print("DROP DATABASE {}".format(self._db['database_name']))
                cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.db['database_name']))
                print("CREATE DATABASE {}".format(self._db['database_name']))
            else:
                print(err.msg)
        finally:
            cursor.close()
            conn.close()


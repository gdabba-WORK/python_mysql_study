import inspect
from connection_pool.connection_pool_study01 import DatabaseConnectionPool

def connection_pool01():
    print("=={}()==".format(inspect.stack()[0][3]))
    connection = DatabaseConnectionPool.get_instance().get_connection()
    print(type(connection), connection)
    connection.close()


if __name__ == "__main__":
    for i in range(10):
        connection_pool01()
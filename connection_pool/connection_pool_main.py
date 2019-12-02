import inspect
from connection_pool.connection_pool_study01 import DatabaseConnectionPool
from connection_pool.connection_pool_study02 import ExplicitlyConnectionPool, get_implicitly_connection


def connection_pool01():
    print("=={}()==".format(inspect.stack()[0][3]))
    connection = DatabaseConnectionPool.get_instance().get_connection()
    print(type(connection), connection)
    connection.close()


def explicitly_connection_pool():
    print("=={}()==".format(inspect.stack()[0][3]))
    connectionPool = ExplicitlyConnectionPool.get_instance()
    connection = connectionPool.get_connection()
    print(type(connection), connection)
    connection.close()


def implicitly_connection_pool():
    print("=={}()==".format(inspect.stack()[0][3]))
    connection = get_implicitly_connection()
    print(type(connection), connection)
    connection.close()


if __name__ == "__main__":
    # for i in range(10):
    #     connection_pool01()
    explicitly_connection_pool()
    implicitly_connection_pool()

    explicitly_connection_pool()
    implicitly_connection_pool()


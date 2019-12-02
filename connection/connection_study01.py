from mysql.connector import Error, MySQLConnection

from connection.python_mysql_dbconfig import read_db_config


def connect():
    try:
        conn = MySQLConnection(host="localhost",
                               database="mysql",
                               user="root",
                               password="rootroot")
        if conn.is_connected():
            print("Connected to MySQL database")
            print(type(conn), conn)

    except Error as e:
        print(e)
    finally:
        conn.close()
        print("Connection closed.")


def connect_use_config():
    db_config = read_db_config()

    try:
        print("Connecting to MySQL database.")
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print("connection established")
            print(type(conn), conn)
        else:
            print("connection failed")
    except Error as error:
        print(error)

    finally:
        conn.close()
        print("Connection closed")
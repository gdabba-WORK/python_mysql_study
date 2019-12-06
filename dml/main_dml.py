from dml.coffee_insert import insert_product, insert_products
from dml.coffee_select import query_with_fetchone
from dml.coffee_select import query_with_fetchall
from dml.coffee_select import query_with_fetchall2
from dml.coffee_select import query_with_fetchall_by_code

from dml.connection_pool import ConnectionPool
from dml.transaction_query import transaction_fail1, transaction_fail2, transaction_success
from dml.create_procedure import create_procedure
from dml.coffee_procedure import call_sale_stat_sp, call_order_price_by_issale


def connection_pool_method():
    connect_pool = ConnectionPool.get_instance()
    print("connection pool : ", connect_pool)
    connection = connect_pool.get_connection()
    print("connection : ", connection)


def query_with_fetchone_method():
    global select_sql
    select_sql = "select * from product"
    query_with_fetchone(select_sql)


def query_with_fetchall_method():
    global select_sql
    # sql = "select * from product"
    select_sql = "select * from product"
    query_with_fetchall(select_sql)


# query_with_fetchall_method를 아래와 같이 sql의 where절의 비교 value를 code와 같은 변수로 분리해서 사용해도 된다.
def query_with_fetchall_method2():
    global select_sql
    code = '\'A001\''
    select_sql = "select * from product where code = {}".format(code)
    print(select_sql)
    query_with_fetchall(select_sql)


def query_with_fetchall2_method():
    global select_sql
    select_sql = "select * from product"
    res = query_with_fetchall2(select_sql)
    print(type(res), 'size = ', len(res), '\n', res)
    for pno, pname in res:
        print(pno, pname)


def query_with_fetchall_by_code_method():
    global select_sql
    select_sql = "select * from product where code = %s"
    code = 'A001'
    res = query_with_fetchall_by_code(select_sql, code)
    print(type(res), 'size = ', len(res), '\n', res)
    for pno, pname in res:
        print(pno, pname)


def insert_product_method():
    global insert_sql
    query_with_fetchall_method()
    insert_product(insert_sql, 'C001', '라떼')
    query_with_fetchall_method()


def insert_products_method():
    global insert_sql
    products = [('C002', '라떼2'), ('C003', '라떼3'), ('C004', '라떼4')]
    insert_products(insert_sql, products)
    query_with_fetchall_method()


if __name__ == "__main__":
    # connection_pool_method()
    select_sql = ""

    # query_with_fetchone_method()

    # query_with_fetchall_method()

    # query_with_fetchall_method2()

    # query_with_fetchall2_method()

    # query_with_fetchall_by_code_method()

    insert_sql = "Insert into product values(%s, %s)"

    # insert_product_method()

    # insert_products_method()

    # transaction_fail1()

    # transaction_fail2()

    # transaction_success()

    # create_procedure()

    # call_sale_stat_sp('proc_sale_stat')

    call_order_price_by_issale('proc_saledetail_orderby', True)
    call_order_price_by_issale('proc_saledetail_orderby', False)
    # print()
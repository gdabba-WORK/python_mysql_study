from mysql.connector import Error, errorcode
from dml.connection_pool import ConnectionPool

PROCEDURE_NAME = ["proc_sale_stat", "proc_saledetail_orderby"]
PROCEDURE_SRC = ["""
                CREATE PROCEDURE proc_sale_stat()
                BEGIN
                    select
                        sum(@saleprice := price*salecnt) sale_price,
                        sum(@addtax := ceil(@saleprice/11)) addtax_price,
                        sum(@supprice := @saleprice - @addtax) supply_price,
                        sum(@marPrice := round(@supprice * (marginrate/100))) margin_price
                    from sale s join product p on s.code = p.code;
                END
                """,
                """
                CREATE PROCEDURE proc_saledetail_orderby (in isSalePrice boolean)
                BEGIN
                    IF isSalePrice THEN
                        SELECT (SELECT COUNT(*)+1 FROM sale_detail s2 where s2.sale_price > s1.sale_price) rank,
                            sale.code code, p.name name, price, salecnt, supply_price, addTax,
                            sale_price, marginRate, marginPrice
                        FROM sale INNER JOIN sale_detail s1 ON sale.no = s1.no JOIN product p ON sale.code = p.code
                            ORDER BY rank;
                    ELSE
                        SELECT (SELECT COUNT(*)+1 FROM sale_detail s2 where s2.marginPrice > s1.marginPrice) rank,
                            sale.code code, p.name name, price, salecnt, supply_price, addTax,
                            sale_price, marginRate, marginPrice
                        FROM sale INNER JOIN sale_detail s1 ON sale.no = s1.no JOIN product p ON sale.code = p.code
                            ORDER BY rank;
                    END IF;
                END
                """]


def create_procedure():
    for proc_name, proc_src in zip(PROCEDURE_NAME, PROCEDURE_SRC):
        try:
            conn = ConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute(proc_src)
            print("CREATE PROCEDURE {}".format(proc_name))
        except Error as err:
            # print(err)
            if err.errno == errorcode.ER_SP_ALREADY_EXISTS:
                cursor.execute("DROP PROCEDURE {}".format(proc_name))
                print("DROP PROCEDURE {}".format(proc_name))
                cursor.execute(proc_src)
                print("CREATE PROCEDURE {}".format(proc_name))
            else:
                print(err.msg)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

import pyodbc

def impalaDecorator(fn):
    def wrapper():
        conn = fn()
        return conn.cursor()
    return wrapper

@impalaDecorator
def impalaCursor():
    conn = pyodbc.connect(f"""
                DSN=Sample Cloudera Impala DSN;
                server=172.30.1.210;
                port:21050;
                Database=default;
                """,autocommit = True)
    return conn


# cursor = impalaCursor()

# cursor.execute("show tables;") 
# row = cursor.fetchone() 
# while row: 
#     print(row[0])
#     row = cursor.fetchone()
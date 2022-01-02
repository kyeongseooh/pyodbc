import pyodbc

def impalaDecorator(fn):
    def wrapper(*args, **kwargs):
        conn = fn(*args, **kwargs)
        return conn
    return wrapper

@impalaDecorator
def impala():
    conn = pyodbc.connect(f"""
                DSN=Sample Cloudera Impala DSN;
                server=172.30.1.210;
                port:21050;
                Database=default;
                """,autocommit = True)
    return conn

@impalaDecorator
def odbc(*args, **kwargs):
    conn = pyodbc.connect(*args, **kwargs)
    return conn


# cursor = odbc(f"""
#                 DSN=Sample Cloudera Impala DSN;
#                 server=172.30.1.210;
#                 port:21050;
#                 Database=default;
#                 """,autocommit = True).cursor()

# # cursor = impala().cursor()

# cursor.execute("show tables;") 
# row = cursor.fetchone() 
# while row: 
#     print(row[0])
#     row = cursor.fetchone()
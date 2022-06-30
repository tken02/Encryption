import pyodbc


connect = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=TNKAY;"
    "Database=ANMTDB;"
    "Trusted_Connection=yes;"
)

insert = connect.cursor()
insert.execute("SELECT * FROM USERINFO")
tables = insert.fetchall()
data = tables[0][0]
print(data)
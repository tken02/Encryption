import pyodbc
import gen_key


connect = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-OHDTVOL\MSSQLSERVER_CUS;"
    "Database=ANMTDB;"
    "Trusted_Connection=yes;"
)


def checkUserPassword(email, password):
    query = f"SELECT * FROM USERINFO WHERE EMAIL = '{email}' AND MATKHAU = {password}"
    print(email)
    print(password)
    exec = connect.cursor()
    exec.execute(query)
    if exec.rowcount != 0:
        data = exec.fetchall()
        exec.close()
        return True, data
    else:
        exec.close()
        return False, ""


def insertUser(email, name, dOBird, address, phone, passwordHash, privateKey, nonce, publicKey, salt):
    insert = f"EXEC SP_INS_USER '{email}','{name}','{dOBird}','{address}','{phone}',{passwordHash},{privateKey},{nonce},{publicKey},'{salt}')"
    print(insert)
    update = connect.cursor()
    update.execute(insert)
    update.commit()
    update.close()


def getSalt(email):
    satl = f"SELECT SATL FROM USERINFO WHERE EMAIL = '{email}'"
    insert = connect.cursor()
    insert.execute(satl)
    tables = insert.fetchall()
    insert.close()
    return tables[0][0]


def updateUserData(email, name, dOBird, address, phone, password, privateKey, nonce):
    updateQuery = f" EXEC SP_UPDATE_INFO '{email}', '{name}', '{dOBird}', '{address}', {phone}, {password}, {privateKey}, {nonce}"
    print(updateQuery)
    update = connect.cursor()
    update.execute(updateQuery)
    update.commit()
    update.close()


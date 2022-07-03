import pyodbc
import gen_key
from Crypto.Hash import SHA256

connect = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=TNKAY;"
    "Database=ANMTDB;"
    "Trusted_Connection=yes;"
)
query = "SELECT DULIEU FROM FILEDATA1 WHERE ID = 2"
exec = connect.cursor()
exec.execute(query)
data = exec.fetchall()
print(data[0][0].decode('utf-8'))

def getPublicKey(email):
    try:
        query = f"SELECT PUBLICKEY FROM USERINFO WHERE EMAIL = '{email}'"
        exec = connect.cursor()
        exec.execute(query)
        if exec.rowcount != 0:
            data = exec.fetchall()
            print(data[0][0])
            exec.close()
            return data[0][0]
        else:
            exec.close()
            return  []
    except:
        
        return False


def getUserKey():
    query = "SELECT EMAIL , PUBLICKEY  FROM USERINFO"
    exec = connect.cursor()
    exec.execute(query)
    if exec.rowcount != 0:
        data = exec.fetchall()
        exec.close()
        return data
    else:
        exec.close()
        return  []

def insertData(email, tenfile, dulieu):
    print(email)
    query = f"EXEC SP_INS_DATA '{email}', '{tenfile}', {dulieu}"
    print(query)
    insert = connect.cursor()
    insert.execute(query)
    insert.commit()
    insert.close()
    return True

def getData(email):
    query = f"SELECT * FROM USERINFO WHERE EMAIL = '{email}'"
    exec = connect.cursor()
    exec.execute(query)
    if exec.rowcount != 0:
        data = exec.fetchall()
        exec.close()
        return data
    else:
        exec.close()
        return  ""


def checkUserPassword(email, password):
    print(password)
    query = f"SELECT * FROM USERINFO WHERE EMAIL = '{email}' AND MATKHAU = {password}"
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
    try:
        inserts = f"EXEC SP_INS_USER '{email}','{name}','{dOBird}','{address}',{phone},{passwordHash},{privateKey},{nonce},{publicKey},'{salt}'"
        print(inserts)
        insert = connect.cursor()
        insert.execute(inserts)
        insert.commit()
        insert.close()
        return True
    except:
        return False


def getSalt(email):
    satl = f"SELECT SATL FROM USERINFO WHERE EMAIL = '{email}'"
    insert = connect.cursor()
    insert.execute(satl)
    tables = insert.fetchall()
    insert.close()
    return tables[0][0]


def updateUserData(email, name, dOBird, address, phone, password, privateKey, nonce):
    try:
        updateQuery = f" EXEC SP_UPDATE_INFO '{email}', '{name}', '{dOBird}', '{address}', {phone}, {password}, {privateKey}, {nonce}"
        update = connect.cursor()
        update.execute(updateQuery)
        update.commit()
        update.close()
        return True
    except:
        return False
    
    
def getListFile(email):
    try:
        list = f"EXEC SP_GET_LISTDATA '{email}'"
        print(list)
        insert = connect.cursor()
        insert.execute(list)
        tables = insert.fetchall()
        insert.commit()
        insert.close()
        return tables
    except:
        return False
    
def getFileData(email,tenfile):
    try:
        file = f"EXEC SP_GET_FILEDATA '{email}', '{tenfile}'"
        print(file)
        insert = connect.cursor()
        insert.execute(file)
        tables = insert.fetchall()
        insert.commit()
        insert.close()
        return tables[0][0]
    except:
        return False

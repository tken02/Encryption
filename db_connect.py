import pyodbc
import gen_key
from Crypto.Hash import SHA256

connect = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=TNKAY;"
    "Database=ANMTDB;"
    "Trusted_Connection=yes;"
)


def checkUserPassword(email, password):
    passwordSalt, salt = gen_key.genSalt(password)
    passwordHash = hex(int(SHA256.new(passwordSalt.encode('utf-8')).hexdigest(), 16))
    print(passwordHash)
    query = f"SELECT * FROM USERINFO WHERE EMAIL = '{email}' AND MATKHAU = {passwordHash}"
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
    inserts = f"EXEC SP_INS_USER '{email}','{name}','{dOBird}','{address}',{phone},{passwordHash},{privateKey},{nonce},{publicKey},'{salt}'"
    print(inserts)
    insert = connect.cursor()
    insert.execute(inserts)
    insert.commit()
    insert.close()


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
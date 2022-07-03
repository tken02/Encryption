
import db_connect as db
from Crypto.Hash import SHA256
import gen_key


def signUp(email, name, dOBird, address, phone, password):
    passwordSalt, salt = gen_key.genSalt(password)
    passwordHash = hex(int(SHA256.new(passwordSalt.encode('utf-8')).hexdigest(), 16))
    publicKey, priKey, nonce = gen_key.genKeyPair(2048, password)
    
    # convert to hex
    publicKey = '0x' + publicKey.hex()
    priKey = '0x' + priKey.hex()
    nonce = '0x' + nonce.hex()
    return db.insertUser(email, name, dOBird, address, phone,
                  passwordHash, priKey, nonce, publicKey, salt)

#signUp("khanhnu","khanh","02/01/2001","tnkay",103108391,"12345")
def signIn(email, password ):
    password_salt = password + '_ANMT_' + db.getSalt(email)
    password_hash = hex(int(SHA256.new(password_salt.encode('utf-8')).hexdigest(), 16))
    correctUser, data = db.checkUserPassword(email, password_hash)
    return correctUser,data 


def updateInfo(data,email, name, dOBird, address, phone,oldPass , newPass):
    password_salt, salt = gen_key.genSalt(newPass, satl=data[0][9])
    # hashed_string = hex(int(hashlib.sha256("hung".encode('utf-8')).hexdigest(), 16))
    password_hash = hex(int(SHA256.new(password_salt.encode('utf-8')).hexdigest(), 16))
    oldKeyCipher = data[0][6]
    oldNonce = data[0][7]
    privateK, nonceK = gen_key.handleNewPass(oldKeyCipher, oldPass, oldNonce, newPass)
    return db.updateUserData(email, name, dOBird, address,
                      phone, password_hash, '0x' + privateK.hex(), '0x' + nonceK.hex())


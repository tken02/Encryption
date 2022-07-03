import hashlib
from turtle import end_fill
import rsa
import base64
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

#RSA:
def generate_key():
    pub_key, pr_key = rsa.newkeys(1024)
    return pub_key, pr_key

def signSHA256(filepath,privateKey):
    signFile = filepath.split('/')[-1]
    outputPath = filepath.replace(filepath.split('/')[-1],signFile+'.sig')
    # print(outputPath)
    try:
        with open(filepath, "rb") as image_file:
            encoded_string = image_file.read()
        # print(hashFILE)
        cipher_rsa = RSA.import_key(privateKey)
        hashFILE = SHA256.new(encoded_string)
        sign = pkcs1_15.new(cipher_rsa).sign(hashFILE)
        
        print('sign',sign)
        file = open(outputPath,'wb')
        file.write(sign)
        file.close()
        return True
    except:
        return False

def verifySign(filepath,signpath, data_email_publicK):
    list_user = {}
    for i in  range(len(data_email_publicK)):
        list_user[data_email_publicK[i][0]] =  data_email_publicK[i][1]
    
    print(list_user)
    with open(filepath, "rb") as image_file:
        encoded_string = image_file.read()
    
    hashFILE = SHA256.new(encoded_string)
    print(hashFILE)
    file = open(signpath,'rb')
    sign = file.read()
    file.close()
    # print('sign',sign)
    for user in list_user:
        cipher_rsa = RSA.import_key(list_user[user])
        try:
            pkcs1_15.new(cipher_rsa).verify(hashFILE,sign)
            return True,user
        except (ValueError, TypeError):
            continue    
    return False, ''

# print('pubK',pubK)
# print('priK',priK)
# signSHA256('',priK)
# file = open('a.txt.sig','rb')
# print(file.read())
# verifySign('','',pubK)


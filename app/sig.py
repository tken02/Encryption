import hashlib
from turtle import end_fill
import rsa
import base64

#RSA:
def generate_key():
    pub_key, pr_key = rsa.newkeys(1024)
    return pub_key, pr_key
def signSHA256(filepath,privateKey):
    signFile = filepath.split('/')[-1]
    try:
        with open(filepath, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        sign = rsa.sign(encoded_string, privateKey, 'SHA-256')
        file = open(signFile+'.sig','wb')
        file.write(sign)
        file.close()
        return True
    except:
        return False

def verifySign(filepath,signpath,publicKey):
    with open("a.txt", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    file = open('a.txt.sig','rb')
    sign = file.read()
    try:
        rsa.verify(encoded_string, sign, pubK)
        return True
    except:
        print('not valid')
        return False

pubK,priK= generate_key()
# print('pubK',pubK)
# print('priK',priK)
# signSHA256('',priK)
# file = open('a.txt.sig','rb')
# print(file.read())
# verifySign('','',pubK)


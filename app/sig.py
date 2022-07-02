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
    outputPath = filepath.replace(filepath.split('/')[-1],signFile+'.sig')
    # print(outputPath)
    try:
        with open(filepath, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        sign = rsa.sign(encoded_string, privateKey, 'SHA-256')
        print('sign',sign)
        file = open(outputPath,'wb')
        file.write(sign)
        file.close()
        return True
    except:
        return False

def verifySign(filepath,signpath,publicKey):
    print(publicKey)
    # print('p',filepath)
    # print('s',signpath)
    p1,k1 = generate_key()
    p2,k2 = generate_key()
    p3,k3 = generate_key()
    p4,k4 = generate_key()
    list_user = {
        'user1' : p1,
        'user2' : p2,
        'user3' : p3,
        'teo' : publicKey
    }

    with open(filepath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    file = open(signpath,'rb')
    sign = file.read()
    # print('sign',sign)
    for user in list_user:
        # print(user,user.values())
        try:
            rsa.verify(encoded_string, sign,list_user[user])
            return True, user
        except:
            continue
    return False, ''

# print('pubK',pubK)
# print('priK',priK)
# signSHA256('',priK)
# file = open('a.txt.sig','rb')
# print(file.read())
# verifySign('','',pubK)


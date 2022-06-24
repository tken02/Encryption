from Crypto.Cipher import AES

def padding(key):
    tem = key
    while len(tem) < 16:
        tem = tem +" "
    return bytes(tem,'utf-8')

def encry_AES(key, msg):
    cipher = AES.new(key,AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt_AES(key, nonce, ciphertext,tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except ValueError:
        return False



if __name__ == "__main__":
    key = padding("khanh")
    n,c,t = encry_AES(key,"khanhnggu")
    print(c);
    p = decrypt_AES(key,n,c,t)
    if not p:
        print("plaintxt: {p}")
    else:
        print(f'plaintxt:{p}')
   
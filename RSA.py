import rsa
#RSA:
def generate_key():
    pub_key, pr_key = rsa.newkeys(1024)
    return pub_key, pr_key

def encry_RSA(msg,key):
    return rsa.encrypt(msg.encode('ascii'),key)

def decry_RSA(cipher,key):
    try:
        return rsa.decrypt(cipher,key).decode('ascii')
    except:
        return False

# if __name__ == "__main__":
#     pb,pr = generate_key()
#     c = encry_RSA("khanh",pb)
#     print(c)
#     p = decry_RSA(c,pr)
#     print(p)
from math import fabs
from tkinter import EW
import gen_key as gk
import rsa
import RSA as cr
import ast
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

def encry_file(filename ,publicKey):
    print(type(publicKey))
    print(publicKey)
    #gen Ksession
    Ksession = gk.genKsession()
    with open(filename, "rb") as f:
        data = f.read()
    ciphertext_data, nonce = gk.encryptKey(data,Ksession)
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(publicKey))
    encry_Ksesion = cipher_rsa.encrypt(Ksession.encode('utf-8'))
    encry_data_and_key = {"data":ciphertext_data, "Ksession": encry_Ksesion, "nonce":nonce}
    print(type(str(encry_data_and_key)))
    return '0x'+ str(encry_data_and_key).encode('utf-8').hex()

def decry_file(cipherFile, Kpri):
    print(cipherFile)
    data_and_key = ast.literal_eval(cipherFile)
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(Kpri))
    Ksession = cipher_rsa.decrypt(data_and_key["Ksession"])
    Nonce = data_and_key["nonce"]
    return gk.decryptKey(data_and_key["data"],Ksession.decode('utf-8'),Nonce)
    
# if __name__ == "__main__":
#     pb,pr = cr.generate_key()
#     try:
#         data = encry_file("input.jpg",pb)
#         plaintext = decry_file(data,pr)
#         with open("outpur.jpg", "wb") as binary_file:
#             binary_file.write(plaintext)
#     except:
#         print(0)

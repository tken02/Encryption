from tkinter import EW
import gen_key as gk
import rsa
import RSA as cr
import ast

def encry_file(filename ,publicKey):
    Ksession = gk.genKsession()
    with open(filename, "rb") as f:
        data = f.read()
    
    ciphertext_data, nonce = gk.encryptKey(data,Ksession)
    pub_key = publicKey
    # pub_key = data[0][8]
    encry_Ksesion =  rsa.encrypt(str(Ksession).encode('ascii'),pub_key)
    encry_data_and_key = {"data":ciphertext_data, "Ksession": encry_Ksesion, "nonce":nonce}
    
    return str(encry_data_and_key)

def decry_file(cipherFile, Kpri):
    # data_and_key = json.loads(cipherFile)
    data_and_key = ast.literal_eval(cipherFile)
  
    Ksession = cr.decry_RSA(data_and_key["Ksession"],Kpri)
    Nonce = data_and_key["nonce"]
    return gk.decryptKey(data_and_key["data"],Ksession,Nonce)
    
if __name__ == "__main__":
    pb,pr = cr.generate_key()
    data = encry_file("input.jpg",pb)
    plaintext = decry_file(data,pr)
   
    with open("outpur.jpg", "wb") as binary_file:
	    binary_file.write(plaintext)

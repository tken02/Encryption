from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Cipher import AES, PKCS1_OAEP
from rsa import PublicKey
from Crypto.Signature import pkcs1_15

keypair = RSA.generate(1024)
keypub = keypair.public_key().export_key()
pri = keypair.export_key()




with open("a.txt", "rb") as image_file:
    encoded_string = image_file.read()


#hashFILE = hex(int(SHA256.new(encoded_string).hexdigest(), 16)).encode('utf-8')
hashFILE = "kafan"

# Encrypt the session key with the public RSA key
cipher_rsa1 = RSA.import_key(pri)
hashFILE = SHA256.new(encoded_string)

sign = pkcs1_15.new(cipher_rsa1).sign(hashFILE)
print(sign)

#de 
# cipher_rsa = PKCS1_OAEP.new(RSA.import_key(pri))
# session_key = cipher_rsa.decrypt(enc_session_key)
# prin(session_key.decode('utf-8'))

# if hashFILE == session_key:
#     print("dung")


''
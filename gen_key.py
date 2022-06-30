from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Cipher import AES, PKCS1_OAEP
import random

def genKeyPair(size, passphase):
    keypair = RSA.generate(size)
    passphase = passphase + "0123456789101112"
    passphase = passphase[:16]
    cipher = AES.new(passphase.encode('utf-8'), AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(keypair.export_key())
    return keypair.public_key().export_key(), ciphertext, nonce

def encryptKey(plaintext, passphase):
    passphase = passphase + "0123456789101112"
    passphase = passphase[:16]
    cipher = AES.new(passphase.encode('utf-8'), AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return ciphertext, nonce

def decryptKey(ciphertext, passphase, nonce):
    passphase = passphase + "0123456789101112"
    passphase = passphase[:16]
    cipher = AES.new(passphase.encode('utf-8'), AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def handleNewPass(ciphertext, oldpassphare, oldnonce, newpassphare):
    prvateKey = decryptKey(ciphertext,oldpassphare,oldnonce)
    return encryptKey(prvateKey,newpassphare)


def genKsession():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = []
    for i in range(16):
        chars.append(random.choice(ALPHABET))
    return  "".join(chars)

def genSalt(password, satl =None):
    if satl is None:
        ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        chars = []
        for i in range(16):
            chars.append(random.choice(ALPHABET))
        satlN = "".join(chars)
        return password + '_ANMT_' + satlN, satlN
    return password + '_ANMT_' + satl, satl


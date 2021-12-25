#27-3-2021
from Crypto.Cipher import AES
from getpass import getpass

key = ''
key = str.encode(key)

data = "#Vu Hoai Nam - VN1103 - 28/3/2021"
data = data.encode()
t = open('T.txt','wb')
t.write(data)
t.close()

cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

f = open("tag.txt","wb")
f.write(tag)
f.close()
f = open("nonce.txt","wb")
f.write(nonce)
f.close();
t = open("C.txt","wb")
t.write(ciphertext)
t.close();

f = open("tag.txt","rb")
tag = f.read()
f.close()
f = open("nonce.txt","rb")
non = f.read()
f.close();

t = open("C.txt","rb")
d = t.read()
t.close();

cipher = AES.new(key, AES.MODE_EAX, nonce=non)
plaintext = cipher.decrypt(d)
try:
    cipher.verify(tag)
    print("Authentic!")
except ValueError:
    print("Key incorrect or message corrupted")

p = plaintext.decode()
print(p)

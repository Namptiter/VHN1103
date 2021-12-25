#27-3-2021 - VHN1103
from Crypto.Cipher import AES
from getpass import getpass
import os, sys
class Switch(object):
    def out(self):
        print('[ok]Type "ok" if you really want to out: ', end='')
        t = input()
        if(t=='ok'):
            try:
                t = open('T.txt','w')
                t.write('-')
                t.close()
                os.remove('T.txt')
                print('Bye!')
                sys.exit()
            except:
                ch()
        else:
            ch()
    def read(self):
        key = getpass("[key]>> ")
        key = str.encode(key)

        t = open('C.txt', 'rb')
        data = t.read()
        t.close()

        #check password
        non, plaintext = checkPass(key, data)

        # cipher = AES.new(key, AES.MODE_EAX, nonce=non)
        # plaintext = cipher.decrypt(data)
        p = plaintext.decode()

        t = open('T.txt', 'w', encoding='utf-8');
        t.write(p);
        t.close();
        print("Data is Decoded!")
        ch()
    def work(self):
        try:
            key = getpass("[key]>> ")
            key = str.encode(key)

            t = open('C.txt', 'rb')
            data = t.read()
            t.close()

            #check password
            non,_ = checkPass(key, data)

            c = open('T.txt', 'r', encoding='utf-8')
            data = c.read()
            data = str.encode(data)

            cipher = AES.new(key, AES.MODE_EAX)
            nonce = cipher.nonce
            ciphertext, tag = cipher.encrypt_and_digest(data)

            f = open("tag.txt","wb")
            f.write(tag)
            f.close()
            f = open("nonce.txt","wb")
            f.write(nonce)
            f.close();
            f=open("C.txt", "wb");
            f.write(ciphertext)
            f.close()

            print("Data is Encrypted!")
            ch()
        except:
            print("ERROR")
            ch()

    def sw(self, i):
        method_name=str(i)
        method=getattr(self,method_name,lambda :'Invalid')
        return method()

def checkPass(key, data):
    t = open("nonce.txt","rb")
    non = t.read()
    t.close()
    t = open("tag.txt","rb")
    tag = t.read()
    t.close()

    cipher = AES.new(key, AES.MODE_EAX, nonce=non)
    plaintext = cipher.decrypt(data)
    cipher.verify(tag)
    print("Authentic!")
    return non, plaintext
def ch():
    print("[read, work, out]>> ", end='')
    t = str(input())
    s = Switch()
    s.sw(t)

def main():
    #command
    ch()

if __name__ == "__main__":
    main()

#!/usr/bin/env python
#coding: utf-8

import zlib
import hashlib
import binascii
import sys
from os import system,name
from time import sleep


#globally assigning color values
if sys.platform == "linux2" or sys.platform == "linux":
    #Green \033[1;36m \033[1;m
    #def prGreen(skk): 
    # print("\033[92m {}\033[00m" .format(skk)) 
    G="\033[32;1m"
    R = "\033[31;1m"
    Y="\033[33;1m"

elif sys.platform == "win32":
    G=""
    R=""



#banner_for_logo
def banner():
    print(''' \033[1;36m
-------------------------------------------------------------------------------        
-------------------------------------------------------------------------------
+                         <<<<< ALL HASH GENERATOR>>>>>                       +
+                     GitHub : www.github.com/monishmonish                    +
+         DEVELOPED BY : MONISH KUMAR R       +
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------     \n \033[1;m''')

#clearing the screen
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear') 


def hashing(get_input):
    #encoding code for hexadecimal conversion
    encoded_input=get_input.encode()
    print("-"*80)
   
    '''
    #md2
    m=MD2.new()
    m.update(get_input)
    print(G+"{+}The MD2 Hash Value Of Your Input Is {+}: "+m.hexdigest())
    '''
    

    #md4
    m = hashlib.new("md4")
    m.update(get_input)
    md4_hash = m.hexdigest()
    print(G+"{+}The MD4 Hash Value Of Your Input Is {+}: "+Y+md4_hash)

    #md5
    md5_hash=hashlib.md5(encoded_input)
    print(G+"{+}The MD5 Hash Value Of Your Input Is {+}: "+Y+md5_hash.hexdigest())

    #md5 crypt
    from passlib.hash import md5_crypt as mc
    md5_crypt = mc.encrypt(get_input)
    print (G+"{+}The MD5 Crypt Hash Value Of Your Input Is {+}: "+Y+md5_crypt)

    #sun md5 crypt
    from passlib.hash import sun_md5_crypt as mc
    sunmd5_crypt = mc.encrypt(get_input)
    print (G+"{+}The Sun MD5 Crypt Hash Value Of Your Input Is {+}: "+Y+sunmd5_crypt)

    #apache's md5 crypt
    from passlib.hash import apr_md5_crypt as mc
    apachemd5_crypt = mc.encrypt(get_input)
    print (G+"{+}The Apache MD5 Crypt Hash Value Of Your Input Is {+}: "+Y+apachemd5_crypt)

    
    #sha1
    sha1_hash=hashlib.sha1(encoded_input)
    print(G+"{+}The SHA1 Hash Value Of Your Input Is {+}: "+Y+sha1_hash.hexdigest())
    
    #sha224
    sha224_hash=hashlib.sha224(encoded_input)
    print(G+"{+}The SHA224 Hash Value Of Your Input Is {+}: "+Y+sha224_hash.hexdigest())
    
    #sha256
    sha256_hash=hashlib.sha256(encoded_input)
    print(G+"{+}The SHA256 Hash Value Of Your Input Is {+}: "+Y+sha256_hash.hexdigest())
    
    #sha384
    sha384_hash=hashlib.sha384(encoded_input)
    print(G+"{+}The SHA384 Hash Value Of Your Input Is {+}: "+Y+sha384_hash.hexdigest())
    
    #sha512
    sha512_hash=hashlib.sha512(encoded_input)
    print(G+"{+}The SHA512 Hash Value Of Your Input Is {+}: "+Y+sha512_hash.hexdigest())

    #sha1 Crypt
    from passlib.hash import sha1_crypt as mc
    sha1=mc.encrypt(get_input)
    print (G+"{+}The SHA1 Crypt Hash Value Of Your Input Is {+}: "+Y+sha1)

    #sha256 Crypt
    from passlib.hash import sha256_crypt as mc
    sha256_crypt=mc.encrypt(get_input)
    print (G+"{+}The SHA256 Crypt Hash Value Of Your Input Is {+}: "+Y+sha256_crypt)

    # Sha512 crypt
    from passlib.hash import sha512_crypt as mc
    sha512_crypt = mc.encrypt(get_input)
    print (G+"{+}The SHA512 Crypt Hash Value Of Your Input Is {+}: "+Y+sha512_crypt)
    
    #django sha1
    from passlib.hash import django_pbkdf2_sha1 as m25
    django_sha1 = m25.encrypt(get_input)
    print (G+"{+}The Django HMAC SHA1 Hash Value Of Your Input Is {+}: "+Y+django_sha1)

    #django sha256
    from passlib.hash import django_pbkdf2_sha256 as m25
    django_sha256 = m25.encrypt(get_input)
    print (G+"{+}The Django HMAC SHA256 Hash Value Of Your Input Is {+}: "+Y+django_sha256)

    '''
    #ntlm
    ntlm_hash=hashlib.new('md4', "password".encode('utf-16le')).digest()
    print(G+"{+}The NTLM Hash Value Of Your Input Is {+}: "+ntlm_hash)
    '''

    #blake2b
    from pyblake2 import blake2b
    h=blake2b()
    h.update(get_input)
    blake2b_hash=h.hexdigest()
    print (G+"{+}The Blake2b Hash Value Of Your Input Is {+}: "+Y+blake2b_hash)

    #blake2s
    from pyblake2 import blake2s
    h=blake2s()
    h.update(get_input)
    blake2s_hash=h.hexdigest()
    print (G+"{+}The Blake2s Hash Value Of Your Input Is {+}: "+Y+blake2s_hash)

    #whirlpool
    m = hashlib.new("whirlpool")
    m.update(get_input)
    whirlpool_hash = m.hexdigest()
    print(G+"{+}The Whirlpool Hash Value Of Your Input Is {+}: "+Y+whirlpool_hash)
   
    #ripemd160
    m = hashlib.new("ripemd160")
    m.update(get_input)
    ripemd160_hash = m.hexdigest()
    print(G+"{+}The Ripemd160 Hash Value Of Your Input Is {+}: "+Y+ripemd160_hash)

    #crc32
    crc32_value=zlib.crc32(get_input)
    crc32='%08X' % (crc32_value & 0xffffffff,)
    print (G+"{+}The CRC32 Hash Value Of Your Input Is {+}: "+Y+crc32.lower())
    
    #adler32
    adler32_value=zlib.adler32(get_input)
    adler32='%08X' % (adler32_value & 0xffffffff,)
    print (G+"{+}The Adler32 Hash Value Of Your Input Is {+}: "+Y+adler32.lower())
    
    #des
    from passlib.hash import des_crypt
    des_hash=des_crypt.encrypt(get_input)
    print (G+"{+}The DES Hash Value Of Your Input Is {+}: "+Y+des_hash)

    #bsdicrypt
    from passlib.hash import bsdi_crypt
    bsdi_hash=bsdi_crypt.encrypt(get_input)
    print (G+"{+}The BSDI Hash Value Of Your Input Is {+}: "+Y+bsdi_hash)

    #bigcrypt
    from passlib.hash import bigcrypt
    big_hash=bigcrypt.encrypt(get_input)
    print (G+"{+}The BigCrypt Hash Value Of Your Input Is {+}: "+Y+big_hash)


    #crypt16
    from passlib.hash import crypt16
    crypt16_hash=crypt16.encrypt(get_input)
    print (G+"{+}The Crypt16 Hash Value Of Your Input Is {+}: "+Y+crypt16_hash)

    #phppass
    from passlib.hash import phpass as mc
    phpass = mc.encrypt(get_input)
    print (G+"{+}The PHPass Hash Value Of Your Input Is {+}: "+Y+phpass)
    
    #Cryptacular's PBDF2
    from passlib.hash import cta_pbkdf2_sha1 as mc
    cryp_pbkdf2_sha1 = mc.encrypt(get_input)
    print (G+"{+}The Cryptacular's PBDF2 Hash Value Of Your Input Is {+}: "+Y+cryp_pbkdf2_sha1)

    #dwayne PBDF2
    from passlib.hash import dlitz_pbkdf2_sha1 as mc
    dwayne_pbkdf2_sha1 = mc.encrypt(get_input)
    print (G+"{+}The Dwayne PBDF2 Hash Value Of Your Input Is {+}: "+Y+dwayne_pbkdf2_sha1)

    #Atlassian's PBKDF2 Hash
    from passlib.hash import cta_pbkdf2_sha1 as mc
    atl_pbkdf2_sha1 = mc.encrypt(get_input)
    print (G+"{+}The Atlassin's PBKDF2 SHA1 Hash Value Of Your Input Is {+}: "+Y+atl_pbkdf2_sha1)

    #grub pbkdf2
    from passlib.hash import grub_pbkdf2_sha512 as m25
    grub_pbkdf2_sha512 = m25.encrypt(get_input)
    print (G+"{+}The Grub PBKDF2 SHA512 Hash Value Of Your Input Is {+}: "+Y+grub_pbkdf2_sha512)

    #scram
    from passlib.hash import scram as mc
    scram=mc.encrypt(get_input)
    print (G+"{+}The Scram Hash Value Of Your Input Is {+}: "+Y+scram)

    #freebsd nthash
    from passlib.hash import bsd_nthash as mc
    bsd_nthash=mc.encrypt(get_input)
    print (G+"{+}The BSD1 NTHash Value Of Your Input Is {+}: "+Y+bsd_nthash)

    #oracle11
    from passlib.hash import oracle11 as m25
    oracle11 = m25.encrypt(get_input)
    print (G+"{+}The Oracle11G Hash Value Of Your Input Is {+}: "+Y+oracle11)

    #lanManager
    from passlib.hash import lmhash as m25
    lmhash = m25.encrypt(get_input)
    print (G+"{+}The LMHash Hash Value Of Your Input Is {+}: "+Y+lmhash)

    #nthash
    from passlib.hash import nthash as m25
    nthash = m25.encrypt(get_input)
    print (G+"{+}The Windows-Nthash Hash Value Of Your Input Is {+}: "+Y+nthash)

    #cisco type 7
    from passlib.hash import cisco_type7 as m25
    cisco = m25.encrypt(get_input)
    print (G+"{+}The CISCO Type-7 Hash Value Of Your Input Is {+}: "+Y+cisco)

    #fshp
    from passlib.hash import fshp as m25
    fshp = m25.encrypt(get_input)
    print (G+"{+}The FSHP-Fairly Secured Hashed Password Hash Value Of Your Input Is {+}: "+Y+fshp)

    #mysql323
    from passlib.hash import mysql323
    mysql323hash=mysql323.encrypt(get_input)
    print(G+"{+}The MySQL 3.2.3 Hash Value Of Your Input Is {+}: "+Y+mysql323hash)

    #mysql41
    from passlib.hash import mysql41
    mysql141hash=mysql41.encrypt(get_input)
    print(G+"{+}The MySQL 4.1 Hash Value Of Your Input Is {+}: "+Y+mysql141hash)

    #mssql2000
    from passlib.hash import  mssql2000 as m20
    mssql2000hash = m20.encrypt(get_input)
    print(G+"{+}The MS-SQL 2000 Hash Value Of Your Input Is {+}: "+Y+mssql2000hash)

    #mssql2005
    from passlib.hash import  mssql2005 as m25
    mssql2005hash= m25.encrypt(get_input)
    print(G+"{+}The MS-SQL 2005 Hash Value Of Your Input Is {+}: "+Y+mssql2005hash)


def main():
    try:
        banner()
        #getting input string from user
        try:
            get_input=raw_input(G+"{+} Enter the string to be hashed (Eg:Hashthestring) {+}: "+R)
        except KeyboardInterrupt:
            print(R+"{+} You Pressed CTRL+C {+}")
            sys.exit()
        sleep(2)
        hashing(get_input)
    except KeyboardInterrupt:
        print(R+"{+} You Pressed CTRL+C {+}")
        sys.exit()
        
def check_modules():
    try:
        import passlib,pyblake2
        main()
    except:
        print(R+"Install the required modules using \n\t pip install passlib \n\t pip install pyblake2")

#hashing function_contains_all_methods_using_Py Libraries{hashlib,zlib},Pip_Libraries{pyblake2,passlib}
#install pyblake2 using pip install pyblake2
#install passlib using pip install passlib

clear()
check_modules()


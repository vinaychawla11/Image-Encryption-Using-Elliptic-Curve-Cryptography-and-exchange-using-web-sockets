import random
import keyderivationfunction as KDF
import base64
from Crypto.Cipher import AES
from Crypto import Random
from PIL import Image as IG
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import hmac
import hashlib
import base64
import ECDH as oy
from Tkinter import * 
import tkFileDialog as filedialog
ftw=oy.DiffieHellman()
#ftw1=oy.DiffieHellman()
a=ftw.get_private_key()
b=ftw.gen_public_key()
#c=ftw1.get_private_key()
#d=ftw1.gen_public_key()
digest_maker = hmac.new(b'You can see this')
digest=digest_maker.hexdigest()
#r_digest=digest_maker.hexdigest()
image_selected = False
image_file_name = None
file_to_copy = ""
file_new_home = None
class Receiver:
	
	def decrypt( self, enc,PKS ):
		global digest
		chunk_size = 64*1024
	        output_file = enc[:-9] + 'd' 
		SK=ftw.gen_shared_key(PKS)
		#print SK
		SK=int(SK,16)
		SK=str(SK)
		keyhr=SK[:-16]
		SK=SK[:32]
		#print SK
		
        	with open(enc, 'rb') as inf:
        	    filesize = long(inf.read(16))
        	    IV = inf.read(16)
		    #print(IV)
        	    decryptor = AES.new(SK, AES.MODE_CBC, IV)
        	    with open(output_file, 'wb') as outf:
        	        while True:
        	            chunk = inf.read(chunk_size)
        	            if len(chunk)==0:
        	                break
        	            outf.write(decryptor.decrypt(chunk))
        	        outf.truncate(filesize)
		print "Done\n%s ==> %s"%(enc,enc[:-4])
		
		digest_maker = hmac.new(bin(int(keyhr)))
		with open(output_file, 'rb') as f:
    			while True:
			        block = f.read(1024)
			        if not block:
		        	        break
			        digest_maker.update(block)
		digest = digest_maker.hexdigest()
		#print(r_digest,s_digest)
		#if hmac.compare_digest(r_digest, s_digest):
       		#	 print('OK:')
    		#else:
		 #       print('WARNING: Data corruption')

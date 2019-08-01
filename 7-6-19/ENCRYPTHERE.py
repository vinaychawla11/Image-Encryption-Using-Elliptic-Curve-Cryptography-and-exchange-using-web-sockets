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
class Sender:	
	def encrypt( self, raw, PKR ):
		global digest
		chunk_size = 64*1024
		output_file = raw+".enc"
		file_size = str(os.path.getsize(raw)).zfill(16)
		#PKR=tuple(int(PKR))
		SS=ftw.gen_shared_key(PKR)
		#print SS
		SS=int(SS,16) 
		SS=str(SS)
		keyh=SS[:-16]
		SS=SS[:32]
		#print SS
		digest_maker = hmac.new(bin(int(keyh)))
		with open(raw, 'rb') as f:
    			while True:
			        block = f.read(1024)
			        if not block:
		        	        break
			        digest_maker.update(block)
		digest = digest_maker.hexdigest()
		#print(s_digest)
	        IV = Random.new().read( AES.block_size)
		#print(SS)
        	
    		encryptor = AES.new(SS, AES.MODE_CBC, IV)
		with open(raw, 'rb') as inputfile:
		        with open(output_file, 'wb') as outf:
		                outf.write(file_size)
		                outf.write(IV)
				while True:
               			        chunk = inputfile.read(chunk_size)
			                if len(chunk) == 0:
			                        break
			                elif len(chunk) % 16 != 0:
			                        chunk += ' '*(16 - len(chunk)%16)
			                outf.write(encryptor.encrypt(chunk))
		print "Done\n%s ==> %s"%(raw, raw[:-4])



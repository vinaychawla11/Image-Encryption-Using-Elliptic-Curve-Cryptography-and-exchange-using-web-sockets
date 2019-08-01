

import os
import binascii
import hashlib
import keyderivationfunction as KDF




class DiffieHellman:
	""" Class to represent the Diffie-Hellman key exchange protocol """
	# Current minimum recommendation is 2048 bit.
	def __init__(self, group=14):
		self.__a = int(binascii.hexlify(os.urandom(32)), base=16)

	def get_private_key(self):
		""" Return the private key (a) """
		print('THE PRIVATE KEY')
		print(self.__a)
		return self.__a

	def gen_public_key(self):
		""" Return A, A = g ^ a mod p """
		# calculate G^a mod p
		print('THE PUBLIC KEY')
		print(KDF.EccMultiply(KDF.GPoint,self.__a))
		return KDF.EccMultiply(KDF.GPoint,self.__a)

	def check_other_public_key(self, x,y):
		# check if the other public key is valid based on NIST SP800-56
		# 2 <= g^b <= p-2 and Lagrange for safe primes (g^bq)=1, q=(p-1)/2

		#if 2 <= other_contribution and other_contribution <= int(KDF.N) - 2:
			
        	if (x < 0 or x >= KDF.N or y < 0 or y > KDF.N):
			return False
	        if not self:
		        return False
		return True

		

	def gen_shared_key(self, PR):
		""" Return g ^ ab mod p """
		# calculate the shared key G^ab mod p
		self.shared_key = KDF.EccMultiply(PR,self.__a)
		return hashlib.sha256(str(self.shared_key).encode()).hexdigest()
		

    

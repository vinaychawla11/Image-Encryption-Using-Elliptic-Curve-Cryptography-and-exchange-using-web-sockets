# Image-Encryption-Using-Elliptic-Curve-Cryptography-and-exchange-using-web-sockets
This is my final year project along with 2 of my peers, which uses AES-256 along with Elliptic Curve key generation and sharing to encrypt images. It uses what is known as Elliptic Curve Integrated Encryption Scheme. It is coded in Python and uses web socket to share images between 2 clients. It encrypts the image before sending and decrypts it on the receiver side using the above mentioned scheme. 

Works well with Python 2, hasn't been tested with Python 3. 


In order to run this code, just execute the ENCRYPTHERE.py or DECRYPTHERE.py present in 7-6-19 folder. Configure the UDPClient.py with the IP address of the sender and receiver to send or receive images. 

The websocket uses UDP and the sender and receiver should be on the same network for the transmission to take place. 


Libraries used: 
Tkinter
Opencv
matplotlib
random
PIL
Crypto
hmac
hashlib
binascii
socket

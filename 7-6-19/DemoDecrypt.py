import DECRYPTHERE as DN
import cv2
from matplotlib import pyplot as plt
import hmac
import socket,os
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("10.10.12.136", 5005))
k = ' '
size = 1024
PKS=[]

#    print "Do you want to transfer a \n1.Text File\n2.Image\n3.Video\n"
  #  k = raw_input()
PKS.append(long(client_socket.recv(1024)))
PKS.append(long(client_socket.recv(1024)))
#PKSR=tuple(int(x) for x in PKS)
#PKS.append(int( (client_socket.recv(1024))))
#PKSS=tuple(PKS)	
PKSS=tuple(PKS)
val=str(DN.b[0]) 
client_socket.send(val)
val=str(DN.b[1])
client_socket.send(val)
#client_socket.send(str(DN.b[1]))
       # print "Enter file name of the image with extentsion (example: filename.jpg,filename.png or if a video file then filename.mpg etc) - "
       # fname = raw_input()
       # client_socket.send(fname)
        #fname = 'documents/'+fname
data=client_socket.recv(1024)
print data
fp = open(data,'w')
while True:
	strng = client_socket.recv(512)
        if not strng:
	        break
        fp.write(strng)
fp.close()
print "Data Received successfully"
RDIG=client_socket.recv(1024)
       # exit()
c=DN.Receiver()
c.decrypt(data,PKSS)

print RDIG
if hmac.compare_digest(RDIG, DN.digest):
	print('OK:')
else:       
	print('WARNING: Data corruption')
img=cv2.imread(data[:-9]+"d",0)
hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.figure(2)
plt.show()

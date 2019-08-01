import ENCRYPTHERE as EN
from Tkinter import *
import tkFileDialog as filedialog
import cv2
from matplotlib import pyplot as plt
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("", 5005))
server_socket.listen(5)
import os
PKR=[]
client_socket, address = server_socket.accept()
print "Connected to - ",address,"\n"
val=str(EN.b[0])
client_socket.send(val)        
val=str(EN.b[1])
client_socket.send(val)
#client_socket.send(str(EN.b[1]))
PKR.append(long(client_socket.recv(1024)))
PKR.append(long(client_socket.recv(1024)))
#PKRR=tuple(PKR)
#PKRR=tuple(int(x) for x in PKR)
#PKR.append(int((client_socket.recv(1024))))
PKRR=tuple(PKR)
print PKR
Tk().withdraw() # Close the root window
in_path = str(filedialog.askopenfilename())
#print in_path
inp=re.search(r'(.*)/(.*)',in_path).group(2)
#buttonAddImage = Button(root, text="Add Image", command=select_image)
#root.filename = filedialog.askopenfilename(filetypes = ((("All files","*.*"))))
s= EN.Sender()
s.encrypt(inp,PKRR)
img=cv2.imread(inp,0)
hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256]) 
plt.figure(1)
#plt.show()
	#all_pixels = []
        
       # data = client_socket.recv(1024)
	#print "Enter file name of the image with extentsion (example: filename.jpg,filename.png or if a video file then filename.mpg etc) - "
#        fname = raw_input()
client_socket.send(inp+".enc")
       # print "The following data was received - ",data
        #print "Opening file - ",data
imag = open(inp+".enc",'r')
while True:
	strng = imag.readline(512)
        if not strng:
	        break
        client_socket.send(strng)
imag.close()
print "Data sent successfully"
client_socket.send(EN.digest)
client_socket.close()
print EN.digest
       # exit()
        #data = 'viewnior '+data
        #os.system(data)



import socket            
 
# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
#agar 127 wala hota toh restriced ip pe bind hota sirf iss computer se le paate requests
#0.0.0.0 types ya ' ' rakhne pe we bind it to private wali ipv4s in a sense and to 127.0.0.1(but that's for this computer only and to other ipv4 that this computer has for 
# other networks) and toh same network pe kahi se bhi kisi bhi device se request maarlo
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           
 
# a forever loop until we interrupt it or
# an error occurs
while True:
 
# Establish connection with client.
    c, addr = s.accept()    
    print ('Got connection from', addr )
    
    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())
    
    # Close the connection with the client
    c.close()
    
    # Breaking once connection closed
    break
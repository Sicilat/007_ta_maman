import select
import socket
import sys

host = 'localhost' # what address is the server listening on
port = 666 # what port the server accepts connections on
backlog = 5  # how many connections to accept
maxsize = 1024 # Max receive buffer size, in bytes, per recv() call

#now initialize the server and accept connections at localhost:50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(backlog)
input = [server,] #a list of all connections we want to check for data
                  #each time we call select.select()

running = 1 #set running to zero to close the server
while running:
  inputready,outputready,exceptready = select.select(input,[],[])

  for s in inputready: #check each socket that select() said has available data

    if s == server: #if select returns our server socket, there is a new
                    #remote socket trying to connect
      client, address = server.accept()
      input.append(client) #add it to the socket list so we can check it now
      print('new client added%s'%str(address))

    else:
      # select has indicated that these sockets have data available to recv
      data = s.recv(maxsize)
      if data:
        print('%s received from %s'%(data,s.getsockname()))

        #Uncomment below to echo the recv'd data back
        #to the sender... loopback!
        #s.send(data)
      else: #if recv() returned NULL, that usually means the sender wants
            #to close the socket.
        s.close()
        input.remove(s)

#if running is ever set to zero, we will call this
server.close()
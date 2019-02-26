from mastermind_import import *
from settings import *

import threading
from time import gmtime, strftime

bricks_1 = [[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0]]
bricks_2 = [[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0]]

def update_game(player, pos):
    global bricks_1, bricks_2



class ServerGame(MastermindServerTCP):
    def __init__(self):
        MastermindServerTCP.__init__(self, 0.5, 0.5, 10.0)  # server refresh, connections' refresh, connection timeout

        self.chat = [None] * scrollback
        self.mutex = threading.Lock()

    def add_message(self, msg):
        timestamp = strftime("%H:%M:%S", gmtime())

        self.mutex.acquire()
        self.chat = self.chat[1:] + [timestamp + " | " + msg]
        self.mutex.release()

    def callback_connect(self):
    # Something could go here
        return super(ServerGame, self).callback_connect()

    def callback_disconnect(self):
    # Something could go here
        return super(ServerGame, self).callback_disconnect()

    def callback_connect_client(self, connection_object):
    # Something could go here
        return super(ServerGame, self).callback_connect_client(connection_object)

    def callback_disconnect_client(self, connection_object):
    # Something could go here
        return super(ServerGame, self).callback_disconnect_client(connection_object)

    def callback_client_receive(self, connection_object):
    # Something could go here
        return super(ServerGame, self).callback_client_receive(connection_object)

    def callback_client_handle(self, connection_object, data):
        cmd = data[0]
        if cmd == "introduce":
          self.add_message("Server: " + data[1] + " has joined.")
          self.callback_client_send(connection_object, ["Jonbour"])
        elif cmd == "update":
          player = data[1]
          pos = data[2]
          data = update_game(player, pos)
          self.callback_client_send(connection_object, data)
        elif cmd == "leave":
         self.add_message("Server: " + data[1] + " has left.")

    def callback_client_send(self, connection_object, data, compression=None):
        # Something could go here
        return super(ServerGame, self).callback_client_send(connection_object, data, compression)

if __name__ == "__main__":
    print("V-Bricks Server")
    print("This computer's IP is \""+mastermind_get_local_ip()+"\".")
    server = ServerGame()
    print("Starting.")
    server.connect(server_ip, port)
    try:
        server.accepting_allow_wait_forever()
    except:
        pass
    server.accepting_disallow()
    server.disconnect_clients()
    server.disconnect()
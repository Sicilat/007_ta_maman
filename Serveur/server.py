from mastermind_import import *
from settings import *

import threading
from time import gmtime, strftime
from math import cos,pi,sin

lose_1 = False
lose_2 = False

sens1 = -1
sens2 = 1
horizon1 = 1
horizon2 = 2

x1 = 0
y1 = 0
x2 = 0
y2 = 0

lost_1 = 0
lost_2 = 0
lost_1b = False
lost_2b = False
pos1 = 0
pos2 = 0

bricks_1 = [[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0]]
bricks_2 = [[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0]]

def update_game(self, connection_object, player, pos):
    global bricks_1, bricks_2, lost_1, lost_1b, lost_2, lost_2b, y1, y2, x1, x2, sens1, sens2, horizon1, horizon2, pos1, pos2

    angle1 = pi / 3
    angle2 = pi / 3
    y1 += sin(angle1) * sens1 * 5
    x1 += (cos(angle1)) * horizon1
    y2 += sin(angle2) * sens2 * 5
    x2 += (cos(angle2)) * horizon2

    if player == 1:
        pos1 = pos
    elif player == 2:
        pos2 = pos

    i = 0
    j = 0

    while i < len(bricks_1):  # Pour chaque brique
        while j < len(bricks_1[i]):
            if bricks_1[i][j] == 0:
                pass
            elif j * 29 - 5 <= y1 <= j + 34 and i - 5 <= x1 <= i + 93:
                bricks_1[i][j] = 0
                sens1 = (-1)*sens1
                break
            j += 1
        i += 1

    i = 0
    j = 0

    if x1 <= 5 or x1 >= 435:  # Si on tape sur le bord gauche/droit
        horizon1 = (-1) * horizon1

    if x2 <= 5 or x2 >= 435:  # Si on tape sur le bord gauche/droit
        horizon2 = (-1) * horizon2

    if y1 <= 5:  # Si on tape le plafond
        sens1 = (-1) * sens1

    if y2 <= 5:  # Si on tape le plafond
        sens2 = (-1) * sens2

    while i < len(bricks_2):  # Pour chaque brique
        while j < len(bricks_2[i]):
            if bricks_2[i][j] == 0:
                pass
            elif j * 29 - 5 <= y2 <= j + 34 and i - 5 <= x2 <= i + 93:
                bricks_2[i][j] = 0
                sens2 = (-1) * sens2
                break
            j += 1
        i += 1

    if 515 <= y1 <= 530 and pos1 - 70 < x1 < pos1 + 70 and player == 1:
        if pos1 - 10 <= x1 <= pos1 + 5:
            angle1 = 2 * pi / 3
            horizon1 = 5

            # Si c'est sur le coin droit, un angle plus petit
        if pos1 + 37 <= x1 <= pos1 + 47:
            angle1 = pi / 5
            horizon1 = 5

            # Sinon l'angle sera dans l'autre sens
        if pos1 + 5 < x1 < pos1 + 40:
            angle1 = pi / 3

        sens1 = (-1) * sens1

    if 390 <= y2 <= 400 and pos2 - 70 < x2 < pos2 + 70 and player == 2:
        if pos2 - 10 <= x2 <= pos2 + 5:
            angle2 = 2 * pi / 3
            horizon2 = 5

            # Si c'est sur le coin droit, un angle plus petit
        if pos2 + 37 <= x2 <= pos2 + 47:
            angle2 = pi / 5
            horizon2 = 5

            # Sinon l'angle sera dans l'autre sens
        if pos2 + 5 < x2 < pos2 + 40:
            angle2 = pi / 3

        sens2 = (-1) * sens2

    if lost_1b:
        i = 0
        max_b = 0
        lost_1 += 1
        i = int(pow(lost_1, (1/1.2)))
        for v in range(5):
            for t in range(10):
                if bricks_1[v][t] == 1:
                    max_b = v + 1
        if max_b + i >= 11:
            lose_1 = True
        else:
            temp = bricks_1
            for i in range(9):
                bricks_1[i + 1] = temp[i]
            for i in range(5):
                bricks_1[i][0] = 1


    if lost_2b:
        i = 0
        max_b = 0
        lost_2 += 1
        i = int(pow(lost_1, (1 / 1.2)))
        for v in range(5):
            for t in range(10):
                if bricks_2[v][t] == 1:
                    max_b = v + 1
        if max_b + i >= 11:
            lose_2 = True
        else:
            temp = bricks_2
            for i in range(9):
                bricks_2[i + 1] = temp[i]
            for i in range(5):
                bricks_2[i][0] = 1



    if lose_1:
        print("player 1 lose")
        if player == 1:
            data = ['win', [0]]
            self.callback_client_send(connection_object, data)
            self.accepting_disallow()
            self.disconnect_clients()
            self.disconnect()
        if player == 2:
            data = ['win', [1]]
            self.callback_client_send(connection_object, data)
            self.accepting_disallow()
            self.disconnect_clients()
            self.disconnect()
    elif lose_2:
        print("player 2 lose")
        if player == 1:
            data = ['win', [1]]
            self.callback_client_send(connection_object, data)
            self.accepting_disallow()
            self.disconnect_clients()
            self.disconnect()
        if player == 2:
            data = ['win', [0]]
            self.callback_client_send(connection_object, data)
            self.accepting_disallow()
            self.disconnect_clients()
            self.disconnect()

    data = ['bbup',[x1, x2, y1, y2, bricks_1, bricks_2]]
    self.callback_client_send(connection_object, data)

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
          print("introduce")
        elif cmd == "update":
          player = data[1][0]
          pos = data[1][1]
          data = update_game(self, connection_object, player, pos)
          self.callback_client_send(connection_object, data)

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
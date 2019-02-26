try:    name = raw_input("Enter a screen name: ")
except: name =     input("Enter a screen name: ")

import pygame
from pygame.locals import *
import traceback
from mastermind_import import *
from settings import *

client = None
server = None

screen_size = [1080,720]
pygame.display.set_caption("V-Bricks")
surface = pygame.display.set_mode(screen_size)

message = ""
to_send = [
    ["introduce", name]
]

def send_next_blocking():
    global log, to_send, continuing
    try:
        if len(to_send) == 0:
            client.send(["update"],None)
        else:
            client.send(to_send[0],None)
            to_send = to_send[1:]

        reply = None
        while reply == None:
            reply = client.receive(False)
        log = reply
    except MastermindError:
        continuing = False

def get_input():
    global surface, screen_size, message
    for event in pygame.event.get():
        if event.type == QUIT:
            return False

    return True

def main():
    global client, server, continuing

    client = MastermindClientTCP(client_timeout_connect, client_timeout_receive)
    try:
        print("Client connecting on \"" + client_ip + "\", port " + str(port) + " . . .")
        client.connect(client_ip, port)
    except MastermindError:
        print("No server found")
        return
    print("Client connected!")

    clock = pygame.time.Clock()
    continuing = True
    while continuing:
        if not get_input():
            to_send.append(["leave", name])
            send_next_blocking()
            break
        send_next_blocking()
        clock.tick(60)
    pygame.quit()

    client.disconnect()

    if server != None:
        server.accepting_disallow()
        server.disconnect_clients()
        server.disconnect()

if __name__ == "__main__":
    try:
        main()
    except:
        traceback.print_exc()
        pygame.quit()
        input()
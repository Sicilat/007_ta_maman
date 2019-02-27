try:    name = raw_input("Enter a screen name: ")
except: name =     input("Enter a screen name: ")

import pygame
from pygame.locals import *
import traceback
from mastermind_import import *
from settings import *

LeftPad = False
RightPad = False
client = None
server = None
player = int(input('> '))
screen_size = [440,567]
pygame.display.set_caption("V-Bricks")
surface = pygame.display.set_mode(screen_size)

def load_image(name):
    fullname = os.path.join('data', name)
    print(fullname)
    image = pygame.image.load(fullname).convert()
    return image, image.get_rect()

background, backgroundrect = load_image('background.png')

PAD_SPRITE_WIDTH = 485
PAD_SPRITE_HEIGHT = 128

class SpriteSheet(object):

		sprite_sheet = None

		def __init__(self, file_name):
 
				self.sprite_sheet = pygame.image.load(file_name).convert()
 
 
		def get_image(self, x, y, width, height):

				image = pygame.Surface([width, height]).convert()
 
				image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

				for i in range(0, 256):
						image.set_colorkey((i, i, i))

				return image

class Pad:        
        def __init__(self):
                self.move = []

                sprite_sheet = SpriteSheet("data/sprite_pad.png")

                image = pygame.transform.scale(sprite_sheet.get_image(0, 0, PAD_SPRITE_WIDTH, PAD_SPRITE_HEIGHT).convert_alpha(), (139 , 26))
       	        self.move.append(image)
       	        image = pygame.transform.scale(sprite_sheet.get_image(0, 128, PAD_SPRITE_WIDTH, PAD_SPRITE_HEIGHT).convert_alpha(), (139, 26))
                self.move.append(image)

                self.pos = 151
                self.case_x = 151
                self.direction = self.move[0]
                self.frame = 0
    
        def sprite(self, direction):            
                if RightPad == True:
                    if self.case_x < 440 - 139:
                        self.case_x += 1
                        self.pos = self.case_x
                    self.direction = self.move[self.frame]
                    self.frame += 1
                    if self.frame > 1:
                        self.frame = 0
                        
                if LeftPad == True:
                    if self.case_x > 0:
                        self.case_x -= 1
                        self.pos = self.case_x
                    self.direction = self.move[self.frame]
                    self.frame += 1
                    if self.frame > 1:
                        self.frame = 0

pad = Pad()

message = ""
to_send = [
    ["introduce", name]
]
x = 0
data = [0]

def send_next_blocking():
    global log, to_send, continuing, x, data, pos, player
    data = ["update", [player, pad.pos]]
    try:
        if x != 0:
            client.send(data,None)
        else:
            client.send(to_send[0],None)
            to_send = to_send[1:]
            x = 1

        reply = None
        while reply == None:
            reply = client.receive(False)
        log = reply
        print(log)
    except MastermindError:
        continuing = False

def get_input():
    global surface, screen_size, message
    for event in pygame.event.get():
        if event.type == QUIT:
            return False

    return True

def main():
    global client, server, continuing, pos, RightPad, LeftPad

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
        send_next_blocking()                                #uvjfe,jjfibkzfkjhjkfgjzifk
        for event in pygame.event.get():
            if event.type == QUIT:
                display_window = 0
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                display_window = 0
            if event.type == KEYDOWN and event.key == K_LEFT:
                LeftPad = True
                #Pad.sprite(pad, "left")
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                RightPad = True
                #Pad.sprite(pad, "right")
            if event.type == KEYUP and event.key == K_LEFT:
                LeftPad = False
                #Pad.sprite(pad, "left")
            elif event.type == KEYUP and event.key == K_RIGHT:
                RightPad = False
                #Pad.sprite(pad, "right")

            if RightPad == True:
                Pad.sprite(pad, "right")
                        
            if LeftPad == True:
                Pad.sprite(pad, "left")

            surface.blit(background, (0, 0))
            surface.blit(pad.direction, (pad.pos , 522))
            pygame.display.flip()
        data = ["update",[player,pos]]
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



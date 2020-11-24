import pygame
from pygame.locals import *
import paho.mqtt.client as mqtt #import the client
import threading
#keys = [False, True, False, False]
broker_address="192.168.1.67" 
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address)
def roda_loop():
    client.loop()
timer = threading.Timer(60, roda_loop)
timer.start() 
pygame.init()
# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((500, 700))

pygame.display.set_caption("MQTT Tetris Control")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()
joystick = pygame.joystick.Joystick(0)
joystick.init()
axes = joystick.get_numaxes()
axis0=0
axis1=0
while not done:
    #client.loop_start()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            timer.cancel()
            done = True
        if event.type == pygame.JOYAXISMOTION:
            print("joydown")
            axis0 = joystick.get_axis(0)
            axis1 = joystick.get_axis(1)
            print("axis0 = " + str(axis0))
            if axis0 > 0:
                #keys[0]=True
                client.publish("ws_rig","1") #publish
            if axis0 < 0:
                client.publish("ws_lef","1") #publish
               
            if axis1 > 0:
                client.publish("ws_dow","1") #publish
                #keys[2]=True
            if axis1 < 0:
                client.publish("ws_rot","1") #publish
            axis0=0
            axis1=0
            
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                #keys[0]=True
                client.publish("ws_rot","1") #publish
            elif event.key==K_LEFT:
                client.publish("ws_lef","1") #publish
                #keys[1]=True
            elif event.key==K_DOWN:
                client.publish("ws_dow","1") #publish
                #keys[2]=True
            elif event.key==K_RIGHT:
                client.publish("ws_rig","1") #publish
                #keys[3]=True
            #print(str(keys))
            #keys = [False,False,False,False]


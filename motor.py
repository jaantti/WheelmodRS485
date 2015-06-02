__author__ = 't420s'
import pygame
import serial


def move(dir):
    global m
    if dir == -1:
        m.write('1:sd0\n')
        m.write('2:sd0\n')
    if dir == 0:
        m.write('1:sd50\n')
        m.write('2:sd50\n')
    if dir == 1:
        m.write('1:sd-50\n')
        m.write('2:sd50\n')
    if dir == 2:
        m.write('1:sd-50\n')
        m.write('2:sd-50\n')
    if dir == 3:
        m.write('1:sd50\n')
        m.write('2:sd-50\n')


'''
def move(dir):
    #global m
    if dir == -1:
        print 'stop'
    if dir == 0:
        print 'up'
    if dir == 1:
        print 'right'
    if dir == 2:
        print 'down'
    if dir == 3:
        print 'left'
'''

pygame.init()
clk = pygame.time.Clock()
screen = pygame.display.set_mode((1, 1))


#pygame.time.clock.tick(10)
m = serial.Serial('COM18', 19200)
state = -1
run = True
while run:
    move(state)
    clk.tick(10)
    events = pygame.event.get()
    #if len(events) == 0:
    #    move(-1)
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                state = 0
            elif event.key == pygame.K_RIGHT:
                state = 1
            elif event.key == pygame.K_DOWN:
                state = 2
            elif event.key == pygame.K_LEFT:
                state = 3
            elif event.key == pygame.K_ESCAPE:
                run = False
            else:
                move(-1)
        elif event.type == pygame.KEYUP:
            state = -1
m.close()

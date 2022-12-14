import os
import time
from termcolor import colored
import math 


class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.05
        self.pos = [0, 0]

        self.direction = [0, 1]

    def setDegrees(self, degrees):
        radians = (degrees/180) * math.pi 
        self.direction = [math.sin(radians), -math.cos(radians)]

    def setPos(self, pos):
        self.pos = pos

    def up(self):
        self.direction = [0, -1]
        self.forward()

    def down(self):
        self.direction = [0, 1]
        self.forward()

    def right(self):
        self.direction = [1, 0]
        self.forward()

    def left(self):
        self.direction = [-1, 0]
        self.forward()

    def forward(self):
        pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def drawSquare(self, size):
        for i in range(size):
            self.right()
        for i in range(size):
            self.down()
        for i in range(size):
            self.left()
        for i in range(size):
            self.up()

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)

canvas = Canvas(30, 30)

scribeList = [
    {'position' : [1,3], 'direction' : 123, 'name': 'hiya', 'movement':[['forward',20], ['drawSquare', 10]]},
    {'position' : [1,6], 'direction' : 123, 'name': 'scribe2', 'movement':['left', 10]},
    {'position' : [1,8], 'direction' : 123, 'name': 'jim', 'movement':['down', 3]},
    {'position' : [1,9], 'direction' : 123, 'name': 'kendrick', 'movement':['drawSquare', 5]},
]

# Setting up the scribe
newScribe = TerminalScribe(canvas)
print(scribeList[0]['direction'])
newScribe.setDegrees(scribeList[0]['direction'])
newScribe.setPos(scribeList[0]['position'])

# Making the scribe move
for command in scribeList[0]['movement']:
    if command[0] == 'forward':
        for x in range (0, command[1]):
            newScribe.forward()
    elif command[0] == 'drawSquare':
        newScribe.drawSquare(command[1])


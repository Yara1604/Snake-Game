from turtle import Turtle

startingPositions = [(0, 0), (-20, 0), (-40, 0)] 
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def restart(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments=[]
        self.createSnake()
        self.head = self.segments[0]
  
    
    def createSnake(self):
        for pos in startingPositions:
            self.add_segment(pos)

    def add_segment(self,position):
        newSeg = Turtle("square")
        newSeg.color("#9163BF")
        newSeg.penup()
        newSeg.goto(position)
        self.segments.append(newSeg)

    def extend(self):
        self.add_segment(self.segments[len(self.segments)-1].pos())
    

    def move(self):
        for n in range(len(self.segments)-1,0,-1): # The range function comes from the C lang so you can't use (start=2, stop=0, step=-1)
            self.segments[n].goto(self.segments[n-1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    

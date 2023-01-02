from turtle import Turtle
# Turtle.speed(3)
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
PACE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        '''creating a list of the segments of the snake body'''
        self.segments = []
        self.make_snake()
        # Declaring that the first item in the segment list is the head of the snake 
        self.head = self.segments[0]
        
    
    def make_snake(self):
        '''The creating the snake body'''
        for position in STARTING_POSITIONS:
            self.add_segments(position)
            
    
    def add_segments(self, position):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        '''Moving the snake body of the snake by moving the "self.head" and changing the rest of the segment coordinate.'''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(PACE)
    
    
    def up(self):
        '''Moving the snake upwards'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    
    def down(self):
        '''Moving the snake downwards'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    
    def right(self):
        ''' moving the snake body to the right'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    
    def left(self):
        ''' Moving the snake body to the left'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

# snake = Snake()
# snake.make_snake()
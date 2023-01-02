from turtle import Turtle, Screen
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed('fastest')
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
    
    
    def new_position(self):
        '''Moving the position of the food on collision with the snake'''
        new_x = random.randint(-270, 270)
        new_y = random.randint(-270, 270)
        self.goto(new_x, new_y)

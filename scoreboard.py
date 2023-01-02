from turtle import Turtle, Screen

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('White')
        self.penup()
        self.score = 0
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", False, align='center', font=("Ariel", 14, "normal"))
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", False, align='center', font=("Ariel", 14, "normal"))
        

# x = ScoreBoard()
# screen = Screen()
# screen.exitonclick()
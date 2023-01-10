from turtle import Turtle


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('White')
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """change the score board display whenever the snake collides with food"""
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", False, align='center', font=("Ariel", 14, "normal") )

    def add_score(self):
        """Adds the player score when snake collides with food"""
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        """rest the score board and update the high score"""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("data.txt","w") as high_score:
            high_score.write(str(self.high_score))

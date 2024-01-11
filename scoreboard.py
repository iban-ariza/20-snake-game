from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
DATA_FILE = 'data.txt'


class Scoreboard(Turtle):
    """
    Scoreboard of the game. Used as a turtle object to gain all the functionality (pos, clear, color, goto, ...).
    This basically prints a scoreboard in the screen at the top of the screen.
    Functionality - update, reset, increase score (could be a private function).
    """

    def __init__(self):
        """
        Set a color, score, high score, a position for the scoreboard, hide the actual turtle (so only
        the score shows and not the turtle), load the high score from a file, and update the scoreboard
        with the highest score pulled from the file.
        """
        super().__init__()
        self.score = 0
        with open(DATA_FILE) as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the previous score, and write the new one with the new score and high score."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



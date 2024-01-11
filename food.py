from turtle import Turtle
import random


class Food(Turtle):
    """
    Food item that shows in the snake game. You have to instantiate is as a turtle
    for the turtle functionality (size, shape, position, penup/down, ...).
    """

    def __init__(self):
        """
        Initialize the food item, by setting it up as a circle, setting its length/width,
        removing the cursor with the penup() function, setting the speed, and starting at a
        random position.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Place the food item (just a single box) in a random location within the screen."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

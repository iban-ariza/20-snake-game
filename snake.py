from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]   # sets a location for the first 3 squares that define the snake
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Snake of the game.
    Functionality - create a snake, add a new segment to the snake (grow snake), move, up, down, left, right.
    """

    def __init__(self):
        """Create the snake from scratch and set the head of it, and body segments."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the snake from the defined starting positions"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Get the current position and add it to the segments (body segments) that define the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Move from the tail to the head by retracing the movement from tail to head.
        The head then is moved in the new direction set (forward, left, right).
        This is a function to have the snake move in sync as it is defined by multiple body segments that
        need to move in symmetry.
        :return:
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

import turtle as t

INITIAL_SNAKE_LENGTH_UNITS = 3
STARTING_POSITIONS = [(-20 * x, 0) for x in range(INITIAL_SNAKE_LENGTH_UNITS)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for snake_segment_position in STARTING_POSITIONS:
            self.add_segment(snake_segment_position)

    def add_segment(self, snake_segment_position):
        new_snake_segment = t.Turtle(shape="square")
        new_snake_segment.penup()
        new_snake_segment.color("white")
        new_snake_segment.goto(snake_segment_position)
        self.segments.append(new_snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(new_x,new_y)
        self.snake_head.forward(MOVE_DISTANCE)


    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
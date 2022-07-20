from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.goto(position)
        new_seg.color("white")
        new_seg.penup()
        self.segments.append(new_seg)

    def extend(self):
        # add a new segment to the snake(in the end of snake):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # новая координата для нового сегмента будет на
            # месте предыдущего сегмента(на место 1го сегмента станет 2й, на место 2го станет 3й
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,
                                        new_y)  # передаем координаты, чтобы перейти на позицию от второго к 3му сегменту
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # если положение головы змеи не равно вниз, змея ползет только вверх: для того, чтобы голова и хвост
        # не менялись местами и положение вверх-вниз менялось через поворот замеи
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

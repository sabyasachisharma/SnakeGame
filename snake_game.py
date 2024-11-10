import turtle
import time
import random

# Initial game settings
delay = 0.1
score = 0
high_score = 0

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("green")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off the screen updates for smoother animations

# Snake head setup
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("black")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

# Food setup
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# List to store body segments of the snake
snake_body = []

# Score display setup
score_display = turtle.Turtle()
score_display.speed(0)
score_display.shape("square")
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Function to change the direction of the snake
def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

# Function to move the snake in the current direction
def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)

# Keyboard bindings to control the snake
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main game loop
while True:
    screen.update()

    # Check for collision with the screen borders
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"

        # Move body segments off-screen and clear the list
        for segment in snake_body:
            segment.goto(1000, 1000)
        snake_body.clear()

        # Reset the score and delay
        score = 0
        delay = 0.1
        score_display.clear()
        score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for collision with the food
    if snake_head.distance(food) < 20:
        # Move the food to a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new body segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        snake_body.append(new_segment)

        # Shorten the delay to increase game speed
        delay -= 0.001

        # Increase the score and update the high score if needed
        score += 10
        if score > high_score:
            high_score = score

        score_display.clear()
        score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the body segments to follow the head
    for index in range(len(snake_body) - 1, 0, -1):
        x = snake_body[index - 1].xcor()
        y = snake_body[index - 1].ycor()
        snake_body[index].goto(x, y)

    # Move the first segment to the position of the head
    if len(snake_body) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_body[0].goto(x, y)

    move()

    # Check for collision between the head and the body segments
    for segment in snake_body:
        if segment.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"

            # Move body segments off-screen and clear the list
            for segment in snake_body:
                segment.goto(1000, 1000)
            snake_body.clear()

            # Reset the score and delay
            score = 0
            delay = 0.1
            score_display.clear()
            score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Pause the game for a short period
    time.sleep(delay)

# Keep the window open
screen.mainloop()

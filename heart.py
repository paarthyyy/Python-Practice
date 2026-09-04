import turtle
import math

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.colormode(1.0)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def heart_x(angle):
    return 16 * (math.sin(angle) ** 3)

def heart_y(angle):
    return 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)

N = 200
outer_scale = 18.0
inner_scale = 5.0
steps = 20

c_outer = (1.0, 0.70, 0.78)
c_inner = (0.0, 0.0, 0.0)

# --- Completed Drawing Logic ---
for i in range(steps):
    # Linearly interpolate between outer and inner scale
    factor = i / (steps - 1) if steps > 1 else 0
    current_scale = outer_scale - factor * (outer_scale - inner_scale)
    
    # Linearly interpolate colors from c_outer to c_inner
    r = c_outer[0] - factor * (c_outer[0] - c_inner[0])
    g = c_outer[1] - factor * (c_outer[1] - c_inner[1])
    b = c_outer[2] - factor * (c_outer[2] - c_inner[2])
    
    t.color(r, g, b)
    t.begin_fill()
    
    # Draw the heart path for the current scale
    for j in range(N + 1):
        angle = (j / N) * 2 * math.pi
        x = heart_x(angle) * current_scale
        y = heart_y(angle) * current_scale
        if j == 0:
            t.up()
            t.goto(x, y)
            t.down()
        else:
            t.goto(x, y)
            
    t.end_fill()

screen.update()
turtle.done()
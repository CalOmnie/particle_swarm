import sfml as sf
import math
import time
import random
# create the main window
window = sf.RenderWindow(sf.VideoMode(800, 600), "pySFML Window")

class point:
    def __init__(self, x, y, val, shape, speed):
        self.x = x
        self.y = y
        self.val = val
        self.shape = shape
        self.speed = speed
        self.best_pos = (x, y)

d = 50
points = []
target_x = 100
target_y = 200
step = 0.01
best_pos = (0, 0)

def get_dist(a, b):
    return math.sqrt(math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1], 2))

def c_circ(i, j):
    sol = sf.CircleShape()
    sol.radius = 2
    sol.outline_color = sf.Color.RED
    sol.fill_color = sf.Color.RED
    sol.position = (i, j)
    return sol

for i in range(800 / d):
    for j in range(600 / d):
        points.append(point(i*d, j*d, get_dist((i*d, j*d), (target_x, target_y)),
                            c_circ(i*d, j*d), (0,0)))
        if (points[-1].val < get_dist(best_pos, (target_x, target_y))):
            best_pos = points[-1].best_pos


print best_pos
points = sorted(points, key=lambda point: point.val)

def update(target_x, target_y):
    global step
    global best_pos
    global points
    closest = points[0]
    for p in points:
        a1 = random.random()
        a2 = random.random()
        p.speed = (p.speed[0]  +  0.0001 * (p.x - p.best_pos[0]) + 0.0001 * (p.x - best_pos[0]), p.speed[1]  +  0.0001 * (p.y - p.best_pos[1]) + 0.0001 * (p.y - best_pos[1]))
        p.x -= p.speed[0]
        p.y -= p.speed[1]
        p.shape.position = (p.x, p.y)
        if (get_dist((p.x, p.y), (target_x, target_x)) < get_dist((p.x, p.y), p.best_pos)):
            p.best_pos = (p.x, p.y)
            if (get_dist(p.best_pos, (target_x, target_y))
                < get_dist(best_pos, (target_x, target_y))):
                best_pos = p.best_pos
        
    points = sorted(points, key=lambda point: point.val)


targ_circ = c_circ(target_x, target_y)
targ_circ.fill_color = sf.Color.BLUE
targ_circ.radius = 4
targ_circ.origin = (2,2)

# start the game loop
while window.is_open:
    # process events
    for event in window.events:
              # close window: exit
        if type(event) is sf.CloseEvent:
            window.close()


    if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN) and target_y < 800:
        target_y += 1
        targ_circ.position += (0,1)
    if sf.Keyboard.is_key_pressed(sf.Keyboard.UP) and target_y > 0:
        target_y -= 1
        targ_circ.position -= (0,1)
    if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT) and target_x > 0:
        target_x -= 1
        targ_circ.position -= (1,0)
    if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT) and target_x < 600:
        target_x += 1
        targ_circ.position += (1,0)
    #time.sleep(0.3)
    update(target_x, target_y)
    window.clear(sf.Color.WHITE) # clear screen
    window.draw(targ_circ)
    for p in points:
        window.draw(p.shape)


    window.display() # update the window

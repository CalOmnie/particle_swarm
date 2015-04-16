import sfml as sf
import math
import time
# create the main window
window = sf.RenderWindow(sf.VideoMode(800, 600), "pySFML Window")

class point:
    def __init__(self, x, y, val, shape):
        self.x = x
        self.y = y
        self.val = val
        self.shape = shape


d = 50
points = []
target_x = 100
target_y = 200
step = 0.01


def c_circ(i, j):
    sol = sf.CircleShape()
    sol.radius = 2
    sol.outline_color = sf.Color.RED
    sol.fill_color = sf.Color.RED
    sol.position = (i, j)
    return sol

for i in range(800 / d):
    for j in range(600 / d):
        points.append(point(i*d, j*d, math.sqrt(math.pow(target_x - i*d, 2) +
                                                  math.pow(target_y - j*d, 2)),
                      c_circ(i*d, j*d)))


points = sorted(points, key=lambda point: point.val)

def update(target_x, target_y):
    global points
    closest = points[0]
    for p in points:
        p.x -= (p.x - closest.x) * step
        p.y -= (p.y - closest.y) * step
        p.val = math.sqrt(math.pow(target_x - p.x, 2) + math.pow(target_y - p.y, 2))
        p.shape.position = (p.x, p.y)

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

from vpython import *
#GlowScript 3.2 VPython

# here we code a function to create a grid.
def make_grid():
  scene.background = color.white
  thickness = 0.02
  dx = 1
  xmax = 10
  x = -xmax
  while (x <= xmax):
    y = 0
    gridline = curve(pos=[vector(x,y,-thickness)],color=color.black,radius=thickness)
    while (y <= xmax):
      gridline.append(vector(x,y,-thickness))
      y = y + dx
    x = x + dx
  y = 0
  while (y <= xmax):
    x = -xmax
    gridline = curve(pos=[vector(x,y,-thickness)],color=color.black,radius=thickness)
    while (x <= xmax):
      gridline.append(vector(x,y,-thickness))
      x = x + dx
    y = y + dx
  global ground
  ground = box(pos=vector(0,0,-thickness),size=vector(2*xmax+2*thickness,2*thickness,2*thickness),color=color.green)
  return
# we used The `marker()` function is to create a marker for the object's position, and it takes the x and y coordinates as parameters.
def marker(x,y,col):
  sleep(0.1)
  a = sphere(pos=vector(x,y,0),radius=0.4,
             color=col,make_trail=True,
             trail_type="points",
             interval=16,
             initial_pos=vector(x,y,0),
             distance=0)
  return a
#The `accelerate()` function is modified to accept additional parameters `dvx` and `dvy`, which represent the change in velocity 
 #in the x and y directions, respectively. These changes are then added to the object's velocity.  
def accelerate(name,dvx,dvy):
  name.vx = name.vx + dvx
  name.vy = name.vy + dvy
  return

def move(name,dx,dy):
  sleep(0.005)
  name.pos = name.pos + vector(dx,dy,0)
  name.distance = name.distance + sqrt(dx**2+dy**2)
  return

def distance(name):
  return name.distance
  
def displacement(name):
  dx = name.pos.x-name.initial_pos.x
  dy = name.pos.y-name.initial_pos.y
  return sqrt(dx**2+dy**2)

make_grid()

position_graph = graph(xtitle="time", ytitle="position")
velocity_graph = graph(xtitle="time", ytitle="velocity")
acceleration_graph = graph(xtitle="time", ytitle="acceleration")

Ball = marker(0.0, 0, color.red)

# here we get input from the user
def getNumeric(prompt):
    while True:
        response = input(prompt)
        try:
            return float(response)
        except ValueError:
            print("Please enter a number.")
# input of the vertical velocity and initial height. 
Ball.vx = 0.0
Ball.vy = getNumeric("Enter initial vertical velocity in meter per second: ")
Ball.pos.y = getNumeric("Enter initial height in meter: ")

Ball.ax = 0.0
Ball.ay = -9.8

#here we used the `xcurve`, `ycurve`, `vxcurve`, `vycurve`, `axcurve`, and `aycurve` variables 
 # to create graphs to track the object's position, velocity, and acceleration.
Ball.xcurve = gcurve(label="Ball's x", color=color.red, graph=position_graph)
Ball.ycurve = gcurve(label="Ball's y", color=color.blue, graph=position_graph)

Ball.vxcurve = gcurve(label="Ball's vx",
                      color=color.red,
                      graph=velocity_graph)
Ball.vycurve = gcurve(label="Ball's vy",
                      color=color.blue,
                      graph=velocity_graph)

Ball.axcurve = gcurve(label="Ball's ax",
                      color=color.red,
                      graph=acceleration_graph)
Ball.aycurve = gcurve(label="Ball's ay",
                      color=color.blue,
                      graph=acceleration_graph)

#here teacher we have tried to make the accelaration change as height changees but it gives us bulky(not ordinary number) and wehan we trried 
 #to run it it says it must be ordinary number. then we tried to decrease the number to 4 significant figure but it was not working.
G = 6.67430e-11  # Gravitational constant
M = 5.972e24  # Mass of the Earth
R = 6371000  # Radius of the Earth in meters

time = 0
time_step = 0.005

while (Ball.pos.y >= ground.pos.y):
  radius = R + Ball.pos.y  # Effective radius including height
  gravity = -G * M / radius**2 # the gravity


  dvx = Ball.ax * time_step
  dvy = (Ball.ay + 0) * time_step
  accelerate(Ball, dvx, dvy)
#we used `dx` and `dy` values to update the object's position.
  dx = Ball.vx * time_step
  dy = Ball.vy * time_step
  move(Ball, dx, dy)
# we plotd The object's position, velocity, and acceleration on the graphs by using the `plot()` method.
  Ball.xcurve.plot(pos=(time, Ball.pos.x))
  Ball.ycurve.plot(pos=(time, Ball.pos.y))
  Ball.vxcurve.plot(pos=(time, Ball.vx))
  Ball.vycurve.plot(pos=(time, Ball.vy))
  Ball.axcurve.plot(pos=(time, Ball.ax))
  Ball.aycurve.plot(pos=(time, Ball.ay))

  time += time_step
  
#Please note that you would need the necessary libraries installed and
 #run the code in an appropriate environment, such as GlowScript or
 #VPython, for it to work correctly.
 

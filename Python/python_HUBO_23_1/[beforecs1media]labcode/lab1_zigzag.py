from cs1robots import *
create_world()
hubo=Robot()
hubo.set_trace("blue")

def turn_right():
  for _ in range(3):
    hubo.turn_left()
  
def move_9():
  for _ in range(9):
    hubo.move()
  
def zigzag():
  move_9()
  turn_right()
  hubo.move()
  turn_right()
  move_9()

def zig():
  zigzag()
  hubo.turn_left()
  hubo.move()
  hubo.turn_left()

hubo.turn_left()
zig()
zig()
zig()
zig()
zigzag()


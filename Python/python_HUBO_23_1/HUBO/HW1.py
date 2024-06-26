# from cs1robots import *

# # TODO 모든 함수 input으로 robot 받기
# # TODO 계단올라가는 함수 n으로 입력받기

# load_world("./worlds/harvest2.wld")

# hubo = Robot()
# hubo.set_trace('blue')

# count = 0

# def turn_left(robot):
#     robot.turn_left()

# def turn_right(robot):
#     for _ in range(3):
#         turn_left(robot)

# def turn_around(robot):
#     for _ in range(2):
#         turn_left(robot)

# def pick_beeper(robot):
#     robot.pick_beeper()

# # 한 번 이동하면 count += 1 되는 함수
# def move_and_count(robot):
#     global count
#     robot.move()
#     count += 1

# # beepr 줍고 계단한칸 올라가기
# def pick_and_move_right_and_up(robot):
#     pick_beeper(robot)
#     turn_right(robot)
#     move_and_count(robot)
#     turn_left(robot)
#     move_and_count(robot)

# def one_cycle_pick_and_move(robot, n):
#     for _ in range(n):
#         pick_and_move_right_and_up(robot)
#     turn_right(robot)

# # 휴보 (1, 7)로 이동
# turn_left(hubo)
# for _ in range(6):
#     move_and_count(hubo)

# for n in range(5):
#     n = 5-n
#     if n == 5:
#         # 5번 계단 오르기 3번
#         for _ in range(3):
#             one_cycle_pick_and_move(hubo, n)
#     else:
#         # 4~1번 계단 오르기 2번씩
#         for _ in range(2):
#             one_cycle_pick_and_move(hubo, n)
# # 마지막 (6,6) 비퍼 줍기
# pick_beeper(hubo)

# print("move count = ", count)

import time
from cs1robots import *
create_world(avenues=9,streets=9)
hubo = Robot(beepers = 81)
hubo.set_trace('blue')
    
def move():
    hubo.move()

def turn_left():
    hubo.turn_left()

def turn_right():
    for i in range(3):
        hubo.turn_left()
        
def turn_around():
    for i in range(2):
        hubo.turn_left()
        
def drop_and_move():
    if not hubo.on_beeper():
        hubo.drop_beeper()
        hubo.move()
    else:
        hubo.move()
        


def drop_and_move_straight():
    count = 0
    while hubo.front_is_clear():
        drop_and_move()
        count += 1
    return count

for _ in range(3):
    len = drop_and_move_straight()
    turn_left()

for i in range(len):
    i = len - i - 1
    print(i)
    for _ in range(2):
        for _ in range(i):
            drop_and_move()
        turn_left()
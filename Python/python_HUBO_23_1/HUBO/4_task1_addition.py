from cs1robots import *

# load_world("./worlds/add1.wld")
# load_world("./worlds/add2.wld")
load_world("./worlds/add34.wld")

hubo = Robot(street=2, beepers=100)

# 내 풀이 

# def turn_right():
#     for _ in range(3):
#         hubo.turn_left()

# def turn_around():
#     for _ in range(2):
#         hubo.turn_left()

# def collect_number_at_street2():
#     num_string = ""                                 # street 2에서 최종적으로 만든 숫자(String)
#     while hubo.front_is_clear():
#         hubo.move()
#         num_string = num_string + pick_and_count()   # 최종 숫자 str = 지금까지 컬렉 str + 이번에 센 str
#     return num_string

# def collect_number_at_street1():
#     num_string = ""                                # street 1에서 최종적으로 만든 숫자(String)
#     while hubo.front_is_clear():
#         num_string = pick_and_count() + num_string  # 최종 숫자 str = 이번에 센 str + 지금까지 컬렉 str
#         hubo.move()
#     return num_string

# def pick_and_count():
#     count = 0
#     if hubo.on_beeper():
#         while hubo.on_beeper():
#             hubo.pick_beeper()
#             count += 1
#     return str(count)

# def right_move_right():
#     turn_right()
#     hubo.move()
#     turn_right()

# def move_until_front_not_clear():
#     while hubo.front_is_clear():
#         hubo.move()

# def drop_beepers_by_num(result_str):
#     for i in result_str[::-1]:
#         i = int(i)
#         for i in range(i):
#             hubo.drop_beeper()
#         hubo.move()


# first_num_string = collect_number_at_street2()

# right_move_right()

# second_num_string = collect_number_at_street1()

# plus_result = str(int(first_num_string) + int(second_num_string))

# turn_around()
# move_until_front_not_clear()
# turn_around()

# drop_beepers_by_num(plus_result)

# 교수님 풀이
# 10을 곱하고 뒤에걸 먹는것을 반복
# 다 더하고 아래로 내려오면서 하나씩 계산하면서 바로바로 drop
# step2 + step1의 1자리수 한다음 1자리수 버리고. 그 후 두번째자리 더하고 한다음 2자리수 버리고
# 끝까지 갔다가 다시 돌아가서 내려놓는것 아님
def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()

def pick_and_count():
    count = 0
    if hubo.on_beeper():
        while hubo.on_beeper():
            hubo.pick_beeper()
            count += 1
    return count

def multiply_10_and_add():
    result_st2 = 0
    while hubo.front_is_clear():
        hubo.move()
        count = pick_and_count()
        result_st2 = 10 * result_st2 + count
    return result_st2

def right_move_right():
    turn_right()
    hubo.move()
    turn_right()

def add_and_drop_result(result_st2):
    result = 0
    while hubo.on_beeper() or result != 0:
        count = pick_and_count()
        result = str(int(result) + result_st2)[-1]
        drop_beepers_by_num(result)
        result = result[:-1]
        hubo.move()

def drop_beepers_by_num(num):
    for _ in range(int(num)):
        hubo.drop_beeper()


result_st2 = multiply_10_and_add()
right_move_right()
add_and_drop_result(result_st2)
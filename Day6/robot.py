# Building a robot to solve the maze on the website:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json
# O mapa de desafio esta no arquivo 'problem_world3.json'
# ''' As funções abaixo não precisam ser implementadas no site
def turn_left():
    pass
def at_goal():
    pass
def front_is_clear():
    pass
def move():
    pass
def right_is_clear():
    pass
# '''

# Algortimo de solução
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    while front_is_clear():
        move()
        while right_is_clear() and not at_goal() and not front_is_clear():
            turn_right()
            move()
    else:
        turn_left()
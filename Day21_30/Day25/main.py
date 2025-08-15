import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
lista_states = data["state"].tolist()
score = 0

while len(lista_states) > 0:
    answer_state = screen.textinput(f"{score}/50 Guess the State", prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        break

    # Se o estado digitado pelo usuário é um dos 50 estados da lista
    elif answer_state in lista_states:
        # buscar coordenadas
        coordenada = data[data["state"] == answer_state]
        print(coordenada.x)
        print(coordenada.y)
        # criar tartaruga e escrever o nome
        name = turtle.Turtle()
        name.penup()
        name.hideturtle()
        name.goto(coordenada.x.item(), coordenada.y.item()) # item retorna o valor sem o index da Serie
        name.write(answer_state)
        #somar score
        score += 1
        #remove estado da lista
        lista_states.remove(answer_state)

#states_to_learn.csv
x = pandas.DataFrame(lista_states, columns=["state"])
x.to_csv("states_to_learn.csv", index=False)
import colorgram
from turtle import Turtle, Screen, colormode
from random import choice

colormode(255)
my_turtle = Turtle()
my_turtle.speed("fastest")
my_turtle.hideturtle()
my_turtle.setpos(0,0)
numero_de_cores = 30
lista_cores = [tuple(c.rgb) for c in colorgram.extract('imagem_turtle.png', numero_de_cores)]
LINHAS = 10
TAMANHO_PONTO = 20
ESPACAMENTO = 50
# configurando para comecar mais embaixo
my_turtle.setheading(225)
my_turtle.penup()
my_turtle.fd(250)
my_turtle.setheading(0)

def seleciona_cor_aleatoria(lista):
    cor = choice(lista)
    return cor

def linha(turtle):
    for _ in range(LINHAS):
        turtle.color(seleciona_cor_aleatoria(lista_cores))
        turtle.dot(size=TAMANHO_PONTO)
        turtle.penup()
        turtle.fd(ESPACAMENTO)

def proxima_linha(turtle, direcao):
    if direcao == 'esquerda':
        for _ in range(2):
            turtle.setheading(turtle.heading() - 90)
            turtle.fd(ESPACAMENTO)
    else:
        for _ in range(2):
            turtle.setheading(turtle.heading() + 90)
            turtle.fd(ESPACAMENTO)

for _ in range(LINHAS//2):
    linha(my_turtle)
    proxima_linha(my_turtle,'direita')
    linha(my_turtle)
    proxima_linha(my_turtle, 'esquerda')



my_screen = Screen()
my_screen.exitonclick()
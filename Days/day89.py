"""Gerar fractais - Árvore de Pythagoras"""

import turtle


def arvore(t, comprimento, nivel):
    if nivel == 0:
        return
    t.forward(comprimento)
    t.left(30)
    arvore(t, comprimento * 0.7, nivel - 1)
    t.right(60)
    arvore(t, comprimento * 0.7, nivel - 1)
    t.left(30)
    t.backward(comprimento)


def main():
    nivel = int(input("Digite a profundidade da árvore (ex: 6): "))
    comprimento = 100

    tela = turtle.Screen()
    tela.title("Árvore Fractal")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()

    arvore(t, comprimento, nivel)

    t.hideturtle()
    tela.mainloop()


if __name__ == "__main__":
    main()

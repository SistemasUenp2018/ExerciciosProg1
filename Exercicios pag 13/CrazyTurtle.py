import colorsys
import turtle

caneta = turtle.Turtle() #Faz a instancia da classe turtle
caneta.hideturtle()  #Esconde p cursor
caneta.shape("turtle")
caneta.speed("fastest")
cont =0
num = 150
num2 = 3
while (cont < 150) :
    print("Cont ", cont )
    print("num ", num)
    print("num2 ", num2)
    caneta.circle(num) #desenha um circulo de 50px
    caneta.up() #Levanta a caneta do turtle, pra nao deixar o rastro do cursor
    caneta.setposition(0, num2) #posiciona o circulo dentro do outro circulo
    caneta.down() #desce a caneta do turtle, para voltar a desenhar
    cont += 1
    num -= 3
    num2 += 3
turtle.done()     #O cursor turtle para.

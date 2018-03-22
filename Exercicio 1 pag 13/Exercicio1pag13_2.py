import colorsys
import turtle

tata = turtle.Turtle() #Faz a instancia da classe turtle
tata.hideturtle()  #Esconde p cursor
tata.circle(50) #desenha um circulo de 50px
tata.up() #Levanta a caneta do turtle, pra nao deixar o rastro do cursor
tata.setposition(0,10) #posiciona o circulo dentro do outro circulo
tata.down() #desce a caneta do turtle, para voltar a desenhar
tata.circle(40) #desenha um circulo de 40px
tata.up() #Levanta a caneta do turtle, pra nao deixar o rastro do cursor
tata.setposition(0,20) #posiciona o circulo dentro do outro circulo
tata.down() #desce a caneta do turtle, para voltar a desenhar
tata.circle(30) #desenha um circulo de 30px
tata.up() #Levanta a caneta do turtle, pra nao deixar o rastro do cursor
tata.setposition(0,30) #posiciona o circulo dentro do outro circulo
tata.down() #desce a caneta do turtle, para voltar a desenhar
tata.circle(20) #desenha um circulo de 20px
turtle.done()     #O cursor turtle para.
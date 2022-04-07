'''
Created on Apr 6, 2022

@author: tyler
'''
import turtle

from Graph import Graph

g = Graph()

g.addNode(1)
g.addNode(2)
g.addNode(3)

g.addEdge(1,2)
g.addEdge(2,3)


t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
ws = turtle.Screen()
t2.pensize(10)
t2.color('green')
r = 30

t.up()
t.goto(-200, -200)
t.down()
t.begin_fill()
t.color('red')
t.circle(r)
t.end_fill()

t1.up()
t1.goto(-250, -250)
t1.color('black')
t1.write('Driver', font=('Arial', 20))
t1.down()

t2.up()
t2.goto(-200, -140)
t2.down()
t2.goto(0, 150)

t.up()
t.goto(0, 150)
t.down()
t.begin_fill()
t.color('orange')
t.circle(r)
t.end_fill()

t2.goto(200, -140)
t1.up()
t1.goto(-60, 250)
t1.color('black')
t1.write('Restaurant', font=('Arial', 20))
t1.down()

t.up()
t.goto(200, -200)
t.down()
t.begin_fill()
t.color('yellow')
t.circle(r)
t.end_fill()

t1.up()
t1.goto(175, -250)
t1.color('black')
t1.write('Customer', font=('Arial', 20))
t1.down()


ws.exitonclick()





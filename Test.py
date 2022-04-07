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
g.addedge(3,1)


t = turtle.Turtle()
ws = turtle.Screen()

r = 30
t.up()
t.goto(-200, -200)
t.down()
t.begin_fill()
t.color('red')
t.circle(r)
t.end_fill()

t.goto(0, 150)
t.begin_fill()
t.color('green')
t.circle(r)
t.end_fill()

t.goto(200, -200)
t.begin_fill()
t.color('yellow')
t.circle(r)
t.end_fill()
ws.exitonclick()



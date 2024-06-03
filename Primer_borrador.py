#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Insight -> Insound
Evidencia -> 


# # Ejemplos fractales

# # Koch
# 
# Cada iteración divide cada segmento en 3 partes

# In[ ]:


### Curva de Koch

import turtle
from music21 import *

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

### Curva de Koch

axiom = "F--F--F"
rules = {"F":"F+F--F+F"}
iterations = 3 # TOP: 7
angle = 60
create_l_system(1, axiom, rules)

### 

types = ['maxima', 'breve', 'half', 'eighth', '32nd', '64th']  ### máxima 8 compases, breve 2 compases, half es medio compás, etc.
its = iterations + 1
t = stream.Stream()
L = []
for it in range(its):
    nota = int(36+12*it)
    k = 0
    for cmd in create_l_system(it, axiom, rules):
        if cmd == 'F':
            n = note.Note(nota, type=types[it]) ### types es la duración de la nota
            t.insert( k*(8/4**it), n)
            L += [nota]
            #print(k, nota, n, n.octave, n.duration)
            k += 1 
        elif cmd == '+':
            nota = (nota-angle/30)
        elif cmd == '-':
            nota = (nota+angle/30)
            
            

def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

#Cada iteración divide los segmentos en 3
def main(iterations, axiom, rules, angle, length=18, size=4, y_offset=-250,
        x_offset=150, offset_angle=0, width=700, height=700):

    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()

    cv = turtle.getcanvas()
    #cv.postscript(file='/Users/pepino/Documents/Tesis/PS/Koch/Koch_it0.ps', colormode='color')
    wn.exitonclick()

t.show('midi')

#t.write('midi', '/Users/pepino/Documents/Tesis/Midis/Koch/Koch_it5.midi')
main(iterations, axiom, rules, angle)


# In[2]:


t.show('midi')


# # Hilbert
# 
# Cada iteración divide los segmentos en 2n + 1

# In[8]:


## Hilbert's 
axiom = "L"
rules = {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"}
iterations = 1 # TOP: 9
angle = 90

import turtle

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

def main(iterations, axiom, rules, angle, length=630, size=2, y_offset=-310,
        x_offset=-320, offset_angle=0, width=800, height=800):

    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    
    cv = turtle.getcanvas()
    #cv.postscript(file='/Users/pepino/Documents/Tesis/PS/Hilbert/Hilbert_it7.ps', colormode='color')

    wn.exitonclick()

#durations = L
durations = [3, 15, 63, 255, 1023, 4095, 16383]
from music21 import *
t = stream.Stream()

types = ['maxima', 'breve', 'half', 'eighth', '32nd', '64th', '128th', '256th', '512th']  ### máxima 8 compases, breve 2 compases, half es medio compás, etc.
its = iterations + 1
t = stream.Stream()
L = []
for it in range(its-1,its): ###Para que suene una sola iteración: range(its-1, its) para que suenen todas range(its)
    nota = int(36+12*it)
    k = 0
    for cmd in create_l_system(it, axiom, rules):
        if cmd == 'F':
            n = note.Note(nota, type=types[it]) ### types es la duración de la nota
            t.insert( k*(8/4**it), n)
            L += [nota]
            #print(k, nota, n, n.octave, n.duration)
            k += 1 
        elif cmd == '+':
            nota = (nota-angle/30)
        elif cmd == '-':
            nota = (nota+angle/30)
            
t.show('midi')
#t.write('midi', '/Users/pepino/Documents/Tesis/Midis/Hilbert/Hilbert_it8.midi')
#print(create_l_system(iterations, axiom, rules))
#main(iterations, axiom, rules, angle)


# It 1: 1x1
# It 2: 3x3
# It 3: 7x7
# It 4: 15x15
# It 5: 31x31
# 

# # Gosper
# 
# Cada iteración divide el largo en...

# In[ ]:


### 19/04/22

#Gosper

axiom = "FX"
rules = {"X":"X+YF++YF-FX--FXFX-YF+", "Y": "-FX+YFYF++YF+FX--FX-Y"}
iterations = 0 #TOP: 6
angle = 60
#draw_l_system(iterations, axiom, rules)

#durations = L
durations = [3, 15, 63, 255, 1023, 4095, 16383]
from music21 import *
t = stream.Stream()

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

types = ['maxima', 'breve', 'half', 'eighth', '32nd', '64th', '128th']  ### máxima 8 compases, breve 2 compases, half es medio compás, etc.
its = iterations + 1 ## NÚMERO DE ITERACIONES
t = stream.Stream()
L = []
for it in range(its-1, its): ###Para que suene una sola iteración: range(its-1, its) para que suenen todas range(its)
    nota = int(36+12*it)
    k = 0
    for cmd in create_l_system(it, axiom, rules):
        if cmd == 'F':
            n = note.Note(nota, type=types[it]) ### types es la duración de la nota
            t.insert( k*(8/4**it), n)
            L += [nota]
            #print(k, nota, n, n.octave, n.duration)
            k += 1 
        elif cmd == '+':
            nota = (nota-angle/30)
        elif cmd == '-':
            nota = (nota+angle/30)
 
## ------------------------------Conjunto de instrucciones para dibujar ------------------------

import turtle

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

##------------------- Función para interpretar las funciones y que dibuje -------------------------------

def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

def main(iterations, axiom, rules, angle, length=600, size=2, y_offset=-300,
        x_offset=0, offset_angle=0, width=800, height=800):

    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    
    cv = turtle.getcanvas()
    cv.postscript(file='/Users/pepino/Documents/Tesis/PS/Gosper/gosper_it0.ps', colormode='color')

    wn.exitonclick()
            
t.show('midi')
#t.write('midi', '/Users/pepino/Documents/Tesis/Midis/Gosper/gosper_it4.midi')
#print(create_l_system(iterations, axiom, rules))
main(iterations, axiom, rules, angle)


# # Dragón

# In[ ]:


##dragon 

import turtle
axiom = "FX+FX+FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 0 # TOP: 15
angle = 90


from music21 import *
t = stream.Stream()

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

##------------------- Función para interpretar las funciones y que dibuje -------------------------------

def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

def main(iterations, axiom, rules, angle, length=600, size=2, y_offset=-300,
        x_offset=-300, offset_angle=0, width=800, height=800):

    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    
    cv = turtle.getcanvas()
    cv.postscript(file='/Users/pepino/Documents/Tesis/PS/Dragon/Dragon_it0.ps', colormode='color')

    wn.exitonclick()

    

    

types = ['maxima', 'longa', 'breve', 'whole', 'half', 'quarter', 'eighth','16th', '32nd', '64th', '128th', '256th', '512th']
### máxima 8 compases, breve 2 compases, half es medio compás, etc.
its = iterations + 1
t = stream.Stream()
L = []
for it in range(its):
    nota = int(36+12*it)
    k = 0
    for cmd in create_l_system(it, axiom, rules):
        if cmd == 'F':
            n = note.Note(nota, type=types[it+1]) ### types es la duración de la nota
            t.insert( k*(8/2**it), n) #8 compases entre 2**it porque para cada iteración sucesiva, la siguiente nota viene en la mitad del compás anterior.
            L += [nota]
            k += 1 
        elif cmd == '+':
            nota = (nota-angle/30)
        elif cmd == '-':
            nota = (nota+angle/30)


t.show('midi')

#t.show('text')
#t.write('midi', '/Users/pepino/Documents/Tesis/Midis/Dragon/dragón_it11.midi')

main(iterations, axiom, rules, angle)

#Para extraer el canvas:



# # Triángulo
# 
# Cada iteración se divide en 

# In[ ]:


##triángulo 

import turtle
axiom = "F+F+F"
rules = {"F":"F-F+F"}
iterations = 2
angle = 120


from music21 import *
t = stream.Stream()

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

##------------------- Función para interpretar las funciones y que dibuje -------------------------------

def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

def main(iterations, axiom, rules, angle, length=175, size=2, y_offset=-300,
        x_offset=150, offset_angle=0, width=800, height=800):

    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    
    cv = turtle.getcanvas()
    #cv.postscript(file='/Users/pepino/Documents/Tesis/PS/Triangulo/Triangulo_it3.ps', colormode='color')

    wn.exitonclick()

    

    
#types = ['longa', 'whole', 'quarter', '16th', '64th' ]
types = ['maxima', 'longa', 'breve', 'whole', 'half', 'quarter', 'eighth','16th', '32nd', '64th', '128th', '256th', '512th']
#types = ['maxima', 'breve', 'half', 'eighth', '32nd', ]  ### máxima 8 compases, breve 2 compases, half es medio compás, etc.
its = iterations + 1
t = stream.Stream()
L = []
for it in range(its):
    nota = int(36+12*it)
    k = 0
    for cmd in create_l_system(it, axiom, rules):
        if cmd == 'F':
            n = note.Note(nota, type=types[it+1]) ### types es la duración de la nota
            t.insert( k*(8/2**it), n) #8 compases entre 2**it porque para cada iteración sucesiva, la siguiente nota viene en la mitad del compás anterior.
            L += [nota]
            #print(k, nota, n, n.octave, n.duration)
            k += 1 
        elif cmd == '+':
            nota = (nota-angle/30)
        elif cmd == '-':
            nota = (nota+angle/30)


t.show('midi')

#t.show('text')
#t.write('midi', '/Users/pepino/Documents/Tesis/Midis/Triangulo/Triangulo_it3.midi')

main(iterations, axiom, rules, angle)

#Para extraer el canvas:



# # Cuadrado de Sierpinski
# 
# Cada iteración se divide en 

# In[ ]:


##Cuadrado de 

import turtle
axiom = "F+XF+F+XF"
rules = {"X":"XF-F+F-XF+F+XF-F+F-X"}
iterations = 1 
angle = 90


from music21 import *
t = stream.Stream()

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

##------------------- Función para interpretar las funciones y que dibuje -------------------------------

def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

def main(iterations, axiom, rules, angle, length=50, size=2, y_offset=0,
        x_offset=0, offset_angle=0, width=800, height=800):

    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    
    cv = turtle.getcanvas()
    #cv.postscript(file='/Users/pepino/Documents/Tesis/PS/CuadradodeSierpinski/CuadradodeSierpinski_it0.ps', colormode='color')

    wn.exitonclick()

    

    
#types = ['longa', 'whole', 'quarter', '16th', '64th' ]
types = ['maxima', 'longa', 'breve', 'whole', 'half', 'quarter', 'eighth','16th', '32nd', '64th', '128th', '256th', '512th']
#types = ['maxima', 'breve', 'half', 'eighth', '32nd', ]  ### máxima 8 compases, breve 2 compases, half es medio compás, etc.
its = iterations + 1
t = stream.Stream()
L = []
for it in range(its):
    nota = int(36+12*it)
    k = 0
    for cmd in create_l_system(it, axiom, rules):
        if cmd == 'F':
            n = note.Note(nota, type=types[it+1]) ### types es la duración de la nota
            t.insert( k*(8/2**it), n) #8 compases entre 2**it porque para cada iteración sucesiva, la siguiente nota viene en la mitad del compás anterior.
            L += [nota]
            #print(k, nota, n, n.octave, n.duration)
            k += 1 
        elif cmd == '+':
            nota = (nota-angle/30)
        elif cmd == '-':
            nota = (nota+angle/30)


t.show('midi')

#t.show('text')
#t.write('midi', '/Users/pepino/Documents/Tesis/Midis/CuadradoDeSierpinski/CuadradoDeSierpinski_it11.midi')

main(iterations, axiom, rules, angle)

#Para extraer el canvas:



# # Para extraer el canvas:
# 
# cv = turtle.getcanvas()
#     cv.postscript(file='/Users/pepino/Documents/Tesis/SageMath/PS/Dragon_it6.ps', colormode='color')

# In[10]:


from midi2audio import FluidSynth
fs = FluidSynth('/Users/pepino/Documents/Tesis/SageMath/Midis/dragón.midi')
fs.midi_to_audio(, '/Users/pepino/Documents/Tesis/SageMath/Midis/dragón.wav')


# 

# # Ejemplos naturales

# # Rosmarin
# 
# Cada iteración divide los segmentos en tres.

# In[ ]:


#rosmarin

import turtle

D = 90 #D de Direction
L = 10 #L de length

def iterate(axiom, num=0, initator='F'):
    """
    Compute turtle rule string by iterating on an axiom
    """

    def translate(current, axiom):
        """
        Translate all the "F" with the axiom for current string
        """
        result = ''
        consts = {'+', '-', '[', ']'}
        for c in current:
            if c in consts:
                result += c
                continue
            if c == 'F':
                result += axiom
        return result

    # Set initator
    result = initator
    for i in range(0, num):
        # For ever iteration, translate the rule string
        result = translate(result, axiom)
    return result

def draw(axiom, d=D, l=L):
    
    stack  = []                 # Para rastrear la ubicacion de tortuga
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    alex   = turtle.Turtle()

    alex.speed(3)               # Velocidad de tortuga
    alex.left(90)               # apuntar hacia arriba en vez de la derecha
    alex.penup()
    alex.setx(0)
    alex.sety(-300)
    alex.pendown()
    for i in range(len(axiom)):
        c = axiom[i]

        if c == 'F':
            alex.forward(l)

        if c == 'f':
            alex.penup()
            alex.forward(l)
            alex.pendown()

        if c == '+':
            alex.left(d)

        if c == '-':
            alex.right(d)

        if c == '[':
            stack.append((alex.heading(), alex.pos()))

        if c == ']':
            heading, position = stack.pop()
            alex.penup()
            alex.goto(position)
            alex.setheading(heading)
            alex.pendown()

    screen.onkey(screen.bye, 'q')
    screen.listen()
    
    cv = turtle.getcanvas()
    cv.postscript(file='/Users/.../CURVA_itN.ps', colormode='color')
    
    alex.hideturtle()
    turtle.mainloop()

#rosmarin

axiom = "F[+F]F[-F]F"



from music21 import *
angle = 25
t = stream.Stream()
L = []
types = ['maxima', 'breve', 'half', 'eighth', '32nd', '64th']
its = 0 #Aqui cambio las iteraciones que suenan
axioma = iterate(axiom, its-1, "F")

for it in range(its):
    nota = int(35+12*it) #Empieza en Si en lugar de Do
    k = 0
    for cmd in iterate(axiom, it, "F"):
        if cmd == 'F':
            n = note.Note(int(nota), type=types[it])
            t.insert( k, n)
            L += [(nota, str(n.duration).split(' ')[1][:-1])]
            k = k + 16/4**it
        elif cmd == '+':
            nota = (nota-3)
        elif cmd == '-':

            nota = (nota+3)
        elif cmd == '[':
            guardada = nota
        elif cmd == ']':
            nota = guardada    
        
#t.show('text')           
t.show('midi')
t.write('midi', '/Users/pepino/Documents/Tesis/Midis/Rosmarin/Rosmarin_it0.midi')
draw(axioma, 25, 600)

#Rosmarin


# # Ramitas
# 
# Cada iteración divide los segmentos en 3

# In[ ]:


#Ramitas

import turtle

D = 90 #D de Direction
L = 10 #L de length

def iterate(axiom, num=0, initator='F'):
    """
    Compute turtle rule string by iterating on an axiom
    """

    def translate(current, axiom):
        """
        Translate all the "F" with the axiom for current string
        """
        result = ''
        consts = {'+', '-', '[', ']'}
        for c in current:
            if c in consts:
                result += c
                continue
            if c == 'F':
                result += axiom
        return result

    # Set initator
    result = initator
    for i in range(0, num):
        # For ever iteration, translate the rule string
        result = translate(result, axiom)
    return result

def draw(axiom, d=D, l=L):
    """
    Use turtle to draw the L-System
    """
    stack  = []                 # For tracking turtle positions
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    alex   = turtle.Turtle()

    #alex.hideturtle()           # Don't show the turtle
    alex.speed(3)               # Make the turtle faster
    alex.left(90)               # Point up instead of right
    alex.penup()
    alex.setx(0)
    alex.sety(-360)
    alex.pendown()
    for i in range(len(axiom)):
        c = axiom[i]

        if c == 'F':
            alex.forward(l)

        if c == 'f':
            alex.penup()
            alex.forward(l)
            alex.pendown()

        if c == '+':
            alex.left(d)

        if c == '-':
            alex.right(d)

        if c == '[':
            stack.append((alex.heading(), alex.pos()))

        if c == ']':
            heading, position = stack.pop()
            alex.penup()
            alex.goto(position)
            alex.setheading(heading)
            alex.pendown()

    screen.onkey(screen.bye, 'q')
    screen.listen()
    
    cv = turtle.getcanvas()
    #cv.postscript(file='/Users/pepino/Documents/Tesis/PS/Ramitas/Ramitas_it5.ps', colormode='color')
    
    alex.hideturtle()
    turtle.mainloop()

its = 3
axiom = "F[-F]F[+F]F"
axioma = iterate(axiom, its-1, "F")


from music21 import *
angle = 60
t = stream.Stream()
L = []
types = ['maxima', 'breve', 'half', 'eighth', '32nd', ]

for it in range(its):
    nota = int(35+12*it)
    k = 0
    for cmd in iterate(axiom, it, "F"):
        if cmd == 'F':
            n = note.Note(int(nota), duration = duration.Duration(25/5**it))
            t.insert( k*(125/5**it), n)
            L += [(nota, str(n.duration).split(' ')[1][:-1])]
            #k = k + 10/5**it
            k += 1
        elif cmd == '+':
            nota = (nota-3)
        elif cmd == '-':
            nota = (nota+3)
        elif cmd == '[':
            guardada = nota
        elif cmd == ']':
            nota = guardada

#t.show('text')
t.show('midi')
#t.write('midi', '/Users/pepino/Documents/Tesis/Midis/Ramitas/Ramitas_it5.midi')
draw(axioma, 60, 27)


# OBSERVACIONES RAMITAS:
#     Suenan dos notas en cada inicio y fin de un árbol (más de un paso)
#     Tiempo?

# # Bola de Ramitas
# 
# Cada iteración divide los segmentos en:

# In[ ]:


#Bola de ramitas

import turtle

D = 90 #D de Direction
L = 10 #L de length

def iterate(axiom, num=0, initiator='F'):
    """
    Compute turtle rule string by iterating on an axiom
    """

    def translate(current, axiom):
        """
        Translate all the "F" with the axiom for current string
        """
        result = ''
        consts = {'+', '-', '[', ']'}
        for c in current:
            if c in consts:
                result += c
                continue
            if c == 'F':
                result += axiom
        return result

    # Set initiator
    result = initiator
    for i in range(0, num):
        # For every iteration, translate the rule string
        result = translate(result, axiom)
    return result

def draw(axiom, d=D, l=L):
    """
    Use turtle to draw the L-System
    """
    stack  = []                 # For tracking turtle positions
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    alex   = turtle.Turtle()

    #alex.hideturtle()           # Don't show the turtle
    alex.speed(50)               # Make the turtle faster
    alex.left(90)               # Point up instead of right
    alex.penup()
    alex.setx(-100)
    alex.sety(100)
    alex.pendown()
    for i in range(len(axiom)):
        c = axiom[i]

        if c == 'F':
            alex.forward(l)

        if c == 'f':
            alex.penup()
            alex.forward(l)
            alex.pendown()

        if c == '+':
            alex.left(d)

        if c == '-':
            alex.right(d)

        if c == '[':
            stack.append((alex.heading(), alex.pos()))

        if c == ']':
            heading, position = stack.pop()
            alex.penup()
            alex.goto(position)
            alex.setheading(heading)
            alex.pendown()

    screen.onkey(screen.bye, 'q')
    screen.listen()
    
    cv = turtle.getcanvas()
    #cv.postscript(file='/Users/pepino/Documents/Tesis/PS/BolaDeRamitas/BolaDeRamitas_it5.ps', colormode='color')
    
    alex.hideturtle()
    turtle.mainloop()

its = 3
axiom = "F -> F[+F]F[-F][F]"
sistema = iterate(axiom, its-1, "F")


from music21 import *
angle = 20
t = stream.Stream()
L = []
types = ['maxima', 'breve', 'half', 'eighth', '32nd', ]

for it in range(its):
    nota = int(25+12*it)
    k = 0
    for cmd in iterate(axiom, it, "F"):
        if cmd == 'F':
            n = note.Note(int(nota), duration = duration.Duration(25/5**it))
            t.insert( k*(25/5**it), n)
            L += [(nota, str(n.duration).split(' ')[1][:-1])]
            #k = k + 10/5**it
            k += 1
        elif cmd == '+':
            nota = (nota-1)
        elif cmd == '-':
            nota = (nota+1)
        elif cmd == '[':
            guardada = nota
        elif cmd == ']':
            nota = guardada
            
t.show('midi')
#t.write('midi', '/Users/pepino/Documents/Tesis/Midis/BolaDeRamitas/BolaDeRamitas_it5.midi')
draw(sistema, 20, 30)


# # Tupida simétrica
# 
# 

# In[ ]:


#tupida simétrica

import turtle

D = 90 #D de Direction
L = 10 #L de length

def iterate(axiom, num=0, initator='F'):
    """
    Compute turtle rule string by iterating on an axiom
    """

    def translate(current, axiom):
        """
        Translate all the "F" with the axiom for current string
        """
        result = ''
        consts = {'+', '-', '[', ']'}
        for c in current:
            if c in consts:
                result += c
                continue
            if c == 'F':
                result += axiom
        return result

    # Set initator
    result = initator
    for i in range(0, num):
        # For ever iteration, translate the rule string
        result = translate(result, axiom)
    return result

def draw(axiom, d=D, l=L):
    """
    Use turtle to draw the L-System
    """
    stack  = []                 # For tracking turtle positions
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    alex   = turtle.Turtle()

    #alex.hideturtle()           # Don't show the turtle
    alex.speed(3)               # Make the turtle faster
    alex.left(90)               # Point up instead of right
    alex.penup()
    alex.setx(0)
    alex.sety(-300)
    alex.pendown()
    for i in range(len(axiom)):
        c = axiom[i]

        if c == 'F':
            alex.forward(l)

        if c == 'f':
            alex.penup()
            alex.forward(l)
            alex.pendown()

        if c == '+':
            alex.left(d)

        if c == '-':
            alex.right(d)

        if c == '[':
            stack.append((alex.heading(), alex.pos()))

        if c == ']':
            heading, position = stack.pop()
            alex.penup()
            alex.goto(position)
            alex.setheading(heading)
            alex.pendown()

    screen.onkey(screen.bye, 'q')
    screen.listen()
    
    cv = turtle.getcanvas()
   # cv.postscript(file='/Users/pepino/Documents/Tesis/PS/Rosmarin/Rosmarin_it0.ps', colormode='color')
    
    alex.hideturtle()
    turtle.mainloop()


axiom = "F[+F[+F][-F]F][-F[+F][-F]F]F[+F][-F]F"



from music21 import *
angle = 25
t = stream.Stream()
L = []
types = ['maxima', 'breve', 'half', 'eighth', '32nd', '64th']
its = 4 #Aquí cambio las iteraciones que suenan
axioma = iterate(axiom, its-1, "F")

for it in range(its):
    nota = int(35+12*it) #Empieza en Si en lugar de Do
    k = 0
    for cmd in iterate(axiom, it, "F"):
        if cmd == 'F':
            n = note.Note(int(nota), type=types[it])
            t.insert( k, n)
            L += [(nota, str(n.duration).split(' ')[1][:-1])]
            k = k + 16/4**it
        elif cmd == '+':
            nota = (nota-3)
        elif cmd == '-':

            nota = (nota+3)
        elif cmd == '[':
            guardada = nota
        elif cmd == ']':
            nota = guardada    
        
#t.show('text')           
t.show('midi')
#t.write('midi', '/Users/pepino/Documents/Tesis/Midis/Rosmarin/Rosmarin_it0.midi')
draw(axioma, 30, 10)


# # Arbusto
# 
# 

# In[1]:


#tupida simétrica

import turtle

D = 90 #D de Direction
L = 10 #L de length

def iterate(axiom, num=0, initator='F'):
    """
    Compute turtle rule string by iterating on an axiom
    """

    def translate(current, axiom):
        """
        Translate all the "F" with the axiom for current string
        """
        result = ''
        consts = {'+', '-', '[', ']'}
        for c in current:
            if c in consts:
                result += c
                continue
            if c == 'F':
                result += axiom
        return result

    # Set initator
    result = initator
    for i in range(0, num):
        # For ever iteration, translate the rule string
        result = translate(result, axiom)
    return result

def draw(axiom, d=D, l=L):
    """
    Use turtle to draw the L-System
    """
    stack  = []                 # For tracking turtle positions
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    alex = turtle.Turtle()

    #alex.hideturtle()           # Don't show the turtle
    alex.speed(3)               # Make the turtle faster
    alex.left(90)               # Point up instead of right
    alex.penup()
    alex.setx(0)
    alex.sety(-300)
    alex.pendown()
    for i in range(len(axiom)):
        c = axiom[i]

        if c == 'F':
            alex.forward(l)

        if c == 'f':
            alex.penup()
            alex.forward(l)
            alex.pendown()

        if c == '+':
            alex.left(d)

        if c == '-':
            alex.right(d)

        if c == '[':
            stack.append((alex.heading(), alex.pos()))

        if c == ']':
            heading, position = stack.pop()
            alex.penup()
            alex.goto(position)
            alex.setheading(heading)
            alex.pendown()

    screen.onkey(screen.bye, 'q')
    screen.listen()
    
    cv = turtle.getcanvas()
   # cv.postscript(file='/Users/pepino/Documents/Tesis/PS/Rosmarin/Rosmarin_it0.ps', colormode='color')
    
    alex.hideturtle()
    turtle.mainloop()


axiom = "FF+[+F-F-F]-[-F+F+F]"



from music21 import *
angle = 22.5
t = stream.Stream()
L = []
types = ['maxima', 'breve', 'half', 'eighth', '32nd', '64th']
its = 2 #Aquí cambio las iteraciones que suenan
axioma = iterate(axiom, its-1, "F")

for it in range(its):
    nota = int(35+12*it) #Empieza en Si en lugar de Do
    k = 0
    for cmd in iterate(axiom, it, "F"):
        if cmd == 'F':
            n = note.Note(int(nota), type=types[it])
            t.insert( k, n)
            L += [(nota, str(n.duration).split(' ')[1][:-1])]
            k = k + 16/4**it
        elif cmd == '+':
            nota = (nota-3)
        elif cmd == '-':

            nota = (nota+3)
        elif cmd == '[':
            guardada = nota
        elif cmd == ']':
            nota = guardada    
        
#t.show('text')           
t.show('midi')
#t.write('midi', '/Users/pepino/Documents/Tesis/Midis/Rosmarin/Rosmarin_it0.midi')
draw(axioma, 30, 10)


# # Sistemas L Estocásticos

# In[ ]:


w: F
p1: F -> F[+F]F[-F]F
p2: F -> F[+F]F
p3: F -> F[-F]F


# In[ ]:


from random import randint as rint

#Aquí están las reglas
Rules = ["F[+F]F[-F][F]", "F[+F]F", "F[-F]F"]

d_elecciones = {}
l_elecciones = []

#Aqui estan las iteraciones
its = 4

def iterate(Rules, num=0, initiator='F'):
    """
    Compute turtle rule string by iterating on an axiom
    """
    
    def translate(current, Rules):
        """
        Translate all the "F" with the axiom for current string
        """
        result = ''
        consts = {'+', '-', '[', ']'}
        for c in current:
            if c in consts:
                result += c
                continue
            if c == 'F':
                r = rint(0, len(Rules)-1)
                axiom = Rules[r]
                d_elecciones[i][0].append(r)
                result += axiom
        return result

    # Fijar inicial
    result = initiator
    for i in range(0, num):
        d_elecciones[i] = [[],'']
        # Para cada iteracion traduce el string de la regla
        result = translate(result, Rules)
        d_elecciones[i][1] += result
    return result

def elecc_str_dur(dicc, dur):
    dicc2 = dicc
    divs = [5,3,3]
    dur_ps = [dur]
    dur_f = []
    for key in dicc2.keys():
        dur_p = dur
        x = 0
        for i in dicc2[key][0]:

            dur = dur_ps[x]/divs[i]

            x += 1
            for j in range(0,divs[i]):
                dur_f.append(dur)
                dur_ps.append(dur)

            
        dicc2[key].append(dur_ps[len(dicc2[key][0]):])
        dur_ps = dur_ps[len(dicc2[key][0]):]
        
    return dicc2


# In[ ]:


final = iterate(Rules, its, "F")
final


# In[ ]:


d_elecciones


# In[ ]:


dur = 90
master = elecc_str_dur(d_elecciones,dur)
master


# In[ ]:


from music21 import *
dur = 90
master = elecc_str_dur(d_elecciones,dur)
angle = 60
t = stream.Stream()
L = []
types = ['maxima', 'breve', 'half', 'eighth', '32nd', ]



divs = [5,3,3]
r_indx = 0 #indice de la lista de elecciones aleatoras


 

for key in master.keys():
    
    it = key
    nota = int(35+12*it)
    ins_pos = 0 #insert position
    
    i = 0    
    for cmd in master[key][1]:
        
        if cmd == 'F':
            dur_nota = master[key][2][i]
            n = note.Note(int(nota), 
            duration = duration.Duration(dur_nota))
            t.insert(ins_pos,n)
            L += [(nota, str(n.duration).split(' ')[1][:-1])]
            ins_pos += dur_nota
            i += 1
            
        elif cmd == '+':
            nota = (nota-3)
        elif cmd == '-':
            nota = (nota+3)
        elif cmd == '[':
            guardada = nota
        elif cmd == ']':
            nota = guardada
    
    if r_indx > len(d_elecciones[key][0])-1:
        break
    
    num_F = divs[d_elecciones[key][0][r_indx]] 
    #cant. Fs en regla elegida

    r_indx += 1
    
t.show("midi")
#t.show("text")


# In[ ]:


import turtle

D = 90 #D de Direction
L = 10 #L de length

def draw(axiom, d=D, l=L):
    """
    Use turtle to draw the L-System
    """
    stack  = []                 # For tracking turtle positions
    screen = turtle.Screen()
    alex   = turtle.Turtle()

    alex.hideturtle()           # Don't show the turtle
    alex.speed(0)               # Make the turtle faster
    alex.left(90)               # Point up instead of right

    for i in range(len(axiom)):
        c = axiom[i]

        if c == 'F':
            alex.forward(l)

        if c == 'f':
            alex.penup()
            alex.forward(l)
            alex.pendown()

        if c == '+':
            alex.left(d)

        if c == '-':
            alex.right(d)

        if c == '[':
            stack.append((alex.heading(), alex.pos()))

        if c == ']':
            heading, position = stack.pop()
            alex.penup()
            alex.goto(position)
            alex.setheading(heading)
            alex.pendown()

    screen.onkey(screen.bye, 'q')
    screen.listen()
    turtle.mainloop()
    
draw(final, 20, 10)


# # Sistemas L Sensibles a Contexto

# In[ ]:




#pos = ['[F', 'F]', '+F', 'F+', '-F', 'F-', 'FF']
#pos_r = ['[F', '+F', '-F', 'FF']

Axiom = ["FF", "F[+F]F[-F][F]","[--F]", "F[+F]F", "F[-F]F", "[++F]", ]


pos_l = ['F', 'F]', 'F+', 'F-', 'F[', "FF"]

def iterate(Axiom, num=0, initator='F'):
    """ Produccion de string de iteraciones"""
    def translate(current, Axiom):
        """Traducir las "F" a partir del axioma y las reglas"""
        result = ''
        consts = {'+', '-', '[', ']'}
        iii = int(0)
        for c in current:
            if c in consts:
                result += c
                iii += 1
                continue
            if c == 'F':
                try:
                    axiom = Axiom[pos_l.index(current[iii:iii+2])]
                except Exception as e:
                    print(e, iii, current, c)
                    axiom = Axiom[-1]
                result += axiom
                iii += 1
        return result        
    # Set initator
    result = initator
    for i in range(0, num):
        # Para cada iteracion, traducir la cadena
        result = translate(result, Axiom)
    return result

from music21 import *
angle = 20
t = stream.Stream()
L = []
types = ['maxima', 'breve', 'half', 'eighth', '32nd', ]
its = 5
for it in range(its):
    nota = int(25+12*it)
    k = 0
    for cmd in iterate(Axiom, it, "F"):
        if cmd == 'F':
            n = note.Note(int(nota), duration = duration.Duration(25/5**it))
            t.insert( k*(125/5**it), n)
            L += [(nota, str(n.duration).split(' ')[1][:-1])]
            k += 1
        elif cmd == '+':
            nota = (nota-1)
        elif cmd == '-':
            nota = (nota+1)
        elif cmd == '[':
            guardada = nota
        elif cmd == ']':
            nota = guardada

sistema = iterate(Axiom, its-1, "F")
t.show('midi')

import turtle
D = 90 #D de Direction
L = 10 #L de length
def draw(axiom, d=D, l=L):
    """
    Use turtle to draw the L-System
    """
    stack  = []                 # For tracking turtle positions
    screen = turtle.Screen()
    alex   = turtle.Turtle()

    alex.hideturtle()           # Don't show the turtle
    alex.speed(0)               # Make the turtle faster
    alex.left(90)               # Point up instead of right

    for i in range(len(axiom)):
        c = axiom[i]

        if c == 'F':
            alex.forward(l)

        if c == 'f':
            alex.penup()
            alex.forward(l)
            alex.pendown()

        if c == '+':
            alex.left(d)

        if c == '-':
            alex.right(d)

        if c == '[':
            stack.append((alex.heading(), alex.pos()))

        if c == ']':
            heading, position = stack.pop()
            alex.penup()
            alex.goto(position)
            alex.setheading(heading)
            alex.pendown()

    screen.onkey(screen.bye, 'q')
    screen.listen()
    turtle.mainloop()
    

t.show('text')
draw(sistema, 20, 10)


# In[ ]:





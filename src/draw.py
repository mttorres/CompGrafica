from tkinter import Tk, Canvas, Frame, Button, Label, BOTH
from PIL import Image, ImageTk
import math
import numpy as np
from copy import deepcopy
import os
import pathlib

"""
This file is used to draw figures using the Canvas object (and its methods) from Tkinter
library. It also stores the data structures that represent these figures in vectors and matrixes.

Each figure is composed by at least one face, which in turn is composed by at least
two vertices, and these vertices are coordinates in the (x,y) or (x,y,z) systems (for 2D or 3D,
respectively). The origin (0,0) is located at the top left corner of the screen.
The data structures are as following:

==> Figure: contains the figure's faces.
    E.g.: Line = (f1) ==> l = [f1]

==> Faces: contains the face's vertices.
    E.g.: Face 1: (v1, v2) ==> f1 = [v1,v2]

==> Vertex: contains the vertex's coordinates.
    E.g.: Vertex 1: (2,5) ==> v1 = [2,5]
          Vertex 2: (4,10) ==>  v2 = [4,10]   

"""

# Data Structures
""""
The figures can be separated by amount of vertices into categories.

The simple figures have less than 6 vertices.
The average figures have between 6 and 8 vertices.
The complex have more than 8 vertices.
"""
##Vertices

### Arrow
v1_arrow = [10, 40]
v2_arrow = [30, 40]

v3_arrow = [30, 30]
v4_arrow = [50, 50]
v5_arrow = [30, 70]

v6_arrow = [30, 60]
v7_arrow = [10, 60]

### Triangle
v1_t1 = [100, 20]
v2_t1 = [140, 60]
v3_t1 = [60, 60]

### Cup
v1_cup = [160, 15]
v2_cup = [170, 60]
v3_cup = [195, 60]
v4_cup = [205, 15]

### Box
v1_box = [260, 20]
v2_box = [260, 60]
v3_box = [300, 60]
v4_box = [300, 20]

### Pentagon
v1_pent = [320, 38]
v2_pent = [330, 60]
v3_pent = [360, 60]
v4_pent = [370, 38]
v5_pent = [345, 20]

### Hexagon
v1_hexa = [400, 38]
v2_hexa = [400, 60]
v3_hexa = [425, 75]
v4_hexa = [450, 60]
v5_hexa = [450, 38]
v6_hexa = [425, 20]


### Chair
v1_chair = [30, 100]
v2_chair = [30, 200]
v3_chair = [40, 200]
v4_chair = [40,170]

v5_chair = [80,170]
v6_chair = [80,200]
v7_chair = [90,200]

v8_chair = [90,160]
v9_chair = [40,160]
v10_chair = [40,100] 


### Star
v1_star = [140,115]
v2_star = [150,135]
v3_star = [170,140]
v4_star = [150,150]
v5_star = [160,170]
v6_star = [140,160]
v7_star = [120,170]
v8_star = [130,150]
v9_star = [110,140]
v10_star = [130,135]

### Bottle
v1_bottle = [190, 200]
v2_bottle = [220,200]
v3_bottle = [220,140]
v4_bottle = [210,130]
v5_bottle = [210,120]
v6_bottle = [200,120]
v7_bottle = [200,130]
v8_bottle = [190,140]


### House, minha casa minha vida

v1_house = [410, 38]
v2_house = [410, 60]
v3_house = [440, 60]
v4_house = [440, 38]
v5_house = [425, 20]

## Faces
arrow_f1 = [v1_arrow, v2_arrow, v3_arrow, v4_arrow, v5_arrow, v6_arrow, v7_arrow]
arrow_f2 = [v1_arrow, v7_arrow, v6_arrow, v5_arrow, v4_arrow, v3_arrow, v2_arrow]

box_f1 = [v1_box, v2_box, v3_box, v4_box]
box_f2 = [v1_box, v4_box, v3_box, v2_box]

cup_f1 = [v1_cup, v2_cup, v3_cup, v4_cup]
cup_f2 = [v1_cup, v4_cup, v3_cup, v2_cup]

triangle_f1 = [v1_t1, v2_t1, v3_t1]
triangle_f2 = [v1_t1, v3_t1, v2_t1]

pentagon_f1 = [v1_pent, v2_pent, v3_pent, v4_pent, v5_pent]
pentagon_f2 = [v1_pent, v5_pent, v4_pent, v3_pent, v2_pent]

hexagon_f1 = [v1_hexa, v2_hexa, v3_hexa, v4_hexa, v5_hexa, v6_hexa]
hexagon_f2 = [v1_hexa, v6_hexa, v5_hexa, v4_hexa, v3_hexa, v2_hexa]

house_f1 = [v1_house, v2_house, v3_house, v4_house, v5_house]
house_f2 = [v1_house, v5_house, v4_house, v3_house, v2_house]

chair_f1 = [v1_chair, v2_chair, v3_chair, v4_chair, v5_chair, v6_chair, v7_chair, v8_chair, v9_chair, v10_chair]
chair_f2 = [v1_chair, v10_chair, v9_chair, v8_chair, v7_chair, v6_chair, v5_chair, v4_chair, v3_chair, v2_chair]

star_f1 = [v1_star, v2_star, v3_star, v4_star, v5_star, v6_star, v7_star, v8_star, v9_star, v10_star]
star_f2 = [v1_star, v10_star, v9_star, v8_star, v7_star, v6_star, v5_star, v4_star, v3_star, v2_star]

bottle_f1 = [v1_bottle, v2_bottle, v3_bottle, v4_bottle, v5_bottle, v6_bottle, v7_bottle, v8_bottle]
bottle_f2 = [v1_bottle, v8_bottle, v7_bottle, v6_bottle, v5_bottle, v4_bottle, v3_bottle, v2_bottle]
# Figures

### Arrow
arrow_image = [arrow_f1, arrow_f2]

### Box
box_image = [box_f1, box_f2]

### Cup
cup_image = [cup_f1, cup_f2]

### Triangle
triangle_image = [triangle_f1, triangle_f2]

### Pentagon
pentagon_image = [pentagon_f1, pentagon_f2]

### Hexagon
hexagon_image = [hexagon_f1, hexagon_f2]

### House
house_image = [house_f1, house_f2]

### Chair
chair_image = [chair_f1, chair_f2]

### Star 
star_image = [star_f1, star_f2]

### Bottle
bottle_image = [bottle_f1, bottle_f2]



# Transformations 

## Scale
def scale_2D(image, k):
    position=translateOrigin(image)
    face = image[0]
    for vertex in face:
        matrixScale=np.array([[k[0], 0, 0],
                                [0, k[1], 0],
                                [0, 0, 1]])
        matrixPosition=np.array([vertex[0],vertex[1],1])
        result=np.matmul(matrixScale,matrixPosition)
        vertex[0] = result[0]
        vertex[1] = result[1]
    translate_2D(image,position[0],position[1])
    return image

## Shear
def cisa_2D(image, k):
    position=translateOrigin(image)
    face = image[0]
    for vertex in face:
        matrixScale=np.array([[1, k[0], 0],
                                [k[1], 1, 0],
                                [0, 0, 1]])
        matrixPosition=np.array([vertex[0],vertex[1],1])
        result=np.matmul(matrixScale,matrixPosition)
        vertex[0] = result[0]
        vertex[1] = result[1]
    translate_2D(image,position[0],position[1])
    return image

## Translation
def translate_2D(image, x_amount, y_amount):
    face = image[0]
    for vertex in face:
        matrixTranslate=np.array([[1, 0, x_amount],
                            [0, 1, y_amount],
                            [0, 0, 1]])
        matrixPosition=np.array([vertex[0],vertex[1],1])
        result=np.matmul(matrixTranslate,matrixPosition)
        vertex[0] = result[0]
        vertex[1] = result[1]
    return image

## Translate image midpoint to (0,0)
def translateOrigin(image):
    # Procurando os extremos para calcular o ponto medio
    esquerda = None
    direita = None
    cima = None
    baixo = None
    face = image[0]
    for vertex in face:
        if ((esquerda == None) or (esquerda < vertex[0])):
            esquerda = vertex[0]
        if ((direita == None) or (direita > vertex[0])):
            direita = vertex[0]
        if ((cima == None) or (cima < vertex[1])):
            cima = vertex[1]
        if ((baixo == None) or (baixo > vertex[1])):
            baixo = vertex[1]
    # Calculando o ponto medio em relação  x e y e transladando a imagem para a origem
    medio_x = (direita - esquerda) / 2
    medio_y = (baixo - cima) / 2
    position=[esquerda + medio_x,cima + medio_y]
    image = translate_2D(image, -position[0], -position[1])
    return position

## Rotation
def rotation_2D(image, angle=90):
    radian = angle * (math.pi / 180)
    position=translateOrigin(image)
    # Fazendo a rotação
    face = image[0]
    for vertex in face:
        matrixRotation=np.array([[math.cos(radian), (math.sin(radian))],[-(math.sin(radian)), math.cos(radian)]])
                        
        vetorPosition=np.array([vertex[0],vertex[1]])
        result=np.matmul(matrixRotation,vetorPosition)
        vertex[0] = result[0]
        vertex[1] = result[1]
    # Transladando a imagem pro ponto original
    image = translate_2D(image, position[0], position[1])
    return image


# Inicialização da tela base (root)
root = Tk()
canvas = Canvas(root, width=800, height=600)
root.pages = []
root.current_page = 0
pages = root.pages



# The method 'create_polygon' will decapsulate the structure by itself, no need to iterate through it.
# Removes fill(polygon is filled by default) and draws outline(invisible by default).
# Gets the pages from the root object and draw each page's images.
def next_page():
    next_button = Button(canvas, text="Próxima página", command=next_page)
    next_button.place(x=canvas.winfo_width()*0.40, y=canvas.winfo_height()*0.70)
    if(root.current_page < 0):
        return
    if(root.current_page > len(pages) -1):
        root.current_page = 0
    start_button.destroy()
    canvas.delete('all')
    page_list = pages[root.current_page]
    for image in page_list:
        canvas.create_polygon(image, fill='', outline='black')
    position = midpoint(page_list[-1])
    questiion_mark = canvas.create_text(position[0] + 95, position[1], font=("Times New Roman", 40), text="?")
    root.current_page += 1

# Gets the midpoint of an image
def midpoint(image):
    esquerda = None
    direita = None
    cima = None
    baixo = None
    face = image[0]
    for vertex in face:
        if ((esquerda == None) or (esquerda < vertex[0])):
            esquerda = vertex[0]
        if ((direita == None) or (direita > vertex[0])):
            direita = vertex[0]
        if ((cima == None) or (cima < vertex[1])):
            cima = vertex[1]
        if ((baixo == None) or (baixo > vertex[1])):
            baixo = vertex[1]
    medio_x = (direita - esquerda) / 2
    medio_y = (baixo - cima) / 2
    position=[esquerda + medio_x,cima + medio_y]
    return position

# Creating the question's images

##First question 
arrow_origin = translateOrigin(arrow_image)

arrow1_pos = translate_2D(deepcopy(arrow_image),270,150)
arrow2_pos = translate_2D(deepcopy(arrow1_pos), 100, 0)
arrow3_pos = translate_2D(deepcopy(arrow2_pos), 100, 0)

arrow4_pos = translate_2D(deepcopy(arrow1_pos), 0, 100)
arrow5_pos = translate_2D(deepcopy(arrow2_pos), 0, 100)
arrow6_pos = translate_2D(deepcopy(arrow3_pos), 0, 100)

arrow7_pos = translate_2D(deepcopy(arrow4_pos), 0, 100)
arrow8_pos = translate_2D(deepcopy(arrow5_pos), 0, 100)

arrow2_pos = rotation_2D(arrow2_pos, 90)
arrow3_pos = rotation_2D(arrow3_pos, 180)

arrow4_pos = rotation_2D(arrow4_pos, 90)
arrow6_pos = rotation_2D(arrow6_pos, -90)

arrow7_pos = rotation_2D(arrow7_pos, 180)
arrow8_pos = rotation_2D(arrow8_pos, -90)

page1=[arrow1_pos, arrow2_pos, arrow3_pos, arrow4_pos, arrow5_pos, arrow6_pos, arrow7_pos, arrow8_pos]
pages.append(page1)

## Second question
triangle_position = translateOrigin(triangle_image)

triangle1_pos = translate_2D(deepcopy(triangle_image), 270, 150)
triangle2_pos = translate_2D(deepcopy(triangle1_pos), 100, 0)
triangle3_pos = translate_2D(deepcopy(triangle2_pos), 100, 0)

triangle4_pos = translate_2D(deepcopy(triangle1_pos), 0, 100)
triangle5_pos = translate_2D(deepcopy(triangle2_pos), 0, 100)
triangle6_pos = translate_2D(deepcopy(triangle3_pos), 0, 100)

triangle7_pos = translate_2D(deepcopy(triangle4_pos), 0, 100)
triangle8_pos = translate_2D(deepcopy(triangle5_pos), 0, 100)

triangle2_pos = scale_2D(triangle2_pos, [1,2])
triangle2_pos = translate_2D(triangle2_pos, 0, -20)

triangle3_pos = scale_2D(triangle3_pos, [0.5,0.5])
triangle3_pos = translate_2D(triangle3_pos, -20, 10)

triangle4_pos = scale_2D(triangle4_pos, [1,2])
triangle4_pos = translate_2D(triangle4_pos, 0, -20)

triangle6_pos = scale_2D(triangle6_pos, [0.5,0.5])
triangle6_pos = translate_2D(triangle6_pos, -20, 10)
triangle7_pos = scale_2D(triangle7_pos, [0.5,0.5])
triangle7_pos = translate_2D(triangle7_pos, 5, 10) 

page2 = [triangle1_pos, triangle2_pos, triangle3_pos, triangle4_pos, triangle5_pos, triangle6_pos, triangle7_pos, triangle8_pos]
pages.append(page2)

### Third question

chair_origin = translateOrigin(chair_image)

chair1_pos = translate_2D(deepcopy(chair_image), 320, 160)
chair2_pos = translate_2D(deepcopy(chair1_pos), 100, 0)

chair3_pos = translate_2D(deepcopy(chair1_pos), 0, 120)

chair1_pos = scale_2D(chair1_pos, [-1, 1])
chair3_pos = scale_2D(chair3_pos, [-1, -1])
page3 = [chair1_pos, chair2_pos, chair3_pos]
pages.append(page3)


##fourth question
box_origin_1 = translateOrigin(box_image)

box1_pos = translate_2D(deepcopy(box_image),270,150)

box2_pos = translate_2D(deepcopy(box1_pos), 80, 0)
box3_pos = translate_2D(deepcopy(box2_pos), 40, 0)


box4_pos = translate_2D(deepcopy(box3_pos), 80, 0)
box5_pos = translate_2D(deepcopy(box4_pos), 40, 0)
box6_pos = translate_2D(deepcopy(box5_pos), 40, 0)


box7_pos = translate_2D(deepcopy(box1_pos), 0, 100)
box8_pos = translate_2D(deepcopy(box7_pos), 40, 0)
box9_pos = translate_2D(deepcopy(box8_pos), 40, 0)
box10_pos = translate_2D(deepcopy(box9_pos), 40, 0)

box11_pos = translate_2D(deepcopy(box10_pos), 80, 0)
box12_pos = translate_2D(deepcopy(box11_pos), 40, 0)
box13_pos = translate_2D(deepcopy(box12_pos), 40, 0)
box14_pos = translate_2D(deepcopy(box13_pos), 40, 0)
box15_pos = translate_2D(deepcopy(box14_pos), 40, 0)


box16_pos = translate_2D(deepcopy(box1_pos), 0, 200)
box17_pos = translate_2D(deepcopy(box16_pos), 40, 0)
box18_pos = translate_2D(deepcopy(box17_pos), 40, 0)
box19_pos = translate_2D(deepcopy(box18_pos), 40, 0)
box20_pos = translate_2D(deepcopy(box19_pos), 40, 0)
box21_pos = translate_2D(deepcopy(box20_pos), 40, 0)


page4=[box1_pos, box2_pos, box3_pos,box4_pos,box5_pos,box6_pos,box7_pos,box8_pos,box9_pos,box10_pos,box11_pos,box12_pos,box13_pos,box14_pos,box15_pos
,box16_pos,box17_pos,box18_pos,box19_pos,box20_pos,box21_pos]
pages.append(page4)

#fifth question
penta_origin = translateOrigin(pentagon_image)
penta1_pos = translate_2D(deepcopy(pentagon_image),270,150)

penta2_pos = translate_2D(deepcopy(penta1_pos),120,0)
penta2_pos = rotation_2D(penta2_pos, 90)
penta2_pos = scale_2D(penta2_pos,[0.75,0.75])

penta3_pos = translate_2D(deepcopy(penta1_pos),240,0)
penta3_pos = rotation_2D(penta3_pos, 180)
penta3_pos = scale_2D(penta3_pos,[0.50,0.50])


penta4_pos = translate_2D(deepcopy(penta1_pos),0,100)
penta4_pos = rotation_2D(penta4_pos, 270)
penta4_pos = scale_2D(penta4_pos,[0.25,0.25])

penta5_pos = translate_2D(deepcopy(penta1_pos),120,100)
penta5_pos = rotation_2D(penta5_pos,360)
penta5_pos = scale_2D(penta5_pos,[1.25,1.25])

page5 = [penta1_pos,penta2_pos,penta3_pos,penta4_pos,penta5_pos]
pages.append(page5)

## Sixth question

cup_origin = translateOrigin(cup_image)
star_origin = translateOrigin(star_image)
box_origin = translateOrigin(box_image)

cup1_pos = translate_2D(deepcopy(cup_image), 270, 150)
cup1_mid = midpoint(cup1_pos)
star1_pos = translate_2D(deepcopy(star_image), cup1_mid[0], cup1_mid[1])
star1_pos = scale_2D(star1_pos, [0.5, 0.5])

box19_pos = translate_2D(deepcopy(box_image), 370, 150)
box19_mid = midpoint(box19_pos)
arrow9_pos = translate_2D(deepcopy(arrow_image),box19_mid[0], box19_mid[1])
arrow9_pos = scale_2D(arrow9_pos, [0.5,0.5])
arrow9_pos = rotation_2D(arrow9_pos, 90)

cup2_pos = translate_2D(deepcopy(cup1_pos), 200, -50)
cup2_mid = midpoint(cup2_pos)
star2_pos = translate_2D(deepcopy(star_image), cup2_mid[0], cup2_mid[1])
cup2_pos = scale_2D(cup2_pos, [1.5, 1.5])
star2_pos = scale_2D(star2_pos, [0.75,0.75])

cup3_pos = translate_2D(deepcopy(cup1_pos), 0, 100)
star3_pos = translate_2D(deepcopy(star1_pos), 0, 100)

arrow10_pos = translate_2D(deepcopy(arrow9_pos), 0, 100)

cup4_pos = translate_2D(deepcopy(cup3_pos), 200, -50)
cup4_mid = midpoint(cup4_pos)
star4_pos = translate_2D(deepcopy(star_image), cup4_mid[0], cup4_mid[1])
star4_pos = scale_2D(star4_pos, [0.5,0.5])

cup5_pos = translate_2D(deepcopy(cup3_pos),0,100)
cup5_mid = midpoint(cup5_pos)
star5_pos = translate_2D(deepcopy(star_image), cup5_mid[0], cup5_mid[1])
star5_pos = scale_2D(star5_pos, [0.5,0.5])

box20_pos = translate_2D(deepcopy(box19_pos), 0, 200)
box20_mid = midpoint(box20_pos)
arrow11_pos = translate_2D(deepcopy(arrow_image), box20_mid[0], box20_mid[1])
arrow11_pos = scale_2D(arrow11_pos, [0.5,0.5])
arrow11_pos = rotation_2D(arrow11_pos, -90)

page6 = [cup1_pos, star1_pos, box19_pos, arrow9_pos, cup2_pos, star2_pos, cup3_pos, star3_pos, arrow10_pos,
        cup4_pos, star4_pos, cup5_pos, star5_pos, box20_pos, arrow11_pos]
pages.append(page6)

## Seventh question

hexagon_origin = translateOrigin(hexagon_image)
bottle_origin = translateOrigin(bottle_image)
pentagon_origin = translateOrigin(pentagon_image)

hex1_pos = translate_2D(deepcopy(hexagon_image), 270, 150)
box21_pos = translate_2D(deepcopy(box_image), 370, 150)
star6_pos = translate_2D(deepcopy(star_image), 470, 150 )

pent1_pos = translate_2D(deepcopy(pentagon_image), 270, 250)
triangle9_pos = translate_2D(deepcopy(triangle_image), 370, 250)
bottle1_pos = translate_2D(deepcopy(bottle_image), 470, 250)

pent2_pos = translate_2D(deepcopy(pent1_pos), 0, 100)
triangle10_pos = translate_2D(deepcopy(triangle9_pos), 0, 100)

hex1_pos = cisa_2D(hex1_pos, [-0.225, 0])
box21_pos = cisa_2D(box21_pos, [-0.225, 0])
star6_pos = scale_2D(star6_pos, [1.5, 1.5])

pent1_pos = cisa_2D(pent1_pos, [-0.225, 0])
triangle9_pos = cisa_2D(triangle9_pos, [-0.225, 0])
bottle1_pos = scale_2D(bottle1_pos, [1.5, 1.5])

pent2_pos = cisa_2D(pent2_pos, [0.225, 0])
triangle10_pos = cisa_2D(triangle10_pos, [0.225, 0])

page7 = [hex1_pos, box21_pos, star6_pos, pent1_pos, triangle9_pos, bottle1_pos, pent2_pos, triangle10_pos]
pages.append(page7)



# eighth question
house_origin = translateOrigin(house_image)
star_origin = translateOrigin(star_image)

house1_pos = translate_2D(deepcopy(house_image),240,150)
star_pos1 = translate_2D(deepcopy(star_image),230,165)
starzinha1 = scale_2D(star_pos1,[0.15,0.15])

house2_pos = translate_2D(deepcopy(house1_pos),100,0)
starzinha2 = translate_2D(deepcopy(starzinha1),100,-20)

house3_pos = scale_2D(translate_2D(deepcopy(house1_pos),200,0),[1,-1])
starzinha3 = translate_2D(deepcopy(starzinha1),200,-10)

house4_pos = translate_2D(deepcopy(house3_pos),100,0)
starzinha4 = translate_2D(deepcopy(starzinha3),100,-20)

page8 = [house1_pos,starzinha1,starzinha2,house2_pos,starzinha3,house3_pos,starzinha4,house4_pos]
pages.append(page8)


## Ninth question
triangle11_pos = translate_2D(deepcopy(triangle_image), 270, 150)
box22_pos = translate_2D(deepcopy(box_image), 370, 150)
pent3_pos = translate_2D(deepcopy(pentagon_image), 460, 150)

page10 = [triangle11_pos, box22_pos, pent3_pos]
pages.append(page10)


#x question

box_origin = translateOrigin(deepcopy(box_image))

box1_pos = translate_2D(deepcopy(box_image),270,150)

box2_pos = translate_2D(deepcopy(box1_pos),80,0)
disto2_pos = cisa_2D(deepcopy(box2_pos), [1, 0])
box3_pos = translate_2D(deepcopy(box2_pos),100,0)
disto3_pos = cisa_2D(deepcopy(box3_pos), [2, 0])


box4_pos = translate_2D(deepcopy(box1_pos),0,100)

box5_pos = translate_2D(deepcopy(box4_pos),100,0)
disto5_pos = cisa_2D(deepcopy(box5_pos), [0, 1])
box6_pos = translate_2D(deepcopy(box5_pos),100,0)
disto6_pos = cisa_2D(deepcopy(box6_pos), [0, 2])


box7_pos = translate_2D(deepcopy(box4_pos),0,100)
box8_pos = translate_2D(deepcopy(box7_pos),100,0)
disto8_pos = cisa_2D(deepcopy(box8_pos), [1, 1])

pageX = [box1_pos,box2_pos,disto2_pos,box3_pos,disto3_pos,box4_pos,box5_pos,disto5_pos,box6_pos,disto6_pos,box7_pos,box8_pos,disto8_pos]
pages.append(pageX)

canvas.pack()
root.update()

start_button = Button(canvas, text="Começar o jogo!", command=next_page)
start_button.place(x=canvas.winfo_width()*0.40, y=canvas.winfo_height()*0.70)
""" file_path = "Trabalho 1\src\\velosem_logo.png"
img = ImageTk.PhotoImage(Image.open(file_path))
canvas.create_image """
root.mainloop()





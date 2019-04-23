from tkinter import Tk, Canvas, Frame, Button, BOTH
import math
import numpy as np
from copy import deepcopy

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
box_f1 = [v1_box, v2_box, v3_box, v4_box]
cup_f1 = [v1_cup, v2_cup, v3_cup, v4_cup]
triangle_f1 = [v1_t1, v2_t1, v3_t1]
pentagon_f1 = [v1_pent, v2_pent, v3_pent, v4_pent, v5_pent]
hexagon_f1 = [v1_hexa, v2_hexa, v3_hexa, v4_hexa, v5_hexa, v6_hexa]
house_f1 = [v1_house, v2_house, v3_house, v4_house, v1_house, v5_house, v4_house]
chair_f1 = [v1_chair, v2_chair, v3_chair, v4_chair, v5_chair, v6_chair, v7_chair, v8_chair, v9_chair, v10_chair]
star_f1 = [v1_star, v2_star, v3_star, v4_star, v5_star, v6_star, v7_star, v8_star, v9_star, v10_star]
bottle_f1 = [v1_bottle, v2_bottle, v3_bottle, v4_bottle, v5_bottle, v6_bottle, v7_bottle, v8_bottle]
# Figures

### Arrow
arrow_image = [arrow_f1]

### Box
box_image = [box_f1]

### Cup
cup_image = [cup_f1]

### Triangle
triangle_image = [triangle_f1]

### Pentagon
pentagon_image = [pentagon_f1]

### Hexagon
hexagon_image = [hexagon_f1]

### House
house_image = [house_f1]

### Chair
chair_image = [chair_f1]

### Star 
star_image = [star_f1]

### Bottle
bottle_image = [bottle_f1]
def scale_2D(image, k):
    position=translateOrigin(image)
    for face in image:
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

def cisa_2D(image, k):
    position=translateOrigin(image)
    for face in image:
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

def translate_2D(image, x_amount, y_amount):
    for face in image:
        for vertex in face:
            matrixTranslate=np.array([[1, 0, x_amount],
                             [0, 1, y_amount],
                             [0, 0, 1]])
            matrixPosition=np.array([vertex[0],vertex[1],1])
            result=np.matmul(matrixTranslate,matrixPosition)
            vertex[0] = result[0]
            vertex[1] = result[1]
    return image


def translateOrigin(image):
    # Procurando os extremos para calcular o ponto medio
    esquerda = None
    direita = None
    cima = None
    baixo = None
    for face in image:
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


def rotation_2D(image, angle=90):
    radian = angle * (math.pi / 180)
    position=translateOrigin(image)
    # Fazendo a rotação
    for face in image:
        for vertex in face:
            matrixRotation=np.array([[math.cos(radian), math.sin(radian), 0],
                            [math.sin(radian), math.cos(radian), 0],
                            [0, 0, 1]])
            vetorPosition=np.array([vertex[0],vertex[1],1])
            result=np.matmul(matrixRotation,vetorPosition)
            vertex[0] = result[0]
            vertex[1] = result[1]
    # Transladando a imagem pro ponto original
    image = translate_2D(image, position[0], position[1])
    return image




# inicialização da tela base (root)
root = Tk()
canvas = Canvas(root, width=800, height=600)
root.pages = []
pages = root.pages
root.current_page = 0


# The method 'create_polygon' will decapsulate the structure by itself, no need to iterate through it.
# Removes fill(polygon is filled by default) and draws outline(invisible by default).
# Gets the pages from the root object and draw each page's images.
def next_page():
    if(root.current_page > len(pages) -1):
        root.current_page = 0
    canvas.delete('all')
    for image in pages[root.current_page]:
        canvas.create_polygon(image, fill='', outline='black')
    root.current_page += 1

page1=[arrow_image, box_image, cup_image, chair_image, star_image, bottle_image]
page2=[triangle_image, pentagon_image,hexagon_image]
pages.append(page1)
pages.append(page2)

""" arrow = canvas.create_polygon(arrow_image, fill='', outline='black')
box = canvas.create_polygon(box_image, fill='', outline='black')
cup = canvas.create_polygon(cup_image, fill='', outline='black')
triangle = canvas.create_polygon(triangle_image, fill='', outline='black')
pentagon = canvas.create_polygon(pentagon_image, fill='', outline='black')
hexagon = canvas.create_polygon(hexagon_image, fill='', outline='black')
house = canvas.create_polygon(house_image, fill='', outline='black') """
# Translates the pentagon 100 px down
#new_pentagon_image = translate_2D(pentagon_image, 0, 100)
# print(new_pentagon_image)

# Rotate the pentagon
#new_pentagon_image = rotation_2D(new_pentagon_image, 90)
#  print(new_pentagon_image)
#novopenta = canvas.create_polygon(new_pentagon_image)

# desenhando a casa sem ter que fazer a soma "manualmente" ou seja testando a transalate_2D
#criar_casa = translate_2D(house_image, 80, 0)

""" minhacasa = canvas.create_polygon(criar_casa, fill='', outline='blue')

# Draw a bigger box
copia = deepcopy(box_image)


blue_box = translate_2D(box_image, 0, 100)
canvas.create_polygon(blue_box, fill='', outline='blue')
big_box = scale_2D(blue_box, [2, 2])
inverpenta = scale_2D(new_pentagon_image, [1, -1])
#big_box = cisa_2D(blue_box, [1, 0])
canvas.create_polygon(inverpenta, fill='', outline='blue')
canvas.create_polygon(big_box, fill='', outline='blue')
 """
canvas.pack()

clear_button = Button(canvas, text="Próxima página", command=next_page)
clear_button.place(x=0, y=0)
root.mainloop()




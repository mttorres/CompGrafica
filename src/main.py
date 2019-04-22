from tkinter import *
import math
from src.draw import *


##### estou pensando em separar cada uma dessas partes abaixo em modulos .py


######### paginas ##################

# estou pensando em criar um dicionario com 10 chaves que contem as configuracoes de cada pagina....


#######################################


########funcoes auxiliares##############
def genericcreator(vi, i, nvertices):
    vr = [0] * 2
    if (nvertices == 3):
        vr = generictrianglecreator(vi, i)
    if (nvertices == 4):
        vr = genericboxcreator(vi, i)
    return vr


def generictrianglecreator(vi, i):
    # vertice resposta
    vr = [0] * 2
    # para cada indice de vertice ele cria os vertices na proporcao de um quadrilatero
    if (i == 0):
        vr = vi
    if (i > 0):
        vr[1] = vi[1] + 40
        if (i == 1):
            vr[0] = vi[0] - 40
        else:
            vr[0] = vi[0] + 40

    return vr


def genericboxcreator(vi, i):
    # vertice resposta
    vr = [0] * 2
    # para cada indice de vertice ele cria os vertices na proporcao de um quadrilatero
    if (i == 0):
        vr = vi

    if (i == 1):
        vr[0] = vi[0]
        vr[1] = vi[1] + 40
    if (i > 1):
        vr[0] = vi[0] + 200
        if (i == 3):
            vr[1] = vi[1]
        else:
            vr[1] = vi[1] + 40

    return vr  # sempre retorna o vertice , se i for igual a zero nao fazer alteração nenhuma


def polygonimagecreator(nvertices, data):
    image_f1 = [0] * nvertices
    vi = data
    for i in range(0, nvertices):
        image_f1[i] = genericcreator(vi, i, nvertices)
    image = [image_f1]
    return image


def drawoptions(canvas, v, lados, preenc, contor, corretas, quase, respostas, rot=False, trans=False):
    options = Canvas(canvas, width=800, height=300, bg="RED")
    offsetx = 270
    offsety = 80
    data = [0, 0]
    for i in range(1, 7):
        j = i - 1

        b = Radiobutton(options, bg="#ffffcc", text=i, variable=v, value=i)
        b.pack(fill=BOTH)
        # divide entre esses botoes 1 e 2    ,  3 e 4 ,   5 e 6
        proporcaox = i // 3  # pode ser  1  ,  2   ,  3

        paridade = i % 2
        proporcaoy = 1
        if (paridade == 0):
            proporcaoy = 2
        else:
            proporcaoy = 0

        if (i != 5):
            b.place(x=offsetx * proporcaox, y=offsety * proporcaoy)
            data[0] = offsetx * proporcaox + 50
        else:
            b.place(x=offsetx * (proporcaox + 1), y=offsety * proporcaoy)
            data[0] = offsetx * (proporcaox + 1) + 50

        data[1] = offsety * proporcaoy + 10

        # desenha uma imagem em cada botao seguindo as propriedades do vetor de cada imagem

        image = polygonimagecreator(lados[j], data)
        if (preenc[j] == ""):
            options.create_polygon(image, fill=preenc[j], outline=contor[j])
        else:
            options.create_polygon(image, fill=preenc[j], outline=contor[j])

    options.pack()
    options.place(x=0, y=300)


def drawquestions(canvas, v, lados, preenc, contor, rot=False, trans=False):
    board = Canvas(canvas, width=800, height=300, bg="BLUE")
    offsetx = 270
    offsety = 80
    data = [0, 0]
    for i in range(1, 7):
        j = i - 1

        # OBS: vou mudar ainda como essa funcao se comporta, por enquanto ela ta uma copia similar da drawoptions somente para testes

        # divide entre esses botoes 1 e 2    ,  3 e 4 ,   5 e 6
        proporcaox = i // 3  # pode ser  1  ,  2   ,  3

        paridade = i % 2
        proporcaoy = 1
        if (paridade == 0):
            proporcaoy = 2
        else:
            proporcaoy = 0

        if (i != 5):

            data[0] = offsetx * proporcaox + 50
        else:

            data[0] = offsetx * (proporcaox + 1) + 50

        data[1] = offsety * proporcaoy + 10

        # desenha uma imagem em cada botao seguindo as propriedades do vetor de cada imagem

        image = polygonimagecreator(lados[j], data)
        if (preenc[j] == ""):
            board.create_polygon(image, fill=preenc[j], outline=contor[j])
        else:
            board.create_polygon(image, fill=preenc[j], outline=contor[j])

    board.pack()
    board.place(x=0, y=0)


# For mouse event debugging
def callback(event):
    print("Clicked at", event.x, event.y)


def quit_loop(v, root):
    print("Selection:", v.get())
    global selection
    selection = v.get()


# root.destroy()
########################################
def main():
    root = Tk()
    canvas = Canvas(root, width=800, height=600, bg="Blue")
    canvas.bind("<Button-1>", callback)

    v = IntVar()
    v.set(1)

    corretas = [5] * 10
    quase = [4] * 10
    respostas = []

    ladospergunta = [4, 4, 4, 4, 4, 4]
    ladosopcoes = [4, 3, 4, 3, 4, 3]
    pagina = [ladospergunta, ladosopcoes]

    contor = ["blue", "blue", "blue", "blue", "blue", "blue"]
    cores = []

    ppergunta = ["black", "black", "black", "black", "black", ""]
    presposta = ["black", "black", "black", "black", "black", ""]
    p = [ppergunta, presposta]

    contorpergunta = ["red", "red", "red", "red", "red", "red"]
    contorresposta = ["blue", "blue", "blue", "blue", "blue", "blue"]
    cores = []

    drawoptions(canvas, v, ladosopcoes, presposta, contorresposta, corretas, quase, respostas)
    drawquestions(canvas, v, ladospergunta, presposta, contorpergunta)
    canvas.pack()

    # termina de desenhar a tela
    bnext = Button(root, text="PROXIMA", command=quit_loop(v, root))
    bnext.place(x=380, y=575)
    canvas.pack()
    # bnext.pack()
    mainloop()


if __name__ == '__main__':
    main()

from tkinter import *


#####transformacoes######
def translate_2D(image, x_amount, y_amount):
    new_image = image
    for face in new_image:
        for vertex in face:
            vertex[0] += x_amount
            vertex[1] += y_amount
    return new_image


########################
# inicialização da tela base (root)
master = Tk()
canvas = Canvas(master, width=800, height=600, bg="Blue")
# valor da opção atual escolhida
v = IntVar()
# vetor de respostas corretas
corretas = [5] * 10  # nesse caso teste a opcao 5 é a correta em todos os casos
quase = [4] * 10  # nesse caso a opcao 5 é a quase correta em todos os casos
respostas = []


# facilita nao ter que desenhar manualmente cada uma das figuras repetidas

def genericcreator(vi, i, nvertices):
    vr = [0] * 2
    if (nvertices == 3):
        vr = generictrianglecreator(vi, i)
    if (nvertices == 4):
        vr = genericboxcreator(vi, i)

    return vr


''' #tentativa de criar uma funcao generica o bastante para criar qualquer figura
def genericcreator(vi,i):
	#vertice resposta
	vr = [0]*2
	# para cada indice de vertice ele cria os vertices na proporcao de um quadrilatero
	if(i == 0):
		vr = vi
	
	offsetx = 0
	offsety = 0

	if(nvertices == 3):
		offsetx = 120
	if(nvertices == 4):
		offsetx = 200
		offsety = 40

	if(i == 1):
		vr[0] = vi[0]
		vr[1] = vi[1] + offsety
	if(i > 1):
		vr[0] = vi[0] + offsetx
		if(i == 3):  
			vr[1] = vi[1]
		else:
			vr[1] = vi[1] + offsety

	return vr # sempre retorna o vertice , se i for igual a zero nao fazer alteração nenhuma
'''


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


###########
def drawoptions(canvas, v, lados, preenc, contor, corretas, quase, respostas, rot=False, trans=False):
    options = Canvas(canvas, width=800, height=300, bg="RED")
    offsetx = 280
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


# vetor de lados , diz ao drawoptions o que ele deve desenhar das 6 figuras possiveis
lados = [4, 3, 4, 3, 4, 3]
contor = ["blue", "blue", "blue", "blue", "blue", "blue"]
presposta = ["black", "black", "black", "black", "black", ""]

drawoptions(canvas, v, lados, presposta, contor, corretas, quase, respostas)
canvas.pack()

mainloop()

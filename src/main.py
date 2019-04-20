from tkinter import *

##### estou pensando em separar cada uma dessas partes abaixo em modulos .py


###### transformacoes ########################
def translate_2D(image, x_amount, y_amount):
    new_image = image
    for face in new_image:
        for vertex in face:
            vertex[0] += x_amount
            vertex[1] += y_amount
    return new_image

def scale_2D(image,k):
    new_image = image
    print(new_image)
    for face in new_image:
        for vertex in face:
            #xtemp = vertex[0] 
            #ytemp = vertex[1]
            vertex[0] = vertex[0] * k[0]
            vertex[1] = vertex[1] * k[1]
    return new_image

def rotation_2D(image, angle=90):
    radian = angle*(math.pi/180)
    new_image = image
    #Procurando os extremos para calcular o ponto medio
    esquerda = None
    direita = None
    cima = None
    baixo = None
    for face in new_image:
        for vertex in face:
            if ((esquerda == None) or (esquerda < vertex[0])) :
                esquerda=vertex[0]
            if ((direita == None) or (direita > vertex[0])):
                direita=vertex[0]
            if ((cima == None) or (cima < vertex[1])):
                cima=vertex[1]
            if ((baixo == None) or (baixo > vertex[1])):
                baixo=vertex[1]
    #Calculando o ponto medio em relação  x e y e transladando a imagem para a origem
    medio_x = (direita-esquerda)/2
    medio_y = (baixo-cima)/2
    new_image = translate_2D(new_image, -(esquerda+medio_x), -(cima+medio_y))
    #Fazendo a rotação
    for face in new_image:
        for vertex in face:
            x = vertex[0]
            y = vertex[1]
            vertex[0] = x*math.cos(radian) - y*math.sin(radian)
            vertex[1] = x*math.sin(radian) + y*math.cos(radian)
    #Transladando a imagem pro ponto original
    new_image = translate_2D(new_image, (esquerda+medio_x), (cima+medio_y))
    return new_image


######### paginas ##################

#estou pensando em criar um dicionario com 10 chaves que contem as configuracoes de cada pagina....





#######################################



########funcoes auxiliares##############
def genericcreator(vi,i,nvertices):
	vr = [0]*2
	if(nvertices == 3):
		vr = generictrianglecreator(vi,i)
	if(nvertices == 4):
		vr = genericboxcreator(vi,i)		

	return vr



def generictrianglecreator(vi,i):
	#vertice resposta
	vr = [0]*2
	# para cada indice de vertice ele cria os vertices na proporcao de um quadrilatero
	if(i == 0):
		vr = vi
	if(i > 0):
		vr[1] = vi[1] + 40
		if(i == 1):
			vr[0] = vi[0] - 40
		else:
			vr[0] = vi[0] + 40

	return vr

def genericboxcreator(vi,i):
	#vertice resposta
	vr = [0]*2
	# para cada indice de vertice ele cria os vertices na proporcao de um quadrilatero
	if(i == 0):
		vr = vi
	
	if(i == 1):
		vr[0] = vi[0]
		vr[1] = vi[1] + 40
	if(i > 1):
		vr[0] = vi[0] + 200
		if(i == 3):  
			vr[1] = vi[1]
		else:
			vr[1] = vi[1] + 40 

	return vr # sempre retorna o vertice , se i for igual a zero nao fazer alteração nenhuma

def polygonimagecreator(nvertices,data):
	image_f1 = [0]*nvertices
	vi = data
	for i in range(0,nvertices):
		image_f1[i] = genericcreator(vi,i,nvertices)
	image = [image_f1]
	return image

def drawoptions(canvas,v,lados,preenc,contor,corretas,quase,respostas,rot= False,trans = False):
	options = Canvas(canvas, width=800, height=300,bg="RED")
	offsetx = 280
	offsety = 80
	data = [0,0]
	for i in range(1,7):
		j = i-1

		b = Radiobutton(options,bg="#ffffcc",text=i, variable=v, value=i)
		b.pack(fill=BOTH) 
		# divide entre esses botoes 1 e 2    ,  3 e 4 ,   5 e 6 
		proporcaox = i // 3 # pode ser  1  ,  2   ,  3 
		
		paridade = i % 2
		proporcaoy = 1
		if(paridade == 0):
			proporcaoy = 2
		else:
			proporcaoy = 0

		if(i != 5):
			b.place(x = offsetx*proporcaox, y = offsety*proporcaoy)
			data[0] = offsetx*proporcaox + 50
		else:
			b.place(x = offsetx*(proporcaox+1), y = offsety*proporcaoy)
			data[0] = offsetx*(proporcaox+1) + 50
		
		data[1] = offsety*proporcaoy + 10

		#desenha uma imagem em cada botao seguindo as propriedades do vetor de cada imagem

		image = polygonimagecreator(lados[j],data)
		if(preenc[j] == ""):
			options.create_polygon(image,fill=preenc[j], outline = contor[j])
		else:
			options.create_polygon(image,fill=preenc[j], outline = contor[j])


	options.pack()
	options.place(x= 0, y = 300)



#For mouse event debugging
def callback(event):
    print("Clicked at", event.x, event.y)
########################################
def main():
	root = Tk()
	canvas= Canvas(root , width=800, height= 600,bg="Blue")
	canvas.bind("<Button-1>", callback)

	v = IntVar()
	corretas = [5]*10
	quase = [4]*10 
	respostas = []

	ladospergunta = [4,3,4,3,4,3]
	ladosopcoes = [4,3,4,3,4,3]
	pagina = [ladospergunta,ladosopcoes]

	contor = ["blue","blue","blue","blue","blue","blue"]
	cores = []

	ppergunta = ["black","black","black","black","black",""]
	presposta = ["black","black","black","black","black",""]
	p = [ppergunta,presposta]

    
	drawoptions(canvas,v,ladosopcoes,presposta,contor,corretas,quase,respostas)
	canvas.pack()


	#termina de desenhar a tela
	canvas.pack()
	mainloop()



if __name__ == '__main__':
    main() 
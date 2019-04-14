from tkinter import *

master = Tk()
v = IntVar()
canvas= Canvas(master, width=800, height= 600,bg="Blue")

######### image config
v1_box = [0,20]
v2_box = [0,60]
v3_box = [200,60]
v4_box = [200,20]
box_f1 = [v1_box,v2_box,v3_box,v4_box]
box_image = [box_f1]

def genericboxcreator(vi,i):
	vr = [0]*2
	
	if(i == 0):
		vr = vi
	'''
	if(i == 1):
		vr[0] = vi[0]
		vr[1] = vi[1]*(i+1) # só alterar a coordenada y
	if(i > 1):
		vr[0] = vi[0]*2 # alterar de forma igual a coordenada x para cada um deles
		if(i == 3):
			vr[1] = vi[1]
		else:
			vr[1] = vi[1]*2	
	'''
	if(i == 1):
		vr[0] = vi[0]
		vr[1] = vi[1] + 40
	if(i > 1):
		vr[0] = vi[0] + 200
		if(i == 3):  
			vr[1] = vi[1]
		else:
			vr[1] = vi[1] + 40 

	return vr # sempre retorna o cara , se i for igual a zero nao fazer alteração nenhuma

def polygonimagecreator(nvertices,data):
	image_f1 = [0]*nvertices
	vi = data
	for i in range(0,nvertices):
		image_f1[i] = genericboxcreator(vi,i)
	

	image = [image_f1]
	return image
###########
def drawoptions(canvas,v,lados):
	options = Canvas(canvas, width=800, height=300)
	offsetx = 280
	offsety = 80
	data = [0,0]
	for i in range(1,7):
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

		print(data)
		print()
		image = polygonimagecreator(lados[i-1],data)
		print(image)
		print()
		new = options.create_polygon(image)

	options.pack(fill=BOTH)
	options.place(x= 0, y = 300)


lados = [4]*6
drawoptions(canvas,v,lados)
canvas.pack(fill=BOTH)



mainloop()



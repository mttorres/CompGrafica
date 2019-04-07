from tkinter import Tk, Canvas, Frame, BOTH
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

##Vertices
v1 = [20,50]
v2 = [40,100]
v3 = [160,100]
v4 = [140,50]

##Faces
f1 = [v1,v2,v3,v4]
f2 = None

#Figures

### Parallelogram
p1 = [f1,f2]


class Drawing(Frame):
  
    def __init__(self):
        super().__init__()   
        self.initUI()
        
        
    def initUI(self):
      
        self.master.title("Lines")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

#For mouse event debugging
def callback(event):
    print("Clicked at", event.x, event.y)
    
def main():

    root = Tk()
    canvas= Canvas(root, width=800, height=600)
    canvas.bind("<Button-1>", callback)
    
    #Removes fill and draws outline.
    #The method itself will decapsulate the structure.
    parallelogram = canvas.create_polygon(p1, fill='', outline ='black')

    canvas.pack()    
    root.mainloop()  


if __name__ == '__main__':
    main()  
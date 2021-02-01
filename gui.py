from tkinter import Scale, Tk, Frame, Label, Button ,IntVar,PhotoImage,Canvas
from tkinter.ttk import Notebook, Entry
import PIL 
from PIL import ImageTk, Image,ImageSequence
from main import Graph


'''
_BACKGROUNDCOLOR = "#c3fdff"
_BACKGROUNDCOLOR_VARIANT = '#5adbee'
'''
_BACKGROUNDCOLOR = "#E5DEF1"
_BACKGROUNDCOLOR_VARIANT = "#898590"

window = Tk()
window.title("Graph articulation points")
window.geometry("1280x1000")
window["bg"] = _BACKGROUNDCOLOR
window.resizable(False, False)

title = Label(window ,text="Graph articulation points")
title.config(font=('Arial' , 27))
title["bg"] = _BACKGROUNDCOLOR
title.pack(padx = 20, pady = 20)


right_side_container = Frame(window)

class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = Canvas(parent, width=669, height=639)
        self.canvas.pack(side='top',padx = 20, pady = 20)
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'dfsanimation.gif'))]
        self.image = self.canvas.create_image(350,350, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))


gif = App(right_side_container)

dfs_title = Label(right_side_container ,text="DFS Animation")
dfs_title.config(font=('Arial' , 15))
dfs_title["bg"] = _BACKGROUNDCOLOR
dfs_title.pack(side='bottom', padx = 20, pady = 20)

right_side_container.pack(side='right')




left_side_container = Frame(window)


nodes = Frame(left_side_container)

nombre_nodes_label = Label(nodes, text='Nombre de noeuds : ').pack(side="left")
nombre_nodes_entry = Entry(nodes)
nombre_nodes_entry.pack(side="right",padx=5 , pady = 5)

nodes.pack()

arc = Frame(left_side_container)

nombre_arc_label = Label(arc, text="Nombre d'arc : ").pack(side="left")
nombre_arc_entry = Entry(arc)
nombre_arc_entry.pack(side="right",padx=5 , pady = 5)
arc.pack()





left_side_container.pack(side='left')

def get_values():
    wt = list()
    val = list()
    n = int(nombre_arc_entry.get())
    for i in range(1,n+1):
        wt.append(int(tab1.grid_slaves(i, 1)[0].get()))
        val.append(int(tab1.grid_slaves(i, 2)[0].get()))
    print(wt,val)    

    initial_graph = Graph(int(nombre_nodes_entry.get()))

    for i in range(n):
        initial_graph.addEdge(wt[i],val[i])
    
    initial_graph.PrintGraph()



def reset_table():
    for widget in frame2.winfo_children():
       widget.destroy()
    frame2.pack_forget()
    
def print_table():
    global tab1
    n = int(nombre_arc_entry.get())
    global frame2
    frame2 = Frame(left_side_container)
    frame2['bg'] = _BACKGROUNDCOLOR
    frame2.pack(fill="both")
    tablayout = Notebook(frame2)
    tab1 = Frame(tablayout)
    tab1['bg'] = _BACKGROUNDCOLOR
    tab1.pack(fill="both")

    for row in range(n+1):
        for column in range(3):
            if row == 0 :
                if column == 1:
                    label = Label(tab1, text="Nœud A ")
                    label.config(font=('Arial', 14))
                    label['bg']=_BACKGROUNDCOLOR_VARIANT
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    tab1.grid_columnconfigure(column, weight=1)
                if column == 2:
                    label = Label(tab1, text="Nœud B ")
                    label.config(font=('Arial', 14))
                    label['bg']=_BACKGROUNDCOLOR_VARIANT
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    tab1.grid_columnconfigure(column, weight=1)
            
            else:
                if column == 0:
                    label = Label(tab1, text="Transition : " + str(row))
                    label.config(font=('Arial', 14))
                    label['bg']=_BACKGROUNDCOLOR_VARIANT
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    tab1.grid_columnconfigure(column, weight=1)
                else:
                    label = Entry(tab1, text="Row : " + str(row) + " , Column : " + str(column))
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    tab1.grid_columnconfigure(column, weight=1)


    tablayout.pack(fill="both")
    calc = Button(frame2, text="Générer le Graph", command =get_values)
    calc.pack(padx = 20, pady = 20)

    reset = Button(frame2, text = "Reset" , command = reset_table)
    reset.pack(padx = 5, pady = 5)
    return tab1


button = Button(left_side_container, text="Ajouter les transitions", command=print_table)
button.pack()










window.mainloop()
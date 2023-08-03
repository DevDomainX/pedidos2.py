import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.config(bg="black")


"""imagen = tk.PhotoImage(file="bart.png")
back = tk.Label( image = imagen, text="Hola")
back.place(relwidth=1, relheight=1)"""

def jumbito():
    uno.config(text="JUMBITO\n3 kilos / 1 1/2 Hallulla\n1 1/2 Frances")
   
def suny():
    dos.config(text="SUNY\nBolsa / 3 kilos \nSurtido")   
     
def cintia():
    tres.config(text="CINTIA\nCaja / 7 kilos \n5 Hallulla / 2 Frances")   
    
def guindo():
    cuatro.config(text="GUINDO \n 5 kilos \n3 Hallulla / 2 Frances")     
    
def hogar():
    cinco.config(text="HOGAR\n70 Hallullas calientes\n10 Frances\n(Domingo / Lunes / Martes \n85 Hallullas 10 Frances)") 
    
def josefa():
    seis.config(text="JOSEFA\n4 kilos \n2 Hallullas / 2 Frances")  
      
def margarita():
    siete.config(text="MARGARITA\n8 kilos de Frances / Calientes")            
                
def reset():
    uno.config(text=" ")  
    dos.config(text=" ")  
    tres.config(text=" ")  
    cuatro.config(text=" ")  
    cinco.config(text=" ")  
    seis.config(text=" ")  
    siete.config(text=" ")
    
def exit():
    root.destroy()    
    
saludo = tk.Label(root)
saludo.place(x=300, y=150)
  
titulo = tk.Label(root, text="PEDIDOS VUELTA 2 ", bg="black", fg="orange", font=("Carier 10"))       
titulo.place(x=300, y=40)           
                                 
uno = tk.Label(root, bg="black", fg="orange", font=("Carier 10"))
uno.place(x=300, y=300)

dos = tk.Label(root, bg="black", fg="orange", font=("Carier 10"))
dos.place(x=300, y=300)

tres = tk.Label(root, bg="black", fg="orange", font=("Carier 10"))
tres.place(x=300, y=300)

cuatro = tk.Label(root, bg="black", fg="orange", font=("Carier 10"))
cuatro.place(x=300, y=300)

cinco = tk.Label(root, bg="black", fg="orange", font=("Carier 10"))
cinco.place(x=300, y=300)

seis = tk.Label(root, bg="black", fg="orange", font=("Carier 10"))
seis.place(x=300, y=300)

siete = tk.Label(root, bg="black", fg="orange", font=("Carier 10"))
siete.place(x=300, y=300)


b1 = tk.Button(root, text="JUMBITO", command=jumbito, bg="black", fg="cyan", bd=10)
b1.place(x=350, y=650)

b2 = tk.Button(root, text="SUNY", command=suny, bg="black", fg="cyan", bd=10)
b2.place(x=350, y=760)

b3 = tk.Button(root, text="CINTIA", command=cintia, bg="black", fg="cyan", bd=10)
b3.place(x=350, y=860)

b4 = tk.Button(root, text="GUINDO", command=guindo, bg="black", fg="cyan", bd=10)
b4.place(x=350, y=960)

b5 = tk.Button(root, text="HOGAR", command=hogar, bg="black", fg="cyan", bd=10)
b5.place(x=350, y=1060)

b6 = tk.Button(root, text="JOSEFA", command=josefa, bg="black", fg="cyan", bd=10)
b6.place(x=350, y=1360)

vuelta = tk.Label(root, text="Calientes ", bg="black", fg="orange", font=("arial 10"))
vuelta.place(x=360, y=1250)

b7 = tk.Button(root, text="MARGARITA", command=margarita, bg="black", fg="cyan", bd=10)
b7.place(x=350, y=1460)

r = tk.Button(root, text="BORRAR", command=reset, bg="black", fg="cyan", bd=10)
r.place(x=750, y=2000)

salir = tk
H = tk.Label(root, text="Created by: Hans Saldias", bg="black", fg="red")
H.place(x=30, y=2000)

salir = tk.Button(root, text="Salir", bg="black", fg="red", command=exit, bd=20)
salir.place(x=100, y=1800)
root.mainloop()
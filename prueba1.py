from tkinter import *

#creacion de ventana
ventana = Tk()

ventana.configure(width= "400", height="400", bg="black")
ventana.title("Programa de prueba")

def hola():
    print("Hola Ian")

boton1 = Button(text="saludar", fg="black", bg = "white", command= lambda: hola())

boton1.grid(row= 5, column= 5, padx = 5, pady= 5)

print("hola")
ventana.mainloop()
from tkinter import*

raiz=Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(0,0)

raiz.iconbitmap()     #Poner la imagen en .ico

raiz.config(bg="blue")

raiz.config(bd=45)

raiz.config(relief="groove")

elFrame=Frame()

elFrame.pack()

elFrame.config(bg="red")

elFrame.config(width="650", height="350")

elFrame.config(bd=35)

elFrame.config(relief="groove")

elFrame.config(cursor="pirate")

sec=Frame()

sec.pack()

sec.config(bg="green")

sec.config(width="650", height="350")

sec.config(bd=35)

sec.config(relief="groove")

sec.config(cursor="hand2")

raiz.mainloop()
from tkinter import *
from tkinter import messagebox

# abrir toplevel centigrados
def abrir_toplevel_datos_academicos():
    global toplevel_datos_academicos
    toplevel_datos_academicos = Toplevel()
    toplevel_datos_academicos.title("Centigrados")
    toplevel_datos_academicos.resizable(False, False)
    toplevel_datos_academicos.geometry("300x200")
    toplevel_datos_academicos.config(bg="white")

    # logo de la app
    lb_logo2 = Label(toplevel_datos_academicos, bg="white")
    lb_logo2.place(x=10,y=10)

    # etiqueta para valor en centigrados
    lb_c = Label(toplevel_datos_academicos, text = "Notas: ")
    lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_c.place(x=130, y=60)

    # caja de texto para valor en centigrados
    entry_c = Entry(toplevel_datos_academicos, textvariable=c)
    entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=210,y=60)
# boton para convertir
    bt_aceptar = Button(toplevel_datos_academicos,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=150, width=100, height=30)

# aceptar
def aceptar():
    global datos
    datos = int(c.get())
    toplevel_datos_academicos.destroy()

# convertir
def estado():
    messagebox.showinfo("Estabilidad estudiante", "este es tu estado actual")
    
# borrar
def borrar():
    messagebox.showinfo("Estabilidad estudiante", "Los datos serán borrados")
    c.set("")
    t_resultados.delete("1.0","end")

# salir
def salir():
    messagebox.showinfo("Estabilidad estudiante", "La app se va a cerrar")
    ventana_principal.destroy()

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Estabilidad estudiante")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="blue")

c = StringVar()
kf = StringVar()
global logo
#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo de la app
lb_logo = Label(frame_entrada, bg="white")
lb_logo.place(x=70,y=40)

# titulo de la app
titulo = Label(frame_entrada, text="Estabilidad estudiante")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=240,y=10)

# boton para abrir Toplevel para ingresar °C
bt_datos_academicos = Button(frame_entrada, text="Ingresa tus notas", command=abrir_toplevel_datos_academicos)
bt_datos_academicos.place(x=244, y=60)

# radiobutton para kelvin
rb_a = Radiobutton(frame_entrada, text="Datos Académicos", variable=kf, value="Datos Académicos")
rb_a.config(bg="white", fg="blue", font=("Helvetica", 18))
rb_a.place(x=240, y=110)

# radiobutton para farenheit
rb_s = Radiobutton(frame_entrada, text="Datos Médicos", variable=kf, value="Datos Médicos")
rb_s.config(bg="white", fg="blue", font=("Helvetica", 18))
rb_s.place(x=240, y=140)

#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# boton para convertir
bt_estado = Button(frame_operaciones,text="Estado", command=estado)
bt_estado.place(x=45, y=35, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones,text="Salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)

#--------------------------------
# frame resultados
#--------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 18))
t_resultados.place(x=10,y=10,width=460,height=160)

# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()


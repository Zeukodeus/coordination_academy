from tkinter import *
from tkinter import messagebox

# Abrir toplevel para datos académicos
def abrir_datos():
   if kf.get()=="medico":
      global toplevel_datos_medicos
      toplevel_datos_medicos = Toplevel()
      toplevel_datos_medicos.title("Datos medicos")
      toplevel_datos_medicos.resizable(False, False)
      toplevel_datos_medicos.geometry(300,200)
      toplevel_datos_medicos.config(bg= "white")
   elif kf.get()=="academico":
      global toplevel_datos_academicos
      toplevel_datos_academicos = Toplevel()
      toplevel_datos_academicos.title("Datos medicos")
      toplevel_datos_academicos.resizable(False, False)
      toplevel_datos_academicos.geometry(300,200)
      toplevel_datos_academicos.config(bg= "white")
      
# Convertir
def estado():
    messagebox.showinfo("Estabilidad estudiante", "Este es tu estado actual")

# Borrar
def borrar():
    messagebox.showinfo("Estabilidad estudiante", "Los datos serán borrados")
    c.set("")
    t_resultados.delete("1.0","end")

#Salir
def salir():
 messagebox.showinfo("Estabilidad estudiante", "La app se va a cerrar")
 ventana_principal.destroy()

#Se declara una variable llamada ventana_principal, que adquiere las características de un objeto Tk()
ventana_principal = Tk()

#Título de la ventana
ventana_principal.title("Estabilidad estudiante")

#Tamaño de la ventana
ventana_principal.geometry("500x500")

#Deshabilitar botón de maximizar
ventana_principal.resizable(False, False)

#Color de fondo de la ventana
ventana_principal.config(bg="blue")

c = StringVar()
kf = StringVar()

#Frame entrada datos
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

#Logo de la app
lb_logo = Label(frame_entrada, bg="white")
lb_logo.place(x=70, y=40)

#Título de la app
titulo = Label(frame_entrada, text="Estabilidad estudiante")
titulo.config(bg="white", fg="blue", font=("Helvetica", 20))
titulo.place(x=240, y=10)

#Radiobutton para datos académicos
rb_a = Radiobutton(frame_entrada, text="Datos Académicos", variable=kf, value="Datos Académicos")
rb_a.config(bg="white", fg="blue", font=("Helvetica", 18))
rb_a.place(x=240, y=110)

#Radiobutton para datos médicos
rb_s = Radiobutton(frame_entrada, text="Datos Médicos", variable=kf, value="Datos Médicos")
rb_s.config(bg="white", fg="blue", font=("Helvetica", 18))
rb_s.place(x=240, y=140)

#Botón para abrir Toplevel para ingresar datos académicos
bt_datos_academicos = Button(frame_entrada, text="Ingresa tus notas", command=abrir_datos)
bt_datos_academicos.place(x=244, y=60)


#Frame operaciones
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

#Botón para mostrar estado
bt_estado = Button(frame_operaciones, text="Estado", command=estado)
bt_estado.place(x=45, y=35, width=100, height=30)

#Botón para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

#Botón para salir
bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)

#Frame resultados
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

#Área de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 18))
t_resultados.place(x=10,y=10,width=460,height=160)

# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()


from tkinter import*
from tkinter import messagebox
import tkinter as tk


#Funciones de la APP
def calcular_IMC():
    peso = float(entry_e.get())
    altura = float(entry_d.get())
    imc = round(peso / (altura ** 2), 2)
    t_resultados.insert(INSERT, f"IMC del estudiante: {imc}\n")

def calcular_Prom():
    Nota1 = float(entry_f.get())
    Nota2 = float(entry_g.get())
    Nota3 = float(entry_h.get())
    Nota4 = float(entry_i.get())
    promedio = round((Nota1 + Nota2 + Nota3 +Nota4) / 4, 2)
    t_resultados.insert(INSERT, f"Promedio del estudiante: {promedio}\n")

def borrar():
    messagebox.showinfo("Datos Medicos", "Se borraran todos los datos")
    Peso.set("")
    Altura.set("")
    Edad.set("")
    Nota1.set("")
    Nota2.set("")
    Nota3.set("")
    Nota4.set("")
    t_resultados.delete("1.0", "end")


def salir():
    messagebox.showinfo("Datos Medicos", "La APP se cerrara, ¿Desea continuar?")
    ventana_principal.destroy()


#Diseño de la app
ventana_principal = tk.Tk( )



# Establecerlo como ícono de la ventana.


#Titulo de la ventana
ventana_principal.title("Datos Medicos")

#Tamaño de la ventana
ventana_principal.geometry("500x800")

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fonde de la ventana
ventana_principal.config(bg="Sky blue2")

#Variables de control
Estudiante = StringVar()
TI_CC = StringVar()
Edad = StringVar()
Altura = StringVar()
Peso = StringVar()
Nota1 = StringVar()
Nota2 = StringVar()
Nota3 = StringVar()
Nota4 = StringVar()

#Ventana secundaria superior
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=200)
frame_entrada.place(x=10, y=20)

#Logo de la ONG

lb_logo = Label(frame_entrada, bg="white")
lb_logo.place(x=11, y=8)

#Informacion del paciente
lb_titulo = Label(frame_entrada, text="Datos del Usuario")
lb_titulo.config(bg="white", fg="Black", font=("Helvetica", 20))
lb_titulo.place(x=240, y=10)

#Etiqueta para Paciente
lb_a = Label(frame_entrada, text="Estudiante: ")
lb_a.config(bg="white", fg="Red", font=("Helvetica", 17))
lb_a.place(x=235, y=60)

#Caja de texto 
entry_a = Entry(frame_entrada, textvariable=Estudiante)
entry_a.config(bg="white", fg="Black", font=("Courier", 12))
entry_a.focus_set()
entry_a.place(x=355, y=60, width=115, height=30)

#Etiqueta para TI_CC
lb_b = Label(frame_entrada, text="TI_CC :")
lb_b.config(bg="white", fg="Red", font=("Helvetica", 17))
lb_b.place(x=235, y=100)

#Caja de texto 
entry_b = Entry(frame_entrada, textvariable=TI_CC)
entry_b.config(bg="white", fg="Black", font=("Courier", 12))
entry_b.place(x=355, y=100, width=115, height=30)

#Ventana secundaria intermedio
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=310)
frame_operaciones.place(x=10, y=265)

#Etiqueta para Edad
lb_c = Label(frame_operaciones, text="Edad: ")
lb_c.config(bg="white", fg="Blue", font=("Helvetica", 17))
lb_c.place(x=10, y=30)

#Caja de texto
entry_c = Entry(frame_operaciones, textvariable=Edad)
entry_c.config(bg="white", fg="Black", font=("Courier", 12))
entry_c.place(x=113, y=30, width=115, height=30)

#Etiqueta para Altura
lb_d = Label(frame_operaciones, text="Altura(M): ")
lb_d.config(bg="white", fg="Blue", font=("Helvetica", 17))
lb_d.place(x=10, y=100)

#Caja de texto
entry_d = Entry(frame_operaciones, textvariable=Altura)
entry_d.config(bg="white", fg="Black", font=("Courier", 12))
entry_d.place(x=113, y=100, width=115, height=30)

#Etiqueta para Peso corporal
lb_e = Label(frame_operaciones, text="Peso(Kg): ")
lb_e.config(bg="white", fg="Blue", font=("Helvetica", 17))
lb_e.place(x=10, y=165)

#Caja de texto
entry_e = Entry(frame_operaciones, textvariable=Peso)
entry_e.config(bg="white", fg="Black", font=("Courier", 12))
entry_e.place(x=113, y=165, width=115, height=30)

#Etiqueta para Nota 1
lb_f = Label(frame_operaciones, text="Nota 1: ")
lb_f.config(bg="white", fg="Blue", font=("Helvetica", 15))
lb_f.place(x=240, y=20)

#Caja de texto
entry_f = Entry(frame_operaciones, textvariable=Nota1)
entry_f.config(bg="white", fg="Black", font=("Courier", 12))
entry_f.place(x=320, y=20, width=115, height=30)

#Etiqueta para Nota 2
lb_g = Label(frame_operaciones, text="Nota 2: ")
lb_g.config(bg="white", fg="Blue", font=("Helvetica", 15))
lb_g.place(x=240, y=75)

#Caja de texto
entry_g = Entry(frame_operaciones, textvariable=Nota2)
entry_g.config(bg="white", fg="Black", font=("Courier", 12))
entry_g.place(x=320, y=75, width=115, height=30)

#Etiqueta para Nota 3
lb_h = Label(frame_operaciones, text="Nota 3: ")
lb_h.config(bg="white", fg="Blue", font=("Helvetica", 15))
lb_h.place(x=240, y=130)

#Caja de texto
entry_h = Entry(frame_operaciones, textvariable=Nota3)
entry_h.config(bg="white", fg="Black", font=("Courier", 12))
entry_h.place(x=320, y=130, width=115, height=30)

#Etiqueta para Nota 4
lb_i = Label(frame_operaciones, text="Nota 4: ")
lb_i.config(bg="white", fg="Blue", font=("Helvetica", 15))
lb_i.place(x=240, y=180)

#Caja de texto
entry_i = Entry(frame_operaciones, textvariable=Nota4)
entry_i.config(bg="white", fg="Black", font=("Courier", 12))
entry_i.place(x=320, y=180, width=115, height=30)

#Boton de calcular IMC
bt_calcular=Button(frame_operaciones, text="calcular IMC", command=calcular_IMC)
bt_calcular.place(x=100, y=220,width=100, height=30)

#Boton de calcular Promedio
bt_calcular=Button(frame_operaciones, text="calcular promedio", command=calcular_Prom)
bt_calcular.place(x=300, y=220,width=100, height=30)

#Boton de Borrar
bt_calcular=Button(frame_operaciones, text="Borrar", command=borrar)
bt_calcular.place(x=205, y=270,width=100, height=30)

#Ventana secundaria inferior
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=485, height=180)
frame_resultados.place(x=10, y=600)

#Area de texto para resultados
t_resultados=Text(frame_resultados)
t_resultados.config(bg="black", fg="green", font=("Courier", 20))
t_resultados.place(x=10, y=10, width=460, height=160)

#Boton de salir
bt_salir=Button(frame_resultados, text="salir", command=salir)
bt_salir.place(x=200, y=145,width=100, height=30)

#Correr el programa
ventana_principal.mainloop()
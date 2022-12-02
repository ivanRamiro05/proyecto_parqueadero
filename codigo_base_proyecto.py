from tkinter import *

def send_data():
    username_data =username.get()
    código_data =str(código.get())
   # tipodevehículo_data =tipodevehículo.get()
    placa_data =str(placa.get())
    tiempo_data =tiempo.get()
    print("NOMBRE: ",username_data, "\t","CODIGO",código_data, "\t","TIPO DE VEHICILO" ,"PLACA ", placa_data, "\t","TIEMPO", tiempo_data)

    newfile=open("Registros.txt", "a")
    newfile.write("NOMBRE: ")
    newfile.write(username_data)
    newfile.write("\t")
    newfile.write("CODIGO: ")
    newfile.write(código_data)
    newfile.write("\t")
    newfile.write("TIPO DE VEHICULO: ")
    #newfile.write(tipodevehículo_data)
    newfile.write("\t")
    newfile.write("PLACA: ")
    newfile.write(placa_data)
    newfile.write("\t")
    newfile.write("TIEMPO: ")
    newfile.write(tiempo_data)
    newfile.write("\n")
    newfile.close()
    print("Nuevo usuario registrado. NOMBRE: {} | TIEMPO: {} ".format(username_data, tiempo_data))

    username_entry.delete(0, END)

    #tipodevehículo_entry.delete(0, END)
    placa_entry.delete(0, END)
    tiempo_entry.delete(0, END)

ventana = Tk()
ventana.title("Registro del usuario para ingresar al parqueadero")
ventana.geometry("800x500")
"""
logo=PhotoImage(file="img/download.png")
lb_logo = Label(image=logo)
lb_logo.place(x=480,y=150)"""

ventana.resizable(False,False)
ventana.config(background="#E8EAEC")
lbl =Label(ventana,text="Hola bienvendido a la UIS por favor ingresa tus datos y los de tu vehículo: ", font=("Cambria", 13), bg="#56cd63", fg="white", width="550", height="2")
lbl.pack()
ventana.config(bg="green")

def cancelar():
    vehiculo_var.set("Pulse sobre \"vehiculo\"")
    selecciones_label.config(text="")

def es_Carro():
    vehiculo_var.set("Carro")

def es_Moto():
    vehiculo_var.set("Moto")

def espacio():
    if opcion == carro:
        espacios_disponibles.list=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    if opcion== moto:
        espacios_disponibles.list=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

def ventana_sec():
    ventana_sec = Toplevel()
    ventana_sec.title("VEHICULOS EN EL PARQUEADERO")
    ventana_sec.geometry("800x500")
    ventana_sec.config(bg="green")
    frame_resultados = Frame(ventana_sec)
    frame_resultados.config(bg="white", width=780, height=480)
    frame_resultados.place(x=10, y = 10)
    t_resultados = Text(frame_resultados)
    t_resultados.config(bg="green", fg="black", font=("Arial",10))
    t_resultados.place(x=10,y=10, width=760, height= 460)
    with open("Registros.txt") as archivo:
        for linea in archivo:
            t_resultados.insert(INSERT, linea)
    
    
    
username_label = Label(text="NOMBRE COMPLETO", bg="red")
username_label.place(x=22, y=70)
código_label = Label(text="CÓDIGO", bg="#FFEEDD")
código_label.place(x=22, y=130)
tipodevehículo_label = Label(text="TIPO DE VEHÍCULO", bg="#FFEEDD")
#tipodevehículo_label.place(x=22, y=190)
placa_label = Label(text="PLACA", bg="#FFEEDD")
placa_label.place(x=22, y=250)
tiempo_label = Label(text="LUGAR DE ESTACIONAMIENTO", bg="#FFEEDD")
tiempo_label.place(x=22, y=310)

username = StringVar()
código = StringVar()
#tipodevehículo = StringVar()
placa = StringVar()
tiempo = StringVar()
vehiculo_var = StringVar()
var_provincia = StringVar()

username_entry = Entry(textvariable=username, width="40")
código_entry = Entry(textvariable=código, width="40")
#tipodevehículo_entry = Entry(textvariable=tipodevehículo, width="40")
placa_entry = Entry(textvariable=placa, width="40")
tiempo_entry = Entry(textvariable=tiempo, width="40")


vehiculo_entry = Entry(bd=5, state="disabled", textvariable=vehiculo_var)
vehiculo_var.set("Pulse sobre \"vehiculo\"")

vehiculo_menu = Menubutton(text = "vehiculo:", relief="raised")
vehiculo_menu.menu = Menu(vehiculo_menu, tearoff=0)
vehiculo_menu.menu.add_command(label="Carro", command=es_Carro())
vehiculo_menu.menu.add_command(label="Moto", command=es_Moto)
vehiculo_menu["menu"]= vehiculo_menu.menu


def aceptar():
    selecciones = ""
    
##
    if provincia != "Pulse para ver las permitidas":
        selecciones += "Provincia : "+provincia+"\n"
    selecciones += "Edad: "+edad
    selecciones_label.config(text=selecciones)




##
#provincia_label = Label(text="Tipo de vehiculo:")
provincia_menu = OptionMenu(ventana, var_provincia, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
var_provincia.set("LUGAR DE APARCAMIENTO")




#provincia_label.place(x= 22, y=270)
provincia_menu.place(x= 22, y=340)




ventana.columnconfigure(1, weight=1)

username_entry.place(x=22, y=100)
código_entry.place(x=22, y=160)
#tipodevehículo_entry.place(x=22, y=220)
vehiculo_menu.place(x=22, y= 190)
vehiculo_entry.place(x=22, y= 220)
placa_entry.place(x=22, y=280)
#tiempo_entry.place(x=22, y=340)

submit_btn =Button(ventana, text="Cargar datos", command=send_data, width="30", height="2")
submit_btn.place(x=22, y=390)

mostrar_btn =Button(ventana, text="Mostar datos", command=ventana_sec, width="30", height="2")
mostrar_btn.place(x=250, y=390)


ventana.mainloop()
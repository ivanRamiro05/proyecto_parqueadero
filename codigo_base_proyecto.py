from tkinter import *
def tiempo_usuario():
    from tkinter import Tk, Label, Button, StringVar

    hora=minuto=segundo=0
    inicio=False

    def actualizar_tiempo():
        global hora, minuto, segundo

        if inicio:  
            segundo += 1
            if segundo == 60:
                segundo = 0
                minuto += 1
            if minuto == 60:
                segundo = 0
                minuto = 0
                hora += 1
            if hora == 99:
                segundo = 0
                minuto = 0
                hora = 0
            if hora < 10: hora_str = "0"+str(hora)
            else: hora_str = str(hora)
            if minuto < 10: minuto_str = "0"+str(minuto)
            else: minuto_str = str(minuto)
            if segundo < 10: segundo_str = "0"+str(segundo)
            else: segundo_str = str(segundo)
            variable_control.set(hora_str+":"+minuto_str+":"+segundo_str)
            root.after(1000, actualizar_tiempo)

    def start():
        global hora, minuto, segundo, inicio

        if not(inicio):
            variable_control.set("00:00:00")
            hora=minuto=segundo=0
            inicio=True
            root.after(1000, actualizar_tiempo)

    def stop():
        global inicio
        inicio=False

    root = Tk()
    root.resizable(False, False)

    variable_control = StringVar(value="00:00:00")

    reloj = Label(textvariable= variable_control, fg="blue", font=("Arial", 18), padx=20, pady=20)
    boton_start = Button(text="Start", padx=10,  fg="white", bg="green", command=start)
    boton_stop = Button(text="Stop", padx=10, fg="white", bg="red", command=stop)

    reloj.pack()
    boton_start.pack(side="left", padx=10, pady=10)
    boton_stop.pack(side="right", padx=10, pady=10)

    root.mainloop()

def send_data():
    username_data =username.get()
    código_data =str(código.get())
    tipodevehículo_data =tipodevehículo.get()
    placa_data =str(placa.get())
    tiempo_data =tiempo.get()
    print(username_data, "\t", código_data, "\t", tipodevehículo_data, "\t", placa_data, "\t", tiempo_data)

    newfile=open("Registros.txt", "a")
    newfile.write(username_data)
    newfile.write("\t")
    newfile.write(código_data)
    newfile.write("\t")
    newfile.write(tipodevehículo_data)
    newfile.write("\t")
    newfile.write(placa_data)
    newfile.write("\t")
    newfile.write(tiempo_data)
    newfile.write("\n")
    newfile.close()
    print("Nuevo usuario registrado. NOMBRE: {} | TIEMPO: {} ".format(username_data, tiempo_data))

    username_entry.delete(0, END)
    código_entry.delete(0, END)
    tipodevehículo_entry.delete(0, END)
    placa_entry.delete(0, END)
    tiempo_entry.delete(0, END)
BASE=1000
ALTURA=800
ventana = Tk()
ventana.title("Registro del usuario para ingresar al parqueadero")
ventana.geometry("800x500")

"""logo=PhotoImage(file="img/download.png")
lb_logo = Label(image=logo)
lb_logo.place(x=480,y=150)"""

ventana.resizable(False,False)
ventana.config(background="#E8EAEC")
lbl =Label(ventana,text="Hola bienvendido a la UIS por favor ingresa tus datos y los de tu vehículo: ", font=("Cambria", 13), bg="#56cd63", fg="white", width="550", height="2")
lbl.pack()
ventana.config(bg="green")


#Nombre de los usuarios
username_label = Label(text="NOMBRE COMPLETO", bg="#FFEEDD")
username_label.place(x=22, y=70)
# Codigo de un usuario uis
código_label = Label(text="CÓDIGO", bg="#FFEEDD")
código_label.place(x=22, y=130)
#Tipos de vehculos
tipodevehículo_label = Label(text="TIPO DE VEHÍCULO", bg="#FFEEDD")
tipodevehículo_label.OptionMenu((root, var_provincia, "Carro", "Moto")
tipodevehículo_label.place(x=22, y=190)

# placa del vehiculo
placa_label = Label(text="PLACA", bg="#FFEEDD")
placa_label.place(x=22, y=250)
#Tiempo de estadia del usuario
tiempo_label = Label(text="TIEMPO DE ESTADÍA EN EL PARQUEADERO", bg="#FFEEDD")
tiempo_label.place(x=22, y=310)
#Almacenamiento de los datos del usuario
username = StringVar()
código = StringVar()
tipodevehículo = StringVar()
placa = StringVar()
tiempo = StringVar()

username_entry = Entry(textvariable=username, width="40")
código_entry = Entry(textvariable=código, width="40")
tipodevehículo_entry = Entry(textvariable=tipodevehículo, width="40")
placa_entry = Entry(textvariable=placa, width="40")
tiempo_entry = Entry(textvariable=tiempo, width="40")

#Ubicacion de,los datos
username_entry.place(x=22, y=100)
código_entry.place(x=22, y=160)
tipodevehículo_entry.place(x=22, y=220)
placa_entry.place(x=22, y=280)
tiempo.OptionMenu((root, var_provincia, "León", "Zamora", "Salamanca", "Valladolid", "Palencia")

submit_btn =Button(ventana, text="Cargar datos", command=send_data, width="35", height="2")
submit_btn.place(x=22, y=390)

ventana.mainloop()

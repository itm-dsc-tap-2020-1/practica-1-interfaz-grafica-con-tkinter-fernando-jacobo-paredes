import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext
from tkinter import Label
#funciones----------------------------------------------------------------------------------
def salir():
    ventana.quit()
    ventana.destroy()
    exit()
def click1():
    if nombre.get()!="" and apellidop.get()!="" and apellidom.get()!="" and direccion.get()!="":
        mBox.showinfo("Datos personales",
                      "Nombre: "+nombre.get()+"\nApellido Paterno: "+apellidop.get()+
                      "\nApellido Materno: "+apellidom.get()+"\nDireccion: "+direccion.get()+
                      "\nColonia: "+colonia.get()+"\nCiudad: "+ciudad.get()+
                      "\nMunicipio: "+municipio.get())
    else:
        mBox.showinfo("Advertencia", "Favor de llenar todos los datos.")
        
def click2():
    if (opcion1.get()=="" and opcion2.get()=="" and opcion3.get()=="") or (op.get()!=1 and op.get()!=2 and op.get()!=3) or caja.get('1.0', 'end-1c')=="": mBox.showinfo("Advertencia", "Datos incompletos, favor de llenarlos")
    else:    
        All="Pasatiempos:\n"
        if opcion1.get()==1: All+="\tLeer\n"
        if opcion2.get()==1: All+="\tPeliculas\n"
        if opcion3.get()==1: All+="\tRedes Sociales\n"
        All+="Estado Civil:\n"
        if op.get()==1: All+="\tCasado"
        elif op.get()==2: All+="\tSoltero"
        elif op.get()==3: All+="\tViudo"
        All+="\n Objetivo de la vida:\n"
        if caja.get('1.0', 'end-1c')!="": All+=caja.get('1.0', 'end-1c')
        mBox.showinfo("Datos Extras",All)
    
def click3():
    if nombre.get()!="" and apellidop.get()!="" and apellidom.get()!="" and direccion.get()!="":
        if (opcion1.get()=="" and opcion2.get()=="" and opcion3.get()=="") or (op.get()!=1 and op.get()!=2 and op.get()!=3) or caja.get('1.0', 'end-1c')=="": mBox.showinfo("Advertencia", "Datos incompletos, favor de llenarlos")
        else:    
            All="Pasatiempos:\n"
            if opcion1.get()==1: All+="\tLeer\n"
            if opcion2.get()==1: All+="\tPeliculas\n"
            if opcion3.get()==1: All+="\tRedes Sociales\n"
            All+="Estado Civil:\n"
            if op.get()==1: All+="\tCasado"
            elif op.get()==2: All+="\tSoltero"
            elif op.get()==3: All+="\tViudo"
            All+="\n Objetivo de la vida:\n"
            if caja.get('1.0', 'end-1c')!="": All+=caja.get('1.0', 'end-1c')
            mBox.showinfo("Datos personales",
                        "Nombre: "+nombre.get()+"\nApellido Paterno: "+apellidop.get()+
                        "\nApellido Materno: "+apellidom.get()+"\nDireccion: "+direccion.get()+
                        "\nColonia: "+colonia.get()+"\nCiudad: "+ciudad.get()+
                        "\nMunicipio: "+municipio.get()+"\n"+All)
    else:
        mBox.showinfo("Advertencia", "Favor de llenar todos los datos.")
        
def ayuda():
    mBox.showinfo("Acerca de", "Programa  desarrollado por Fernando Jacobo Paredes")
    
ventana=tk.Tk()
ventana.title("Sistema Escolar")
#Pestañas-----------------------------------------------------------------------------------
tabc=ttk.Notebook(ventana)
tab1=ttk.Frame(tabc)
tabc.add(tab1, text="Datos personales")
tabc.pack(expand=1, fill="both")
tab2=ttk.Frame(tabc)
tabc.add(tab2, text="Extras")
tabc.pack(expand=2, fill="both")
#Menus--------------------------------------------------------------------------------------
bmenu=Menu(ventana)
ventana.config(menu=bmenu)
op=Menu(bmenu)
op.add_command(label="Imprimir", command=click3)
op.add_command(label="Salir", command=salir)
bmenu.add_cascade(label="Sistema", menu=op)
#Menu2--------------------------------------------------------------------------------------
menu_ayuda=Menu(bmenu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=ayuda)
bmenu.add_cascade(label="Ayuda", menu=menu_ayuda)
#Etiquetas pestaña 1------------------------------------------------------------------------
tk.Label(tab1 , text="Nombre:").grid(column=0, row=0)
tk.Label(tab1, text="Apellido P.:").grid(column=0, row=1)
tk.Label(tab1, text="Apellido M.:").grid(column=0, row=2)
tk.Label(tab1, text="Direccion:").grid(column=0, row=3)
tk.Label(tab1, text="Colonia:").grid(column=0, row=4)
tk.Label(tab1, text="Ciudad:").grid(column=0, row=5)
tk.Label(tab1, text="Municipio:").grid(column=0, row=6)
#Etiquetas pestaña 2------------------------------------------------------------------------
tk.Label(tab2, text="Pasatiempos:").grid(column=0, row=0)
tk.Label(tab2, text="Estado Civil:").grid(column=0, row=2)
ttk.Label(tab2, text="Objetivo de la vida:").grid(column=0, row=4)
    #Campos pestaña 1-----------------------------------------------------------------------
#Entradas1----------------------------------------------------------------------------------
nombre=tk.StringVar()
nombre1=ttk.Entry(tab1, textvariable=nombre)
nombre1.grid(column=1, row=0)
apellidop=tk.StringVar()
apellidop1=ttk.Entry(tab1, textvariable=apellidop)
apellidop1.grid(column=1, row=1)
apellidom=tk.StringVar()
apellidom1=ttk.Entry(tab1, textvariable=apellidom)
apellidom1.grid(column=1, row=2)
direccion=tk.StringVar()
direccion1=ttk.Entry(tab1, textvariable=direccion)
direccion1.grid(column=1, row=3)
#Entradas2----------------------------------------------------------------------------------
caja=scrolledtext.ScrolledText(tab2, width=30, height=3, wrap=tk.WORD)
caja.grid(column=0, row=5)
#Listas-------------------------------------------------------------------------------------
colonia=tk.StringVar()
colonia1=ttk.Combobox(tab1, width=10, textvariable=colonia, state="readonly")
colonia1['values']=("4 de Marzo", "Prados Verdes", "Lomas de Santiaguito", "Industrial", "Lopez Mateos")
colonia1.grid(column=1, row=4)
colonia1.current(0)
ciudad=tk.StringVar()
ciudad1=ttk.Combobox(tab1, width=10, textvariable=ciudad, state="readonly")
ciudad1['values']=("Morelia", "Leon", "Guadalajara", "Pachuca", "Toluca")
ciudad1.grid(column=1, row=5)
ciudad1.current(0)
municipio=tk.StringVar()
municipio1=ttk.Combobox(tab1, width=10, textvariable=municipio, state="readonly")
municipio1['values']=("Maravatio", "Capula", "Iratzio", "Santiago Undameo", "Tiripetio")
municipio1.grid(column=1, row=6)
municipio1.current(0)
#Botones pestaña 1---------------------------------------------------------------------------
button1=ttk.Button(tab1, text="Imprimir Datos Personales", command=click1)
button1.grid(column=1, row=7)
#Botones pestaña 2---------------------------------------------------------------------------
#Checkbutton---------------------------------------------------------------------------------
opcion1=tk.IntVar()
cas1=tk.Checkbutton(tab2, text="Leer", variable=opcion1)
cas1.grid(column=0, row=1, sticky=tk.W)
opcion2=tk.IntVar()
cas2=tk.Checkbutton(tab2, text="Peliculas", variable=opcion2)
cas2.grid(column=1, row=1, sticky=tk.W)
opcion3=tk.IntVar()
cas3=tk.Checkbutton(tab2, text="Redes Sociales", variable=opcion3)
cas3.grid(column=2, row=1, sticky=tk.W)
#Radiobutton---------------------------------------------------------------------------------
op=tk.IntVar()
r1=tk.Radiobutton(tab2, text="Soltero", variable=op, value=1)
r1.grid(column=0, row=3, sticky=tk.W)
r2=tk.Radiobutton(tab2, text="Casado", variable=op, value=2)
r2.grid(column=1, row=3, sticky=tk.W)
r3=tk.Radiobutton(tab2, text="Viudo", variable=op, value=3)
r3.grid(column=2, row=3, sticky=tk.W)
#Boton acciones------------------------------------------------------------------------------
button2=ttk.Button(tab2, text="Boton Imprimir Datos", command=click2)
button2.grid(column=2, row=6)

ventana.mainloop()
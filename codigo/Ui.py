# Seccion de librerias a usar dentro del programa
import tkinter
import matplotlib.pyplot as plt


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import json


#Instanciones para nuestras matrices y el comprobador
lista = []
lista2 = []
resul = []
resul2 = []
p1 = 0
p2 = 0
r1 = []
r2 = []
r3 = []
comprobador = [-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
def onlyn(P):
    return P.isdigit()

#Funcion para la primera actualizacion de pagina de nuestro programa
def abrir_segundaventana():
    tt = "Elige el SEL"

    ventana1.title("Eleccion de SEL")
    varet.set(tt)
    boton1.destroy()
    btn2.place(x=10 , y= 120)

    btn3.place(x = 260 , y = 120)
    boton1.destroy()



def Sel2():
    tex2 = "Rellene los datos del SEl 2*2"
    ventana1.title("SEL 2*2")
    varet.set(tex2)
    btn2.destroy()
    btn3.destroy()
    eti.place(x = 70 , y =80)

    t1.place(x = 70 , y = 130)
    t2.place(x=160, y=130)
    t3.place(x=250, y=130)


    eti4.place(x= 70 , y = 170)
    t4.place(x = 70 , y = 230)
    t5.place(x= 160 , y =230)
    t6.place(x = 250 , y =230)

    btn4.place(x = 160 , y = 280)



def Sel3():
    tex2 = "Rellene los datos del SEl 3*3"
    ventana1.title("SEL 3*3")
    varet.set(tex2)
    btn2.destroy()
    btn3.destroy()

    eti5.place(x = 20 , y = 80)
    t1.place(x =20 , y=120)
    t2.place(x=100, y=120)
    t3.place(x=190, y=120)
    t4.place(x=290 , y = 120)

    eti6.place(x=20 , y = 170)
    t5.place(x=20, y=210)
    t6.place(x=100, y=210)
    t7.place(x=190, y=210)
    t8.place(x=290, y=210)

    eti7.place(x = 20 , y = 270)
    t9.place(x=20, y=310)
    t10.place(x=100, y=310)
    t11.place(x=190, y=310)
    t12.place(x=290, y=310)

    btn5.place(x=160 , y = 350)


def guardardatoSel2():

    etiqueta.destroy()
    eti.destroy()
    eti4.destroy()
    ventana1.geometry("700x1000")


    panel = tkinter.Frame(ventana1,bg="#088395",width=900,height=1000)
    panel.pack()
    text = tkinter.Text(panel,height=180 , width=20)

    ncomprobador = json.dumps(comprobador, indent=4)
    text.insert(tkinter.END, ncomprobador)
    text.config(state=tkinter.DISABLED)
    text.place(x=2 , y =2)


    lista = [t1.get(), t2.get(), t3.get() , t4.get() , t5.get() , t6.get()]
    # 0 al 2 es x y k , 3 al 5 es x2 y2 2
    listaint = [int(x) for x in lista]

    widgetdestroy = [t1, t2, t3, t4, t5, t6, btn4]
    for bye in widgetdestroy:
        bye.destroy()

    try:
        for incognita in comprobador:
            p1 = listaint[2] + (-1 * listaint[0]) * incognita / listaint[1]

            resul.append(p1)

    except ZeroDivisionError:
        p1=0
        resul.append(p1)

    try:
        for incognita2 in comprobador:
            p2 = listaint[5] + (-1 * listaint[3]) * incognita2 / listaint[4]
            resul2.append(p2)

    except ZeroDivisionError:
        p2=0
        resul2.append(p2)

    text2 = tkinter.Text(panel,height=180 , width=40)
    text2.place(x=130 , y = 2)


    nr1 = json.dumps(resul,indent=4)
    text2.insert(tkinter.END,nr1)
    text2.config(state=tkinter.DISABLED)
    nr2 = json.dumps(resul2,indent=4)


    text3 = tkinter.Text(panel,height=180,width=40)
    text3.insert(tkinter.END,nr2)
    text3.config(state=tkinter.DISABLED)
    text3.place(x=360,y=2)



    for i in resul2:
        print(i)

    for i in resul:
        print(i)


    x = np.array(comprobador)
    y = np.array(resul)

    y2 = np.array(resul2)

    plt.plot(x, y, label="y2")
    plt.plot(x, y2, label="y1", color="orange")
    plt.title("Mi grafica")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()



def guardardatoSel3():
    ventana1.title("SEL 3*3")

    varet.set("Tabla de Valores 3*3")
    lista2 = [t1.get() , t2.get() , t3.get() , t4.get() , t5.get() , t6.get(),t7.get() , t8.get() , t9.get() , t10.get() , t11.get() , t12.get()]
    print(len(lista2))
    listaint2 = [int(x) for x in lista2 if x.strip().isdigit()]
    for i in lista2:
        print(i)

    # 0 al 3 prt1 , 4 al 7 prt2 , 8 al 11 prt3

    widgetd= [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,eti5 , eti6,eti7,eti,btn5]
    for u in widgetd:
        u.destroy()
    ventana1.geometry("400x400")
    panel2 = tkinter.Frame(ventana1, bg="#088395", width=600, height=700)
    panel2.pack()


    #subparte1
    p1 = [listaint2[3] / listaint2[2], listaint2[3] / listaint2[1], listaint2[3] / listaint2[0]]

    p2 = [listaint2[7] / listaint2[6], listaint2[7] / listaint2[5], listaint2[7] / listaint2[4]]

    p3 = [listaint2[11] / listaint2[10], listaint2[11] / listaint2[9], listaint2[11] / listaint2[8]]

    text5=tkinter.Text(panel2,height=8 , width=30)
    pr1 = json.dumps(p1, indent=4)
    text5.insert(tkinter.END, pr1)
    text5.config(state=tkinter.DISABLED)
    text5.place(x=2,y=2)

    text6=tkinter.Text(panel2,height=8 , width=30)
    pr2 = json.dumps(p2, indent=4)
    text6.insert(tkinter.END, pr2)
    text6.config(state=tkinter.DISABLED)
    text6.place(x=2, y=100)

    text7 = tkinter.Text(panel2,height=8 , width=30)
    pr3 = json.dumps(p3, indent=4)
    text7.insert(tkinter.END, pr3)
    text7.config(state=tkinter.DISABLED)
    text7.place(x=2, y=200)

    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection = "3d")
    ax1.plot(p1,p2,p3)
    plt.show()


#Parte de codigo de nuestra ventana principal
ventana1 = tkinter.Tk()
ventana1.geometry("400x400")
ventana1.title("Programa de SELs")
ventana1.configure(bg="#EBF4F6")
ventana1.resizable(False,False)
#Datos de la etiqueta de texto
varet= tkinter.StringVar()
varet.set("Bienvenido a nuestro programa")
etiqueta =tkinter.Label(ventana1,textvariable=varet,bg="#77E4C8",font=("Arial Rounded MT Bold",18),padx=20,pady=20 )
etiqueta.pack(fill = tkinter.BOTH)
boton1 = tkinter.Button(ventana1,font=("Arial Rounded MT Bold",10),text = "Comenzar",padx = 40 , pady = 50 , bg="#37B7C3",command=abrir_segundaventana)
eti = tkinter.Label(ventana1 , text="X          Y         K" , font=("Comic Sans MS",20))
eti4 = tkinter.Label(ventana1 , text="X2       Y2         K2" , font=("Comic Sans MS",20))
eti5 = tkinter.Label(ventana1 , text="X1       Y1       Z1        K1" , font=("Comic Sans MS",20))
eti6 = tkinter.Label(ventana1 , text="X2       Y2       Z2        K2" , font=("Comic Sans MS",20))
eti7 = tkinter.Label(ventana1 , text="X3       Y3       Z3        K3" , font=("Comic Sans MS",20))
boton1.place(x = 120 , y= 160)

btn2 = tkinter.Button(ventana1 ,font=("Comic Sans MS",13) , text="2*2" ,padx = 40 , pady = 40 , bg= "#37B7C3",command=Sel2)
btn3 = tkinter.Button(ventana1, font=("Comic Sans MS",13) ,text="3*3", padx=40, pady=40, bg="#088395",command=Sel3)

btn4 = tkinter.Button(ventana1,text="Enviar",bg="#77E4C8",command=guardardatoSel2 , padx=20 , pady=20)
btn5 = tkinter.Button(ventana1,text="Enviar",bg="#478CCF",command=guardardatoSel3 , padx=10 , pady=10)
t1 = tkinter.Entry(ventana1,width=10 ,validate="key", validatecommand=(ventana1.register(onlyn),"%P") )
t2 = tkinter.Entry(ventana1, width=10,validate="key", validatecommand=(ventana1.register(onlyn),"%P"))
t3 = tkinter.Entry(ventana1 , width=10,validate="key", validatecommand=(ventana1.register(onlyn),"%P"))
t4 = tkinter.Entry(ventana1 , width=10,validate="key", validatecommand=(ventana1.register(onlyn),"%P"))
t5 = tkinter.Entry(ventana1 , width=10,validate="key", validatecommand=(ventana1.register(onlyn),"%P"))
t6 = tkinter.Entry(ventana1 , width=10,validate="key", validatecommand=(ventana1.register(onlyn),"%P"))
t7 = tkinter.Entry(ventana1 , width=10,validate="key", validatecommand=(ventana1.register(onlyn),"%P"))
t8 = tkinter.Entry(ventana1 , width=10,validate="key", validatecommand=(ventana1.register(onlyn),"%P"))
t9 = tkinter.Entry(ventana1 , width=10,validate="key", validatecommand=(ventana1.register(onlyn),"%P"))
t10 = tkinter.Entry(ventana1 , width=10,validate="key", validatecommand=(ventana1.register(onlyn),"%P"))
t11= tkinter.Entry(ventana1 , width=10,validate="key", validatecommand=(ventana1.register(onlyn),"%P"))
t12 = tkinter.Entry(ventana1 , width=10,validate="key", validatecommand=(ventana1.register(onlyn),"%P"))

ventana1.mainloop()
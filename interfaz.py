import tkinter
from tkinter.filedialog import askopenfilename
import customtkinter
from imagen import Imagen
from PIL import Image

imagen = Imagen()
label_array = [0] * 4
MOSTRAME_EL_LOADING_EN_LA_GUI = False

# Función para agregar una imagen en un tab
def agregar_imagen(path, tab, px, py, index):
    my_image = customtkinter.CTkImage(
        dark_image=Image.open(path, mode='r').convert('L'), size=(400, 400))
    my_image_lb = customtkinter.CTkLabel(
        master=tabview.tab(tab), image=my_image, text="")
    my_image_lb.place(x=px, y=py)
    label_array[index] = my_image_lb

# Funciones para cargar imágenes
def cargar_imagen_a_encriptar():
    filename = askopenfilename()
    imagen.set_img_encriptar(filename)
    agregar_imagen(imagen.get_img_normal_encriptar(), "Modo Cifrar", 250, 0, 0)


def cargar_imagen_a_desencriptar():
    filename = askopenfilename()
    imagen.set_img_desencriptar(filename)
    agregar_imagen(imagen.get_img_normal_desencriptar(), "Modo Descifrar", 250, 0, 2)

# Funciones para limpiar imágenes
def limpiar_imagenes_encriptar():
    if imagen.get_img_normal_encriptar() != "" and imagen.get_img_encriptada() != "":
        for i in range(2):
            label_array[i].destroy()

def limpiar_imagenes_desencriptar():
    if imagen.get_img_normal_desencriptar() != "" and imagen.get_img_desencriptada() != "":
        for i in range(2, 4):
            label_array[i].destroy()

# Funciones para encriptar y desencriptar
def encriptar():
    global MOSTRAME_EL_LOADING_EN_LA_GUI
    MOSTRAME_EL_LOADING_EN_LA_GUI = True
    if imagen.get_img_normal_encriptar() != "":
        imagen.encriptar_imagen()
        agregar_imagen(imagen.get_img_encriptada(), "Modo Cifrar", 700, 0, 1)
        agregar_imagen(imagen.get_img_encriptada(), "Modo Descifrar", 250, 0, 2)

def desencriptar():
    if imagen.get_img_normal_desencriptar() != "":
        imagen.desencriptar_imagen()
        agregar_imagen(imagen.get_img_desencriptada(), "Modo Descifrar", 700, 0, 3)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
wdth = app.winfo_screenwidth()
hgt = app.winfo_screenheight()
app.geometry("%dx%d" % (wdth, hgt))
app.maxsize(1400, 900)
app.minsize(1400, 900)
app.title("Grupo 07 - Parcial 2 - Criptografía")

tabview = customtkinter.CTkTabview(master=app)
tabview.pack(fill="both", expand=1)

tabview.add("Modo Cifrar")
tabview.add("Modo Descifrar")
tabview.set("Modo Cifrar")

# Botones y acciones
cargar_imagen_encriptar_btn = customtkinter.CTkButton(master=tabview.tab("Modo Cifrar"), font=("Helvetica", 25),
                                                     text="Cargar Imagen", width=230, height=80, command=cargar_imagen_a_encriptar, compound='left')
cargar_imagen_encriptar_btn.place(x=0, y=0)

encriptar_btn = customtkinter.CTkButton(master=tabview.tab("Modo Cifrar"), font=("Helvetica", 25),
                                       text="Cifrar Imagen", width=230, height=80, command=encriptar, compound='left')
encriptar_btn.place(x=0, y=100)

limpiar_encriptar_btn = customtkinter.CTkButton(master=tabview.tab("Modo Cifrar"), font=("Helvetica", 25),
                                               text="Limpiar todo", width=230, height=80, command=limpiar_imagenes_encriptar, compound='left')
limpiar_encriptar_btn.place(x=0, y=200)

cargar_imagen_desencriptar_btn = customtkinter.CTkButton(master=tabview.tab("Modo Descifrar"), font=("Helvetica", 25),
                                                       text="Cargar Imagen", width=230, height=80, command=cargar_imagen_a_desencriptar, compound='left')
cargar_imagen_desencriptar_btn.place(x=0, y=0)

desencriptar_btn = customtkinter.CTkButton(master=tabview.tab("Modo Descifrar"), font=("Helvetica", 25),
                                           text="Descifrar Imagen", width=230, height=80, command=desencriptar, compound='left')
desencriptar_btn.place(x=0, y=100)

limpiar_desencriptar_btn = customtkinter.CTkButton(master=tabview.tab("Modo Descifrar"), font=("Helvetica", 25),
                                                 text="Limpiar todo", width=230, height=80, command=limpiar_imagenes_desencriptar, compound='left')
limpiar_desencriptar_btn.place(x=0, y=200)

# LOADING VA ACA
if (MOSTRAME_EL_LOADING_EN_LA_GUI is True):
    loading = customtkinter.CTkLabel(text='laburando', font=("Helvetica", 25), width=230, height=80, compound='left', master=app)
    loading.place(x=500, y=400)

app.mainloop()

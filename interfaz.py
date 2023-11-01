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
        progressbar.set(0)

def limpiar_imagenes_desencriptar():
    if imagen.get_img_normal_desencriptar() != "" and imagen.get_img_desencriptada() != "":
        for i in range(2, 4):
            label_array[i].destroy()
        progressbar.set(0)

# Funciones para encriptar y desencriptar
def encriptar():
    global MOSTRAME_EL_LOADING_EN_LA_GUI
    MOSTRAME_EL_LOADING_EN_LA_GUI = True
    if imagen.get_img_normal_encriptar() != "":
        imagen.encriptar_imagen()
        agregar_imagen(imagen.get_img_encriptada(), "Modo Cifrar", 700, 0, 1)
        agregar_imagen(imagen.get_img_encriptada(), "Modo Descifrar", 250, 0, 2)
        valor_de_progreso = 100  # Aquí deberías calcular el progreso real
        progressbar.set(valor_de_progreso)  # Actualiza el valor de la ProgressBar

def desencriptar():
    if imagen.get_img_normal_desencriptar() != "":
        imagen.desencriptar_imagen()
        agregar_imagen(imagen.get_img_desencriptada(), "Modo Descifrar", 700, 0, 3)
        valor_de_progreso = 100  # Aquí deberías calcular el progreso real
        progressbar.set(valor_de_progreso)  # Actualiza el valor de la ProgressBar

customtkinter.set_appearance_mode("Dark")
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

#Ventanas superiores
tabview.add("Modo Cifrar")
tabview.add("Modo Descifrar")

#Seteamos la view por defecto
tabview.set("Modo Cifrar")

# Botones y acciones
cargar_imagen_encriptar_btn = customtkinter.CTkButton(master=tabview.tab("Modo Cifrar"), font=("Helvetica", 25),
                                                     text="Cargar Imagen", width=230, height=80, command=cargar_imagen_a_encriptar, compound='left')
cargar_imagen_encriptar_btn.place(x=0, y=200)

encriptar_btn = customtkinter.CTkButton(master=tabview.tab("Modo Cifrar"), font=("Helvetica", 25),
                                       text="Cifrar Imagen", width=230, height=80, command=encriptar, compound='left')
encriptar_btn.place(x=0, y=300)

limpiar_encriptar_btn = customtkinter.CTkButton(master=tabview.tab("Modo Cifrar"), font=("Helvetica", 25),
                                               text="Limpiar todo", width=230, height=80, command=limpiar_imagenes_encriptar, compound='left')
limpiar_encriptar_btn.place(x=0, y=400)

#Label

label = customtkinter.CTkLabel(master=app,
                               text="Estado",
                               width=150,
                               height=50,
                               corner_radius=8,font=("Helvetica", 25))
label.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)


# Agrega la ProgressBar en el lugar adecuado en la interfaz
progressbar = customtkinter.CTkProgressBar(master=app, width=160, height=20, border_width=5,progress_color="Green",bg_color="Green")
progressbar.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
progressbar.set(0)

cargar_imagen_desencriptar_btn = customtkinter.CTkButton(master=tabview.tab("Modo Descifrar"), font=("Helvetica", 25),
                                                       text="Cargar Imagen", width=230, height=80, command=cargar_imagen_a_desencriptar, compound='left')
cargar_imagen_desencriptar_btn.place(x=0, y=200)

desencriptar_btn = customtkinter.CTkButton(master=tabview.tab("Modo Descifrar"), font=("Helvetica", 25),
                                           text="Descifrar Imagen", width=230, height=80, command=desencriptar, compound='left')
desencriptar_btn.place(x=0, y=300)

limpiar_desencriptar_btn = customtkinter.CTkButton(master=tabview.tab("Modo Descifrar"), font=("Helvetica", 25),
                                                 text="Limpiar todo", width=230, height=80, command=limpiar_imagenes_desencriptar, compound='left')
limpiar_desencriptar_btn.place(x=0, y=400)


app.mainloop()

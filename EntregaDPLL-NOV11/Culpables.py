#-*-coding: utf-8-*-
# Alejandra Campo y Nicolas Duque, Octubre 2018

# Visualizacion del problema "¿Quién es el culpable?"

# Formato de la entrada: - las letras proposionales seran: 5, 6, 7, 8, 9;
#                        - la negación de n es "-n"  
#                        - solo se aceptan literales

# Salida: archivo culpables_%i.png, donde %i es un numero natural

# python Culpables.py Culpables.csv

def dibujar_tablero(f, n):
    # Visualiza un tablero dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step = 1./6

    tangulos = []
    # Creo los cuadrados claros en el tablero
    tangulos.append(patches.Rectangle(*[(0, 0), 3 * step, 3 * step],\
            facecolor='white'))
    tangulos.append(patches.Rectangle(*[(3 * step, 0), 3 * step, 3 * step],\
            facecolor='white'))
    tangulos.append(patches.Rectangle(*[(0, 3 * step), 2 * step, 3 * step],\
            facecolor='white'))
    tangulos.append(patches.Rectangle(*[(2 * step, 3 * step), 2 * step, 3 * step],\
            facecolor='white'))
    tangulos.append(patches.Rectangle(*[(4 * step, 3 * step), 2 * step, 3 * step],\
            facecolor='white'))

    # Creo las lineas del tablero
    tangulos.append(patches.Rectangle(*[(3 * step, 0), 0.005, 3 * step],\
            facecolor='black'))
      
    tangulos.append(patches.Rectangle(*[(0, 3 * step), 1, 0.005],\
            facecolor='black'))
      
    tangulos.append(patches.Rectangle(*[(2 * step, 3 * step), 0.005, 3 * step],\
            facecolor='black'))
      
    tangulos.append(patches.Rectangle(*[(4 * step, 3 * step), 0.005, 3 * step],\
            facecolor='black'))


    for t in tangulos:
        axes.add_patch(t)

    # Cargando las imagenes de los presuntos culpables
    arr_img = plt.imread("Ernesto.png", format='png')
    imagebox1 = OffsetImage(arr_img, zoom=0.178)
    imagebox1.image.axes = axes

    arr_img = plt.imread("Deductor.png", format='png')
    imagebox2 = OffsetImage(arr_img, zoom=0.089)
    imagebox2.image.axes = axes

    arr_img = plt.imread("Berticio.png", format='png')
    imagebox3 = OffsetImage(arr_img, zoom=0.089)
    imagebox3.image.axes = axes

    arr_img = plt.imread("Armando.png", format='png')
    imagebox4 = OffsetImage(arr_img, zoom=0.089)
    imagebox4.image.axes = axes

    arr_img = plt.imread("Carnicero.png", format='png')
    imagebox5 = OffsetImage(arr_img, zoom=0.08)
    imagebox5.image.axes = axes

    arr_img = plt.imread("EQUIS.png", format='png')
    imagebox = OffsetImage(arr_img, zoom=0.08)
    imagebox.image.axes = axes

    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[0] = [0, 0]
    direcciones[1] = [0, 0]
    direcciones[2] = [0, 0]
    direcciones[3] = [0, 0]
    direcciones[4] = [0, 0]

    # Direcciones de los personajes
    direcciones[5] = [0.165, 0.745]
    direcciones[6] = [0.5, 0.745]
    direcciones[7] = [0.835, 0.745]
    direcciones[8] = [0.255, 0.25]
    direcciones[9] = [0.745, 0.25]
    
    # Añadiendo los presuntos culpables
    Ernesto = AnnotationBbox(imagebox1, direcciones[5], frameon=False)
    axes.add_artist(Ernesto)

    Deductor = AnnotationBbox(imagebox2, direcciones[6], frameon=False)
    axes.add_artist(Deductor)
    
    Berticio = AnnotationBbox(imagebox3, direcciones[7], frameon=False)
    axes.add_artist(Berticio)
    
    Armando = AnnotationBbox(imagebox4, direcciones[8], frameon=False)
    axes.add_artist(Armando)

    Carnicero = AnnotationBbox(imagebox5, direcciones[9], frameon=False)
    axes.add_artist(Carnicero)

    ## Determinando los culpables con EQUIS
    for l in f:
        if "-" not in l:
            ab = AnnotationBbox(imagebox, direcciones[int(l)], frameon=False)
            axes.add_artist(ab)

    # plt.show()
    fig.savefig("culpables_" + str(n) + ".png")


#################
# importando paquetes para dibujar
print "Importando paquetes..."
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import csv
from sys import argv
print "Listo!"

script, data_archivo = argv

with open(data_archivo) as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    contador = 1
    for l in data:
        print "Dibujando tablero:", l
        dibujar_tablero(l, contador)
        contador += 1

csv_file.close()
#-*-coding: utf-8-*-

# Alejandra Campo y Nicolas Duque, 2018
# Codigo para crear la formula del problema de los culpables

print "Importando paquetes..."
from timeit import default_timer as timer
import Tableaux as T
print "Importados!"

# Guardo el tiempo al comenzar el procedimiento
start = timer()

# Regla 1: Debe haber exactamente dos proposiciones falsas

# Creo las letras proposicionales de las afirmaciones
letrasProposicionales = []
for i in range(0, 5):
    letrasProposicionales.append(str(i))

conjunciones = '' # Para ir guardando las conjunciones de trios de disyunciones de literales
inicial = True # Para inicializar la primera conjuncion

for p in letrasProposicionales:
    aux1 = [x for x in letrasProposicionales if x != p] # Todas las letras excepto
    # print "aux1: ", aux1
    for q in aux1:
        aux2 = [x for x in aux1 if x != q] # Todas las letras excepto p y q
        # print "aux2", aux2
        for r in aux2:
            literal = r + q + p + 'Y' + 'Y'
            aux3 = [x + '-' for x in aux2 if x != r]
            for k in aux3:
                literal = k + literal + 'Y'
            # print "Literal: ", literal
            if inicial: # Inicializar la primera conjuncion
                conjunciones = literal
                inicial = False
            else:
                conjunciones = literal + conjunciones + 'O'

# Creo las letras proposicionales de los personajes en la tabla
for i in range(5, 10):
  letrasProposicionales.append(str(i))

# Regla 2: No pueden haber contradicciones en las proposiciones

conjunciones = '4-3>' + conjunciones + 'Y'
conjunciones = '1-0>' + conjunciones + 'Y'
conjunciones = '3-4>' + conjunciones + 'Y'
conjunciones = '0-1>' + conjunciones + 'Y'

# Añadiendo las letras proposicionales de los personajes en la tabla
# Aprovechando que con la regla 2 se pudo concluir que esta es siempre verdadera

conjunciones = '89Y2>' + conjunciones + 'Y'
conjunciones = '67Y2>' + conjunciones + 'Y'
conjunciones = '52>' + conjunciones + 'Y'

# Regla 3: Hacer caso a las proposiciones. Ej: Si Armando es culpable, EQUIS sobre Armando

conjunciones = '8-0>' + conjunciones + 'Y'
conjunciones = '80->' + conjunciones + 'Y'
conjunciones = '81>' + conjunciones + 'Y'
conjunciones = '8-1->' + conjunciones + 'Y'
conjunciones = '5-2>' + conjunciones + 'Y'
conjunciones = '52->' + conjunciones + 'Y'
conjunciones = '93>' + conjunciones + 'Y'
conjunciones = '9-3->' + conjunciones + 'Y'
conjunciones = '9-4>' + conjunciones + 'Y'
conjunciones = '94->' + conjunciones + 'Y'

# Creo la formula como objeto

A = T.StringtoTree(conjunciones, letrasProposicionales)
print "Formula: ", T.Inorder(A)

lista_hojas = [[A]] # Inicializa la lista de hojas

OK = '' # El tableau regresa Satisfacible o Insatisfacible
interpretaciones = [] # lista de lista de literales que hacen verdadera lista_hojas

OK, INTS = T.Tableaux(lista_hojas, letrasProposicionales)

print "Tableau terminado!"
# Guardo el tiempo al terminar el procedimiento
end = timer()
print u"El procedimiento demoró: ", end - start

if OK == 'Satisfacible':
    if len(INTS) == 0:
        print u"Error: la lista de interpretaciones está vacía"
    else:
        print "Guardando interpretaciones en archivo..."
        import csv
        archivo = 'tableros_automatico.csv'
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(INTS)

        print "Interpretaciones guardadas en " + archivo

        import Culpables as C
        contador = 1
        for i in INTS:
            print "Trabajando con literales: ", i
            C.dibujar_tablero(i,contador)
            contador += 1

print "FIN"
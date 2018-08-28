#Creacion de la clase Tree
class Tree(object):
    def __init__(self,l,iz,der):
        self.left = iz
        self.right = der
        self.label = l
        
#Funcion recursiva que convierte los objectos Tree en formulas
def Inorder(f):
    if f.right == None:
        print f.label,
    elif f.label == '-':
        print f.label,
        Inorder(f.right)
    else:
        print "(",
        Inorder(f.left),
        print f.label,
        Inorder(f.right)
        print ")",

#Muestra las posibles interpretaciones tomando a p, q y r como los atomos
letrasProposicionales = ['p', 'q', 'r']
interps = []
aux = {}

for a in letrasProposicionales:
    aux[a] = 1

interps.append(aux)

for a in letrasProposicionales:
    interps_aux =  [i for i in interps]

    for i in interps_aux:
        aux1 = {}

        for b in letrasProposicionales:
            if a == b:
                aux1[b] = 1 - i[b]
            else:
                aux1[b] = i[b]

        interps.append(aux1)

print 'Interpretaciones: '
for i in interps:
    print i

#Funcion que convierte de notacion polaca invertida a arboles
def Pol_Tree():
    f = raw_input('Ingrese una cadena: ') or 'rqpO>' 
    #print "Cadena ingresada " + f
    cadena = list(f)
    #print cadena

    letrasProposicionales = ['p', 'q', 'r', 's', 't', 'v']
    conectivos = ['O', 'Y', '>']
    pila = [] # inicializamos la pila

    for c in cadena:
        if c in letrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c == '-':
            aux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(aux)
        elif c in conectivos:
            aux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(aux)
    formula = pila[-1]

    print "La formula ",
    Inorder(formula)
    print "fue creada como un objeto!"
    return formula

#Funcion que indica el valor de verdad de una formula que esta como Tree
def VI(f):
    if f.right == None:
        return i[f.label]
    elif f.label == '-':
        if VI(f.right) == 1:
            return 0
        else:
            return 1
    elif f.label == 'Y':
        if (VI(f.left) == 1 and VI(f.right) == 1):
            return 1
        else:
            return 0

    elif f.label == 'O':
        if (VI(f.left) == 1 or VI(f.right) == 1):
            return 1
        else:
            return 0
    elif f.label == '>':
        if (VI(f.left) == 0 or VI(f.right) == 1):
            return 1
        else:
            return 0
    elif f.label == '<->':
        if(VI(f.left) == VI(f.right)):
            return 1
        else:
            return 0

#Lista en la que se almacenara los posibles valores de verdad que puede tomar la primer formula
#Coversion de notacion polaca invertida a formula de la primer formula
interpsForm1 = []
Form1 = Pol_Tree()

#Lista en la que se almacenara los posibles valores de verdad que puede tomar la segunda formula
#Coversion de notacion polaca invertida a formula de la segunda formula
interpsForm2 = []
Form2 = Pol_Tree()

for i in interps:
	interpsForm1.append(VI(Form1))

print "Los valores de verdad de la primer fórmula son:", interpsForm1

for i in interps:
	interpsForm2.append(VI(Form2))

print "Los valores de verdad de la segunda fórmula son:", interpsForm2

review = True
#Verificacion indice por indice de los valores de verdad.
for i in interpsForm1:
	if interpsForm1[i] == interpsForm2[i]:
		i = i + 1
		review = True
	else:
		print "Note que los valores de verdad no son los mismo, por lo tanto, no es una tautología"
		review = False
		break

if(review == True):
	print "Note que los valores de verdad son los mismos uno a uno, por lo tanto, es una tautología"

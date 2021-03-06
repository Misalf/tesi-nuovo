import numpy as np
import openpyxl

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

AMMINOACIDI=['MET', 'LYS', 'PRO', 'THR', 'VAL', 'ALA', 'ASN', 'GLU', 'PRO', 'TYR','ARG']
ALFABETO=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def INIZIALIZZAMATRICE(matrice):
    r=0
    for row in matrice:          
        c=0
        #RigMAX=r
        #print (RigMAX)
        for cell in row:
            matriceinizializzata=[[0 for x in range(r+1)] for y in range(c+1)]
            #print ("Stampo la matriceproteinacodificata ",matriceproteinacodificata[c][r]," di colonna ",c," e riga ",r)
            #print (c,',',r)
            c=c+1
        r=r+1
    return matriceinizializzata

def INIZIALIZZOARRAY(array):
    r=0
    for row in array:
        arrayoutput=[[0 for x in range(r+1)] for y in range(1)]
        #arrayoutput[r]=row[0].value             #AGGIUNGO I VALORI DA EXCEL NELLA MATRICE
        r=r+1   
    return arrayoutput

def CODIFICAMATRICE(matrice, matriceproteinacodificata):
    r=0                        
    for row in matrice:
        c=0
        for cell in row:
            if c==0:
                matriceproteinacodificata[0][r]=AMMINOACIDI.index(cell.value) #CODIFICA(AMMINOACIDI,cell.value)
            elif c==1:
                matriceproteinacodificata[1][r]=ALFABETO.index(cell.value) #CODIFICA(ALFABETO,cell.value)
            elif c==2:
                matriceproteinacodificata[2][r]=ALFABETO.index(cell.value) #CODIFICA(ALFABETO,cell.value)
            elif c==3:
                matriceproteinacodificata[3][r]=cell.value
            elif c==4:
                matriceproteinacodificata[4][r]=AMMINOACIDI.index(cell.value) #CODIFICA(AMMINOACIDI,cell.value)
            elif c==5:
                matriceproteinacodificata[5][r]=ALFABETO.index(cell.value) #CODIFICA(ALFABETO,cell.value)
            elif c==6:
                matriceproteinacodificata[6][r]=ALFABETO.index(cell.value) #CODIFICA(ALFABETO,cell.value)
            elif c==7:
                matriceproteinacodificata[7][r]=cell.value
            c=c+1
        r=r+1
    return matriceproteinacodificata

def CODIFICAARRAY(array, arrayoutput):
    r=0
    for row in array:
        arrayoutput[0][r]=row[0].value             #AGGIUNGO I VALORI DA EXCEL NELLA MATRICE
        r=r+1
    return arrayoutput

#matrice input
FirstInput = openpyxl.load_workbook('first.xlsx')
sheet=FirstInput.active

inputexcel = sheet['B2':'I15']
outputexcel=sheet['J2':'J15']
inputprova=sheet['B16':'I30']
outputprova=sheet['J16':'J30']

print("Inizializzo matrici...")
MatriceInputTraining=INIZIALIZZAMATRICE(inputexcel)
MatriceInputProva=INIZIALIZZAMATRICE(inputprova)
ArrayOutputTraining=INIZIALIZZOARRAY(outputexcel)
ArrayOutputProva=INIZIALIZZOARRAY(outputprova)

print("Codifico matrici...")
MatriceCodificataTraining=CODIFICAMATRICE(inputexcel, MatriceInputTraining)
MatriceCodificataProva=CODIFICAMATRICE(inputprova, MatriceInputProva)
ArrayCodificatoTraining=CODIFICAARRAY(outputexcel, ArrayOutputTraining)
ArrayCodificatoProva=CODIFICAARRAY(outputprova, ArrayOutputProva)

#INIZIALIZZA LA MATRICE
#r=0
#for row in inputexcel:          
#    c=0
#    RigMAX=r
#    #print (RigMAX)
#    for cell in row:
#        matriceproteinacodificata=[[0 for x in range(r+1)] for y in range(c+1)]
 #       #print ("Stampo la matriceproteinacodificata ",matriceproteinacodificata[c][r]," di colonna ",c," e riga ",r)
#        #print (c,',',r)
#        c=c+1
#    r=r+1

#INSERISCO I VALORI DI OUTPUT DA EXCEL IN UN ARRAY DI OUTPUT
#INIZIALIZZO ARRAY OUTPUT
#r=0
#for row in outputexcel:
#    arrayoutput=[[0 for x in range(r+1)] for y in range(1)]
#    #arrayoutput[r]=row[0].value             #AGGIUNGO I VALORI DA EXCEL NELLA MATRICE
#    r=r+1
#r=0
#for row in outputexcel:
#    arrayoutput[0][r]=row[0].value             #AGGIUNGO I VALORI DA EXCEL NELLA MATRICE
#    #print (arrayoutput[r] ,',', r)
#    r=r+1
#INSERISCE NELLA MATRICE I VALORI CODIFICATI
#######print("INIZIO CODIFICA")
#r=0                        
#for row in inputexcel:
#    c=0
#    for cell in row:
#        if c==0:
#            matriceproteinacodificata[0][r]=AMMINOACIDI.index(cell.value) #CODIFICA(AMMINOACIDI,cell.value)
#        elif c==1:
#            matriceproteinacodificata[1][r]=ALFABETO.index(cell.value) #CODIFICA(ALFABETO,cell.value)
#        elif c==2:
#            matriceproteinacodificata[2][r]=ALFABETO.index(cell.value) #CODIFICA(ALFABETO,cell.value)
#        elif c==3:
##            matriceproteinacodificata[3][r]=cell.value
#        elif c==4:
#            matriceproteinacodificata[4][r]=AMMINOACIDI.index(cell.value) #CODIFICA(AMMINOACIDI,cell.value)
#        elif c==5:
#            matriceproteinacodificata[5][r]=ALFABETO.index(cell.value) #CODIFICA(ALFABETO,cell.value)
#        elif c==6:
#            matriceproteinacodificata[6][r]=ALFABETO.index(cell.value) #CODIFICA(ALFABETO,cell.value)
#        elif c==7:
#            matriceproteinacodificata[7][r]=cell.value
#        c=c+1
#    r=r+1
    #if r==RigMAX:
      #  break

#########print ("INIZIO MATRICE CODIFICATA")
#ri,ci=0,0
#for row in range(0,r-1):
#    for cell in range(0,c-1):
        #print (matriceproteinacodificata[cell][row])

X=np.array(MatriceCodificataTraining).T
Y=np.array(ArrayCodificatoTraining).T
Xprova=np.array(MatriceCodificataProva)
Yprova=np.array(ArrayCodificatoProva)

#SI INIZIA A COPIARE
np.random.seed(1)

#INIZIALIZZO I PESI CASUALMENTE CON MEDIA 0
syn0 = 2*np.random.random((8,1)) - 1

for iter in range(10000):
    #forward propagation
    p0=X
    p1=nonlin(np.dot(p0,syn0))

    #quanto è l'errore?
    p1_errore=p1-Y

    #moltiplica quanto abbiamo sbagliato per la derivata della sigmoide al valore in p1
    p1_delta=p1_errore*nonlin(p1,True)

    #aggiorna i pesi
    #syn0=syn0.T
    syn0+=np.dot(p0.T,p1_delta)

print ("Output dopo allenamento:")
print (p1)
print("Prova!")
OutputCalcolato=np.dot(Xprova.T,syn0)
print(OutputCalcolato)

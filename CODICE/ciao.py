import numpy as np
import openpyxl

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

def CODIFICA(ARRAY,INP):
    i=0
    for CONT in ARRAY:
        if INP==CONT:
            return i
        i=i+1

AMMINOACIDI=[] #<------ METTI QUA GLI AMMINOACIDI 
ALFABETO=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]


#matrice input
FirstInput = openpyxl.load_workbook('first.xlsx')
sheet=FirstInput.active
#sheet=FirstInput.get_sheet_names()
#importo matrice input
inputexcel = sheet['B2':'I30']
r, c=0,0
for row in inputexcel:
    for cell in row:
        matriceproteina=[[0 for x in range(r+1)] for y in range(c+1)]
        matriceproteinacodificata=[[0 for x in range(r+1)] for y in range(c+1)]
        matriceproteina[r][c]=cell.value
        if c==0:
            matriceproteinacoficata[r][0]=CODIFICA(AMMINOACIDI,cell.value)
        if c==1 or c==2:
            matriceproteinacodificata[r][1]=CODIFICA(ALFABETO,cell.value)
            matriceproteinacodificata[r][2]=CODIFICA(ALFABETO,cell.value)
            
        print (matriceproteina[r][c]) #<-- ricorda di toglierlo
        r,c=r+1,c+1
print ("INIZIO MATRICE CODIFICATA")
r,c=0,0
for row in matriceproteinacodificata:
    for cell in row:
        print (matriceproteinacodificata[r][c])
        r,c=r+1,c+1


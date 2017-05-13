import numpy as np
import openpyxl

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

def CODIFICA(ARRAY,INP):
    print (ARRAY.index(INP))
    return ARRAY.index(INP)
#    i=0
#    for CONT in ARRAY:
#        if INP==CONT:
#            print ("ciao misa") 
#            return i
#        else:
#            i=i+1

AMMINOACIDI=['MET', 'LYS', 'PRO', 'THR', 'VAL', 'ALA', 'ASN', 'GLU', 'PRO', 'TYR','ARG']
ALFABETO=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#matrice input
FirstInput = openpyxl.load_workbook('first.xlsx')
sheet=FirstInput.active
#sheet=FirstInput.get_sheet_names()
#importo matrice input
inputexcel = sheet['B2':'I30']
#col_range=sheet['B:I']
#print (inputexcel)


r=0
for row in inputexcel:          #CREA LA MATRICE CON TUTTI
    c=0
    RigMAX=r
    #print (RigMAX)
    for cell in row:
        matriceproteinacodificata=[[0 for x in range(r+1)] for y in range(c+1)]
        print ("Stampo la matriceproteinacodificata ",matriceproteinacodificata[c][r]," di colonna ",c," e riga ",r)
        print (c,',',r)
        c=c+1
    r=r+1
print("INIZIO CODIFICA")
r=0                        #INSERISCE NELLA MATRICE I VALORI CODIFICATI

#print("Stampa:",matriceproteinacodificata[7][0])
for row in inputexcel:
    c=0
    for cell in row:
        print (c,',',r)
        if c==0:
            matriceproteinacodificata[0][r]=AMMINOACIDI.index(cell.value) #CODIFICA(AMMINOACIDI,cell.value)
            #print (AMMINOACIDI.index(cell.value))
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
        #print (matriceproteinacodificata[r][c]) #<— ricorda di toglierlo
        c=c+1
    print("CIAO")
    r=r+1
    if r==RigMAX:
        print("Esco dalla CODIFICA")
        break

print ("INIZIO MATRICE CODIFICATA")
ri,ci=0,0
for row in range(0,r-1):
    for cell in range(0,c-1):
        print (matriceproteinacodificata[cell][row])
        #print (row ,",", cell)
        #ci=ci+1
    #ri=ri+1

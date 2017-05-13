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

AMMINOACIDI=['MET', 'LYS', 'PRO', 'THR', 'VAL', 'ALA', 'ASN', 'GLU', 'PRO', 'TYR']
ALFABETO=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#matrice input
FirstInput = openpyxl.load_workbook('first.xlsx')
sheet=FirstInput.active
#sheet=FirstInput.get_sheet_names()
#importo matrice input
inputexcel = sheet['B2':'I30']
#col_range = sheet['B:I']        #<----RICORDA DI MODIFICARE QUESTI INTERVALLI PER ALTRE TABELLE
#rig_range = sheet['2:30']       #<----RICORDA DI MODIFICARE QUESTI INTERVALLI PER ALTRE TABELLE
#matriceproteina=[[0 for x in range(rig_range)] for y in range(col_range)]
#matriceproteinacodificata=[[0 for x in range(rig_range)] for y in range(col_range)]
r, c=0,0
for row in inputexcel:
    for cell in row:
        #matriceproteina=[[0 for x in range(r+1)] for y in range(c+1)]
        matriceproteinacodificata=[[0 for x in range(r)] for y in range(c)]
        r,c=r+1,c+1
        #matriceproteina[r][c]=cell.value
        #print (cell.value)
r, c=0,0
for row in inputexcel:
    for cell in row:
        if c==0:
            matriceproteinacodificata[r][0]=AMMINOACIDI.index(cell.value) #CODIFICA(AMMINOACIDI,cell.value)
            #print (AMMINOACIDI.index(cell.value))
        if c==1:
            matriceproteinacodificata[r][1]=ALFABETO.index(cell.value) #CODIFICA(ALFABETO,cell.value)
        if c==2:
            matriceproteinacodificata[r][2]=ALFABETO.index(cell.value) #CODIFICA(ALFABETO,cell.value)
        if c==3:
            matriceproteinacodificata[r][3]=cell.value
        if c==4:
            matriceproteinacodificata[r][4]=AMMINOACIDI.index(cell.value) #CODIFICA(AMMINOACIDI,cell.value)
        if c==5:
            matriceproteinacodificata[r][5]=ALFABETO.index(cell.value) #CODIFICA(ALFABETO,cell.value)
        if c==6:
            matriceproteinacodificata[r][6]=ALFABETO.index(cell.value) #CODIFICA(ALFABETO,cell.value)
        if c==7:
            matriceproteinacodificata[r][7]=cell.value
        print (matriceproteinacodificata[r][c]) #<— ricorda di toglierlo
        c=c+1
    r=r+1
print ("INIZIO MATRICE CODIFICATA")
ri,ci=0,0
for row in range(0,r):
    for cell in range(0,c):
        print (matriceproteinacodificata[row][cell])
        #print (row ,",", cell)
        #ci=ci+1
    #ri=ri+1

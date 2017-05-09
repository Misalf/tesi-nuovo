import numpy as np
import openpyxl

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

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
        matriceproteina[r][c]=cell.value
        print (matriceproteina[r][c]) #<-- ricorda di toglierlo
        r,c=r+1,c+1
        


import pandas as pd 
datos = (11, 12, 13, 14, 15, 16)
indice = ["A", "B", "C", "D", "E", "F"]

pf = pd.Series(data=datos, index=indice)

print (pf)

pf = pf.reindex(index=["C","B", "A", "D", "E", "F"])

print (pf)

frutas = ["Manzana", "Platano", "Pera", "Sandia", "Uvas", "Piña", "Guayaba"]
fila = [1,2,3,4,5,6,7]

pff = pd.Series(index= fila, data= frutas)
print (pff)

pff = pff.reindex(index = [3,4,5,6,7,1,2])
print (pff)
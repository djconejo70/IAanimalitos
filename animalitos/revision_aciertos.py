import pandas as pd
from datetime import datetime
from home.extraccion_tuazar import*






datos=datos_excel()
dato1=datos[0]
dato2=datos[1]    
contador_aciertos=0

dato1=str(dato1)
dato2=str(dato2)
contador_aciertos=0
temporal_loto=capture_temporal_loto()
for animalitos in temporal_loto:
    if dato1==animalitos:
        contador_aciertos=contador_aciertos+1
    if dato2==animalitos:
        contador_aciertos=contador_aciertos+1
temporal_granja=capture_temp_granja()
for animalitos in temporal_granja:
    if dato1==animalitos:
        contador_aciertos=contador_aciertos+1
    if dato2==animalitos:
        contador_aciertos=contador_aciertos+1    
dia_semana=(datetime.today().weekday())
if dia_semana==0:
    acumulador_aciertos=contador_aciertos
else:
    acumulador_aciertos1=open("D:/ia_animalitos/animalitos/acumulador_aciertos_semana.txt","r")
    acumulador_aciertos=acumulador_aciertos1.read()
    acumulador_aciertos1.close()
    if acumulador_aciertos=="0":
        acumulador_aciertos=contador_aciertos
        
    else:
        acumulador_aciertos=int(acumulador_aciertos)+contador_aciertos
    
f1 = open("D:/ia_animalitos/animalitos/acumulador_aciertos_semana.txt", "w")
acumulador=str(acumulador_aciertos)
f1.write(acumulador)
f1.close()    
numero_datos=0    
numero=pd.read_excel('D:/ia_animalitos/animalitos/numero_indicaciones_semana.xlsx', header=None, names=['Numero']) 
df = pd.DataFrame(numero)
lista1 = df['Numero'].tolist()
acumulador=lista1[0]
if rv==rvb:
    numero_datos=numero_datos+1
else:
    numero_datos=numero_datos+2    
dia_semana=(datetime.today().weekday())
if dia_semana==0:
    acumulador=0

acumulador=acumulador+numero_datos
   
numero= numero.iloc[:0]
lista=[]
lista.append(acumulador)
numero=pd.DataFrame(lista)
numero.to_excel('D:/ia_animalitos/animalitos/numero_indicaciones_semana.xlsx', index=None)



def revision_aciertos_miercoles(dato1, dato2):
    datos=pd.read_excel('D:/ia_animalitos/animalitos/resultados_miercoles_loto.xlsx', header=None, names=['Numero'])
    df = pd.DataFrame(datos)
    lista_miercoles_loto = df['Numero'].tolist()
    ca=0
    for animalitos in lista_miercoles_loto:
        if dato1==animalitos:
            ca=ca+1
        if dato2==animalitos:
            ca=ca+1
    datos=pd.read_excel('D:/ia_animalitos/animalitos/resultados_miercoles_granja.xlsx', header=None, names=['Numero'])   
    df = pd.DataFrame(datos)
    lista_miercoles_granja = df['Numero'].tolist()
    ca=0
    for animalitos in lista_miercoles_granja:
        if dato1==animalitos:
            ca=ca+1
        if dato2==animalitos:
            ca=ca+1    
    return(ca)

def revision_aciertos_jueves(dato1, dato2):
    datos=pd.read_excel('D:/ia_animalitos/animalitos/resultados_jueves_loto.xlsx', header=None, names=['Numero'])
    df = pd.DataFrame(datos)
    lista_jueves_loto = df['Numero'].tolist()
    ca=0
    for animalitos in lista_jueves_loto:
        if dato1==animalitos:
            ca=ca+1
        if dato2==animalitos:
            ca=ca+1
    datos=pd.read_excel('D:/ia_animalitos/animalitos/resultados_jueves_granja.xlsx', header=None, names=['Numero'])   
    df = pd.DataFrame(datos)
    lista_jueves_granja = df['Numero'].tolist()
    ca=0
    for animalitos in lista_jueves_granja:
        if dato1==animalitos:
            ca=ca+1
        if dato2==animalitos:
            ca=ca+1    
    return(ca)

def revision_aciertos_viernes(dato1, dato2):
    datos=pd.read_excel('D:/ia_animalitos/animalitos/resultados_jueves_loto.xlsx', header=None, names=['Numero'])
    df = pd.DataFrame(datos)
    lista_viernes_loto = df['Numero'].tolist()
    ca=0
    for animalitos in lista_viernes_loto:
        if dato1==animalitos:
            ca=ca+1
        if dato2==animalitos:
            ca=ca+1
    datos=pd.read_excel('D:/ia_animalitos/animalitos/resultados_viernes_granja.xlsx', header=None, names=['Numero'])   
    df = pd.DataFrame(datos)
    lista_viernes_granja = df['Numero'].tolist()
    ca=0
    for animalitos in lista_viernes_granja:
        if dato1==animalitos:
            ca=ca+1
        if dato2==animalitos:
            ca=ca+1    
    return(ca)

def revision_aciertos_sabado(dato1, dato2):
    datos=pd.read_excel('D:/ia_animalitos/animalitos/resultados_sabado_loto.xlsx', header=None, names=['Numero'])
    df = pd.DataFrame(datos)
    lista_sabado_loto = df['Numero'].tolist()
    ca=0
    for animalitos in lista_sabado_loto:
        if dato1==animalitos:
            ca=ca+1
        if dato2==animalitos:
            ca=ca+1
    datos=pd.read_excel('D:/ia_animalitos/animalitos/resultados_sabado.xlsx', header=None, names=['Numero'])   
    df = pd.DataFrame(datos)
    lista_sabado_granja = df['Numero'].tolist()
    ca=0
    for animalitos in lista_sabado_granja:
        if dato1==animalitos:
            ca=ca+1
        if dato2==animalitos:
            ca=ca+1    
    return(ca)

    
    
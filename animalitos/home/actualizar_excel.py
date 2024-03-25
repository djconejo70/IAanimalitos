import requests 
from bs4 import BeautifulSoup
import re
import pandas as pd
from collections import Counter




def capture_resultados():
    datos=pd.read_excel('D:/Licoreria/licoreria/lotoactivo.xlsx', header=None)
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")
    resultado_loto=[]
    resultado_loto_numerico=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>12 and c<24):
            resultado_loto.append(x.text.strip())
    for animales in resultado_loto:   
        resultado_loto_numerico.append(re.findall('\d+', animales))
    lista=[]   
    for valores in resultado_loto_numerico:
        for numeros in valores:
            lista.append(numeros)    
    df=pd.DataFrame(lista)
    a=pd.concat([datos, df], axis=0)
    a.to_excel('lotoactivo.xlsx', sheet_name='Hoja1', index=None)
    return ()


def capture_granja():
    datos=pd.read_excel('D:/ia_animalitos/animalitos/lotoactivo.xlsx', header=None)
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")    
    resultado_granja=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>23 and c<36):
            resultado_granja.append(x.text.strip())  

    datos_granja=pd.read_excel('D:/ia_animalitos/animalitos/Granja.xlsx', header=None)
    resultado_granja_numerico=[]
    for animales in resultado_granja:   
        resultado_granja_numerico.append(re.findall('\d+', animales))
    lista_granja=[]   
    for valores in resultado_granja_numerico:
        for numeros in valores:
            lista_granja.append(numeros)    
    df=pd.DataFrame(lista_granja)
    a=pd.concat([datos_granja, df], axis=0)
    a.to_excel('Granja.xlsx', sheet_name='Hoja1', index=None)
    return ()

def mantenimiento_loto():
    datos=pd.read_excel('D:/ia_animalitos/animalitos/lotoactivo.xlsx', header=None) 
    a=datos.count()
    # print(datos)
    c=int(a[0])
    
    if c > 660:
        b=c-660        
        datos= datos.iloc[b:]
        
    datos.to_excel('D:/ia_animalitos/animalitos/lotoactivo.xlsx', sheet_name='Hoja1', index=None)
    return()
def mantenimiento_granja():
    datos=pd.read_excel('D:/ia_animalitos/animalitos/Granja.xlsx', header=None) 
    a=datos.count()
    # print(datos)
    c=int(a[0])
    
    if c > 660:
        b=c-720        
        datos= datos.iloc[b:]
        
    datos.to_excel('D:/ia_animalitos/animalitos/Granja.xlsx', sheet_name='Hoja1', index=None)
    return() 

capture_resultados()
capture_granja()
mantenimiento_loto()
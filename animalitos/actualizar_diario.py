import pandas as pd
import requests 
from bs4 import BeautifulSoup
import re
from datetime import datetime


##################### Lunes Loto
def mantenimiento_lunes_loto():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_lunes_loto.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_lunes_loto.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_lunes_loto():
    
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")
    resultado_loto=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>12 and c<24):
            resultado_loto.append(x.text.strip())            
    resultado_loto_numerico=[]
    for animales in resultado_loto:   
        resultado_loto_numerico.append(re.findall('\d+', animales))
    lista_loto=[]   
    for valores in resultado_loto_numerico:
        for numeros in valores:
            lista_loto.append(numeros)
    df=pd.DataFrame(lista_loto)
    df.to_excel('D:/ia_animalitos/animalitos/resultados_lunes_loto.xlsx', sheet_name='Hoja1', index=None)
    return ()




#############################     Martes loto

def mantenimiento_martes_loto():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_martes_loto.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_martes_loto.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_martes_loto():
    
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")
    resultado_loto=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>12 and c<24):
            resultado_loto.append(x.text.strip())            
    resultado_loto_numerico=[]
    for animales in resultado_loto:   
        resultado_loto_numerico.append(re.findall('\d+', animales))
    lista_loto=[]   
    for valores in resultado_loto_numerico:
        for numeros in valores:
            lista_loto.append(numeros)
    df=pd.DataFrame(lista_loto)
    df.to_excel('D:/ia_animalitos/animalitos/resultados_martes_loto.xlsx', sheet_name='Hoja1', index=None)
    return ()



#############################     Miercoles loto

def mantenimiento_miercoles_loto():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_miercoles_loto.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_miercoles_loto.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_miercoles_loto():
    
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")
    resultado_loto=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>12 and c<24):
            resultado_loto.append(x.text.strip())            
    resultado_loto_numerico=[]
    for animales in resultado_loto:   
        resultado_loto_numerico.append(re.findall('\d+', animales))
    lista_loto=[]   
    for valores in resultado_loto_numerico:
        for numeros in valores:
            lista_loto.append(numeros)
    df=pd.DataFrame(lista_loto)
    df.to_excel('D:/ia_animalitos/animalitos/resultados_miercoles_loto.xlsx', sheet_name='Hoja1', index=None)
    return ()



#############################     Jueves loto

def mantenimiento_jueves_loto():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_jueves_loto.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_jueves_loto.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_jueves_loto():
    
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")
    resultado_loto=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>12 and c<24):
            resultado_loto.append(x.text.strip())            
    resultado_loto_numerico=[]
    for animales in resultado_loto:   
        resultado_loto_numerico.append(re.findall('\d+', animales))
    lista_loto=[]   
    for valores in resultado_loto_numerico:
        for numeros in valores:
            lista_loto.append(numeros)
    df=pd.DataFrame(lista_loto)
    df.to_excel('D:/ia_animalitos/animalitos/resultados_jueves_loto.xlsx', sheet_name='Hoja1', index=None)
    return ()




#############################     Viernes loto

def mantenimiento_viernes_loto():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_viernes_loto.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_viernes_loto.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_viernes_loto():
    
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")
    resultado_loto=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>12 and c<24):
            resultado_loto.append(x.text.strip())            
    resultado_loto_numerico=[]
    for animales in resultado_loto:   
        resultado_loto_numerico.append(re.findall('\d+', animales))
    lista_loto=[]   
    for valores in resultado_loto_numerico:
        for numeros in valores:
            lista_loto.append(numeros)
    df=pd.DataFrame(lista_loto)
    df.to_excel('D:/ia_animalitos/animalitos/resultados_viernes_loto.xlsx', sheet_name='Hoja1', index=None)
    return ()




#############################     Sabado loto

def mantenimiento_sabado_loto():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_sabado_loto.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_sabado_loto.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_sabado_loto():
    
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")
    resultado_loto=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>12 and c<24):
            resultado_loto.append(x.text.strip())            
    resultado_loto_numerico=[]
    for animales in resultado_loto:   
        resultado_loto_numerico.append(re.findall('\d+', animales))
    lista_loto=[]   
    for valores in resultado_loto_numerico:
        for numeros in valores:
            lista_loto.append(numeros)
    df=pd.DataFrame(lista_loto)
    df.to_excel('D:/ia_animalitos/animalitos/resultados_sabado_loto.xlsx', sheet_name='Hoja1', index=None)
    return ()





#############################     Domingo loto

def mantenimiento_domingo_loto():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_domingo_loto.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_domingo_loto.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_domingo_loto():
    
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")
    resultado_loto=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>12 and c<24):
            resultado_loto.append(x.text.strip())            
    resultado_loto_numerico=[]
    for animales in resultado_loto:   
        resultado_loto_numerico.append(re.findall('\d+', animales))
    lista_loto=[]   
    for valores in resultado_loto_numerico:
        for numeros in valores:
            lista_loto.append(numeros)
    df=pd.DataFrame(lista_loto)
    df.to_excel('D:/ia_animalitos/animalitos/resultados_domingo_loto.xlsx', sheet_name='Hoja1', index=None)
    return ()








#######################################################################################################3
#######################################################################################################
#################    LA GRANJITA



#################  Lunes Granjita

def mantenimiento_lunes_granja():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_lunes_granja.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_lunes_granja.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_lunes_granja():    
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
    resultado_granja_numerico=[]
    for animales in resultado_granja:   
        resultado_granja_numerico.append(re.findall('\d+', animales))
    lista_granja=[]   
    for valores in resultado_granja_numerico:
        for numeros in valores:
            lista_granja.append(numeros)    
    df=pd.DataFrame(lista_granja)    
    df.to_excel('D:/ia_animalitos/animalitos/resultados_lunes_granja.xlsx', sheet_name='Hoja1', index=None)
    return ()


#################  Martes Granjita

def mantenimiento_martes_granja():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_martes_granja.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_martes_granja.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_martes_granja():    
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
    resultado_granja_numerico=[]
    for animales in resultado_granja:   
        resultado_granja_numerico.append(re.findall('\d+', animales))
    lista_granja=[]   
    for valores in resultado_granja_numerico:
        for numeros in valores:
            lista_granja.append(numeros)    
    df=pd.DataFrame(lista_granja)    
    df.to_excel('D:/ia_animalitos/animalitos/resultados_martes_granja.xlsx', sheet_name='Hoja1', index=None)
    return ()


#################  Miercoles Granjita

def mantenimiento_miercoles_granja():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_miercoles_granja.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_miercoles_granja.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_miercoles_granja():    
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
    resultado_granja_numerico=[]
    for animales in resultado_granja:   
        resultado_granja_numerico.append(re.findall('\d+', animales))
    lista_granja=[]   
    for valores in resultado_granja_numerico:
        for numeros in valores:
            lista_granja.append(numeros)    
    df=pd.DataFrame(lista_granja)    
    df.to_excel('D:/ia_animalitos/animalitos/resultados_miercoles_granja.xlsx', sheet_name='Hoja1', index=None)
    return ()



#################  Jueves Granjita

def mantenimiento_jueves_granja():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_jueves_granja.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_jueves_granja.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_jueves_granja():    
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
    resultado_granja_numerico=[]
    for animales in resultado_granja:   
        resultado_granja_numerico.append(re.findall('\d+', animales))
    lista_granja=[]   
    for valores in resultado_granja_numerico:
        for numeros in valores:
            lista_granja.append(numeros)    
    df=pd.DataFrame(lista_granja)    
    df.to_excel('D:/ia_animalitos/animalitos/resultados_jueves_granja.xlsx', sheet_name='Hoja1', index=None)
    return ()



#################  Viernes Granjita

def mantenimiento_viernes_granja():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_viernes_granja.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_viernes_granja.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_viernes_granja():    
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
    resultado_granja_numerico=[]
    for animales in resultado_granja:   
        resultado_granja_numerico.append(re.findall('\d+', animales))
    lista_granja=[]   
    for valores in resultado_granja_numerico:
        for numeros in valores:
            lista_granja.append(numeros)    
    df=pd.DataFrame(lista_granja)    
    df.to_excel('D:/ia_animalitos/animalitos/resultados_viernes_granja.xlsx', sheet_name='Hoja1', index=None)
    return ()




#################  Sabado Granjita

def mantenimiento_sabado_granja():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_sabado_granja.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_sabado_granja.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_sabado_granja():    
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
    resultado_granja_numerico=[]
    for animales in resultado_granja:   
        resultado_granja_numerico.append(re.findall('\d+', animales))
    lista_granja=[]   
    for valores in resultado_granja_numerico:
        for numeros in valores:
            lista_granja.append(numeros)    
    df=pd.DataFrame(lista_granja)    
    df.to_excel('D:/ia_animalitos/animalitos/resultados_sabado_granja.xlsx', sheet_name='Hoja1', index=None)
    return ()




#################  Domingo Granjita

def mantenimiento_domingo_granja():
    datosl=pd.read_excel('D:/ia_animalitos/animalitos/resultados_domingo_granja.xlsx', header=None) 
    datosl= datosl.iloc[:0]        
    datosl.to_excel('D:/ia_animalitos/animalitos/resultados_domingo_granja.xlsx', sheet_name='Hoja1', index=None)
    return()

def llenar_domingo_granja():    
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
    resultado_granja_numerico=[]
    for animales in resultado_granja:   
        resultado_granja_numerico.append(re.findall('\d+', animales))
    lista_granja=[]   
    for valores in resultado_granja_numerico:
        for numeros in valores:
            lista_granja.append(numeros)    
    df=pd.DataFrame(lista_granja)    
    df.to_excel('D:/ia_animalitos/animalitos/resultados_domingo.xlsx', sheet_name='Hoja1', index=None)
    return ()

dia_semana=(datetime.today().weekday())
if dia_semana==0:
    mantenimiento_lunes_granja()
    llenar_lunes_granja()
    mantenimiento_lunes_loto()
    llenar_lunes_loto()
   
if dia_semana==1:
    mantenimiento_martes_granja()
    llenar_martes_granja()
    mantenimiento_martes_loto()
    llenar_martes_loto()
    
if dia_semana==2:
    mantenimiento_miercoles_granja()
    llenar_miercoles_granja()
    mantenimiento_miercoles_loto()
    llenar_miercoles_loto()
    
if dia_semana==3:
    mantenimiento_jueves_granja()
    llenar_jueves_granja()
    mantenimiento_jueves_loto()
    llenar_jueves_loto()
    
if dia_semana==4:
    mantenimiento_viernes_granja()
    llenar_viernes_granja()
    mantenimiento_viernes_loto()
    llenar_viernes_loto()
    
if dia_semana==5:
    mantenimiento_sabado_granja()
    llenar_sabado_granja()
    mantenimiento_sabado_loto()
    llenar_sabado_loto()
    
if dia_semana==6:
    mantenimiento_domingo_granja()
    llenar_domingo_granja()
    mantenimiento_domingo_loto()
    llenar_domingo_loto()
    
    









from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
'''
abre la pagina y retorna el HTML 
PARAMETROS:
Enlace: para acceder al sitio a examinar
Tiempo: tiempo de sleep para que la pagina se termine de cargar
'''
def pageContent(enlace, tiempo): #parametros: enlace a examinar y tiempo de espera de la pagina
    driver.get(enlace) #abre pagina
    time.sleep(tiempo) #espera un tiempo
    return BeautifulSoup(driver.page_source,'html.parser') #retorna el html del sitio

'''
Guarda un diccionario en el archivo JSON 
PARAMETROS:
baseDeDatos: nombre del diccionario a copiar 
'''
def guardarEnJSON(baseDeDatos):
    with open('baseDeDatos.json','w', encoding="utf-8") as f:
            json.dump(baseDeDatos, f, ensure_ascii=False)
            
'''
Obtiene los datos de una serie o pelicula 
PARAMETROS:
dato: parametros de una serie/pelicula
url: enlace principal del sitio para enlazarlo con la extension de la serie/pelicula
classTitle: solo los h1 entre serie y pelicula tienen diferente className, con esto identificamos 
que titulo queremos estraer

retorna un listado con la informacion a guardar en el diccionario
'''
def obtenerDatos(dato, url, classTitle):
    informacion = []
    enlace = dato.find('a') #recoge el enlace de la serie
    urlCompleto = url+enlace['href']
    dato = pageContent(urlCompleto, 3) #examina y guarda pagina de la serie
    title = dato.find('h1', attrs={'class':classTitle}) #guarda el titulo
    sinopsis = dato.find('div', attrs={'class':'logline'})#logline
    sinopsis = sinopsis.find('p')
    meta = dato.find('ul', attrs={'class':'meta-list'}) #guarda el listado de datos
    metaList = meta.findAll('li') #guarda los 4 li que figuran en la pagina
    
    informacion.append(urlCompleto)
    informacion.append(title.text)
    informacion.append(sinopsis.text)
    informacion.append(metaList)
    return informacion
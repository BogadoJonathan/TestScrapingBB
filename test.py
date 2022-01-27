from bs4 import BeautifulSoup
from funciones import guardarEnJSON, pageContent, obtenerDatos




baseDeDatos = {}


url = 'https://www.starz.com'
extensionSeries = '/ar/es/view-all/blocks/1523514'
extensionPeliculas = '/ar/es/view-all/blocks/1523534'


pageSeries = pageContent(url+extensionSeries,5) #examina y guarda pagina oficial de las series
pagePeliculas = pageContent(url+extensionPeliculas,5)

try:
    baseDeDatos['series'] = [] 
    for dato in pageSeries.findAll('div', attrs={'class':'grid-item'}): #Busca todas las series
        info = obtenerDatos(dato,url,'h1')
        episodios = info[3][1]
        episodios = episodios.find('span')
        informacion = {
                    'titulo': info[1],
                    'año':info[3][3].text,
                    'sinopsis': info[2],
                    'link': info[0],
                    'episodios':episodios.text,
                    }
        baseDeDatos['series'].append(informacion) 
        guardarEnJSON(baseDeDatos)
    
    baseDeDatos['peliculas'] = []
    for dato in pagePeliculas.findAll('div', attrs={'class':'grid-item'}): #Busca todas las peliculas
        info = obtenerDatos(dato,url, 'movie-title')

        informacion = {
                    'titulo': info[1],
                    'año':info[3][3].text,
                    'sinopsis': info[2],
                    'link': info[0],
                    'duracion': info[3][1].text,
                    }
        baseDeDatos['peliculas'].append(informacion)
        guardarEnJSON(baseDeDatos)
            
finally:
    driver.quit()


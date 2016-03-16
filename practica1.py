#!/usr/bin/python
# -*- coding: utf-8 -*-


import webapp
import csv

class Acortador(webapp.webApp):


    URL_real = {}
    URL_acortada = {}

    try:
		with open('acortamientos.csv') as csvfile:
			leer = csv.reader(csvfile)
			for row in leer:
				URL_acortada = row[0]
				URL_real = row[1]
				diccionario[URL_real] = URL_acortada

		with open('acortamientos.csv') as csvfile:
			leer = csv.reader(csvfile)
			for row in leer:
				URL_acortada = row[0]
				URL_real= row[1]
				diccionario[URL_real] = URL_acortada

    except:
		cvsfile = open('redireccion.csv', 'w')
		csvfile.close()

    def parse(self,request):
        metodo = request.split(' ',2)[0]
        recurso = request.split(' ',2)[1]
        cuerpo = request.split('\r\n\r\n')[1]
        return (metodo, recurso, cuerpo)





    def process(self, peticion):

        metodo,recurso,cuerpo = peticion

        if metodo == "GET":
            httpCode = "200 OK"
            htmlBody = '<form action="" method="POST" accept-charset="UTF-8">' +\
                     'Acorta url: <input type="text" name="url">' +\
                     '<input type="submit" value="Enviar"></form>'


            """return ("200 OK", '<html><form action="" method="POST" accept-charset="UTF-8">' +\
                     'Acorta url: <input type="text" name="url">' +\
                     '<input type="submit" value="Enviar"></form>')"""

        elif metodo == "PUT" or metodo == "POST"
            if cuerpo != "" :
                urlReal = cuerpo.split("=")[1]
                urlReal = urllib.unquote(urlReal).decode('utf8')
                inicio = urlReal.split("://")[0]

                if (inicio != 'http') and (inici != 'https'):
                    urlReal = 'http://' + urlReal


            return ("404 Not found" , '<html><body><href>url</href></body>')










if __name__ == "__main__":
    try:
        Servidor = AcortadorApp("localhost", 1234)
    except KeyboardInterrupt:
        print "\nFin de la aplicacion\n"

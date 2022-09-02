from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime


def saludo(request):
	return HttpResponse("<h3>Felicitaciones! Crearon su primera vista!!!! </h3>")


def sumar(request):
    return HttpResponse("En esta pagina voy a sumar numeros.")

def miNombre(self, nombre):
    texto = f"Mi nombre es: {nombre}"
    return HttpResponse(texto)

def calcular(request):
    tiempoActual = datetime.now()

    miCumple = datetime(2022,11,29)

    tiempoFalta = miCumple-tiempoActual

    resultado = tiempoFalta.days *60*60*24 + tiempoFalta.seconds

    return HttpResponse(resultado)

def probandoTemplate(self):

	miHtml = open("C:/Users/dalev/OneDrive/Escritorio/proyectos web/miProyecto/miProyecto/plantillas/template1.html")

	plantilla = Template(miHtml.read())

	miHtml.close()

	miContexto = Context()

	documento = plantilla.render(miContexto)

	return HttpResponse(documento)

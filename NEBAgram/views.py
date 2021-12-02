"""Archivo de vistas del proyecto NEBAgram"""

from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    #Formato de fecha mes, dia y año con horas y minutos
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi Current server time is {now}'
    .format(now=str(now)))


def sorted_numbers(request):
    """Se puede debuggear en tiempo real en la consola"""
    """Se pone antes de la linea deseada para debuggear"""
    #import pdb;pdb.set_trace()
    """Se le mandan numeros a traves de la url"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type="application/json")

def say_hi(request, name, age):
    if age <12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}!, Welcome to NEBAgram'.format(name)
    return HttpResponse(message)
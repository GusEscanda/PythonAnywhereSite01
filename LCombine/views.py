from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

from .forms import MainForm

# pip install pyenchant
import enchant

# Create your views here.

def combLetras( letras, largo = 0 ):
    # devuelve todas las combinaciones posibles de palabras de longitud 'largo' que pueden formarse con las letras del string 'letras'
    # (sin repetir letra salvo que ésta aparezca varias veces en 'letras')
    if largo <= 0 or largo > len(letras):
        largo = len(letras)
    if largo == 0:
        return []
    elif largo == 1:
        return list(letras)
    else:
        lista = []
        for i in range(len(letras)):
            for p in combLetras( letras[:i]+letras[i+1:], largo-1 ):
                if letras[i] + p not in lista:
                    lista.append( letras[i] + p )
        return lista

def palabras( letras, largo=0, desde='', hasta='', diccionario=None ):
    lista = []
    for palabra in combLetras(letras,largo):
        if desde and palabra < desde:
            continue
        if hasta and palabra > hasta + 'z':
            continue
        if diccionario:
            if not diccionario.check(palabra):
                continue
        lista.append(palabra)
    lista.sort()
    return lista


def homePage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MainForm( request.POST )
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            d = form.cleaned_data
            combList = palabras( 
                d['letters'].lower(), 
                d['length'], 
                d['filterFrom'].lower(), 
                d['filterUntil'].lower(), 
                enchant.Dict(d['langTag']) if d['useDict'] else None 
            )
            return render( request, "LCombine.html", { 'form':form, 'combList':combList } )
        else:
            pass # if the form is not valid, leave it unchanged so the templete will display the errors
    else: # if method != 'POST' (it's the 1st call to the form page) create an empty form and present it to the user
        form = MainForm()
    return render( request, "LCombine.html", { 'form':form, 'combList':[] } )



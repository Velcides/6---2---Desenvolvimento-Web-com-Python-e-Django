from django.shortcuts import render, HttpResponse

# Create your views here.
# Função que imprime a mensagem no endereço.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome, idade))

def soma(request, n1, n2):
    return HttpResponse(n1+n2)

def sub(request, n1, n2):
    return HttpResponse(n1-n2)

def mult(request, n1, n2):
    return HttpResponse(n1*n2)

def div(request, n1, n2):
    return HttpResponse(n1/n2)
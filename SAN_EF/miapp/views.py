from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


layout = """
    <h1> Proyecto Web (LP3 - 2024) | Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de Saludo</a>
        </li>
        <li>
            <a href="/rango"> Mostrar Números [a,b]</a>
        </li>
        <li>
            <a href="/rango2/10/15"> Mostrar Números [10,15]</a>
        </li>
    </ul>
    <hr/>
"""


def index(request):
    return render(request,'index.html')


def saludo(request):
    return render(request,'saludo.html')

def persona(request):
    return render(request,'persona.html')



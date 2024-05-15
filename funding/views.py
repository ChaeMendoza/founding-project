from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
import time
from django.template.loader import render_to_string
from collections import Counter

# Create your views here.
from funding.models import Campania, HistorialPago, Categoria, SolCampania

#Número de tarjetas por carga
paginas = 2

def home_view(request):
    campanias = Campania.objects.filter(estado=True).order_by('-fecha_cierre')
    return render(request, 'funding/home.html', {'campanias': campanias})

def register_view(request): 
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'funding/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()        
    return render(request, 'funding/login.html', {'form': form})

# logout  page
def user_logout(request):
    logout(request)
    return redirect('home')

#Campañas por categoría
def get_campanias_por_categoria(request, categoria_id):
    try:
        if(categoria_id == 0):
            campanias = Campania.objects.filter(estado=True).order_by('-fecha_cierre')
        else:
            campanias = Campania.objects.filter(categorias__in = str(categoria_id), estado=True).order_by('-fecha_cierre')
        return render(request, 'funding/categoria.html', {'campanias': campanias, 'categoria_id': categoria_id})
    except Campania.DoesNotExist:
        return redirect('home')

#Campaña descripción
def get_campania_descripcion(request, campania_id):
    try:
        campania = Campania.objects.get(id=campania_id)
        donativos = HistorialPago.objects.filter(campania=campania_id).count()
        return render(request, 'funding/campania.html', {'campania': campania, 'donativos': donativos})
    except Campania.DoesNotExist:
        return redirect('home')

def post_pago(request):
    donacion = json.loads(request.body)
    valor = donacion.get('valor', '')
    campania_id = donacion.get('campania_id', '')

    historial = HistorialPago(
        usuario = request.user,
        campania = Campania.objects.get(pk=campania_id),
        valor = float(valor)
    )
    historial.save()
    
    campania = Campania.objects.get(pk=campania_id)
    campania.monto_recaudado = float(campania.monto_recaudado) + float(valor)
    campania.save()
    
    time.sleep(3)

    response = {'message': 'ok'}
    return JsonResponse(response)

def get_categorias_por_pagina(request):
    data = json.loads(request.body)
    pagina_actual = data.get('page')
    categoria_id = data.get('categoria_id')
    
    if(categoria_id == "0"):
        campanias = Campania.objects.filter(estado=True).order_by('-fecha_cierre')
    else:
        campanias = Campania.objects.filter(categorias__in = str(categoria_id), estado=True).order_by('-fecha_cierre')
        
    paginador = Paginator(campanias, paginas)
    
    objetos_pagina = paginador.get_page(pagina_actual)
    
    if pagina_actual > paginador.num_pages:
        html = ''
    else:    
        html = render_to_string(
            template_name='funding/categoria_ajax.html', context={'campanias': objetos_pagina}
        )
    
    data_dict = {'html_from_view': html}
    return JsonResponse(data=data_dict, safe=False)


def get_home_por_pagina(request):
    campanias = Campania.objects.filter(estado=True).order_by('-fecha_cierre')
    paginador = Paginator(campanias, paginas)
    
    data = json.loads(request.body)
    
    pagina_actual = data.get('page')
    objetos_pagina = paginador.get_page(pagina_actual)
    
    if pagina_actual > paginador.num_pages:
        html = ''
    else:    
        html = render_to_string(
            template_name='funding/home_ajax.html', context={'campanias': objetos_pagina}
        )
    
    data_dict = {'html_from_view': html}
    return JsonResponse(data=data_dict, safe=False)

def nosotros_view(request):
    return render(request, 'funding/nosotros.html')

def solCampania_view(request):
    categorias=Categoria.objects.all()
    return render(request, 'funding/solCampania.html',{'categorias': categorias})

def guardarSolicitudCampania(request):
    try:
        datosSolCap=json.loads(request.body)
        nombreCam=datosSolCap.get('nombre')
        descripcion=datosSolCap.get('descripcion')
        categoria_id=datosSolCap.get('categorias')
        beneficiario=datosSolCap.get('beneficiario')
        monto_x_recaudar=datosSolCap.get('monto_x_recaudar')
        email=datosSolCap.get('email')
        
        categoria=Categoria.objects.get(pk=int(categoria_id))
        nuevaSol=SolCampania(
            nombre=nombreCam,
            categorias=categoria,
            descripcion=descripcion,
            beneficiario=beneficiario, 
            monto_x_recaudar=monto_x_recaudar,
            email=email,
            estado=True
        )
        nuevaSol.save()
        return JsonResponse(status=200,data={'msg':'Campaña creada'})
        
    except Exception as ex:
        return JsonResponse(status=500,data={'msg':str(ex)})
    
# Search Campaign
def search_campaign(request):
    query = request.GET.get('q')
    if query:
        campaigns = Campania.objects.filter(nombre__icontains=query)
    else:
        campaigns = []
    print(f"Campaña: {campaigns}")
    return render(request, 'funding/search.html', {'campaigns': campaigns})

#campaña finalizada
def get_campanias_finalizadas(request):
    try:
        campanias = Campania.objects.filter(estado=False)
        return render(request, 'funding/historias.html', {'campanias': campanias})
    except Campania.DoesNotExist:
        return redirect('home')
    
def get_historias_por_pagina(request):
    campanias = Campania.objects.filter(estado=False).order_by('-fecha_cierre')
    paginador = Paginator(campanias, paginas)
    
    data = json.loads(request.body)
    
    pagina_actual = data.get('page')
    objetos_pagina = paginador.get_page(pagina_actual)
    
    if pagina_actual > paginador.num_pages:
        html = ''
    else:    
        html = render_to_string(
            template_name='funding/historias_ajax.html', context={'campanias': objetos_pagina}
        )
    
    data_dict = {'html_from_view': html}
    return JsonResponse(data=data_dict, safe=False)
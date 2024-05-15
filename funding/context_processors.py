from funding.models import Categoria, FormaPago

def get_all_categorias(request):
    categorias = Categoria.objects.all()
    return {'categorias': categorias}

def get_formas_pago(request):
    usuario_actual = request.user
    if(usuario_actual.id == None):
        formaPago = []
    else:
        formaPago = FormaPago.objects.filter(estado=True)
    return {'formaPago': formaPago}
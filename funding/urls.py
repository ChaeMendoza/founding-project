from django.urls import path
from . import views

urlpatterns = [    
    path('',views.home,name='home'),
    #path('categorias/',views.do_categorias,name='categorias')
]

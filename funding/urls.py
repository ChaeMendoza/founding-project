from django.urls import path
from . import views

urlpatterns = [    
    path('',views.home_view,name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.user_logout, name='logout'),
    #path('categorias/',views.do_categorias,name='categorias')
    path('categorias/<int:categoria_id>/campanias/', views.get_campanias_por_categoria, name='campanias_por_categoria'),
    path('campania/<int:campania_id>/descripcion/', views.get_campania_descripcion, name='campania_descripcion'),
    path('campania/pago/', views.post_pago, name='campania_pago'),
    path('campania/pagina/', views.get_categorias_por_pagina, name='get_categorias_por_pagina'),
    path('home/pagina/', views.get_home_por_pagina, name='get_home_por_pagina'),
    path('nosotros/',views.nosotros_view,name='nosotros'),
    path('solCampania/',views.solCampania_view,name='solCampania'),
    path('guardar/solCampania/',views.guardarSolicitudCampania,name='guardar_solCampania'),
    path('search/', views.search_campaign, name='search_campaign'),
    path('campanias/', views.get_campanias_finalizadas, name='campanias_finalizadas'),
    path('historias/pagina/', views.get_historias_por_pagina, name='get_historias_por_pagina'),
]

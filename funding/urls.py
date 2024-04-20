from django.urls import path
from . import views

urlpatterns = [    
    path('',views.home_view,name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    #path('categorias/',views.do_categorias,name='categorias')
]

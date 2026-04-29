from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('dias/', views.dias_view, name='dias'),
    path('palcos/', views.palcos_view, name='palcos'),
    # Ponto 7 - Nova rota para editar palco
    path('palcos/<int:palco_id>/editar/', views.editar_palco_view, name='editar_palco'),
    # Ponto 4 - Nova rota para criar concerto
    path('concertos/criar/', views.criar_concerto_view, name='criar_concerto'),
    path('concertos/<int:concerto_id>/', views.concerto_view, name='concerto'),
    path('concertos/<int:concerto_id>/editar/', views.editar_concerto_view, name='editar_concerto'),
    # Ponto 4 - Nova rota para apagar concerto
    path('concertos/<int:concerto_id>/apagar/', views.apagar_concerto_view, name='apagar_concerto'),
]
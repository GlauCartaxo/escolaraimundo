from django.urls import path
from avaliacao.views import AvaliacaoCreateView
app_name = 'avaliacao'

urlpatterns = [

    path('addavaliacao', AvaliacaoCreateView.as_view(),name='add_avaliacao'),
]
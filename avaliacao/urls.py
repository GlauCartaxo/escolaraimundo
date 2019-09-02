from django.urls import path
from avaliacao.views import AvaliacaoCreateView, AvaliacaoListView
app_name = 'avaliacao'

urlpatterns = [

    path('addavaliacao', AvaliacaoCreateView.as_view(),name='add_avaliacao'),
    path('nota/<int:pk>/view', AvaliacaoListView.as_view(), name='listnota' ),

]
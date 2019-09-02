from escola.urls import path
from users.views import UserLoginView, UserLogoutView, UserDetailView, AlunoDetailView, ProfessorDetailView

app_name = 'users'

urlpatterns = [
    path('login', UserLoginView.as_view(),name='login_users'),   
    path('logout', UserLogoutView.as_view(),name='logout_users'),
    path('users/<int:pk>/detalhes', UserDetailView.as_view(), name='detail_users'),
    path('users/<int:pk>/aluno', AlunoDetailView.as_view(), name='detalhes_aluno'),
    path('users/<int:pk>/professor', ProfessorDetailView.as_view(), name='detalhes_professor'),


]
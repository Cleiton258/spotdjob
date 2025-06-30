"""
URL configuration for meu_lista_de_tarefas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from tarefas.views import  customLoginView
from django.shortcuts import redirect
from tarefas.views import RegisterView, home, adicionar_vaga, vaga_detalhes, term_sessao, sobre
from django.contrib.auth import views as auth_views
from tarefas.views import activateAccountView, Emprego, Curso__vend, curso_detalhes, adicionar_curso
urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", customLoginView.as_view(), name="Tela_login"),
    path('', lambda request: redirect('Tela_login')),
    path('activate/<str:token>/', activateAccountView.as_view(), name='activate_account'),
    path('register/', RegisterView.as_view(), name="register"),
    path('home/', home.as_view(), name="home"),
    path('adicionar_vaga/', adicionar_vaga, name="adicionar_vaga"),
    path('vaga/<int:vaga_id>/', vaga_detalhes, name="vaga_detalhes"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "tarefas/reset_password.html"), name='reset_password' ),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name = 'tarefas/reset_password_send.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'tarefas/reset_password_confirm.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'tarefas/reset_password_complete.html'), name="password_reset_complete"),
    path('Emprego/', Emprego.as_view(), name="proc_emprego"),
    path('Curso', Curso__vend.as_view(), name="proc_curso" ),
    path('detalhes_Curso/<int:curso_id>/', curso_detalhes, name="curso_detalhes"),
    path('adicionar_curso/', adicionar_curso, name="adicionar_curso"),
    path('terminar_sessao/', term_sessao.as_view(), name="Terminar_sessao" ),
    path('sobre/', sobre.as_view(), name="sobre"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

"""© 2025 Cleiton Ernesto Cumbane. Todos os direitos reservados.
   Este código faz parte do projeto SpotDjob.
   Uso não autorizado, cópia ou distribuição são proibidos sem permissão.
   """
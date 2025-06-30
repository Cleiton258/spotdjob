from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .forms import VagaForm, CursoForm
from .models import empregar, Cursar
from django.utils import timezone
from datetime import date
from django.shortcuts import render, redirect
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import View
    
class CustomLoginView(LoginView):
    template_name = "tarefas/login.html"

    def get_success_url(self):
        return reverse_lazy("home")
    
def send_activate_email(user, request):
    print("Enviando email de activacao")
    signer = TimestampSigner()
    token = signer.sign(user.pk)
    activation_url = request.build_absolute_uri(
        reverse('activate_account', args=[token])
    )
    subject = 'ative a sua conta'
    message = f'Ola {user.username},\n\n Clique no link para activar a sua conta: \n{activation_url}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list, fail_silently = False)  
class RegisterView(CreateView):
    template_name = "tarefas/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("Tela_login")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        send_activate_email(user, self.request)
        return redirect(self.success_url)

    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nome"] = self.request.user.username
        return context

class activateAccountView(View):
    def get(self, request, token):
        signer = TimestampSigner()
        try:
            user_id = signer.unsign(token, max_age=60*60*24)
            user = User.objects.get(pk=user_id)
            if not user.is_active:
                user.is_active = True
                user.save()
                return redirect("Tela_login")
            else:
                return HttpResponse("Essa conta ja foi ativada")
        except SignatureExpired:
            return HttpResponse("Link inspirado. Solicite outro registro")
        except (BadSignature, User.DoesNotExist):
            return HttpResponse("Link invalido . Usuario nao encontrado")
from difflib import SequenceMatcher
def simililaridade(texto1, texto2):
    return SequenceMatcher(None, texto1.lower(), texto2.lower()).ratio()   
class home(LoginRequiredMixin, TemplateView):
    template_name = "tarefas/home.html"
    
    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoje = timezone.now().date()
        cursos = Cursar.objects.filter(limite_inscricao__gte=hoje)
        vagas = empregar.objects.filter(data_limite__gte = hoje)
        
        lista_pares = []
        
        for curso in cursos:
            melhores_vagas = []
            palavras_curso = curso.palavrsa_chave.lower().split(',')
            for vaga in vagas:
                #texto_vaga = f"{vaga.requisitos}".lower()
                for palavra in palavras_curso:
                    if palavra.strip() in texto_vaga:
                        melhores_vagas.append(vaga)
                        break
                if melhores_vagas:
                    for vaga in melhores_vagas:
                        lista_pares.append({
                            'curso': curso,
                            'vaga':None
                        })
        context['lista_pares']= lista_pares
        return context
        BREVEMENTE
    """
class Emprego(TemplateView):
    template_name ="tarefas/Emprego.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoje = timezone.now().date()
        context["vagas"] = empregar.objects.filter(data_limite__gte=hoje)
        return context
         
   
def adicionar_vaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save();
            return redirect(reverse_lazy('home'))
    else:
        form = VagaForm()
    return render (request, 'tarefas/adicionar_vaga.html', {'form': form})

def vaga_detalhes(request, vaga_id):
    emprega =get_object_or_404(empregar, id=vaga_id)
    
    requisitos_lista = [r.strip() for r in emprega.requisitos.split(';') if r.strip()]
    responsabilidades_lista = [r.strip() for r in emprega.responsabilidades.split(';') if r.strip()]
    

    context = {
        'emprega': emprega,
        'requisitos_lista': requisitos_lista,
        'responsabilidades_lista': responsabilidades_lista,
    }
    return render(request, 'tarefas/det_empregos.html', context)

class Curso__vend(TemplateView):
    template_name ="tarefas/cursos.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoje = timezone.now().date()
        context["cursos"] = Cursar.objects.filter(inicio_inscricao__gte=hoje)
        return context

def adicionar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save();
            return redirect(reverse_lazy("home"))
    else:
        form = CursoForm()
    return render(request, 'tarefas/adicionar_curso.html', {'form': form})
            
def curso_detalhes(request, curso_id):
    curso = get_object_or_404(Cursar, id = curso_id)
    requisitos_lista = [r.strip() for r in curso.requisitos.split(';') if r.strip()]
    descricao_lista = [r.strip() for r in curso.Descricao_curso.split(';') if r.strip()]
    

    context = {
        'curso': curso,
        'requisitos_lista': requisitos_lista,
        'descricao_lista': descricao_lista,
        
    }

    return render(request, 'tarefas/det_cursos.html', context)

class sobre(TemplateView):
    template_name = 'tarefas/sobre.html'

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    #messages.success(request, "Sessao terminada com sussesso")
    return redirect('Tela_login')
"""© 2025 Cleiton Ernesto Cumbane. Todos os direitos reservados.
   Este código faz parte do projeto SpotDjob.
   Uso não autorizado, cópia ou distribuição são proibidos sem permissão.
   """
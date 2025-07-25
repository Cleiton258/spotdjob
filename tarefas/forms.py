from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from .models import empregar, Cursar

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  # conta inativa até confirmação
        if commit:
            user.save()
        return user

class VagaForm(forms.ModelForm):
    class Meta:
        model = empregar
        fields = ["empresa", "titulo", "Descricao", "responsabilidades", "requisitos", "processo_candidatura","data_limite", "localizacao","site", "imagem"]

class CursoForm(forms.ModelForm):
    class Meta:
         model = Cursar
         fields = ["instituicao", "Nome_curso", "imagem", "Descricao_curso", "requisitos", "inscricao",
                   "mensalidade", "limite_inscricao", "localizacao", "email_contato", "site", "Duracao", "banner"]
#sobre nos, opcoes, terminar a sessao, conteudo, contactos whatsapp e email do site por baixo e opcao de terminar a sssao, informar aos anunciantes de vagas que tem que colocar ; no fim de cada requisito...
#Template de confirmacao que a conta ja foi criada quando o usuario colocar o link e um botao de voltar a tela de login e iniciar a sessao, o mesmo na reset password depois de confirmar o email 
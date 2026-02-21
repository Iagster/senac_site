from django.shortcuts import render

def home(request):
    contexto = {
        'mensagem': 'Bem-vindo ao meu primeiro projeto Django!'
    }
    return render(request, 'pages/home.html', contexto)

# Create your views here.

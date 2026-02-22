from django.shortcuts import render
from .forms import ContatoForm

def home(request):
    return render(request, 'pages/home.html')


def sobre(request):
    return render(request, 'pages/sobre.html')


def ajuda(request):
    return render(request, 'pages/ajuda.html')

def contato(request):
    # Se a requisição for GET:
    # O usuário apenas acessou a página pelo navegador e criamos um formulário
    # vazio para exibição.
    if request.method == 'GET':
        form = ContatoForm()
        return render(request, 'pages/contato.html', {'form': form})

    # Se a requisição for POST:
    # Significa que o usuário enviou o formulário e os dados enviados vêm em
    # request.POST.
    elif request.method == 'POST':
        form = ContatoForm(request.POST)

        # form.is_valid():
        # Executa todas as validações do Django Forms:
        # campos obrigatórios, validação de email e validações personalizadas
        # Ex: clean_nome
        if form.is_valid():

            # cleaned_data:
            # Contém apenas dados já validados e seguros.
            # Não deve-se usar request.POST direto.
            dados = form.cleaned_data

            return render(
                request,
                'pages/contato_resultado.html',
                {'dados': dados}
            )

        # Se o formulário tiver erros ele é reenviado para a página com mensagens
        # exibidas.
        return render(request, 'pages/contato.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Malte


def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # redireciona para a página inicial após login
        else:
            return render(request, 'accounts/login.html', {'form': form, 'error': 'Credenciais inválidas'})
    return render(request, 'accounts/login.html', {'form': form})


@login_required(login_url="/login/")
def malte_list(request):
    maltes = Malte.objects.all()
    return render(request, 'brewery/malte_list.html', {'maltes': maltes})

@login_required(login_url="/login/")
def malte_detail(request, pk):
    malte = get_object_or_404(Malte, pk=pk)
    return render(request, 'brewery/malte_detail.html', {'malte': malte})

@login_required(login_url="/login/")
def malte_create(request):
    if request.method == "POST":
        # Criar lógica para salvar um novo Malte
        pass
    return render(request, 'brewery/malte_form.html')

@login_required(login_url="/login/")
def malte_update(request, pk):
    malte = get_object_or_404(Malte, pk=pk)
    if request.method == "POST":
        # Criar lógica para atualizar o Malte
        pass
    return render(request, 'brewery/malte_form.html', {'malte': malte})

@login_required(login_url="/login/")
def malte_delete(request, pk):
    malte = get_object_or_404(Malte, pk=pk)
    if request.method == "POST":
        malte.delete()
        return redirect('malte_list')
    return render(request, 'brewery/malte_confirm_delete.html', {'malte': malte})

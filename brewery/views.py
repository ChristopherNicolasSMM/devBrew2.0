from django.shortcuts import render, get_object_or_404, redirect
from .models import Malte

def malte_list(request):
    maltes = Malte.objects.all()
    return render(request, 'brewery/malte_list.html', {'maltes': maltes})

def malte_detail(request, pk):
    malte = get_object_or_404(Malte, pk=pk)
    return render(request, 'brewery/malte_detail.html', {'malte': malte})

def malte_create(request):
    if request.method == "POST":
        # Criar lógica para salvar um novo Malte
        pass
    return render(request, 'brewery/malte_form.html')

def malte_update(request, pk):
    malte = get_object_or_404(Malte, pk=pk)
    if request.method == "POST":
        # Criar lógica para atualizar o Malte
        pass
    return render(request, 'brewery/malte_form.html', {'malte': malte})

def malte_delete(request, pk):
    malte = get_object_or_404(Malte, pk=pk)
    if request.method == "POST":
        malte.delete()
        return redirect('malte_list')
    return render(request, 'brewery/malte_confirm_delete.html', {'malte': malte})

from django.shortcuts import render
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            return render(request, 'blog/home.html')
    else:
        form = RegistroForm()
    return render(request, 'blog/registro.html', {'form': form})




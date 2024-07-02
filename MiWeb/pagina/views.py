from django.shortcuts import render, redirect
from .models import Index
from pagina.forms import IndexForm

def index(request):
    index = Index.objects.first()
    # index = Index.objects.all()
    return render(request, 'index.html', {'index': index})

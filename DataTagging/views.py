from django.shortcuts import render, redirect
from inputs.models import Inputs
def home(request):
    # texts = Inputs.objects
    random_text = Inputs.objects.order_by('?')[0]
    return render(request, 'home.html', {'texts':random_text})
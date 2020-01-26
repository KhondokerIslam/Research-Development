from django.shortcuts import render, redirect
from inputs.models import Input
from django.shortcuts import get_object_or_404
def home(request):
    # texts = Inputs.objects
    random_text = Input.objects.order_by('?')[0]
    # print (random_text.id)
    return render(request, 'home.html', {'texts':random_text})

def homePost(request, text_id):
    if request.method == 'POST':
        innput = get_object_or_404(Input, pk=text_id)
        if request.POST.get('expression') == "1":
            innput.happy += 1
        if request.POST.get('expression') == "2":
            innput.sad += 1
        if request.POST.get('expression') == "3":
            innput.stupyfied += 1
        if request.POST.get('expression') == "4":
            innput.angry += 1
        if request.POST.get('expression') == "5":
            innput.others += 1
        innput.save()
        random_text = Input.objects.order_by('?')[0]
        return render(request, 'home.html', {'texts':random_text})

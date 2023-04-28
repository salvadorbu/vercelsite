from django.shortcuts import render
from .forms import ContactForm

def index(request):
    return render(request, 'main/index.html')

def projects(request):
    return render(request, 'main/projects.html')

def resume(request):
    return render(request, 'main/resume.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/contact.html', context)

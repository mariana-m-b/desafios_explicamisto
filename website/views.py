#from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse


#class HomeView(TemplateView):
#    template_name = "home.html"


from .forms import adicionar_nota
from auth_explicamisto.models import Aluno 
from django.contrib import messages


def home(response):
    return render(response, "home.html", {})


def grades(request):
    if request.method == 'POST':
        form = adicionar_nota(request.POST)
        if form.is_valid():
            # gets the data from the form
            submitted_name = form.cleaned_data['name']
            submitted_grade = form.cleaned_data['nota_primeiro_teste']
            
            # searches aluno with the submitted name
            try:
                aluno = Aluno.objects.get(user__username=submitted_name) 
            except Aluno.DoesNotExist:
                messages.error(request, 'Aluno not found.') # info displayed in the admin page
                return render(request, 'grades.html', {'form': form})

            aluno.nota_primeiro_teste = submitted_grade
            aluno.save()

            messages.success(request, 'Nota do primeiro teste saved successfully.')  
            return render(request, 'success.html')
    else:
        form = adicionar_nota()
    return render(request, 'grades.html', {'form': form})



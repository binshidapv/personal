from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ContactForm
from . models import Project



# Create your views here.


def HomeView(request):
     projects = Project.objects.all()
     context = {
         'projects': projects
          }
     return render(request, 'home.html', context)

    # define other views for other pages here...



def AboutView(request):
    return render(request,'about.html')

def ProjectsView(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)
def ProjectDetailView(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_details.html', context)






def SkillView(request):
    return render(request,'skill.html')


def ContactsView(request):
    form = ContactForm()
    context = {'form': form}
    return render(request,'contact.html',context)
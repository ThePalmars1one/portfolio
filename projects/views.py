from django.shortcuts import render
from .models import Programate_projects
from technologies.models import Tech


def projects_views(request):
    context = {
        'projects': Programate_projects.objects.all(),
        'technologies': Tech.objects.all(),
    }
    return render(request, 'projects.html', context)

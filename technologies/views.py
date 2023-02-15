from django.shortcuts import render
from .models import Tech

def tech_views(request):
    techs = Tech.objects.all()
    return render(request, 'tech.html', {'techs': techs})

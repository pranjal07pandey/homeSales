from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    homes = Home.objects.all()
    agents = Agent.objects.count()
    print(agents)
    return render(request, 'sales/index.html',{
        'homes': homes,
        'agents': agents
    })


def homeDetails(request, pk):
    home = Home.objects.get(id=pk)
    return render(request, 'sales/homeDetails.html',{
        'home': home
    })


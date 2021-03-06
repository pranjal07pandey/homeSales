from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from .forms import CreateUserForm, OrderForm
from .filters import HomeFilter
from django.contrib.auth import authenticate, login, logout 



def registerUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
    
        return render(request, 'sales/register.html',{
            'form':form
        })


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('index')
    
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username= username, password= password)

            if user is not None:
                login(request, user)
                return redirect('index')

        return render(request, 'sales/login.html',{

    })

def logoutUser(request):
    logout(request)
    return redirect('index')       


def index(request):
    homes = Home.objects.all()
    paginator = Paginator(homes,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    agents = Agent.objects.count()
    print(agents)
    return render(request, 'sales/index.html',{
        'homes': page_obj,
        'agents': agents
    })


def homeDetails(request, pk):
    home = Home.objects.get(id=pk)
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.home = home
            fs.save()
            return redirect('dashboard', request.user.id)
            
    return render(request, 'sales/homeDetails.html',{
        'home': home,
        'form':form
    })

def allHomes(request):
    f = HomeFilter(request.GET, queryset = Home.objects.all()) 
    homes = Home.objects.all()
    return render(request, 'sales/houses.html',{
        'homes':homes,
        'filter': f
    })

def agents(request):
    agents = Agent.objects.all()
    mvp = Agent.objects.filter(is_mvp=True)
    return render(request, 'sales/agents.html',{
        'agents': agents,
        'mvp' : mvp
    })

def individualAgent(request, pk):
    agent = Agent.objects.get(id=pk)
    home = Home.objects.filter(agent=agent)
    return render(request, 'sales/individualAgent.html',{
        'agent':agent,
        'home':home
    })


def dashboard(request, pk):
    orders = Contact.objects.filter(user = request.user).order_by('-id')
    return render(request, 'sales/dashboard.html', {
        'orders': orders
    })
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("login_view")
    return render(request,"airplanes/index.html")


def aeropuertos(request):
    airports = Airport.objects.all()
    return render(request,"airplanes/airports.html", {"airports": airports})

def vuelos(request):
    flights = Flight.objects.all()
    return render(request, "airplanes/flights.html", {"flights": flights })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username, password=password)

        if user:
            login(request, user)
            return redirect("index")
        else:
            message = "Usuario incorrecto"
            return render(request, "airplanes/users.html", { "msg": message})
    else:
        return render(request, "airplanes/users.html")
    
def register(request):

    if request.POST:
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()

            return redirect("login_view")

    else:
        user_form = UserRegisterForm()
    return render(request, 'airplanes/register.html', {'form': user_form})

def logout_view(request):
    logout(request)
    return redirect("login_view")


def add_airport(request):

    form = AirportForm(request.POST)
    # if request.method == "POST"
    if request.POST:

        if form.is_valid():
            cd = form.cleaned_data
            code = cd["code"]
            city = cd["city"]

            Airport.objects.create(code=code, city=city)
            return redirect(reverse('aeropuertos'))


    return render(request, "airplanes/agregar.html", {"form": form})




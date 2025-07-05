from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import SurveyResponse
from django.contrib.auth.decorators import login_required

@login_required
def unfinished_page(request):
    return render(request, 'catharsis/unfinished.html')

def index(request):
    return render(request, 'catharsis/index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # or redirect to a dashboard
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'catharsis/login.html')


def register_step2(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'catharsis/register.html')

        if not email:
            messages.error(request, "Email is required.")
            return render(request, 'catharsis/register.html')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'catharsis/register.html')

        # ✅ Create and auto-login user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        login(request, user)  # 🔐 Auto-login after registration

        messages.success(request, "Account created successfully!")
        return redirect('index')  # ✅ Redirect to homepage

    return render(request, 'catharsis/register.html')

def welcome_page(request):
    return render(request, 'catharsis/welcome.html')

def survey(request):
    if request.method == 'POST':
        SurveyResponse.objects.create(
            age_group=request.POST.get('entry.1475680165'),
            gender_identity=request.POST.get('entry.649415742'),
            occupation=request.POST.get('entry.2032508311'),
            stress_level=request.POST.get('entry.661171123'),
            peer_support_availability=request.POST.get('entry.1334253256'),
            comfort_level=request.POST.get('entry.1274209178'),
            stress_sources=request.POST.get('entry.1285999797'),
            used_peer_support=request.POST.get('entry.1572763554'),
            reason_not_seeking=request.POST.get('entry.1458984835', ''),
            societal_stance=request.POST.get('entry.1877443982'),
            desired_features=request.POST.get('entry.1098765432'),
            opinion_on_app=request.POST.get('entry.2098765432')
        )
        return render(request, 'catharsis/thank_you.html')  # Create this template

    return render(request, 'catharsis/survey.html')


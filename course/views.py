from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignForm
from .models import Student, Course

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('login')


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/')
#     else:
#         form = AuthenticationForm()
#         return render(request, "login.html", {'form': form})
    

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')  # Add this line
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
        

def Sigup_view(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            user = form.save()
            Student.objects.create(user=user)
            messages.success(request, "Account created successfully")
            return redirect('login')
    else:
        form = SignForm()
    return render(request, "signup.html", {'form': form})



def home(request):
    return render(request, "home.html")



# @login_required
# def course_list(request):
#     course = Course.objects.all()
#     student = Student.objects.get(user= request.user)
#     context = {
#         "courses":course,
#         "student":student,
#     }
#     return render(request, "course.html", context)



def course_list(request):
    courses = Course.objects.all()  # Always fetch all courses
    student = None
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
    context = {
        "courses": courses,
        "student": student,
    }
    return render(request, "course.html", context)




def course_description(request, course_id):  # Added course_id parameter
    course = get_object_or_404(Course, id=course_id)  # Fetch specific course
    student = Student.objects.get(user=request.user) if request.user.is_authenticated else None  # For potential enrollment checks
    context = {
        "course": course,  # Singular course
        "student": student,
    }
    return render(request, "course_description.html", context)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        username = request.POST['User_name']
        email = request.POST['Email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
        user.save()
        
        print("User Created")
        return redirect('/')
    
    else:

        return render(request, 'register.html')

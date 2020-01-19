from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from users.models import Profile
from users.forms import ProfileForm
# Create your views here.

def update_profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            print(form.cleaned_data)
            return redirect('feed')
    else:
        form = ProfileForm()

    return render(request = request,
                  template_name ='users/update_profile.html',
                  context = {
                  'profile': profile ,
                  'user' : request.user,
                  'form' : form } )

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html',{'error': 'Invalid username and password'})
    return render(request, 'users/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']
        try:
            user = User.objects.create_user(username = username, password = passwd)
        except IntegrityError:
            return render(request, "users/signup.html", {'error' : 'Username is already in use'})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        profile = Profile(user = user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

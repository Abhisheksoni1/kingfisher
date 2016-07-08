from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import  UserRegistrationForm,ProfileEditForm,UserEditForm
from .models import Profile
from django.contrib import messages
import django.contrib.auth.views as auth_views
from django.conf import settings

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return auth_views.login(request)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})

@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',
                  {'section': 'dashboard'})

@login_required
def edit(request):
    if request.method =="POST":
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile updated succesfully')
        else:
            messages.success(request,'Error updating your profile')
    else:
        user_form = UserEditForm()
        profile_form = ProfileEditForm()
    return render(request,'account/edit.html',{'user_form':user_form,
                                               'profile_form':profile_form})

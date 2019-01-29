from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserLoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse('index'))
    
def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'accounts/login.html', {'login_form': login_form})
        

def register(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                #create blank profile for new user
                Profile.objects.create(user=user)
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {
        "registration_form": registration_form})
  
@login_required
def user_list(request):
    object_list = User.objects.filter(is_active=True).order_by('username')
    paginator = Paginator(object_list, 40) # 40 users in each page
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        users = paginator.page(paginator.num_pages)
    return render(request, 'accounts/user/list.html', {'users':users, 'page':page})
    
@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'accounts/user/detail.html', {'user':user})
    
@login_required
def edit(request):
    """ edit user details"""
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                    data = request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                        data=request.POST,
                                        files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(request, 'accounts/edit.html', {'user_form': user_form, 'profile_form': profile_form})    

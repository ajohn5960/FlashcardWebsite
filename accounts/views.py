from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from user_profile.forms import UserProfileForm

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User


from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.

class SignUpView(CreateView):
    form_class = UserProfileForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



def delete_user(request):
    current_user = request.user

    if request.method == "POST":
        current_user.delete()
        return redirect('accounts:user_delete_success')
    context ={
         "current_user" :current_user,
    }
    return render(request, "user_delete.html", context)
    



def user_delete_success(request):
    context = {}
    return render(request, "user_delete_success.html", context)
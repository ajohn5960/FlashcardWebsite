
from django.contrib import admin
from django.urls import path
from accounts.views import (
    SignUpView,
    delete_user,
    user_delete_success
)

app_name = 'accounts'
urlpatterns = [
   path('signup/', SignUpView.as_view(), name='signup'),
   path('delete/', delete_user, name='delete_user'),
   path('delete/success', user_delete_success, name='user_delete_success'),



]


# path('profile/<str:username>', UserProfileDetailView.as_view(), name='user-profile'),
# path('profile/<int:my_id>', profile_detail_view, name="profile-detail"),
    
# https://learndjango.com/tutorials/django-login-and-logout-tutorial

 
 
 
 

from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserProfileForm(UserCreationForm):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name',)
    

    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]

        print(str(first_name) + "\n")
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(user_id=user, first_name=first_name, last_name=last_name)

        return user
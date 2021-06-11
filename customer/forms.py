from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm, LoginForm


class SelfLoginForm (LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["login"].widget.attrs.update({'class': 'form-control-lg rounded-pill border-0 shadow-sm'})
        self.fields["password"].widget.attrs.update({'class': 'form-control-lg rounded-pill border-0 shadow-sm'})
        


class MyCustomSignupForm(SignupForm):

    field_order = ['first_name', 'last_name', 'email', 'password1', 'password2']
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last name')
    

    def signup(self, request, user):

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save() 
        return user

    def __init__(self, *args, **kwargs):
        
            super(MyCustomSignupForm, self).__init__(*args, **kwargs)
            self.fields["email"].label = ''
            self.fields["password1"].label = ''
            self.fields["password2"].label = '' 
            self.fields["first_name"].label = ''
            self.fields["last_name"].label = '' 
            self.fields["first_name"].widget.attrs["placeholder"] = "first name"
            self.fields["last_name"].widget.attrs["placeholder"] = "last name"

# class MyCustomSignupForm(SignupForm):    
#         field_order = ['first_name', 'last_name', 'password1', 'password2', 'username', 'email',]
#         def __init__(self, *args, **kwargs):
#             super(MyCustomSignupForm, self).__init__(*args, **kwargs)
#             self.fields['first_name'] = forms.CharField(required=True)  
#             self.fields['last_name'] = forms.CharField(required=True) 
#             self.fields["email"].label = ''
#             self.fields["username"].label = ''
#             self.fields["password1"].label = ''
#             self.fields["password2"].label = ''  
#             default_field_order = ['first_name', 'last_name', 'password1', 'password2', 'username', 'email',]

#         def save(self, request):
#             field_order = ['first_name', 'last_name', 'password1', 'password2', 'username', 'email',]
#             first_name = self.cleaned_data['first_name']
#             user = super(MyCustomSignupForm, self).save(request)
#             return user

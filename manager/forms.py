from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(   #form 필드
        required=True,
        widget=forms.EmailInput(    #widget 필드
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': 'Ture',
            }
        )
    )

    username = forms.RegexField(label="Username", max_length=30,
	regex=r'^[\w.@+-]+$',
	help_text="Required. 30 characters or fewer. Letters, digits and "
		"@/./+/-/_ only.",
        error_messages={
                'invalid': "This value may contain only letters, numbers and "
			"@/./+/-/_ characters."}) 
    password1 = forms.CharField(label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification.") 
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

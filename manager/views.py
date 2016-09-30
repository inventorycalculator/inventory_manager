from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from manager.forms import SignupForm

def home(request):
    return render(request, "index.html", {})

def signup(request):
    """singup to register users"""

    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['email']
            user.save()

            return HttpResponseRedirect(
                        reverse("signup_complete")
                    )

    elif request.method == "GET":
         signupform = SignupForm()

    return render(request, "registration/signup.html", {
        "signupform": signupform,
    })

def signup_complete(request):
    return render(request, "registration/signup_complete.html", {})



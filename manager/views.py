from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    """singup to register users"""

    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

            return HttpResponseRedirect(
                        reverse("signup_complete")
                    )

    elif request.method == "GET":
         userform = UserCreationForm()

    return render(request, "registration/signup.html", {
        "userform": userform,
    })

def signup_complete(request):
    return render(request, "registration/signup_complete.html", {})

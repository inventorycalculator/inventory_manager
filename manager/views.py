from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from manager.forms import SignupForm
from .models import Product
from manager.forms import ProductForm

#home
def home(request):
    return render(request, "intro.html")

#signup
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

#product
def product_list(request):
    if request.user.is_authenticated():
        productList = Product.objects.filter(user = request.user)

        return render(request, 'product/list.html', {
            'product_list': productList,
         })
    else: 
        return redirect('/login/')

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product/detail.html', {
        'product': product,
    })

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit = False)
            product.user = request.user
            product.save()
            return redirect(product_detail, pk = product.pk)
    else:
        form = ProductForm()
    return render(request, 'product/new.html', {'form': form})



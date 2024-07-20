from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def contact_view(request):
    form = ContactForm()  # Initialize the form variable outside the conditional blocks

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            post=form.save()# Save the form data to the database
            messages.success(request, 'Kaydınızı başarılı bir şekilde oluşturdunuz')
            return HttpResponseRedirect(post.get_absolute_url())
            
     
                 # Redirect to a success page or any other desired URL after successful form submission
    context={
        'form':form,
    }
    return render(request, 'form copy.html', context)



def Contact_detail(request,id):
    post=get_object_or_404(Contact, id=id)

    context={
        'post':post
    }
    return render(request, "contact_detail.html",context)

def login_request(request):
    if request.method=="POST":
       username= request.POST["username"]
       password= request.POST["password"]

       user = authenticate(request, username= username, password=password )

       if user is not None:
           login(request, user) 
           return redirect ('home')
       else:
           return render(request, 'login.html', {
               "error":"Kullanıcı adı yada şifre hatalı"
           })     
    return render (request, "login.html")


def register_request (request):
    if request.method=="POST":
        Firstname=request.POST["firstname"]
        Lastname=request.POST["lastname"]
        email=request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]
       

       


        if password==repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "form copy.html",{
                "error":"Kullanıcı adı daha önce alınmış"
            }) 
            else:
                user=User.objects.create_user(first_name=Firstname, last_name=Lastname,email=email,username=username,
                                    password=password)
                user.save()
                messages.success(request, "Başarılı kayıt oluşturdunuz. Şimdi giriş yapabilirsiniz. ") 
                return redirect ('accounts:Login')
        else:
            return render(request, "form copy.html",{
                "error":"Parolalar eşleşmiyor"
            })
    return render(request, "form copy.html")     


def logout_request(request):
    logout(request) 
    return redirect('home')

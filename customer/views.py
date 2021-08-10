from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from customer import forms
from django.views.generic import TemplateView

# Create your views here.

# registration
class UserRegistrationView(TemplateView):
    form_class=forms.RegistrationForm
    template_name = "registration.html"    #to render this html page
    model=User
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)


class SigninView(TemplateView):
    template_name = "login.html"
    form_class=forms.LoginForm
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("custhome")
            else:
                self.context["form"] = form
                return render(request, self.template_name, self.context)

class CustomerHomeView(TemplateView):
    template_name = "customerhome.html"
#
# class SignOutView(TemplateView):
#     def user_logout(request, *args, **kwargs):
#         logout(request)
#         return redirect("signin")





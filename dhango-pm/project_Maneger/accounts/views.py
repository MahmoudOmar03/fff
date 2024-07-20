from django.shortcuts import render,redirect
from . import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.


class RegisterView(CreateView):
    form_class=forms.userRegisterForm
    template_name='registration/register.html'
    def get_success_url(self):
        login(self.request,self.object)
        return reverse_lazy("Project_list")
    
@login_required
def edit_profile(requset):
    if requset.method=="POST":
        form=forms.ProfileForm(requset.post,instance=requset.user)
        if form.is_valid:
            form.save
            return redirect("profile")
    else:
        form=forms.ProfileForm(instance=requset.user)
        return render(requset,'profile.html',{
            'form':form, 
        })
    


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup_view(request):

 if request.method =='POST':
    form=UserCreationForm(request.POST)
    if form.is_valid():
           form.save()
           return redirect('appointments:list')
#log the user in
 else:
  form = UserCreationForm()
 return render(request, "register.html",{'form':form})
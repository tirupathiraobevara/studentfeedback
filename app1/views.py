from django.shortcuts import render
from . import forms
def thankyou_view(request):
    return render(request,'app1/thankyou.html')
def feedbackview(request):
    form=forms.FeedBackForm()
    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form validation Succes and printing data')
            print('Name:',form.cleaned_data['name'])
            print('Rollno:',form.cleaned_data['rollno'])
            print('Email:',form.cleaned_data['email'])
            print('FeedBack:',form.cleaned_data['feedback'])
            return thankyou_view(request)
    return render(request,'app1/home.html',{'form':form})


# Create your views here.

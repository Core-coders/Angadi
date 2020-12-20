from django.shortcuts import render,redirect
from .forms import ItemForm 
from .models import Survey 
from django import forms

# Create your views here. 
def survey_view(request): 
    my_form = ItemForm()
    if request.method == 'POST':
        my_form = ItemForm(request.POST)
        if my_form.is_valid():
            Survey.objects.create(**my_form.cleaned_data)
        else:
            print(my_forms.errors)
    context={
        "form":my_form
    } 
    
    return render( request, "survey/survey.html", context) 

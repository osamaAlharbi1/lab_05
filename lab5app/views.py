from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

people = []

class Person:
    def __init__(self, name, password):
        self.username = name
        self.password = password

    def __str__(self):
        return self.username

class NewPersonForm(forms.Form):
    name = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)    

# Create your views here.
def default(request):      
    return render(request, "lab5app/default.html", {
        "people": people
    })

def add(request):
    if request.method == "POST":
        form = NewPersonForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            person = Person(name,password)
            people.append(person)
            return HttpResponseRedirect(reverse("default"))
        else:
            return render(request, "lab5app/add.html",{
                "form": form
            })
    else:
        return render(request, "lab5app/add.html",{
            "form": NewPersonForm()
        })
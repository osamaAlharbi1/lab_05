from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse


class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

people = []

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person(username, password)
        people.append(person)
        return HttpResponseRedirect(reverse('default'))
    return render(request, 'lab5app/add.html')

def default(request):
    return render(request, 'lab5app/default.html', {'people': people})






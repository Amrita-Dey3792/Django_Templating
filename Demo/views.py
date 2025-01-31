from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def data(request):
    first_name = "John"
    last_name = "Smith"

    return render(request, 'data.html', {'fullname': {
        'first_name': first_name,
        'last_name': last_name
    }})

def loop(request):
    # names = ['Alice', 'Bob', 'Charlie']
    data = [
        {
            'name': "John Smith",
            'age': 20,
        },
        {
            'name': "Jane Doe",
            'age': 30,
        },
        {
            'name': "David Johnson",
            'age': 40,
        },
        {
            'name': "Emily Davis",
            'age': 50,
        },
        {
            'name': "Michael Wilson",
            'age': 60,
        }

    ]

    temperature = 40
    number = 20

    return render(request, 'loop.html', {'persons': data, 'temperature': temperature, 'number': number})

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def reports(request):
    return render(request, 'reports.html')
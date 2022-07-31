from django.shortcuts import render
from .models import Book
# Create your views here.
from .resources import BookResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

def index(requests):
    books = Book.objects.all()
    return render(requests, 'main/index.html', {'title': 'Главная страница сайта','books': books})

def template(requests):
    return render(requests, 'main/template.html')

def simple_upload(request):
        if request.method == 'POST':
            person_resource = PersonResource()
            dataset = Dataset ()
            new_person = request.FILES['myfile']

            if not new_person.name.endswitch('xlsx'):
                messages.info(request, 'wrong format')
                return render (request, 'upload.html')

        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in imported_data:
            value = Book (
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
            )
            value.save()
        return render(request, 'upload.html')

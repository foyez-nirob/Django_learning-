from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student(request):
    student_data = [{
        'id' : 1,
        'name': 'John Doe',
        'roll': 12345,
        'city': 'New York',
    }]
    return HttpResponse(student_data)

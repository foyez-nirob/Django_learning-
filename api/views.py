from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from student.models import student

from .serializers import studentserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



# def student_views(request):
#     ## manual way of serializing the data ==>
#     students = student.objects.all()
#     students_list = list(students.values())
#     print(students)
#     return JsonResponse(students_list, safe=False)

# for all student data 
@api_view(['GET','POST'])
def student_views(request):
    if request.method == 'GET':
        students = student.objects.all()
        serializer = studentserializer(students, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = studentserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#for one student data =>

@api_view(['GET','PUT','DELETE'])
def student_one_view(request, pk):
    try:
        student_one = student.objects.get(pk = pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = studentserializer(student_one)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = studentserializer(student_one, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student_one.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
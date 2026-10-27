from django.urls import path,include
from . import views         # . -> represent current directory

urlpatterns = [
    path("student/", views.student_views),
    path("student/<int:pk>/", views.student_one_view)
]
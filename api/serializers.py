from rest_framework import serializers
from student.models import student

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

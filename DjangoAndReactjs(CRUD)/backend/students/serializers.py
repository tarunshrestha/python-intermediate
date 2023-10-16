from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'student_id',
            'first_name',
            'last_name',
            'registration_number',
            'phone',
            'email',
            'course')
#
# {
# 'first_name','xia',
# 'last_name','dada',
# 'registration_number','545454-54',
# 'phone','98989898',
# 'email','gaga@gmail.com',
# 'course','sasa'
# }

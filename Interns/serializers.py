from rest_framework import serializers
from .models import *


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = ('first_name', 'middle_name', 'last_name', 'dob', 'phone_number', 'email_address',
                  'name_of_school', 'year', 'course', 'language_name',
                  'framework_name',)

#
# class PastorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pastor
#         fields = ('title', 'first_name', 'second_name', 'surname', 'sex', 'phone_number', 'email_address',)

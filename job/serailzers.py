from rest_framework import serializers
from .models import Job



class Jobserailzers(serializers.ModelSerializer):
    class Meta:
        model=Job
        #fields = '__all__'
        exclude=('loction',)
     
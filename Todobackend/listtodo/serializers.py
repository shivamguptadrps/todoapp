from rest_framework import serializers, parsers
from .models import Todoapp,Todoapps,Cricketapp

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todoapp
        fields = ('id','title','desc','__all__')

class Todo_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Todoapps
        fields = ('id','title','desc','active','file_pic')

class CricketappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cricketapp
        fields = ( 'id','title','opposition','venue')
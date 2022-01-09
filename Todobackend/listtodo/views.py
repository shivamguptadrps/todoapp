from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import Todo_Serializers
from .models import Todoapps
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
#from .serializers import FileSerializer
from django.http.response import JsonResponse

@csrf_exempt
@api_view(["POST","GET","PUT","DELETE"])
def todoapi(request,id=0):
    if request.method == 'GET':
        todo = Todoapps.objects.all()
        todo_serializers =  Todo_Serializers(todo,many=True)
        return JsonResponse(todo_serializers.data, safe=False)
    if request.method == 'POST':
        # form = UploadFileForm(request.POST, request.FILES)
        # todo_data = JSONParser().parse(request)
        # todo_serialize = Todo_Serializers(data=todo_data)
        title = request.data['title']
        desc =  request.data['desc']
        active =  request.data['active']
        tic = request.data['file']
        Todoapps.objects.create(title=title,desc=desc,active=active,file_pic = tic)
        return HttpResponse("Succesfully")
    if request.method == 'PUT':
        todo_data = JSONParser().parse(request)
        todo = Todoapps.objects.get(id=todo_data['id'])
        todo_serializer = Todo_Serializers(todo,data = todo_data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse("Uploaded Successfully, safe =False")
        return HttpResponse("Succesfully")
    if request.method =='DELETE':
        # todo_data = JSONParser().parse(request)
        todo = Todoapps.objects.get(id=id)
        todo.delete()
        return HttpResponse("Succesfully")

@csrf_exempt
@api_view(["POST","GET"])
def todoapidelete(request,id=0):
    todo_data = JSONParser().parse(request)
    p = todo_data['id']
    todo = Todoapps.objects.get(id=p)
    todo.delete()
    return HttpResponse("Succesfully")








from .models import Cricketapp
from .serializers import CricketappSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets,status
from django.http.response import JsonResponse
api_view(['GET'])
def getCricket(request):
    try:
        cricket = Cricketapp.objects.all()
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serialized = CricketappSerializer(cricket,many=True)
        return JsonResponse(serialized.data, safe=False)



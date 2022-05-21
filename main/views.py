
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from rest_framework import serializers,status
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Feature
from main.serializers import FeatureSerializer
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
@permission_classes ((IsAuthenticated,))


class Tasklist(APIView):
   #@method_decorator(cache_page(1))
   
   def get(self,request):
      Tasklist=Feature.objects.all()
      serializers=FeatureSerializer(Tasklist,many=True)
      return Response(serializers.data)
   def post(self,request):
      serializer=FeatureSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return HttpResponse("failed")
      
class deletetask(APIView):    
   def delete (self,request,pk):
      s=Feature.objects.get(id=pk)
      s.delete()
      subject = "Sending an email with Django"
      message = "you have deleted on task "

            # send the email to the recipent
      send_mail(subject, message,'wilsonmwaura697@gmail.com',['njaiya.mwaura1@students.jkuat.ac.ke'])
      print("email sent")     
      return response.JsonResponse({'message': "delete successful"})



      
   

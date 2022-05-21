from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from rest_framework import serializers,status

from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import FeatureSerializer
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@permission_classes ((IsAuthenticated,))
class restricted(APIView):
   def get(self,request):
      return Response("only for AUTH in users")
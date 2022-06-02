
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

#@permission_classes ((IsAuthenticated,))



#@method_decorator(cache_page(1))
class allsites(APIView):
    def get(self,request):
        sites=Feature.objects.all()
        serializer=FeatureSerializer(sites,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=FeatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return HttpResponse("not valid")
class specificsite(APIView):
    def get(self,request,pk):
        site=Feature.objects.get(id=pk)
        serializer=FeatureSerializer(site)
        return Response(serializer.data)
     
class addexperience(APIView):
    def post(self,request,pk):
        addedexperience=request.data['added']
        print(addedexperience)
        posts=Feature.objects.get(id=pk)
        newexp=str(posts.experience) + addedexperience

        posts.experience=newexp
        
        posts.save(update_fields=['experience'])
        return HttpResponse(" experience added  successfully,Thank you !,We love you")


class sitesperregion(APIView):

    def get(self,request,pk):
        sites_per_region=Feature.objects.filter(region=pk)
        serializer=FeatureSerializer(sites_per_region,many=True)
        return Response(serializer.data)
class map(APIView):
    def get(self,request,pk):
        site=Feature.objects.get(id=pk)
        site_name=site.title
        url="https://www.google.com/maps/dir/?api=1&destination="
        mode="&travelmode=driving"

        return redirect (url+site_name+mode)

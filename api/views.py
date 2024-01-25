from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import permissions,authentication
from api.serializers import UserSerializers,TodoSerializers
from todoapp.models import Todos
from rest_framework import serializers


class RegistrationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class TodosView(ViewSet) :    
    authentication_classes=[authentication.BasicAuthentication]   
    permission_classes=[permissions.IsAuthenticated]
    def create(self,request,*args,**kwargs):
        serializer=TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def list(self,request,*args,**kwargs):
        qs=Todos.objects.filter(user=request.user)
        serializer=TodoSerializers(qs,many=True)
        return Response(data=serializer.data)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todos_object=Todos.objects.get(id=id)
        if Todos_object.user!=request.user:
            raise serializers.ValidationError("permission denied for this user")
        Todos_object.delete()
        return Response({"message":"deleted successfully"})


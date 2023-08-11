from rest_framework.decorators import api_view
from User.models import User
from User.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
#from rest_framework import viewsets

"""from django.db.models.signals import post_save
from django.dispatch import receiver"""

class UserListAndCreate(APIView):
    def get(self,request):
        user  = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailChangeAndDelete(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound()
    def get(self,request,pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self,request,pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
"""class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer"""
    
    
"""@receiver(post_save, sender=User)
def apos_criar_objetivo(sender, instance, created, **kwargs):
    if created:
        
        print("objeto criado")"""


from User.models import User
from User.serializers import UserSerializer
from rest_framework import generics
from django.db.models.signals import post_save,pre_delete,pre_save
from django.dispatch import receiver
from values.models import Values
from django.shortcuts import get_object_or_404

class UserListAndCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_object(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User,user_id=user_id)
        return user
    

@receiver(post_save, sender=User)
def after_create_user(sender, instance, created, **kwargs):
    if created:
        user_id = instance.user_id
        value = Values.objects.create(user_id=user_id)
        return value
        
@receiver(pre_delete, sender=User)
def before_delete_user(sender, instance, **kwargs):
    try:
        user_id = instance.user_id
        value = Values.objects.get(user_id=user_id)
        value.delete()
        return value
    except:
        pass




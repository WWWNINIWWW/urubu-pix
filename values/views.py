from values.models import Values
from values.serializers import ValuesSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404

class ValuesList(generics.ListAPIView):
    queryset = Values.objects.all()
    serializer_class = ValuesSerializer
    
class ValuesDetail(generics.RetrieveAPIView):
    queryset = Values.objects.all()
    serializer_class = ValuesSerializer
    def get_object(self):
        user_id = self.kwargs['user_id']
        value = get_object_or_404(Values,user_id=user_id)
        return value



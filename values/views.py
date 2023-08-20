from values.models import Values
from values.serializers import ValuesSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.utils import timezone
from decimal import Decimal
from rest_framework.response import Response

class ValuesList(generics.ListAPIView):
    queryset = Values.objects.all()
    serializer_class = ValuesSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        for obj in queryset:
            current_date = timezone.now().date()
            last_income_date = obj.last_income.date()
            days_difference = (current_date - last_income_date).days
            if days_difference > 0:
                obj.value = obj.value * Decimal(str((1 + (1 / 3)) ** days_difference))
                obj.last_income = timezone.now()
                obj.save()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class ValuesDetail(generics.RetrieveAPIView):
    queryset = Values.objects.all()
    serializer_class = ValuesSerializer
    def get_object(self):
        user_id = self.kwargs['user_id']
        value = get_object_or_404(Values,user_id=user_id)
        return value
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        current_date = timezone.now().date()
        last_income_date = instance.last_income.date()
        days_difference = (current_date - last_income_date).days
        if days_difference > 0:
            instance.value = instance.value * Decimal(str((1 + (1 / 3)) ** days_difference))
            instance.last_income = timezone.now()
            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



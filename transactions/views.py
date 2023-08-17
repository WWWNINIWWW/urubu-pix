from transactions.models import Transactions
from transactions.serializers import TransactionsSerializer
from rest_framework import generics
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404
from values.models import Values
from rest_framework import status
from rest_framework.response import Response

class TransactionsList(generics.ListAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    
    
class TransactionsDetail(generics.RetrieveUpdateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    def get_object(self):
        user_id = self.kwargs['user_id']
        transactions = get_object_or_404(Transactions,user_id=user_id)
        return transactions
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        balance = self.after_deposit_or_withdraw_value(instance)
        if balance:
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def after_deposit_or_withdraw_value(self,transactions):
        if transactions.deposit != 0 or transactions.withdraw != 0:
            user_id = transactions.user_id
            value = Values.objects.get(user_id=user_id)
            value.value += transactions.deposit 
            value.value -= transactions.withdraw
            transactions.deposit = 0
            transactions.withdraw = 0
            transactions.save()
            if value.value >=0:
                value.save()
                return True
            return False
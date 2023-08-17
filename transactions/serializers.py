from transactions.models import Transactions
from rest_framework import serializers

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['user_id','deposit','withdraw','modified_at']
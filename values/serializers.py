from values.models import Values
from rest_framework import serializers

class ValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Values
        fields = ['user_id','value','modified_at']
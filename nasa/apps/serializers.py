from rest_framework import serializers

class GetInfoSerializer(serializers.Serializer):
    name = serializers.CharField()

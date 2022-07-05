from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False, max_length=100)
    description = serializers.CharField(required=False,allow_blank=True)
    image = serializers.CharField(required=True,allow_blank=False)
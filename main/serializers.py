from rest_framework import serializers
from .models import Port, Line


# class PortSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ExportReadFromPdf
#         fields = ('id', 'image', 'url_image', 'data_json')


class PortSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    url_image = serializers.CharField(max_length=500)
    data_json = serializers.JSONField()

    def create(self, validated_data):
        return Port(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.url_image = validated_data.get('url_image', instance.url_image)
        instance.data_json = validated_data.get('data_json', instance.data_json)
        instance.save()
        return instance


class LineSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    url_image = serializers.CharField(max_length=500)
    data_json = serializers.JSONField()

    def create(self, validated_data):
        return Line(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.url_image = validated_data.get('url_image', instance.url_image)
        instance.data_json = validated_data.get('data_json', instance.data_json)
        instance.save()
        return instance


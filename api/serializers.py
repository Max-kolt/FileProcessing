from rest_framework import serializers
from base.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        exclude = ['uploaded_at', 'processed']

    def create(self, validated_data):
        return File.objects.create(**validated_data)



from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from.models import Vox


class VoxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vox
        fields= '__all__'

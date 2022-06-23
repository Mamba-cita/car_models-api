
from vox.models import Vox
from rest_framework import viewsets, permissions
from.serializers import VoxSerializer


class VoxViewSet(viewsets.ModelViewSet):

    queryset = Vox.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VoxSerializer

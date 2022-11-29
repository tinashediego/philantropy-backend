from rest_framework import viewsets
from . import models
from . import serializers

class LawViewset(viewsets.ModelViewSet):
    queryset = models.Law.objects.all()
    serializer_class = serializers.LawSerializer
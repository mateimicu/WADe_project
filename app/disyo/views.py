from rest_framework import viewsets
from disyo.models import DSApplication
from disyo.serializers import DSApplicationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DSApplication.objects.all()
    serializer_class = DSApplicationSerializer

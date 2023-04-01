from .models import Status
from .serializers import StatusSerializer
from rest_framework.response import Response
from rest_framework import generics, parsers, viewsets
# Create your views here.

class StatusViewset(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


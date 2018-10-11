from rest_framework.generics import CreateAPIView

from logs.models import Log

from .serializers import CreateLogSerializer


class CreateLogView(CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = CreateLogSerializer

from rest_framework import viewsets
from egyNationalId.serializers import NationalIDSerializer
from egyNationalId.models import NationalID


class NationalIDView(viewsets.ModelViewSet):
    queryset = NationalID.objects.all()
    serializer_class = NationalIDSerializer

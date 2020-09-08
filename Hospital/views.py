from rest_framework.viewsets import ModelViewSet

from .models import Patient
from .serializers import PatientModelSerializer


class PatientViewSet(ModelViewSet):
    serializer_class = PatientModelSerializer
    queryset = Patient.objects.all()
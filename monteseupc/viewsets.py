from rest_framework import viewsets
from monteseupc.models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class MonteSeuPcViewSet(viewsets.ModelViewSet):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = MonteSeuPc.objects.all()
    serializer_class = MonteSeuPcSerializer

class ProcessadorViewSet(viewsets.ModelViewSet):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Processador.objects.all()
    serializer_class = ProcessadorSerializer

class PlacaMaeViewSet(viewsets.ModelViewSet):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PlacaMae.objects.all()
    serializer_class = PlacaMaeSerializer

class MemoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Memoria.objects.all()
    serializer_class = MemoriaSerializer

class PlacaDeVideoViewSet(viewsets.ModelViewSet):

    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PlacaDeVideo.objects.all()
    serializer_class = PlacaDeVideoSerializer


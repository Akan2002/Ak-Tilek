from rest_framework.viewsets import ModelViewSet
from mainapp.models import (
    Teacher,School,Rewiew,Galeria, Newss
)
from mainapp.serializer import(
    SchoolSerializer,TeacherSerializer,GaleriaSerializer,\
        RewiewSerializer, NewssSerializer ,
)

# Create your views here.


class SchoolView(ModelViewSet):
    queryset= School.objects.all()
    serializer_class= SchoolSerializer

class TeacherView(ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class= TeacherSerializer

class GaleriaView(ModelViewSet):
    queryset=Galeria.objects.all()
    serializer_class=GaleriaSerializer

class RewiewView(ModelViewSet):
    queryset=Rewiew.objects.all()
    serializer_class=RewiewSerializer

# class NewsView(ModelViewSet):
#     queryset=News.objects.all()
#     serializer_class=NewsSerializer
class NewssView(ModelViewSet):
    queryset = Newss.objects.all()
    serializer_class = NewssSerializer
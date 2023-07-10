from mainapp.models import (
    School,Teacher,Rewiew,Galeria,Newss
)

from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=(
            'id','school','name','photo',
        )


class GaleriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Galeria
        fields=(
            'id','school','photo','name',
        )


class RewiewSerializer(serializers.Serializer):
    class Meta:
        model=Rewiew
        fields = (
        'id','photo','parent','description',
        )


class NewssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newss
        fields = (
            'title', 'content', 'created_at', 'create_date',
        )


class SchoolSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many = True, read_only = True)
    newsss = NewssSerializer(many = True, read_only = True)
    rewiews = RewiewSerializer(many = True, read_only = True)
    galleries = GaleriaSerializer(many = True, read_only = True)
    
    class Meta:
        model=School
        fields=(
            'id','logo','whatsapp','twitter','facebook','name','description',\
                'admissiontouniversity','staff','students','successworkyear','mail',\
                    'address','number',
        )
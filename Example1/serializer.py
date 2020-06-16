from rest_framework import routers, serializers, viewsets

from Example1.models import Example1

class Example1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Example1
        fields = ('__all__')
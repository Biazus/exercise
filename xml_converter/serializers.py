from rest_framework.serializers import FileField, Serializer


class ConverterSerializer(Serializer):
    file = FileField()

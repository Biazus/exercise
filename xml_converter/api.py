from xml.etree.ElementTree import ParseError

from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from xml_converter.constants import PARSING_ERROR_MESSAGE
from xml_converter.helpers import convert_xml
from xml_converter.serializers import ConverterSerializer


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser, ]

    @action(methods=['POST'], detail=False, url_path='convert')
    def convert(self, request, **kwargs):
        serializer = ConverterSerializer(data=request.FILES)
        if serializer.is_valid():
            try:
                json_response = convert_xml(request.FILES['file'])
            except ParseError:
                json_response = {'error': [PARSING_ERROR_MESSAGE]}
            return Response(json_response)
        return Response(serializer.errors)

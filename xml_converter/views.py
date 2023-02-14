from xml.etree.ElementTree import ParseError

from django.http import JsonResponse
from django.shortcuts import render

from xml_converter.constants import PARSING_ERROR_MESSAGE
from xml_converter.forms import ConverterForm
from xml_converter.helpers import convert_xml


def upload_page(request):
    form = ConverterForm(request.POST or None)
    status, error = 200, ''
    if request.method == 'POST':
        form = ConverterForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                json_response = convert_xml(request.FILES['file'])
            except ParseError:
                status, error = 400, PARSING_ERROR_MESSAGE
            else:
                return JsonResponse(json_response)
    context = dict(form=form, error=error)
    return render(
        request,
        'upload_page.html',
        context=context,
        status=status
    )

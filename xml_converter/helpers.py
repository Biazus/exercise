from typing import Dict, Union
from xml.etree import ElementTree as ET

from django.core.files.uploadedfile import InMemoryUploadedFile


def convert_xml(xml_file: InMemoryUploadedFile) -> Dict[str, Union[str, list]]:
    """ Creates a dictionary of elements based on a XML file
        returns: dict
    """
    et = ET.parse(xml_file)
    return _convert_element_tree(et)


def _convert_element_tree(tree: ET) -> Dict[str, Union[str, list]]:
    """ Creates a dictionary of elements based on a XML Element Tree
        returns: dict
    """
    result = {}
    iterator = tree.iter()
    for element in iterator:

        # we need to set an attribute identifying the object as already
        # rendered, otherwise we would render it twice: inside the list of
        # the parent and the element itself
        if not element.get('rendered'):
            if list(element):
                element.set('rendered', True)
                result[element.tag] = [
                    _convert_element_tree(tree=a) for a in list(element)
                ]
            else:
                result[element.tag] = element.text or ''
                element.set('rendered', True)
    return result

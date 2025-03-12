from django.shortcuts import render
from django.http import JsonResponse

import yaml
import json
from lxml import etree


def xml_editor(request):
    return render(request, 'editor/xml_editor.html')

def yaml_editor(request):
    return render(request, 'editor/yaml_editor.html')

def validate_xml(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            xml_content = data.get('xml')
            etree.fromstring(xml_content)
            return JsonResponse({'is_valid': True})
        except etree.XMLSyntaxError as err:
            return JsonResponse({'is_valid': True})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def validate_yaml(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            yaml_content = data.get('yaml')
            yaml.safe_load(yaml_content)
            return JsonResponse({'is_valid': True})
        except yaml.YAMLError as e:
            return JsonResponse({'is_valid': False, 'errors': str(e)})

    return JsonResponse({'error': 'Invalid request'}, status=400)

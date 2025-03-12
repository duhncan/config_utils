from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('xml-editor/', views.xml_editor, name='xml_editor'),
    path('yaml-editor/', views.yaml_editor, name='yaml_editor'),
    path('validate-xml/', views.validate_xml, name='validate_xml'),
    path('validate-yaml/', views.validate_yaml, name='validate_yaml'),
]

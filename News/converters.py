import re
from django.urls import register_converter

class CyrillicSlugConverter:
    regex = r'[-\w\u0400-\u04FF]+'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value

register_converter(CyrillicSlugConverter, 'cyrslug')
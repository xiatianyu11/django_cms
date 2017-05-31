# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe

class DocContentInput(forms.Widget):
    def get_context(self, name, value, attrs):
        context = {}
        context['widget'] = {
            'name': name,
            'is_hidden': self.is_hidden,
            'required': self.is_required,
            'value': self.format_value(value),
            'attrs': self.build_attrs(self.attrs, attrs),
        }
        return context
    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        flat_attrs = flatatt(context['widget']['attrs'])
        html = '''
        <script %(attrs)s type="text/plain" ></script>
        ''' % {
            'attrs': flat_attrs,
        }
        return mark_safe(html)
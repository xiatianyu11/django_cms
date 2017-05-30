# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import  forms

# Create your models here.
class ArticleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-text'}))
    ellipsisTitle = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-text'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-text'}))
    source = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-text'}))
    updateTime = forms.DateTimeField()
    readCount = forms.IntegerField()
    state = forms.CharField()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import  forms
from .widgets import DocContentInput


marcas = (
        ('a', 'type 1'),
        ('b', 'type 2'),)
# Create your models here.
class ArticleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-text'}))
    ellipsisTitle = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-text'}))
    category = forms.TypedChoiceField(choices=marcas,widget=forms.Select(attrs={'class' : 'select'}))
    order = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'select'}))
    keywords = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-text'}))
    digest = forms.CharField(widget=forms.Textarea(attrs={'class' : 'textarea', 'placeholder': '说点什么...最少输入10个字符'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-text'}))
    source = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-text'}))
    canComment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id' : 'checkbox-pinglun'}))
    timeOfFirstComment = forms.CharField(widget=forms.TextInput(attrs={"onfocus" : "WdatePicker({dateFmt:'yyyy-MM-dd HH:mm:ss',maxDate:'#F{$dp.$D(\\'datemax\\')||\\'%y-%M-%d\\'}'})", "id" : "datemin", "class" : "input-text Wdate"}))
    timeOfLastComment = forms.CharField(widget=forms.TextInput(attrs={"onfocus": "WdatePicker({dateFmt:'yyyy-MM-dd HH:mm:ss',minDate:'#F{$dp.$D(\\'datemin\\')}'})", "id": "datemax", "class": "input-text Wdate"}))
    content = forms.CharField(widget=DocContentInput(attrs={"id":"editor", "style":"..."}))
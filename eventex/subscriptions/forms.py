#coding: utf-8
from django import forms
from django.utils.translation import ugettext as _
class SubscriptionForm(forms.Form):
	name = forms.CharField(label=_('Nome'), widget=forms.TextInput)
	cpf = forms.CharField(label=_('CPF'))
	email = forms.EmailField(label=_('Email'))
	phone = forms.CharField(label=_('Telefone'))

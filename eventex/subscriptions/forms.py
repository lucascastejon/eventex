#coding: utf-8
from django import forms
from eventex.subscriptions.models import Subscription
from django.forms import ModelForm, TextInput, EmailInput
from django.utils.translation import ugettext as _

class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = Subscription
		exclude = ('paid',) # Segurança
		widgets = {
			'name': TextInput(attrs={'class':'form-control', 'placeholder':_('Nome'), 'type':'text'}),
			'cpf': TextInput(attrs={'class':'form-control', 'placeholder':_('CPF')}),
			'email': EmailInput(attrs={'class':'form-control','placeholder':_('Email')}),
			'phone': TextInput(attrs={'class':'form-control', 'placeholder':_('Telefone')})
		}
			

# class SubscriptionForm(forms.Form):
# 	name = forms.CharField(label=_('Nome'), widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Nome')}))
# 	cpf = forms.CharField(label=_('CPF'), max_length=11, widget=forms.TextInput(attrs={'class':'form-control','placeholder':_('CPF')}))
# 	email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={'class':'form-control','placeholder':_('Email')}))
# 	phone = forms.CharField(label=_('Telefone'), widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Telefone')}))

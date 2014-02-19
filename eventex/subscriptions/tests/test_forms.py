# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.SubscriptionForm

class SubscriptionFormTest(TestCase):
	'Form must have 4 Fields'
	form = SubscriptionForm()
	self.assertItemsEqual(['name','email','cpf','phone'], form.fields)


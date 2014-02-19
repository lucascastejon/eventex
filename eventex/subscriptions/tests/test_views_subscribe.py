# coding: utf-8
from eventex.subscriptions.forms import SubscriptionForm
from django.test import TestCase

class SubscribeTest(TestCase):
	def test_csrf(self):
		'Html must contain csrf token.'
		self.assertContais(self.resp, 'csrfmiddlewaretoken')
	def test_html(self):
		'Html must contain input controls.'
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input',6)
		self.assertContains(self.resp, 'type="text"', 3)
		self.assertContains(self.resp, 'type="email"')
		self.assertContains(self.resp, 'type="submit"')
	def test_has_form(self):
		'Context must have the sobscription form.'
		form = self.resp.context['form']
		self.assertIsInstance(form, SubscriptionForm)
	def test_form_has_fields(self):
		'Form must have 4 fields.'
		form = self.resp.context['form']
		self.assertItemsEqual(['name','email','cpf','phone'], form.fields)

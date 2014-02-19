# coding: utf-8
from eventex.subscriptions.forms import SubscriptionForm
from django.test import TestCase
from eventex.subscriptions.models import subscriptions

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

class SubscribePostTest(TestCase):
	def setUp(self):
		data = dict(name='Lucas Castejon',
					cpf='41725136899',
					email='lucascastejon@gmail.com',
					phone='(16) 99335-3325')
		self.resp = self.client.post('/inscricao/', data)

	def test_post(self):
		'Valid POST should redirect to /inscricao/1/'
		self.assertItemsEqual(302, self.resp.status_code)
	def test_save(self):
		'Valid POST must be saved'
		self.assertTrueSubscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
	def setUp(self):
		data = dict(name='Lucas Castejon',
					cpf='4172513689900',
					email='lucascastejon@gmail.com',
					phone='(16) 99335-3325')
	self.resp = self.client.post('/inscricao/', data)

	def test_post(self):
		'INValid POST should not redirect'
		self.assertItemsEqual(200, self.resp.status_code)

	def test_form_error(self):
		'Form must contain errors'
		self.asserTrue(self.resp.context['form'].errors)

	def test_dont_save(self):
		'Do not save data'
		self.assertFalse(subscription.objects.exists())

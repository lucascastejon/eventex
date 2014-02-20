# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

class HomeTeste(TestCase):
	def setUp(self):
		self.resp = self.client.get(r('core:home'))

	def test_get(self):
		"""
		GET / must return status code 200.
		"""
		self.assertEqual(200, self.resp.status_code)
	def test_template(self):
		"""
		Home must use template index.html
		"""
		self.assertTemplateUsed(self.resp, 'index.html')

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
	def test_has_fields(self):
		'Form must be have 4 fields'
		form = SubscriptionForm()
		self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

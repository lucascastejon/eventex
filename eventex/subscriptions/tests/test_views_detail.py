# coding- utf-8
from eventex.subscriptions.models import Subscription
from django.test import TestCase


class DetailTest(TestCase):
	def setUp(self):
		s = Subscription.objects.create(name='Lucas Castejon',
						cpf='41725136899',
						email='lucascastejon@gmail.com',
						phone='16-993353325')
		self.resp = self.client.get('/inscricao/%d/' % s.pk)

	def test_get(self):
		'GET /inscricao/1/ should return status 200'
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		'Uses template'
		self.assertTemplateUsed(self.resp,
			'subscriptions/subscription_detail.html')

	def test_context(self):
		'Context must have a subscription instance'
		subscription = self.resp.context['subscription']
		self.assertIsInstance(subscription, Subscription)

	def test_html(self):
		'Check if subscription data was rendered'
		self.assertContains(self.resp, 'Lucas Castejon')


class DetailNotFound(TestCase):
	def test_not_found(self):
		response = self.client.get('/inscricao/0/')
		self.assertEqual(404, response.status_code)
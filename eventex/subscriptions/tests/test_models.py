# coding: utf-8
from eventex.subscriptions.models import Subscription
from django.test import TestCase
from datetime import datetime
from django.db import IntegrityError


class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Lucas Castejon',
			cpf='41725136899',
			email='lucascastejon@gmail.com',
			phone='16-993353325'
		)

	def test_create(self):
		'Subscription must have name, cpf, email, phone'
		self.obj.save()
		self.assertEqual(1, self.obj.pk)

	def test_has_created_at(self):
		'Subscriptions must have automatic created_at'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_unicode(self):
		self.assertEqual(u'Lucas Castejon', unicode(self.obj))

	def test_paid_default_value_is_False(self):
		'By default paid must be False.'
		self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
	def setUp(self):
		# Create a first entry to force the collision
		Subscription.objects.create(name='Lucas Castejon',
						cpf='41725136899',
						email='lucascastejon@gmail.com',
						phone='16-993353325')

	def test_cpf_unique(self):
		'CPF must be unique'
		s = Subscription(name='Lucas Castejon',
						cpf='41725136899',
						email='lucascastejon@gmail.com',
						phone='16-993353325')
		self.assertRaises(IntegrityError, s.save)

	def test_email_unique(self):
		'Email must be unique'
		s = Subscription(name='Lucas Castejon',
						cpf='41725136899',
						email='lucascastejon@gmail.com',
						phone='16-993353325')
		self.assertRaises(IntegrityError, s.save)

# coding: utf-8
from django.contrib import admin
from eventex.subscriptions.models import Subscription
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime #buscar quem foi cadastrado "hoje"
# Register your models here.

class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ('name', 'email','cpf','phone', 'created_at','subscribed_today')
	date_hierarchy = 'created_at' #necessário instalar o pytz (sudo pip isntall pytz)
	search_fields = ('name','cpf', 'email','phone', 'created_at')
	list_filter = ['created_at']

	def subscribed_today(self, obj): #obj recebe o obj da linha que está percorrendo
		return obj.created_at.date() == datetime.today().date() #buscar quem foi cadastrado "hoje"
	
	subscribed_today.short_description = _(u'Inscrito Hoje?')
	subscribed_today.boolean = True

admin.site.register(Subscription, SubscriptionAdmin)

from django.contrib import admin

from .models import Accrual, Payment

@admin.register(Accrual)
class AccrualAdmin(admin.ModelAdmin):
	list_display = ['date', 'month', 'pay']


@admin.register(Payment)
class AccrualAdmin(admin.ModelAdmin):
	list_display = ['date', 'month', 'for_debt']

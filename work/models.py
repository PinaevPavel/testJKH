from django.db import models

MONTHS = (
	('Я', 'Январь'),
	('Ф', 'Февраль'),
	('Мр', 'Март'),
	('А', 'Апрель'),
	('М', 'Май'),
	('Ин', 'Июнь'),
	('Ил', 'Июль'),
	('Ав', 'Август'),
	('С', 'Сентябрь'),
	('О', 'Октабрь'),
	('Н', 'Ноябрь'),
	('Д', 'Декабрь'),
	)

class Accrual(models.Model):
	date = models.DateField()
	month = models.CharField(max_length=2, choices=MONTHS)
	pay = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Долг'
		verbose_name_plural = 'Долги'


class Payment(models.Model):
	date = models.DateField()
	month = models.CharField(max_length=2, choices=MONTHS)
	for_debt = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Платеж'
		verbose_name_plural = 'Платежи'
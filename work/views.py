from django.shortcuts import render, redirect
from .models import Accrual, Payment
from django.db.models import Min

def view(request):
	payments = Payment.objects.filter(for_debt=False)
	list = []
	for i in payments:
		flag = True
		accruals = Accrual.objects.filter(pay=False)
		for x in accruals:
			if i.month == x.month and i.date.year == x.date.year and i.date > x.date:
				i.for_debt = True
				i.save()
#				x.pay = True
#				x.save()
				list.append([i, x])
				flag = False
				break
	payments_not_debt = Payment.objects.filter(for_debt=False)

	return render(request, 'list.html',
		{'list': list,
		'payments_not_debt': payments_not_debt,
		})		

def reset(request):
	payments = Payment.objects.filter(for_debt=True)
	accruals = Accrual.objects.filter(pay=True)
	for i in payments:
		i.for_debt = False
		i.save()
	for x in accruals:
		x.pay = False
		x.save()
	return redirect('work:view')
	

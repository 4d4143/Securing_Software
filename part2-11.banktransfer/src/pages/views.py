from django.shortcuts import render
from django.template import loader
from django.db import transaction
from .models import Account


# Create your views here.

def transfer(sender, receiver, amount):
	with transaction.atomic():

		senderAcc = Account.objects.get(iban=sender)
		receiverAcc = Account.objects.get(iban=receiver)

		if senderAcc.balance >= amount and amount >= 0:
			senderAcc.balance -= amount
			receiverAcc.balance += amount

		senderAcc.save()
		receiverAcc.save()


def homePageView(request):
	if request.method == 'POST':
		sender = request.POST.get('from')
		receiver = request.POST.get('to')
		amount = int(request.POST.get('amount'))
		transfer(sender, receiver, amount)

	accounts = Account.objects.all()
	context = {'accounts': accounts}
	return render(request, 'pages/index.html', context)
